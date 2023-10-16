
<h1 align="center">Git Repo Init (GRI)</h3>

# About The Project
Allows you to initialize and create remote repos on the Git interface of your choosing

# Usage

## Options

```shell
usage: Gri [-h] [-gi GIT_INTERFACE] [-p PATH]

Automatically creates a git repo on your chosen git interface (github, gitlab, gitea..)

options:
  -h, --help            show this help message and exit
  -gi GIT_INTERFACE, --git-interface GIT_INTERFACE
  -p PATH, --path PATH
  -v VERBOSE, --verbose VERBOSE
```

## Example
```shell
kjnix@arch gri % python3 main.py -gi github -p ./
```