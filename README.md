# CSC-510 Homework 1 - Group 39 - Vowel Checker
[![Build Status](https://app.travis-ci.com/wangz35/CSC-510-HW1.svg?branch=main)](https://app.travis-ci.com/wangz35/CSC-510-HW1)
[![Build Status](https://github.com/wangz35/CSC-510-HW1/actions/workflows/github-actions-build.yml/badge.svg)](https://github.com/wangz35/CSC-510-HW1/actions)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.7023753.svg)](https://doi.org/10.5281/zenodo.7023753)
[![Contributors](https://img.shields.io/github/contributors/wangz35/CSC-510-HW1)](https://github.com/wangz35/CSC-510-HW1/graphs/contributors)
![Supports Python](https://img.shields.io/pypi/pyversions/pytest)
[![GitHub Release](https://img.shields.io/github/release/wangz35/CSC-510-HW1.svg)](https://github.com/wangz35/CSC-510-HW1/releases)

## Description
This repository contains the codework of the project VowelCheck. The aim of this project is to provide a function to determine whether a given character input is a consonant of a vowel. This code provides correct outputs whether the character is given in upper or lower case.
The designated input value for this code should be a single character and the output will be printed out, and if the input is a vowel will be returned 1, 
While using this code, please keep in mind that this code was built for vowels in Latin alphabet (a, e, i, o, u) and does not currently handle other cases. 
## Installation
To install this package, use the following command on the Command Prompt or Terminal.
```
pip install git+https://github.com/wangz35/CSC-510-HW1.git
```
## Example Cases
To view a particular subset of inputs you can download and run the test file.
```
python test.py
A  is vowel
e  is vowel
B  is not vowel
n  is not vowel
```
To try the code with a specific input, please see the following examples.
```
python
>>> import vowelcheck as v
>>> v.vowel('a')
a  is vowel
1
>>> v.vowel('B')
B  is not vowel
0
```
