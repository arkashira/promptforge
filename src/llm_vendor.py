import json
from dataclasses import dataclass
from typing import Dict, List

@dataclass
class LLMVendor:
    name: str
    model: str

class LLMIntegration:
    def __init__(self):
        self.vendors = {}

    def add_vendor(self, vendor: LLMVendor):
        self.vendors[vendor.name] = vendor

    def get_vendor(self, name: str) -> LLMVendor:
        return self.vendors.get(name)

    def list_vendors(self) -> List[LLMVendor]:
        return list(self.vendors.values())

    def test_vendor(self, name: str, input_text: str) -> str:
        vendor = self.get_vendor(name)
        if vendor:
            # Simulate testing the vendor
            return f"Tested {vendor.name} with input: {input_text}"
        else:
            raise ValueError(f"Vendor {name} not found")

    def to_json(self) -> str:
        vendors = [{"name": vendor.name, "model": vendor.model} for vendor in self.vendors.values()]
        return json.dumps(vendors)

    @classmethod
    def from_json(cls, json_str: str) -> 'LLMIntegration':
        integration = cls()
        vendors = json.loads(json_str)
        for vendor in vendors:
            integration.add_vendor(LLMVendor(vendor["name"], vendor["model"]))
        return integration
