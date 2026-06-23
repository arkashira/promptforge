from model_config import ModelConfig, ModelConfigManager, load_config_from_env
import pytest
import os

@pytest.fixture
def config_manager():
    return load_config_from_env()

def test_model_config_creation():
    config = ModelConfig("OpenAI", "https://api.openai.com/v1", "OPENAI_AUTH_TOKEN", 100)
    assert config.vendor == "OpenAI"
    assert config.endpoint == "https://api.openai.com/v1"
    assert config.auth_token == "OPENAI_AUTH_TOKEN"
    assert config.rate_limit == 100

def test_model_config_manager_add_config(config_manager):
    config = ModelConfig("TestVendor", "https://api.test.com/v1", "TEST_AUTH_TOKEN", 50)
    config_manager.add_config(config)
    assert config_manager.get_config("TestVendor") == config

def test_model_config_manager_get_config(config_manager):
    assert config_manager.get_config("OpenAI").vendor == "OpenAI"

def test_model_config_manager_update_rate_limit(config_manager):
    config_manager.update_rate_limit("OpenAI", 150)
    assert config_manager.get_config("OpenAI").rate_limit == 150

def test_load_config_from_env():
    os.environ["OPENAI_AUTH_TOKEN"] = "test_token"
    config_manager = load_config_from_env()
    assert config_manager.get_config("OpenAI").auth_token == "test_token"

def test_model_config_from_dict():
    data = {
        "vendor": "TestVendor",
        "endpoint": "https://api.test.com/v1",
        "auth_token": "TEST_AUTH_TOKEN",
        "rate_limit": 50
    }
    config = ModelConfig.from_dict(data)
    assert config.vendor == "TestVendor"
    assert config.endpoint == "https://api.test.com/v1"
    assert config.auth_token == "TEST_AUTH_TOKEN"
    assert config.rate_limit == 50
