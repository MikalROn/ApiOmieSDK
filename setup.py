from setuptools import setup, find_packages

VERSION =  '0.4.6.1'


with open('README.md', 'rt', encoding='utf-8') as arq:
      readme = arq.read()

keywords = [
    'Omie API',
    'Omie SDK',
    'Omie integração',
    'Omie Python',
    'API Omie SDK',
    'Omie ERP',
    'Omie automação',
    'Python Omie',
    'Omie API integração',
    'Omie developer',
    'Omie finanças',
    'Omie CRM',
    'Python ERP integração',
    'Omie Brasil',
    'ERP integração Python'
]

classifiers = [
    "Development Status :: 3 - Alpha",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Topic :: Software Development :: Libraries :: Python Modules",
    "Topic :: Office/Business :: Financial :: Accounting"
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
      classifiers=classifiers,
      description='SDK em Python para integração não oficial com a API do Omie ERP',
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
