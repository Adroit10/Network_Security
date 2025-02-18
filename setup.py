from setuptools import find_packages,setup
from typing import List

def get_requirements() -> List[str]:
    
    req_lst:List[str] = []
    try:
        with open('requirements.txt','r') as f:
            lines = f.readlines()
            for line in lines:
                req = line.strip()
                if req and req != "-e.":
                    req_lst.append(req) 
    except FileNotFoundError:
        print("requirements.txt not found")
    return req_lst

setup(
    name='Network_Security',
    version='0.0.0',
    author='Devansh Tripathi',
    author_email='tripathidevansh7@gmail.com',
    packages=find_packages(),
    install_requires = get_requirements()
)