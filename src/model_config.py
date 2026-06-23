import json
import os
from dataclasses import dataclass
from typing import Dict

@dataclass
class ModelConfig:
    vendor: str
    endpoint: str
    auth_token: str
    rate_limit: int

    def to_dict(self):
        return {
            "vendor": self.vendor,
            "endpoint": self.endpoint,
            "auth_token": self.auth_token,
            "rate_limit": self.rate_limit
        }

    @classmethod
    def from_dict(cls, data: Dict):
        return cls(
            vendor=data["vendor"],
            endpoint=data["endpoint"],
            auth_token=data["auth_token"],
            rate_limit=data["rate_limit"]
        )

class ModelConfigManager:
    def __init__(self):
        self.configs = {}

    def add_config(self, config: ModelConfig):
        self.configs[config.vendor] = config

    def get_config(self, vendor: str):
        return self.configs.get(vendor)

    def update_rate_limit(self, vendor: str, new_rate_limit: int):
        if vendor in self.configs:
            self.configs[vendor].rate_limit = new_rate_limit
        else:
            raise ValueError("Vendor not found")

def load_config_from_env():
    config_data = {
        "OpenAI": {
            "vendor": "OpenAI",
            "endpoint": "https://api.openai.com/v1",
            "auth_token": os.environ.get("OPENAI_AUTH_TOKEN", "OPENAI_AUTH_TOKEN"),
            "rate_limit": 100
        },
        "Anthropic": {
            "vendor": "Anthropic",
            "endpoint": "https://api.anthropic.com/v1",
            "auth_token": os.environ.get("ANTHROPIC_AUTH_TOKEN", "ANTHROPIC_AUTH_TOKEN"),
            "rate_limit": 50
        },
        "HuggingFace": {
            "vendor": "HuggingFace",
            "endpoint": "https://api.huggingface.co/v1",
            "auth_token": os.environ.get("HUGGINGFACE_AUTH_TOKEN", "HUGGINGFACE_AUTH_TOKEN"),
            "rate_limit": 200
        }
    }
    manager = ModelConfigManager()
    for vendor, data in config_data.items():
        config = ModelConfig.from_dict(data)
        manager.add_config(config)
    return manager
