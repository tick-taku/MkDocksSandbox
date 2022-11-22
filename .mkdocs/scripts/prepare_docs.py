import yaml
import shutil

with open('.mkdocs/conf.yml') as file:
  conf = yaml.safe_load(file)
  print('Move mkdocs.yml to docs')
  shutil.copy('.mkdocs/mkdocs.yml', 'docs/')
  print('Move top md to docs')
  shutil.copy(conf['top'], 'docs/')
  for doc in conf['docs']:
    print(f'Move {doc} to docs/')
    shutil.copytree(doc, f'docs/{doc}', dirs_exist_ok=True)
