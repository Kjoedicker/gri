
<h1 align="center">Git Repo Init (GRI)</h3>

# About The Project

An easy way to initialize Git repos from the command line

# Usage

Instead of: 

```shell
echo "# hey" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/Kjoedicker/gri.git
git push -u origin main
```

You can do:

```shell
kjnix@arch gri % python3 main.py -gi github -p ./
```

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
