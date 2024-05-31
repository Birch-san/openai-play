import argparse
from typing import Literal
from openai import OpenAI

client = OpenAI(
  api_key=open('key.txt', 'r').read().strip(),
  organization='org-YOURORGHERE',
)

# TODO: need to figure out how to get this working in the newer OpenAI SDK (it rejects these models as being chat models, but I think the older SDK allowed it).
def main():
  # parse args:
  parser = argparse.ArgumentParser(description='Legacy completion API.')
  parser.add_argument('--model', default='gpt-4o', type=str, nargs='?', choices=['gpt-3.5-turbo-instruct', 'gpt-3.5-turbo', 'gpt-4', 'gpt-4o'], required=True)
  args = parser.parse_args()

  model: Literal['gpt-3.5-turbo-instruct', 'gpt-3.5-turbo', 'gpt-4'] = args.model

  # models = openai.Model.list()
  # [model.id for model in models.data]

  acc = ''
  for chunk in client.completions.create(
    model=model,
    prompt="Say this is a test",
    max_tokens=512,
    temperature=0,
    stream=True,
  ):
    new_text: str = chunk.choices[0].text
    print(new_text, end='', flush=True)
    acc += new_text
  pass

if __name__ == '__main__':
  main()