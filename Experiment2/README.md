# Experiment 2

# Explore Git and GitHub commands

# Git

Git is a distributed version control system that helps developers collaborate on projects. It allows you to track changes, revert to previous stages, and branch to create separate lines of development.

# GitHub

GitHub is a web-based platform that uses Git for version control. It provides a collaborative environment for developers to host and review code, manage projects, and build software together.

## Git commands

- `git init`: Initialize a new Git repository
- `git clone <repository>`: Clone an existing repository
- `git status`: Show the working directory status
- `git add <file>`: Add a file to the staging area
- `git commit -m "message"`: Commit changes with a message
- `git log`: Show the commit history
- `git branch`: List, create, or delete branches
- `git checkout <branch>`: Switch to a different branch
- `git merge <branch>`: Merge a branch into the current branch
- `git pull`: Fetch and merge changes from a remote repository
- `git pull origin <branch>`: Fetch and merge changes from a remote repository branch
- `git push`: Push changes to a remote repository
- `git push origin <branch>`: Push changes to a remote repository branch

### About gh

`gh` is GitHub's official command-line tool. It brings GitHub's features to your terminal, allowing you to interact with GitHub repositories, issues, pull requests, and more directly from the command line. This tool helps streamline your workflow by integrating GitHub operations into your existing terminal commands.

#### gh commands

- `gh auth login`: Authenticate with your GitHub account
- `gh repo create`: Create a new repository on GitHub
- `gh repo clone <repository>`: Clone a GitHub repository
- `gh repo fork <repository>`: Fork a repository on GitHub
- `gh issue list`: List issues in a repository
- `gh issue create`: Create a new issue in a repository
- `gh pr list`: List pull requests in a repository
- `gh pr create`: Create a new pull request
- `gh pr merge <pull-request>`: Merge a pull request

### Pull request creation in GitHub

A pull request (PR) is a method of submitting contributions to a project. It allows you to notify project maintainers about changes you'd like them to consider. Here's how to create a pull request in GitHub:

1. **Fork the repository**: Create a copy of the repository under your own GitHub account.
2. **Clone the repository**: Clone the forked repository to your local machine using `git clone <repository-url>`.
3. **Create a new branch**: Create a new branch for your changes using `git checkout -b <branch-name>`.
4. **Make your changes**: Make the necessary changes to the codebase.
5. **Commit your changes**: Commit your changes with a descriptive message using `git commit -m "Your commit message"`.
6. **Push your changes**: Push the changes to your forked repository using `git push origin <branch-name>`.
7. **Create the pull request**: Go to the original repository on GitHub and click on the "New pull request" button. Select the branch you pushed your changes to and create the pull request.

Once the pull request is created, the project maintainers will review your changes and decide whether to merge them into the main codebase.
