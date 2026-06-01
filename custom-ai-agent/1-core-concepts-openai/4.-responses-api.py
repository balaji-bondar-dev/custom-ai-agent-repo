from openai import OpenAI
client = OpenAI()

response = client.responses.create(
    model="gpt-5",
    instructions="You are a helpful assistant.",
    input="Hello!"
)
print(response.output_text)


#Multi-turn conversation
response1 = client.responses.create(
    model="gpt-5",
    input="What is the capital of France?",
    store=True
)
print('First resposne')
print(response1.output_text)

response2 = client.responses.create(
    model="gpt-5",
    input="And its population?",
    previous_response_id=response1.id,
    store=True
)
print('Second resposne')
print(response2.output_text)


#Multi-turn conversation & Store=False
input_list = [{  "role": "user", "content": "Explain why is the sky blue." } ]

response1 = client.responses.create(
    model="gpt-5",
    input=input_list,
    store=False,
    include=['reasoning.encrypted_content']
)
print('First resposne')
#print(response1.output)
print(response1.output_text)

input_list.extend(response1.output)
input_list.append({  "role": "user", "content": "Can you summarize it in one sentence?" })

response2 = client.responses.create(
    model="gpt-5",
    input=input_list,
    #previous_response_id=response1.id,
    store=False,
    include=['reasoning.encrypted_content']
)
print('Second resposne')
#print(response2.output)
print(response2.output_text)

#Structured output with using Pydantic library
response = client.responses.create(
  model="gpt-5",
  input="Balaji, 45 years software engineer", 
  text={
    "format": {
      "type": "json_schema",
      "name": "person",
      "strict": True,
      "schema": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "minLength": 1
          },
          "age": {
            "type": "number",
            "minimum": 0,
            "maximum": 130
          }
        },
        "required": [
          "name",
          "age"
        ],
        "additionalProperties": False
      }
    }
  }
)
print(response.output_text)


