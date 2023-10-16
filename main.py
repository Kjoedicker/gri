import os
import logging

from typing import Callable

from git import Git
from terminal import Terminal

parseDirectoryNameFromPath: Callable[[str], str] = lambda path: path.replace("/", " ").split()[-1]

if __name__ == '__main__':
    logging.basicConfig(format='%(levelname)s: %(message)s', level=20)

    terminal = Terminal()

    (gitInterface, path, verbose) = terminal.parseCommandLineArguments()

    git = Git(gitInterface, verbose)

    if not os.path.isdir(path):
        logging.error(f"{path} is not a valid path")
        exit(0)
    if git.hasGitRepo(path):
        logging.info(f"Skipping. {path} is already a git repo")
        exit(0)

    git.init(path)
    directoryName = parseDirectoryNameFromPath(path)

    (remote, error) = git.createRepository(directoryName)
    if error:
        logging.error(f"Creating github repo for {directoryName}: {error}")
        exit(0)

    git.addRemote(path, remote)
    git.push(path)