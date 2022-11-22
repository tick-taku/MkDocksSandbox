import yaml
import shutil
import os

print('INFO - mkdir docs')
os.makedirs('docs/', exist_ok=True)

with open('.mkdocs/conf.yml') as file:
  conf = yaml.safe_load(file)

  print('INFO - Moving config file: mkdocs.yml')
  shutil.copy('.mkdocs/mkdocs.yml', './')

  top_md = conf['top']
  print(f'INFO - Moving top md file: {top_md}')
  shutil.copy(top_md, 'docs/')

  for doc in conf['docs']:
    print(f'INFO - Moving document: {doc}')
    shutil.copytree(doc, f'docs/{doc}', dirs_exist_ok=True)
