
from setuptools import setup, find_packages
import os
# Get the directory name of the absolute file path


setup(
    name='identicons',
    version='0.1.0',
    description="""A lightweight, easy-to-use Python package for generating unique identicons - graphical representations of hashed user information. It's perfect for adding a touch of personalization to user profiles in web applications, forums, or any platform requiring distinct visual user identification.""",
    author='Luca Vivona',
    author_email='lucavivona01@gmail.com',
    packages=find_packages(exclude=("tests",)),
    install_requires=[
        'numpy>=1.13.3',
        'rich>=13.6.0'
    ],
    entry_points={
        'console_scripts': [
            'identicons=identicons.cli:main',
        ],
    },
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/LVivona/identicons/tree/main',
classifiers=[
    # Specify the Python versions you support here. In particular, ensure
    # that you indicate whether you support Python 2, Python 3 or both.
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
    'Programming Language :: Python :: 3.11',

    # Pick your license as you wish
    'License :: OSI Approved :: MIT License',

    # Specify the development status of your package
    'Development Status :: 3 - Alpha',  # 4 - Beta or 5 - Production/Stable

    # Define the audience and the environment where your package will run
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Libraries :: Python Modules',

    # Other classifiers...
    'Operating System :: OS Independent',
    'Natural Language :: English',
    'Environment :: Console',
    'Topic :: Utilities',
]

)
