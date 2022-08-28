from setuptools import setup, find_packages

setup(
    name='vowelcheck',
    version='1.0.0',
    packages=find_packages(where="code"),
    package_dir={"": "code"},
    url='',
    license='MIT',
    author='Yagmur Bayraktar',
    author_email='ybbayrak@ncsu.edu',
    description='CSC510 Homework 1 Setup'
)
