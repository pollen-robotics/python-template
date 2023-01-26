# Python Guidelines and Coding style

Template code and examples for python project respecting the [PEP8 coding style](https://peps.python.org/pep-0008/).

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black) ![linter](https://github.com/pollen-robotics/python-coding-guidelines/actions/workflows/lint.yml/badge.svg) ![pytest](https://github.com/pollen-robotics/python-coding-guidelines/actions/workflows/pytest.yml/badge.svg) ![coverage](https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/FabienDanieau/58642e8fe4589e710e26627e39ff92d7/raw/covbadge.json)



## Configuration

### git

A *.gitignore* file makes sure that the Python temporary files are not committed. It is adapted from [here](https://github.com/github/gitignore/blob/main/Python.gitignore).

git LFS is configured to handle all non script files (3D models, deep learning model, images, etc.). The list of file is defined in *.gitattributes.* Also, a good practice is to use another repo as a submodule containing all the data.

A git hook can be installed to automatically checks PEP8 compliance before a commit. See *scripts/git_hooks*.

### IDE - Linting

Visual code is the recommended IDE. Make sure to install the python extension and [configure](https://dev.to/adamlombard/how-to-use-the-black-python-code-formatter-in-vscode-3lo0) VS code to automatically format the code with [black](https://black.readthedocs.io).

[Flake8](https://flake8.pycqa.org) will perform complementary checks. Select *flake8* as the [linter for VS Code](https://code.visualstudio.com/docs/python/linting). Errors should be directly indicated within the code.

**A code not compliant with PEP8 guidelines will not be merged.**

## Workflow

### Branches

The git workflow is based on [gitflow](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow):

![git workflow](docs/branches.svg)

The default branch is **develop** which is the working branch. **main** is dedicated to stable code (release) only. Both of them are protected, no one should push directly into them. Any new development **MUST** be done in a feature branch, forked from develop, and then merged back to develop through a pull request. When a code considered to be stable, develop can be also merged to main with a pull request.

### Issues

The issue system is a great tool to track problem, bugs, new features, etc. Commits and branches can be linked to a feature. Thus, before any development, a new issue **MUST** be created.

### Procedure

1. Create an [issue](https://github.com/pollen-robotics/unity-workflow/issues) with the *New Issue* button. Document the problem as much as possible (images, url, ...)
2. Create a new branch. The easiest way is to do it directly from the [issue](https://github.blog/changelog/2022-03-02-create-a-branch-for-an-issue/). Thus, all branch names will be consistent, and the PR will directly close the issue.
3. Checkout your branch locally:
 ```
 git fetch origin
 git checkout <branch-name>
 ```
4. Work in the local branch and commit often. Each commit must be formatted as
 ```
<tag> #<issue number> : <message>
 ```
 With *tag* being fix, bug or any label from the issue system, *issue number* the number of the issue, and *message* the mandatory message associated to the commit. Issue number is important so github can link the commit to the issue.
 
 5. Create unit test to validate the new code (see below).

 6. When the work is implemented, create a *pull request*. Easiest way is to do it from the branch page of the repo.
 
 7. At the PR creation, unit tests will be computed and result reported. The branch will not be merged until they pass. Besides, the project is configured so a developer cannot merge his/her own code. An external review is mandatory.
 8. Merge is completed, go to step 1.

 ### Unit tests and test coverage

 Unit tests must be written to ensure code robustness. [Pytest](https://docs.pytest.org) is the recommended tool. Examples are provided in the *tests* folder.
 
It is recommended to have at least 90% of the code tested. The [coverage](https://coverage.readthedocs.io) package provide this metric.

 The developer must run the test locally before committing any new code. Make sure that *pytest* and *coverage* are installed and run at the root level:
 ```
 coverage run -m pytest
 ```
Then, if all tests are sucessful:
 ```
 coverage report
 ```
 These tests are automatically performed by a github action when a pull request is created.