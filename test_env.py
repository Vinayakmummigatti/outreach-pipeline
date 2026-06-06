from dotenv import load_dotenv
import os

load_dotenv(dotenv_path=".env")

print("Ocean:", os.getenv("OCEAN_API_KEY"))
print("Prospeo:", os.getenv("PROSPEO_API_KEY"))
print("Eazyreach:", os.getenv("EAZYREACH_API_KEY"))
print("Brevo:", os.getenv("BREVO_API_KEY"))