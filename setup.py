from setuptools import setup, find_packages

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()


setup(name ='Bogidden', # 패키지 명

version ='2.1.3.5',

long_description = long_description,

long_description_content_type='text/markdown',

description = 'A module containing only basic functions',

author='Aqouthe',

author_email ='hoonie0929@gmail.com',

url = '',

license = 'MIT', # MIT에서 정한 표준 라이센스 따른다

py_modules = ['Aqouthe_', 'Aqouthe_module'], # 패키지에 포함되는 모듈

python_requires = '>=3',

install_requires = [], # 패키지 사용을 위해 필요한 추가 설치 패키지

packages = ['ko_pack'] # 패키지가 들어있는 폴더들

)