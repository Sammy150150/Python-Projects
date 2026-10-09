import os
from google import genai
from google.genai import types

client = genai.Client(
    api_key=os.environ.get("GEMINI_API_KEY"),
)

model = "gemini-3-flash-preview"
contents = [
    types.Content(
        role="user",
        parts=[
            types.Part.from_text(text=input("> ")),
        ],
    ),
]
generate_content_config = types.GenerateContentConfig(
    thinking_config=types.ThinkingConfig(
        thinking_level="HIGH",
    ),
)

for chunk in client.models.generate_content_stream(
    model=model,
    contents=contents,
    config=generate_content_config,
):
    if text := chunk.text:
        print(text, end="")
