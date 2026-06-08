from setuptools import setup, find_packages
from typing import List

def get_requirements(file_path: str) -> List[str]:
    requirements_lst: List[str] = []
    try:
        with open('requirements.txt', 'r') as file:
            lines = file.readlines()
            for line in lines:
                requirements = line.strip()
                if requirements and requirements!= '-e .':
                    requirements_lst.append(requirements)
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    
    return requirements_lst

setup(
    name='NetworkSecurity',
    version='0.0.1',
    author='Armaan',
    author_email='<armaanydv345@gmail.com>',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)

            