# website-status-cli

[![PyPI version](https://badge.fury.io/py/website_up.svg)](https://badge.fury.io/py/website_up)
[![License](http://img.shields.io/:license-mit-blue.svg)](http://doge.mit-license.org)

Check the status of any website by getting status code of the website or simple True - False i.e., if it is up or not using command line

## Installation
### Using pip
```pip
pip install website_up
```
### Using Git
```
git clone https://github.com/prabhakar267/website-status-cli.git
cd website-status-cli
python setup.py install
```

## Usage
```
website-status [OPTIONS]

Options:
  --url       URL whose status is to be checked [string]
  --code      If set, then returns status code of the URL passed [flag]
  --f         Number of seconds after which the check is to be repeated [integer]
  --help      Show help
```


