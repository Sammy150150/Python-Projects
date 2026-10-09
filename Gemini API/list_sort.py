from google import genai

client = genai.Client();

numberList = input("Number list:")

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents="Sort this list from smallest to greatest: "+numberList
)

print(response.text)
