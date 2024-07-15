# Git Documentation

## Git Commands

- see what brach you’re on - `git branch`
- move to a differnt branch - `git checkout newbranch`
- commit change - `git commit -m ‘msg’` (make sure you’re on the right branch)
- pushing change to the main - `git push origin main` (after that you see in on GitHub)
- this lists all the ignored files like .env - `git status --ignored` 
- pushing change to a diffrent branch - `git push origin newbranch`
- When you switch branches you can notice the on VSC the file also changes.
    - say you have a file app.py, when you do git checkout newb then the open file will be the one that the newb has. When you switch back to main branch then the open file will change.

### Tips

- revert back to previous version - `git checkout 2ea02d8dd10b1450eee0ea026e31d01f923bce92 -- [python.py](http://python.py/)`
- eaisest way to add is just `git add .` (this adds everything)
- use `git log`  to get commit hashes if you need to revert back.
- to exit when you commit without a messge just do `:qw` in terminal
- q to exit log

## BEST PROCESS - clone git

CAFEFUL: dont’ do git inside git 

DO:

1. create a git folder thro UI (DO NOT HAVE GIT ON THERE)

2. open git repo using Github add a .gitignore (python) this will already include .env

3. use clone ssh copy 

4. go to mac terminal (NOT VSC)

5. cd to git dir 

6. run - git clone (paste)

`git clone git@github.com:AshDavid12/projName.git`

you should see under git a new folder with your repo name

7. now open that folder in vsc 

8. now you can create .env file with your keys there add other py files and tomls

## Secrete Key Process

In your py code add:

```
from dotenv import load_dotenv

load_dotenv('.env')
```

In your .env file add:

```
API_KEY=your_api_key
SECRET_KEY=your_secret_key
```

In teminal add:

`poetry python-dotenv` like this:

- `poetry add python-dotenv`
- for new projects - you can copy the pyproject.toml from other projects and just use `poetry install` for all dependencies
- do `git add .` to add all your files
- `git status —ignored` to see your .env file
- `git commit -m “msg”` (here you should see that the number of files changed should be -1 since .env isn’t included
- `git push`
- TADA! you should now see all your files (.lock,.toml,.py,.gitignore) on github without the .env file!
