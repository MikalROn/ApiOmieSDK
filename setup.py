from setuptools import setup, find_packages

VERSION =  '0.4.6'


with open('README.md', 'rt', encoding='utf-8') as arq:
      readme = arq.read()

keywords = [
    'Omie API', 'API Omie', 'Omie integração', 'Omie SDK', 'SDK para Omie', 
    'integração Omie', 'Omie API SDK', 'omieapi', 'apiomiesdk', 'omie sdk', 
    'automatização Omie', 'conexão Omie', 'desenvolvimento Omie', 
    'Omie Python', 'API ERP Omie', 'Omie integração Python', 'Omie API integração',
    'API para Omie', 'Omie API integração'
]

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
      packages=find_packages(exclude=('omieapi/scripts/scrap.py', 'java/*', 'php/*')),
      install_requires=['requests', 'beautifulsoup4', 'pandas', 'httpx'],
      python_requires='>=3',
      project_urls={
            'Demonstrações': 'https://github.com/MikalROn/ApiOmie-nao-oficial/tree/main/demos',
            'Documentação': 'https://MikalROn.github.io/ApiOmieSDK/',
            'Repositório': 'https://github.com/MikalROn/ApiOmie-nao-oficial',
            'Changelog': 'https://github.com/MikalROn/ApiOmie-nao-oficial/blob/main/CHANGELOG.MD',
            'Download PyPI': 'https://pypi.org/project/api-omie/',
            'Documentação Oficial da Omie': 'https://developer.omie.com.br/service-list/',
      }
)