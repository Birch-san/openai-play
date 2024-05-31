import argparse
from typing import Literal
from openai import OpenAI

client = OpenAI(
  api_key=open('key.txt', 'r').read().strip(),
  organization='org-YOURORGHERE',
)

def main():
  # parse args:
  parser = argparse.ArgumentParser(description='Legacy completion API.')
  parser.add_argument('--model', default='gpt-4o', type=str, nargs='?', choices=['gpt-3.5-turbo-instruct', 'gpt-3.5-turbo', 'gpt-4', 'gpt-4-1106-preview', 'gpt-4-turbo', 'gpt-4-turbo-preview', 'gpt-4-turbo-2024-04-09', 'gpt-4o'], required=True)
  args = parser.parse_args()

  model: Literal['gpt-3.5-turbo-instruct', 'gpt-3.5-turbo', 'gpt-4', 'gpt-4-1106-preview', 'gpt-4-turbo', 'gpt-4-turbo-preview', 'gpt-4-turbo-2024-04-09', 'gpt-4o'] = args.model

  # models = openai.Model.list()
  # [model.id for model in models.data]

  acc = ''
  for chunk in client.chat.completions.create(
    model=model,
    messages=[
      {"role": "system", "content": "You are a helpful assistant."},
      {"role": "user", "content": f'''In PyTorch: how can I fuse a multiplicative factor into a matrix multiplication?'''},
    ],
    max_tokens=4096,
    stream=True,
  ):
    new_text = ''
    delta = chunk.choices[0].delta
    if delta.role is not None:
      role_raw = delta.role
      # capitalize first character of role
      role = role_raw[0].upper() + role_raw[1:]
      new_text += f'{role}: '
    if delta.content is not None:
      new_text += delta.content

    print(new_text, end='', flush=True)
    acc += new_text

if __name__ == '__main__':
  main()