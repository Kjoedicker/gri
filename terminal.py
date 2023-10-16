import os
import subprocess

from typing import Callable
import argparse

bytesToArrayOfStrings: Callable[[bytes], list[str]]  = lambda b: b.decode().strip().split("\n")

parser = argparse.ArgumentParser(
    prog='Gri',
    description='Automatically creates a git repo on your chosen git interface (github, gitlab, gitea..)',
)

parser.add_argument('-gi', '--git-interface')      # option that takes a value
parser.add_argument('-p', '--path') 
parser.add_argument('-v', '--verbose') 

class Terminal:
    def parseCommandLineArguments(self) -> (str, list[str]):
        args = parser.parse_args()
        
        path = args.path if args.path not in [".", "./"] else os.getcwd()
        gitInterface = args.git_interface
        verbose = args.verbose

        return (gitInterface, path, verbose)

    def runSequenceOfCommands(self, commands: list):
        commandChain = " && ".join(commands)
        subprocess.run(commandChain, shell=True, capture_output=True)

    def listDirectory(self, path: str) -> list[str]:
        results = subprocess.run(["ls", path], capture_output=True)
        if (results.returncode):
            return []
        return bytesToArrayOfStrings(results.stdout)
