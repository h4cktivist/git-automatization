# git-automatization

## With this Python script, the process of adding a repository to GitHub was automated.

### What does script do?
- Creates new folder with name of your project
- Creates README.md
- Authorizes into your GitHub account and creates new repository
- Does git init, git remote, git commit and push


P.S Idea for script was taken from [@KalleHallden](https://github.com/KalleHallden) I made his script only on Python, without using shell scripts.


### Install

```sh
git clone https://github.com/h4cktivist/git-automatization.git
cd git-automatization
pip install -r requirements.txt
```


### Usage
Put the git-auto.py to directory where you want to create a project.
Then use:
```sh
python git-auto.py
```
