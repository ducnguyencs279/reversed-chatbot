"""Application entry point."""

from app.api.routes import create_app


app = create_app()


if __name__ == "__main__":
    print("reversed-chatbot application scaffold is ready.")
