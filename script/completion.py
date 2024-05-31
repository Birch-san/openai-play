import argparse
import openai
from typing import Literal

def main():
  # parse args:
  parser = argparse.ArgumentParser(description='Legacy completion API.')
  parser.add_argument('--model', default='gpt-4o', type=str, nargs='?', choices=['gpt-3.5-turbo-instruct', 'gpt-3.5-turbo', 'gpt-4', 'gpt-4o'], required=True)
  args = parser.parse_args()

  model: Literal['gpt-3.5-turbo-instruct', 'gpt-3.5-turbo', 'gpt-4', 'gpt-4o'] = args.model

  openai.organization = "org-YOURORGHERE"
  openai.api_key = open('key.txt', 'r').read().strip()
  # models = openai.Model.list()
  # [model.id for model in models.data]

  acc = ''
  for chunk in openai.Completion.create(
    model=model,
    prompt="Say this is a test",
    max_tokens=512,
    temperature=0,
    stream=True
  ):
    new_text: str = chunk['choices'][0]['text']
    print(new_text, end='', flush=True)
    acc += new_text
  pass

if __name__ == '__main__':
  main()