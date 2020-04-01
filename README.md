# Pre-commit-hooks

[![Python: 3.7](https://img.shields.io/badge/Python-3.7-yellow)](https://www.python.org/)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Pre-commit Git hooks I use in my internal projects.

Works with Python 3.6 or newer. Can be used in conjunction with [pre-commit](https://github.com/pre-commit/pre-commit).

## Content
So far, there's only one hook.

- `clean-requirements`: Remove unused or wrong entries from requirements.txt. Used mainly to solve
   [this bug](https://bugs.launchpad.net/ubuntu/+source/python-pip/+bug/1635463).
