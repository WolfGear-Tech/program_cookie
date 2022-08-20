## Welcome to Program Cookie

[![Python](https://img.shields.io/badge/python-3.10-green)](https://www.python.org)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)

Cookiecutter for Python Programs Projects

### Project Requirements

* [Python3.10](https://www.python.org)
* [Poetry](https://python-poetry.org/)

### What is installed?

All dependencies will be installed on his latest versions for:

* PyQt5

### How to use

```shell
# Clone this project
$ git clone https://github.com/WolfGear-Tech/Program-Cookie.git

# Install project dependencies
$ poetry install

# Run `make project` informing your target folder
$ poetry run cookiecutter . -f -o ../

# Go to new project and follow the instructions in INSTALL.md`
```

### Cookiecutter Options
        
| Name                           | Desc                                                | Default Value     |
|:-------------------------------|:----------------------------------------------------|:------------------|
| Project Name                   | The Project Name                                    | Wolf Gear Project |
| Project Name Slug              | Project slug Name                                   | Wolf-Gear-Project |
| Project Name DNS               | Project name for dns                                | wolf-gear-project |
| Project Description            | Brief Project Description for README                | "This project..." |
| Python Version                 | Project Python Version                              | 3.10              |
| Project Squad                  | The squad which will be the CODEOWNER or "No Owner" | No Owner |

### Developing this Project

* Make your alterations inside `{{cookiecutter.project_name_slug}}` folder

