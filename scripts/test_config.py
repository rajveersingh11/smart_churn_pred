from app.core.config import (
    ENV,
    SECRET_KEY,
    PORT,
    BEST_MODEL_PATH,
    DATABASE_URL
)

def main():

    print("ENV:", ENV)
    print("SECRET_KEY:", SECRET_KEY)
    print("PORT:", PORT)
    print("MODEL PATH:", BEST_MODEL_PATH)
    print("DB URL:", DATABASE_URL)


if __name__ == "__main__":
    main()
