from setuptools import setup, find_packages
import shutil

setup(name = 'PyDClass',
      version = 0.5,
      author = 'VitriSnake',
      author_email = 'vitrisnake@celtiumc.fr',
      maintainer = 'CeltiumC',
      maintainer_email = 'contact@celtiumc.fr',
      description = 'PyDClass is a simple web class diagram generator',
      license = 'GPLv3.0',
      packages = find_packages(),
      package_data={'pydclass.templates': ['*'], 'pydclass.static': ['*']},
      include_package_data=True, 
      scripts=[
          'bin/pydclass',
      ],
      zip_safe=False,
      url='https://github.com/CeltiumCDev/PyDClass',
      keywords='diagram class project python generator web svg',
      install_requires=[
          'flask',
          'graphviz',
          'ipdb'
      ],
     )
