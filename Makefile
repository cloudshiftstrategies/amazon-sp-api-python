.PHONY: clean generate

clean:
	rm -rf src/py_sp_api/generated

generate: clean
	git submodule update --remote
	python scripts/generate_schemas.py

test:
	pytest

lint:
	flake8 --statistics

fix:
	black --line-length 120 .
	autoflake -r --in-place --remove-unused-variables --remove-all-unused-imports --ignore-init-module-imports --remove-duplicate-keys .

lint-fix: fix lint
