from setuptools import setup, find_packages
from typing import List
import os
def get_requirements(file_path: str) -> List[str]:
    '''
    This function returns a list of requirements
    '''
    requirements = []
    if os.path.exists(file_path):
        with open(file_path) as file_obj:
            requirements = file_obj.readlines()
            requirements = [req.strip() for req in requirements]
    return requirements

setup(
    name='Project1',
    version='0.0.1',
    author='Deepanshu',
    author_email='deepanshuthakur9756@gmail.com',
    description='A short description of your project',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)
