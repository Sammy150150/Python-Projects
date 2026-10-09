
from google import genai

# The client gets the API key from the environment variable `GEMINI_API_KEY`.
client = genai.Client()

dummy_text = client.files.upload(file="dummytext.txt")

response = client.models.generate_content_stream(
    model="gemini-3-flash-preview", 
    contents=["Rewrite this text with the first letter of each word", dummy_text]
)

for stream in response:
    print(stream.text)
