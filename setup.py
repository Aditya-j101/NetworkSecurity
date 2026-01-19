from setuptools import find_packages, setup
from typing import List

def get_requirements()->List[str]:
    """This function will return list of requirements"""
    requirment_lst:List[str] = []
    try:
        with open("requirements.txt","r") as file:
            #Readlines from the file
            lines = file.readlines()
            for line in lines:
                requirment = line.strip()
                ## Ignore empty lines and -e.
                if requirment and requirment != '-e .':
                    requirment_lst.append(requirment)
    except FileNotFoundError:
        print("requirements.txt file not found")
    
    return requirment_lst

setup(
    name = "NetworkSecurity",
    version = "0.0.1",
    author = "Aditya Jaiswal",
    author_email = "adi13jaiswal@gmail.com",
    packages = find_packages(),
    install_requires = get_requirements()
)

