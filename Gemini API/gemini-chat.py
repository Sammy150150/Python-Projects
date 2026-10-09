from google import genai

client = genai.Client()
chat = client.chats.create(model="gemini-3-flash-preview")

while True:
    response = chat.send_message_stream(input("> "))
    for chunk in response:
        print(chunk.text, end="")
