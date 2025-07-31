from dotenv import load_dotenv
load_dotenv()

# pip install google-genai
from google import genai
client = genai.Client()

image = client.files.upload(file="일출.jpg")

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=[image, "이 사진에 대해 설명해줘"],
)

print(response.text)
