from setuptools import setup


with open('README.md', 'rt', encoding='latin-1') as arq:
      readme = arq.read()

keywords = ['Api omie', 'omie', 'api do omie', 'omieapi']

setup(name='api-omie',
      version='0.1.1',
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