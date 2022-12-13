import yaml
import shutil
import os

PREFERENCE_DIR = '.mkdocs'
DOCKS_DIR = 'docs'

print('INFO - mkdir docs')
os.makedirs(DOCKS_DIR, exist_ok=True)

with open(f'{PREFERENCE_DIR}/conf.yml') as conf_file:
  conf = yaml.safe_load(conf_file)

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

  if 'files' in conf:
    for file in conf['files']:
      print(f'INFO - Moving file: {file}')
      shutil.copy(file, f'{DOCKS_DIR}/{os.path.basename(file)}')

  for doc in conf['docs']:
    print(f'INFO - Moving document: {doc}')
    shutil.copytree(doc, f'{DOCKS_DIR}/{doc}', dirs_exist_ok=True)

  if 'custom_theme' in conf:
    theme = conf['custom_theme']
    print(f'INFO - Moving custom theme dir: {theme}')
    shutil.copytree(f'{PREFERENCE_DIR}/{theme}', theme, dirs_exist_ok=True)
