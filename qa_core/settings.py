from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field
from pathlib import Path
import yaml, os

class Settings(BaseSettings):
    api_base_url: str
    api_key: str
    client_id: str

    model_config = SettingsConfigDict(env_prefix="QA_", case_sensitive=False)

def load_settings(env: str | None = None) -> Settings:
    env = env or os.getenv("QA_ENV", "base")
    cfg_dir = Path(__file__).parent / "config"
    with open(cfg_dir / "base.yaml", "r", encoding="utf-8") as f:
        base = yaml.safe_load(f) or {}
    return Settings(**base)
