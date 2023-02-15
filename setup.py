from setuptools import setup
import os


with open('README.md', 'rt') as arq:
      readme = arq.read()

keywords = ['Api omie', 'omie', 'api do omie', 'omieapi']

setup(name='omieapi',
      version='0.0.1',
      license='MIT license',
      author='Daniel Coêlho',
      long_description=readme,
      long_description_content_type='text/markdown',
      author_email='heromon.9010@gmail.com',
      keywords=keywords,
      description='Ferramenta para api do omie não oficial',
      packages=['omieapi'],
      install_requires=['requests']
)