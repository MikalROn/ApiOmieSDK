from setuptools import setup, find_packages

VERSION =  '0.2.8'


with open('README.md', 'rt', encoding='latin-1') as arq:
      readme = arq.read()

keywords = ['Api omie', 'omie', 'api do omie', 'omieapi']

setup(name='api-omie',
      url='https://github.com/MikalROn/ApiOmie-nao-oficial',
      version= VERSION,
      license='MIT license',
      author='Daniel Coêlho',
      long_description=readme,
      long_description_content_type='text/markdown',
      author_email='heromon.9010@gmail.com',
      keywords=keywords,
      classifiers=[
            "Development Status :: 3 - Alpha"
      ],
      description='Ferramenta para api do omie não oficial',
      packages=find_packages(exclude=('scrap.py')),
      install_requires=['requests', 'beautifulsoup4'],
      python_requires='>=3',
      project_urls={
            'Demonstrações': 'https://github.com/MikalROn/ApiOmie-nao-oficial/tree/main/demos',
      }
)