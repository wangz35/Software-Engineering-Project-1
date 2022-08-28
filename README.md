# CSC-510
![image](https://app.travis-ci.com/wangz35/CSC-510.svg?branch=main)
![DOI](https://zenodo.org/badge/528639981.svg)

#Vowel Checker
##Description
This repository contains the codework of the project VowelCheck. The aim of this project is to provide a function to determine whether a given character input is a consonant of a vowel. This code provides correct outputs whether the character is given in upper or lower case.
The designated input value for this code should be a single character and the output will be printed out, and if the input is a vowel will be returned 1, 
While using this code, please keep in mind that this code was built for vowels in Latin alphabet (a, e, i, o, u) and does not currently handle other cases. 
##Installation
To install this package, use the following command on the Command Prompt or Terminal.
```
pip install git+https://github.com/wangz35/CSC-510-HW1.git
```
##Example Cases
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
