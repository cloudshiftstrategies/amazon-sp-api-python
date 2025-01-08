# coding: utf-8

"""
    Orders v0

    Use the Orders Selling Partner API to programmatically retrieve order information. With this API, you can develop fast, flexible, and custom applications to manage order synchronization, perform order research, and create demand-based decision support tools.   _Note:_ For the JP, AU, and SG marketplaces, the Orders API supports orders from 2016 onward. For all other marketplaces, the Orders API supports orders for the last two years (orders older than this don't show up in the response).

    The version of the OpenAPI document: v0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from py_sp_api.generated.ordersV0.models.amazon_programs import AmazonPrograms
from py_sp_api.generated.ordersV0.models.associated_item import AssociatedItem
from py_sp_api.generated.ordersV0.models.buyer_requested_cancel import BuyerRequestedCancel
from py_sp_api.generated.ordersV0.models.item_buyer_info import ItemBuyerInfo
from py_sp_api.generated.ordersV0.models.measurement import Measurement
from py_sp_api.generated.ordersV0.models.money import Money
from py_sp_api.generated.ordersV0.models.points_granted_detail import PointsGrantedDetail
from py_sp_api.generated.ordersV0.models.product_info_detail import ProductInfoDetail
from py_sp_api.generated.ordersV0.models.shipping_constraints import ShippingConstraints
from py_sp_api.generated.ordersV0.models.substitution_preferences import SubstitutionPreferences
from py_sp_api.generated.ordersV0.models.tax_collection import TaxCollection
from typing import Optional, Set
from typing_extensions import Self

class OrderItem(BaseModel):
    """
    A single order item.
    """ # noqa: E501
    asin: StrictStr = Field(description="The item's Amazon Standard Identification Number (ASIN).", alias="ASIN")
    seller_sku: Optional[StrictStr] = Field(default=None, description="The item's seller stock keeping unit (SKU).", alias="SellerSKU")
    order_item_id: StrictStr = Field(description="An Amazon-defined order item identifier.", alias="OrderItemId")
    associated_items: Optional[List[AssociatedItem]] = Field(default=None, description="A list of associated items that a customer has purchased with a product. For example, a tire installation service purchased with tires.", alias="AssociatedItems")
    title: Optional[StrictStr] = Field(default=None, description="The item's name.", alias="Title")
    quantity_ordered: StrictInt = Field(description="The number of items in the order. ", alias="QuantityOrdered")
    quantity_shipped: Optional[StrictInt] = Field(default=None, description="The number of items shipped.", alias="QuantityShipped")
    product_info: Optional[ProductInfoDetail] = Field(default=None, alias="ProductInfo")
    points_granted: Optional[PointsGrantedDetail] = Field(default=None, alias="PointsGranted")
    item_price: Optional[Money] = Field(default=None, alias="ItemPrice")
    shipping_price: Optional[Money] = Field(default=None, alias="ShippingPrice")
    item_tax: Optional[Money] = Field(default=None, alias="ItemTax")
    shipping_tax: Optional[Money] = Field(default=None, alias="ShippingTax")
    shipping_discount: Optional[Money] = Field(default=None, alias="ShippingDiscount")
    shipping_discount_tax: Optional[Money] = Field(default=None, alias="ShippingDiscountTax")
    promotion_discount: Optional[Money] = Field(default=None, alias="PromotionDiscount")
    promotion_discount_tax: Optional[Money] = Field(default=None, alias="PromotionDiscountTax")
    promotion_ids: Optional[List[StrictStr]] = Field(default=None, description="A list of promotion identifiers provided by the seller when the promotions were created.", alias="PromotionIds")
    cod_fee: Optional[Money] = Field(default=None, alias="CODFee")
    cod_fee_discount: Optional[Money] = Field(default=None, alias="CODFeeDiscount")
    is_gift: Optional[StrictStr] = Field(default=None, description="Indicates whether the item is a gift.  **Possible values**: `true` and `false`.", alias="IsGift")
    condition_note: Optional[StrictStr] = Field(default=None, description="The condition of the item, as described by the seller.", alias="ConditionNote")
    condition_id: Optional[StrictStr] = Field(default=None, description="The condition of the item.  **Possible values**: `New`, `Used`, `Collectible`, `Refurbished`, `Preorder`, and `Club`.", alias="ConditionId")
    condition_subtype_id: Optional[StrictStr] = Field(default=None, description="The subcondition of the item.  **Possible values**: `New`, `Mint`, `Very Good`, `Good`, `Acceptable`, `Poor`, `Club`, `OEM`, `Warranty`, `Refurbished Warranty`, `Refurbished`, `Open Box`, `Any`, and `Other`.", alias="ConditionSubtypeId")
    scheduled_delivery_start_date: Optional[StrictStr] = Field(default=None, description="The start date of the scheduled delivery window in the time zone for the order destination. In [ISO 8601](https://developer-docs.amazon.com/sp-api/docs/iso-8601) date time format.", alias="ScheduledDeliveryStartDate")
    scheduled_delivery_end_date: Optional[StrictStr] = Field(default=None, description="The end date of the scheduled delivery window in the time zone for the order destination. In [ISO 8601](https://developer-docs.amazon.com/sp-api/docs/iso-8601) date time format.", alias="ScheduledDeliveryEndDate")
    price_designation: Optional[StrictStr] = Field(default=None, description="Indicates that the selling price is a special price that is only available for Amazon Business orders. For more information about the Amazon Business Seller Program, refer to the [Amazon Business website](https://www.amazon.com/b2b/info/amazon-business).   **Possible values**: `BusinessPrice`", alias="PriceDesignation")
    tax_collection: Optional[TaxCollection] = Field(default=None, alias="TaxCollection")
    serial_number_required: Optional[StrictBool] = Field(default=None, description="When true, the product type for this item has a serial number.   Only returned for Amazon Easy Ship orders.", alias="SerialNumberRequired")
    is_transparency: Optional[StrictBool] = Field(default=None, description="When true, the ASIN is enrolled in Transparency. The Transparency serial number that you must submit is determined by:  **1D or 2D Barcode:** This has a **T** logo. Submit either the 29-character alpha-numeric identifier beginning with **AZ** or **ZA**, or the 38-character Serialized Global Trade Item Number (SGTIN). **2D Barcode SN:** Submit the 7- to 20-character serial number barcode, which likely has the prefix **SN**. The serial number is applied to the same side of the packaging as the GTIN (UPC/EAN/ISBN) barcode. **QR code SN:** Submit the URL that the QR code generates.", alias="IsTransparency")
    ioss_number: Optional[StrictStr] = Field(default=None, description="The IOSS number of the marketplace. Sellers shipping to the EU from outside the EU must provide this IOSS number to their carrier when Amazon has collected the VAT on the sale.", alias="IossNumber")
    store_chain_store_id: Optional[StrictStr] = Field(default=None, description="The store chain store identifier. Linked to a specific store in a store chain.", alias="StoreChainStoreId")
    deemed_reseller_category: Optional[StrictStr] = Field(default=None, description="The category of deemed reseller. This applies to selling partners that are not based in the EU and is used to help them meet the VAT Deemed Reseller tax laws in the EU and UK.", alias="DeemedResellerCategory")
    buyer_info: Optional[ItemBuyerInfo] = Field(default=None, alias="BuyerInfo")
    buyer_requested_cancel: Optional[BuyerRequestedCancel] = Field(default=None, alias="BuyerRequestedCancel")
    serial_numbers: Optional[List[StrictStr]] = Field(default=None, description="A list of serial numbers for electronic products that are shipped to customers. Returned for FBA orders only.", alias="SerialNumbers")
    substitution_preferences: Optional[SubstitutionPreferences] = Field(default=None, alias="SubstitutionPreferences")
    measurement: Optional[Measurement] = Field(default=None, alias="Measurement")
    shipping_constraints: Optional[ShippingConstraints] = Field(default=None, alias="ShippingConstraints")
    amazon_programs: Optional[AmazonPrograms] = Field(default=None, alias="AmazonPrograms")
    __properties: ClassVar[List[str]] = ["ASIN", "SellerSKU", "OrderItemId", "AssociatedItems", "Title", "QuantityOrdered", "QuantityShipped", "ProductInfo", "PointsGranted", "ItemPrice", "ShippingPrice", "ItemTax", "ShippingTax", "ShippingDiscount", "ShippingDiscountTax", "PromotionDiscount", "PromotionDiscountTax", "PromotionIds", "CODFee", "CODFeeDiscount", "IsGift", "ConditionNote", "ConditionId", "ConditionSubtypeId", "ScheduledDeliveryStartDate", "ScheduledDeliveryEndDate", "PriceDesignation", "TaxCollection", "SerialNumberRequired", "IsTransparency", "IossNumber", "StoreChainStoreId", "DeemedResellerCategory", "BuyerInfo", "BuyerRequestedCancel", "SerialNumbers", "SubstitutionPreferences", "Measurement", "ShippingConstraints", "AmazonPrograms"]

    @field_validator('deemed_reseller_category')
    def deemed_reseller_category_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['IOSS', 'UOSS']):
            raise ValueError("must be one of enum values ('IOSS', 'UOSS')")
        return value

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of OrderItem from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in associated_items (list)
        _items = []
        if self.associated_items:
            for _item_associated_items in self.associated_items:
                if _item_associated_items:
                    _items.append(_item_associated_items.to_dict())
            _dict['AssociatedItems'] = _items
        # override the default output from pydantic by calling `to_dict()` of product_info
        if self.product_info:
            _dict['ProductInfo'] = self.product_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of points_granted
        if self.points_granted:
            _dict['PointsGranted'] = self.points_granted.to_dict()
        # override the default output from pydantic by calling `to_dict()` of item_price
        if self.item_price:
            _dict['ItemPrice'] = self.item_price.to_dict()
        # override the default output from pydantic by calling `to_dict()` of shipping_price
        if self.shipping_price:
            _dict['ShippingPrice'] = self.shipping_price.to_dict()
        # override the default output from pydantic by calling `to_dict()` of item_tax
        if self.item_tax:
            _dict['ItemTax'] = self.item_tax.to_dict()
        # override the default output from pydantic by calling `to_dict()` of shipping_tax
        if self.shipping_tax:
            _dict['ShippingTax'] = self.shipping_tax.to_dict()
        # override the default output from pydantic by calling `to_dict()` of shipping_discount
        if self.shipping_discount:
            _dict['ShippingDiscount'] = self.shipping_discount.to_dict()
        # override the default output from pydantic by calling `to_dict()` of shipping_discount_tax
        if self.shipping_discount_tax:
            _dict['ShippingDiscountTax'] = self.shipping_discount_tax.to_dict()
        # override the default output from pydantic by calling `to_dict()` of promotion_discount
        if self.promotion_discount:
            _dict['PromotionDiscount'] = self.promotion_discount.to_dict()
        # override the default output from pydantic by calling `to_dict()` of promotion_discount_tax
        if self.promotion_discount_tax:
            _dict['PromotionDiscountTax'] = self.promotion_discount_tax.to_dict()
        # override the default output from pydantic by calling `to_dict()` of cod_fee
        if self.cod_fee:
            _dict['CODFee'] = self.cod_fee.to_dict()
        # override the default output from pydantic by calling `to_dict()` of cod_fee_discount
        if self.cod_fee_discount:
            _dict['CODFeeDiscount'] = self.cod_fee_discount.to_dict()
        # override the default output from pydantic by calling `to_dict()` of tax_collection
        if self.tax_collection:
            _dict['TaxCollection'] = self.tax_collection.to_dict()
        # override the default output from pydantic by calling `to_dict()` of buyer_info
        if self.buyer_info:
            _dict['BuyerInfo'] = self.buyer_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of buyer_requested_cancel
        if self.buyer_requested_cancel:
            _dict['BuyerRequestedCancel'] = self.buyer_requested_cancel.to_dict()
        # override the default output from pydantic by calling `to_dict()` of substitution_preferences
        if self.substitution_preferences:
            _dict['SubstitutionPreferences'] = self.substitution_preferences.to_dict()
        # override the default output from pydantic by calling `to_dict()` of measurement
        if self.measurement:
            _dict['Measurement'] = self.measurement.to_dict()
        # override the default output from pydantic by calling `to_dict()` of shipping_constraints
        if self.shipping_constraints:
            _dict['ShippingConstraints'] = self.shipping_constraints.to_dict()
        # override the default output from pydantic by calling `to_dict()` of amazon_programs
        if self.amazon_programs:
            _dict['AmazonPrograms'] = self.amazon_programs.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of OrderItem from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "ASIN": obj.get("ASIN"),
            "SellerSKU": obj.get("SellerSKU"),
            "OrderItemId": obj.get("OrderItemId"),
            "AssociatedItems": [AssociatedItem.from_dict(_item) for _item in obj["AssociatedItems"]] if obj.get("AssociatedItems") is not None else None,
            "Title": obj.get("Title"),
            "QuantityOrdered": obj.get("QuantityOrdered"),
            "QuantityShipped": obj.get("QuantityShipped"),
            "ProductInfo": ProductInfoDetail.from_dict(obj["ProductInfo"]) if obj.get("ProductInfo") is not None else None,
            "PointsGranted": PointsGrantedDetail.from_dict(obj["PointsGranted"]) if obj.get("PointsGranted") is not None else None,
            "ItemPrice": Money.from_dict(obj["ItemPrice"]) if obj.get("ItemPrice") is not None else None,
            "ShippingPrice": Money.from_dict(obj["ShippingPrice"]) if obj.get("ShippingPrice") is not None else None,
            "ItemTax": Money.from_dict(obj["ItemTax"]) if obj.get("ItemTax") is not None else None,
            "ShippingTax": Money.from_dict(obj["ShippingTax"]) if obj.get("ShippingTax") is not None else None,
            "ShippingDiscount": Money.from_dict(obj["ShippingDiscount"]) if obj.get("ShippingDiscount") is not None else None,
            "ShippingDiscountTax": Money.from_dict(obj["ShippingDiscountTax"]) if obj.get("ShippingDiscountTax") is not None else None,
            "PromotionDiscount": Money.from_dict(obj["PromotionDiscount"]) if obj.get("PromotionDiscount") is not None else None,
            "PromotionDiscountTax": Money.from_dict(obj["PromotionDiscountTax"]) if obj.get("PromotionDiscountTax") is not None else None,
            "PromotionIds": obj.get("PromotionIds"),
            "CODFee": Money.from_dict(obj["CODFee"]) if obj.get("CODFee") is not None else None,
            "CODFeeDiscount": Money.from_dict(obj["CODFeeDiscount"]) if obj.get("CODFeeDiscount") is not None else None,
            "IsGift": obj.get("IsGift"),
            "ConditionNote": obj.get("ConditionNote"),
            "ConditionId": obj.get("ConditionId"),
            "ConditionSubtypeId": obj.get("ConditionSubtypeId"),
            "ScheduledDeliveryStartDate": obj.get("ScheduledDeliveryStartDate"),
            "ScheduledDeliveryEndDate": obj.get("ScheduledDeliveryEndDate"),
            "PriceDesignation": obj.get("PriceDesignation"),
            "TaxCollection": TaxCollection.from_dict(obj["TaxCollection"]) if obj.get("TaxCollection") is not None else None,
            "SerialNumberRequired": obj.get("SerialNumberRequired"),
            "IsTransparency": obj.get("IsTransparency"),
            "IossNumber": obj.get("IossNumber"),
            "StoreChainStoreId": obj.get("StoreChainStoreId"),
            "DeemedResellerCategory": obj.get("DeemedResellerCategory"),
            "BuyerInfo": ItemBuyerInfo.from_dict(obj["BuyerInfo"]) if obj.get("BuyerInfo") is not None else None,
            "BuyerRequestedCancel": BuyerRequestedCancel.from_dict(obj["BuyerRequestedCancel"]) if obj.get("BuyerRequestedCancel") is not None else None,
            "SerialNumbers": obj.get("SerialNumbers"),
            "SubstitutionPreferences": SubstitutionPreferences.from_dict(obj["SubstitutionPreferences"]) if obj.get("SubstitutionPreferences") is not None else None,
            "Measurement": Measurement.from_dict(obj["Measurement"]) if obj.get("Measurement") is not None else None,
            "ShippingConstraints": ShippingConstraints.from_dict(obj["ShippingConstraints"]) if obj.get("ShippingConstraints") is not None else None,
            "AmazonPrograms": AmazonPrograms.from_dict(obj["AmazonPrograms"]) if obj.get("AmazonPrograms") is not None else None
        })
        return _obj


