from setuptools import setup, find_packages
import shutil

with open('requirements.txt', 'r') as f:
    f = f.readlines()

setup(name = 'PyDClass',
      version = 1.0,
      author = 'VitriSnake',
      author_email = 'vitrisnake@celtiumc.fr',
      maintainer = 'CeltiumC',
      maintainer_email = 'contact@celtiumc.fr',
      description = 'PyDClass is a simple web class diagram generator',
      license = 'GPLv3.0',
      install_requires = f,
      packages = find_packages(),
      package_data={'pydclass.templates': ['*'], 'pydclass.static': ['*']},
      include_package_data=True, 
      scripts=[
          'bin/pydclass',
      ],
      zip_safe=False
     )
