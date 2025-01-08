import os
from pathlib import Path
import subprocess
import logging
import shutil

logging.basicConfig(level=os.getenv("LOG_LEVEL", logging.INFO))
formatter = logging.Formatter("%(levelname)s: %(message)s")
logging.getLogger().handlers.clear()
handler = logging.StreamHandler()
handler.setFormatter(formatter)
logging.getLogger().addHandler(handler)


def sanitize_module_name(name: str) -> str:
    """
    Convert a string to a valid Python module name.
    - Replace dashes with underscores
    - Replace spaces with underscores
    - Remove any other invalid characters
    - Ensure it doesn't start with a number
    """
    # Replace dashes and spaces with underscores
    name = name.replace("-", "_").replace(" ", "_")

    # Remove any characters that aren't alphanumeric or underscore
    name = "".join(c for c in name if c.isalnum() or c == "_")

    # Ensure it doesn't start with a number
    if name[0].isdigit():
        name = f"_{name}"

    return name


def find_json_files(directory: str) -> list[str]:
    json_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".json"):
                json_files.append(os.path.join(root, file))
    return json_files


def generate_clients():
    logging.info("Generating clients")
    base_dir = Path(__file__).parent.parent
    models_dir = base_dir / "selling-partner-api-models" / "models"
    output_dir = base_dir / "src" / "py_sp_api" / "generated"
    base_client = base_dir / "src" / "py_sp_api" / "base_client.py"
    logging.debug(f"Base dir: {base_dir}")
    logging.debug(f"Models dir: {models_dir}")
    logging.debug(f"Output dir: {output_dir}")
    logging.debug(f"Base client: {base_client}")

    # Create output directory if it doesn't exist
    output_dir.mkdir(parents=True, exist_ok=True)

    # Create empty __init__.py with package name prefix
    init_file = output_dir / "__init__.py"
    init_file.write_text('"""Generated SP-API client models."""\n\n')
    logging.debug(f"Created Init file: {init_file}")

    json_files = find_json_files(str(models_dir))
    package_name = "py_sp_api"

    for input_file in json_files:
        model_name = sanitize_module_name(Path(input_file).stem)
        logging.info(f"Generating model: {model_name}")
        model_dir = output_dir / model_name
        temp_dir = model_dir.with_name(f"{model_name}_temp")
        logging.debug(f"Model dir: {model_dir}")
        logging.debug(f"Temp dir: {temp_dir}")
        model_dir.mkdir(exist_ok=True)

        try:
            # Generate into a temporary directory first
            cmd = [
                "openapi-generator-cli",
                "generate",
                "-i",
                input_file,
                "-g",
                "python",
                "-o",
                str(temp_dir),
                "--package-name",
                f"{package_name}.generated.{model_name}",
                "--skip-validate-spec",
                "--global-property",
                "apiTests=false,modelTests=false",
                "--additional-properties",
                "packageUrl=,generateSourceCodeOnly=true,projectName=sp-api,"
                "packageVersion=1.0.0,generateSetupPy=false,"
                "generateTox=false,generateGitIgnore=false,"
                "hideGenerationTimestamp=true",
            ]
            logging.debug(f"Running command: {cmd}")
            subprocess.run(cmd, check=True, capture_output=True, text=True)

            # Move the generated files from nested directory to the correct location
            generated_dir = temp_dir / "py_sp_api" / "generated" / model_name
            logging.debug(f"Generated dir: {generated_dir}")
            if not generated_dir.exists():
                logging.error(f"Generated dir does not exist: {generated_dir}")
                raise SystemExit(1)
            # Remove existing files in target directory
            if model_dir.exists():
                logging.debug(f"Removing existing files in {model_dir}")
                shutil.rmtree(model_dir)
            # Move files to correct location
            logging.debug(f"Moving files from {generated_dir} to {model_dir}")
            shutil.move(str(generated_dir), str(model_dir))

            # Add base_client.py to the model directory
            base_client_file = model_dir / "base_client.py"
            logging.debug(f"Adding base_client.py to {model_dir}")
            base_client_file.write_text(base_client.read_text())

            # Update __init__.py to include SPAPIClient
            init_path = model_dir / "__init__.py"
            logging.debug(f"Updating {init_path}")
            with init_path.open("a") as f:
                f.write("\nfrom .base_client import SPAPIClient\n")

            # Clean up temp directory
            logging.debug(f"Cleaning up temp directory {temp_dir}")
            shutil.rmtree(temp_dir)

        except subprocess.CalledProcessError as e:
            logging.error(f"Error generating client for {input_file}:")
            logging.error(f"Exit code: {e.returncode}")
            logging.error(f"stdout: {e.stdout}")
            logging.error(f"stderr: {e.stderr}")
            raise SystemExit(1)
        except OSError as e:
            logging.error(f"Error handling files for {model_name}: {e}")
            raise SystemExit(1)

        # Use absolute imports in __init__.py
        try:
            logging.debug(f"Updating {init_file}")
            with init_file.open("a") as f:
                f.write(f"from {package_name}.generated.{model_name} import *\n")
        except IOError as e:
            logging.error(f"Error writing to __init__.py: {e}")
            raise SystemExit(1)


if __name__ == "__main__":
    try:
        generate_clients()
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        raise SystemExit(1)
