from llm_vendor import LLMIntegration, LLMVendor

def test_add_vendor():
    integration = LLMIntegration()
    vendor = LLMVendor("Test Vendor", "Test Model")
    integration.add_vendor(vendor)
    assert integration.get_vendor("Test Vendor") == vendor

def test_get_vendor():
    integration = LLMIntegration()
    vendor = LLMVendor("Test Vendor", "Test Model")
    integration.add_vendor(vendor)
    assert integration.get_vendor("Test Vendor") == vendor

def test_list_vendors():
    integration = LLMIntegration()
    vendor1 = LLMVendor("Test Vendor 1", "Test Model 1")
    vendor2 = LLMVendor("Test Vendor 2", "Test Model 2")
    integration.add_vendor(vendor1)
    integration.add_vendor(vendor2)
    assert integration.list_vendors() == [vendor1, vendor2]

def test_test_vendor():
    integration = LLMIntegration()
    vendor = LLMVendor("Test Vendor", "Test Model")
    integration.add_vendor(vendor)
    assert integration.test_vendor("Test Vendor", "Test Input") == "Tested Test Vendor with input: Test Input"

def test_test_vendor_not_found():
    integration = LLMIntegration()
    try:
        integration.test_vendor("Test Vendor", "Test Input")
        assert False, "Expected ValueError"
    except ValueError as e:
        assert str(e) == "Vendor Test Vendor not found"

def test_to_json():
    integration = LLMIntegration()
    vendor = LLMVendor("Test Vendor", "Test Model")
    integration.add_vendor(vendor)
    json_str = integration.to_json()
    assert json_str == '[{"name": "Test Vendor", "model": "Test Model"}]'

def test_from_json():
    json_str = '[{"name": "Test Vendor", "model": "Test Model"}]'
    integration = LLMIntegration.from_json(json_str)
    assert integration.get_vendor("Test Vendor").name == "Test Vendor"
