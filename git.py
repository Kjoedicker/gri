from terminal import Terminal
from github import Github

class Git(Terminal):
    def __init__(self, gitInterface: str, verbose=False):
        self.verbose = verbose

        match gitInterface:
            case "github":
                self.gitInterface = Github()
            case _:
                print(f"{gitInterface} is currently not implemented as an interface")
                exit(1)

    def init(self, path):
        if self.verbose:
            print("Initializing repo...")

        commands = [
            "cd " + path,
            "git init .",
            "git add .",
            "git commit -m 'Initial commit'",
        ]
        self.runSequenceOfCommands(commands)

    def addRemote(self, path, remote):
        if self.verbose:
            print("Adding remote...")

        commands = [
            f"cd {path}",
            f"git remote add origin {remote}",
            "git remote -v"
        ]
        self.runSequenceOfCommands(commands)

    def push(self, path: str):
        if self.verbose:
            print("Pushing main branch...")

        commands = [
            f"cd {path}",
            "git branch -M main",
            "git push -u origin main",
        ]
        self.runSequenceOfCommands(commands)

    def hasGitRepo(self, path: str) -> bool:
        files = self.listDirectory(path + " .git")
        return bool(len(files))

    def createRepository(self, name: str) -> (str, bool):
        if self.verbose:
            print("Creating remote repo")

        return self.gitInterface.createRepository(name)