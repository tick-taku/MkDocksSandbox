import yaml
import shutil

with open('.mkdocs/conf.yml') as file:
  conf = yaml.safe_load(file)
  shutil.copy('.mkdocs/mkdocs.yml', 'docs/')
  shutil.copy(conf['top'], 'docs/')
  for doc in conf['docs']:
    shutil.copytree(doc, f'docs/{doc}', dirs_exist_ok=True)
