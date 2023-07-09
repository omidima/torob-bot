from dotenv import load_dotenv
import os

load_dotenv()

generate_auto_desc = os.getenv("AUTO_DESC")
api_key = os.getenv("NARANGI_API_KEY")