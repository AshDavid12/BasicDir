import openai
from langsmith.wrappers import wrap_openai
from langsmith import traceable
from dotenv import load_dotenv

#smith.env has keys
load_dotenv('smith.env')


# Auto-trace LLM calls in-context
client = wrap_openai(openai.Client())


completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
    {"role": "user", "content": "write one sentence explaining python."}
  ]
)


# @traceable # Auto-trace this function
# def pipeline(user_input: str):
#     result = client.chat.completions.create(
#         messages=[{"role": "user", "content": user_input}],
#         model="gpt-3.5-turbo"
#     )
#     return result.choices[0].message.content

# pipeline("Hello, give me a name for an American resturant")
# # Out:  Hello there! How can I assist you today?
