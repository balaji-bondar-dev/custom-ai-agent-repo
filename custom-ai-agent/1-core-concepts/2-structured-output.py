#Structured Outputs for chain-of-thought math tutoring
from openai import OpenAI
from pydantic import BaseModel
import json
from typing import List

client = OpenAI()

class Step(BaseModel):
    explanation: str
    output: str

class MathReasoning(BaseModel):
    steps: list[Step]
    final_answer: str

response = client.responses.parse(
    model="gpt-5.5",
    input=[
        {
            "role": "system",
            "content": "You are a helpful math tutor. Guide the user through the solution step by step.",
        },
        {"role": "user", "content": "how can I solve 8x + 7 = -23"},
    ],
    text_format=MathReasoning,
)
# 2. Extract the stringified JSON via response.output_text
raw_json_string = response.output_text

# 3. Safely parse the text into a real Python dictionary / JSON object
json_data = json.loads(raw_json_string)

# Print formatted JSON output
print(json.dumps(json_data, indent=4))


#Refusals with Structured Outputs
completion = client.chat.completions.parse(
model="gpt-5.5",
messages=[
{"role": "system", "content": "You are a helpful math tutor. Guide the user through the solution step by step."},
{"role": "user", "content": "how can I solve 8x + 7 = -23"},
],
response_format=MathReasoning,
)

math_reasoning = completion.choices[0].message

# If the model refuses to respond, you will get a refusal message
print("Refusal message (if any):", math_reasoning.refusal)
if math_reasoning.refusal:
    print(math_reasoning.refusal)
else:
    print(math_reasoning.parsed)



#Handle streaming with Structured Outputs
class EntitiesModel(BaseModel):
    attributes: List[str]
    colors: List[str]
    animals: List[str]

with client.responses.stream(
model="gpt-5.5",
input=[
        {"role": "system", "content": "Extract entities from the input text"},
        {
        "role": "user",
        "content": "The quick brown fox jumps over the lazy dog with piercing blue eyes",
        },
    ],
text_format=EntitiesModel,
) as stream:
    
    for event in stream:
        if event.type == "response.refusal.delta":
            print(event.delta, end="")
        elif event.type == "response.output_text.delta":
            print(event.delta, end="")
        elif event.type == "response.error":
            print(event.error, end="")
        elif event.type == "response.completed":
            print("Completed") # print(event.response.output)

response = stream.get_final_response()
#print(response.output_text)

# 2. Extract the stringified JSON via response.output_text
raw_json_string = response.output_text

# 3. Safely parse the text into a real Python dictionary / JSON object
json_data = json.loads(raw_json_string)

# Print formatted JSON output
print(json.dumps(json_data, indent=4))


