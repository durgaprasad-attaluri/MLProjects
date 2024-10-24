# it acts like a package for our ml application, anyone can install or import when they use this
from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path: str) -> List[str]: # function return a list
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements]  # Stripping whitespace and newlines

    # '-e .' when we run requirements.txt it automatically triggers setup.py file run
    # Remove '-e .' if present
    if '-e .' in requirements:
        requirements.remove('-e .')

    return requirements

setup(
    # name='mlproject',
    # author='Durga',
    # author_email='loyolite181901@gmail.com',
    name='mlproject',
    version='0.1',
    packages=find_packages(),
    #install_requires=['pandas', 'numpy', 'seaborn'] #- when we have less libraries
    install_requires=get_requirements('requirements.txt'),
)

