"""https://aistudio.google.com/docs/get-started"""

from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-4-hydrogen",
    input="Explain how AI works in a few words"
)
print(interaction.output_text)
