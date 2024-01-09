
from setuptools import setup, find_packages
import os
# Get the directory name of the absolute file path
directory_name = os.path.dirname(os.path.abspath(__file__))
print(os.path.join(directory_name, 'requirements.txt'))
with open(os.path.join(directory_name, 'requirements.txt')) as f:
    required = f.read().splitlines()

print(required)
setup(
    name='identicon',
    version='0.1.0',
    description="""A lightweight, easy-to-use Python package for generating unique identicon - graphical representations of hashed user information. It's perfect for adding a touch of personalization to user profiles in web applications, forums, or any platform requiring distinct visual user identification.""",
    author='Luca Vivona',
    author_email='lucavivona01@gmail.com',
    packages=find_packages(),
    install_requires=required,
    entry_points={
        'console_scripts': [
            'identicon=identicon.cli:main',
        ],
    },
)
