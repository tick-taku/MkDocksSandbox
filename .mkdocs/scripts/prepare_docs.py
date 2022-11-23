import yaml
import shutil
import os

PREFERENCE_DIR = '.mkdocs'
DOCKS_DIR = 'docs'

print('INFO - mkdir docs')
os.makedirs(DOCKS_DIR, exist_ok=True)

with open(f'{PREFERENCE_DIR}/conf.yml') as file:
  conf = yaml.safe_load(file)

  print('INFO - Moving config file: mkdocs.yml')
  shutil.copy(f'{PREFERENCE_DIR}/mkdocs.yml', './')

  if 'top' in conf:
    top_md = conf['top']
    print(f'INFO - Moving top md file: {top_md}')
    shutil.copy(top_md, f'{DOCKS_DIR}/{os.path.basename(top_md)}')

  if 'logo' in conf:
    logo = conf['logo']
    print(f'INFO - Moving logo image file: {logo}')
    shutil.copy(logo, f'{DOCKS_DIR}/{os.path.basename(logo)}')

  if 'favicon' in conf:
    favicon = conf['favicon']
    print(f'INFO - Moving favicon image file: {favicon}')
    shutil.copy(favicon, f'{DOCKS_DIR}/{os.path.basename(favicon)}')

  if 'mds' in conf:
    for md in conf['mds']:
      print(f'INFO - Moving md file: {md}')
      shutil.copy(md, f'{DOCKS_DIR}/{os.path.basename(md)}')

  for doc in conf['docs']:
    print(f'INFO - Moving document: {doc}')
    shutil.copytree(doc, f'{DOCKS_DIR}/{doc}', dirs_exist_ok=True)
