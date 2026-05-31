from openai import OpenAI
import base64
import pathlib

client = OpenAI()

#Generate text from a simple prompt
response = client.responses.create(
    model="gpt-5.5",
    input="Write a one-sentence bedtime story about a unicorn."
)

print(response.output_text)

#Generate text with instructions
response = client.responses.create(
    model="gpt-5",
    reasoning={"effort": "low"},
    instructions="Talk like a pirate.",
    input="Are semicolons optional in JavaScript?",
)

print(response.output_text)

#Generate text with messages using different roles
response = client.responses.create(
    model="gpt-5",
    reasoning={"effort": "low"},
    input=[
        {
            "role": "developer",
            "content": "Talk like a pirate."
        },
        {
            "role": "user",
            "content": "Are semicolons optional in JavaScript?"
        }
    ]
)
print(response.output_text)

#Generate text with a prompt template
file = client.files.create(
    file=open("draconomicon.pdf", "rb"),
    purpose="user_data",
)
print("File uploaded with ID:", file.id)

response = client.responses.create(
  prompt={
    "id": "pmpt_6a1c5a059118819688153f24f89f0e0306bd4bcd9092feb5",
    "version": "1",
    "variables": {
      "topic": "example topic",
      "reference_pdf": file.id,
    }
  }
)
print("Response with prompt template:")
print(response.output_text)
