
import openai
from openai import OpenAI
client = OpenAI(
    api_key="sk-some-key"
)

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a flamboyant host"},
    {"role": "user", "content": "please greet me"}
  ]
)

print(completion.choices[0].message)
