import os
from pathlib import Path
from dotenv import load_dotenv


# Load environment variables from .env
load_dotenv()


# Base Directory

BASE_DIR = Path(__file__).resolve().parent.parent.parent



# Environment

ENV = os.getenv("ENV", "development")

DEBUG = ENV == "development"


# Security Config


SECRET_KEY = os.getenv("SECRET_KEY", "smart-churn-secret-key")

ALGORITHM = "HS256"

TOKEN_EXPIRE_MINUTES = int(
    os.getenv("TOKEN_EXPIRE_MINUTES", 60)
)


# Server Config

APP_NAME = "Smart Churn Prediction API"

APP_VERSION = "1.0.0"

HOST = os.getenv("HOST", "0.0.0.0")

PORT = int(os.getenv("PORT", 8000))



# Database Config

DB_HOST = os.getenv("DB_HOST", "localhost")

DB_PORT = os.getenv("DB_PORT", "3306")

DB_NAME = os.getenv("DB_NAME", "churn_db")

DB_USER = os.getenv("DB_USER", "churn_user")

DB_PASSWORD = os.getenv("DB_PASSWORD", "1009")


DATABASE_URL = (
    f"mysql+pymysql://{DB_USER}:"
    f"{DB_PASSWORD}@"
    f"{DB_HOST}:"
    f"{DB_PORT}/"
    f"{DB_NAME}"
)


# Model Paths


MODEL_DIR = BASE_DIR / "data" / "models"

BEST_MODEL_PATH = MODEL_DIR / "best_model.pkl"


# Data Paths


DATA_DIR = BASE_DIR / "data"

RAW_DATA_DIR = DATA_DIR / "raw"

PROCESSED_DATA_DIR = DATA_DIR / "processed"



# Logging Config

LOG_DIR = BASE_DIR / "logs"

LOG_FILE = LOG_DIR / "app.log"

# Feature Config

FEATURE_ORDER = [
    "payment_delay_flag",
    "low_usage_flag",
    "support_intensity",
    "account_age_days",
    "days_since_last_login",
    "failed_payments_count"
]



# Validation

def validate_config():
    """
    Validate critical configs on startup
    """

    if not BEST_MODEL_PATH.exists():
        raise FileNotFoundError(
            f"Model not found: {BEST_MODEL_PATH}"
        )

    if not DATA_DIR.exists():
        raise FileNotFoundError(
            f"Data directory missing: {DATA_DIR}"
        )


# Print (Debug Only)

if DEBUG:

    print("Running in Development Mode")
    print("Base Dir:", BASE_DIR)
    print("Model Path:", BEST_MODEL_PATH)
