from setuptools import setup, find_packages

setup(name='Pokemail',
      version='0.0.1',
      description='Pokemail, a wrapper around guerillamail.com\'s pokemail service',
      author='Cody Quist',
      author_email='codyjquist@gmail.com',
      url='https://github.com/nubonics/pokemail',
      packages=find_packages(),
      install_requirements=['requests'],
      keywords=['pokemail', 'guerillamail', 'disposable email', 'email'],
      classifiers=[
          "Development Status :: 1 - Planning",
          "Intended Audiences :: Developers",
          "Programming Language :: Python :: 3",
          "Operating System :: Unix",
          "Operating System :: MacOS :: MacOS",
          "Operating System :: Microsoft :: Windows",
      ]
     )