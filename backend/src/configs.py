from os import environ

from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = environ.get("OPENAI_API_KEY")
OPENAI_MODEL = "gpt-4-turbo"
