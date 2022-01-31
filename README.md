#LEARNINGSPACE ENVIRONMENT

This is README file lists down the development, staging and production environments for LEARNINGSPACE project.

## Installations

1. Git-SCM Client
2. Vagrant (Windows; optional for Linux)
3. VirtualBox (Windows; optional for Linux)
4. ModHeader (Chrome Browser Extension)
5. Linux ubuntu/bionic64 (will be done my vagrant script if you opt to use it)
6. Python Installations (will be done my vagrant script if you opt to use it)
  * python3-dev
  * sqlite
  * python-pip
  * pip
  * virtualenvwrapper
7. Atom (recommended editor)

## Get Git url

1. Local Git URL __ssh://git-kims@192.168.0.100/~/learningspace.git__

## Get setup

1. git config --global user.email "you@example.com"
2. git config --global user.name "Your Name"
3. git clone _git url_

## Vagrant setup (Windows; optional for Linux)

Open Git Bash shell on Windows and execute the following commands (Vagrant and VirtualBox must be installed)
1. vagrant up (first time setup)
2. vagrant reload (good idea to do this for the first time)
2. vagrant ssh
3. cd /vagrant/ or ~/workspace/learningspace (this is the directory on Vagrant VirtualBox that is mapped to the windows project directory)

## Python setup

On Linux, execute the following commands (first time setup)
1. python --version
2. lsvirtualenv
3. mkvirtualenv learningspace --python=python3
4. python --version
5. cd ~/workspace/learningspace
6. pip install -r requirements.txt
NOTE: if pyscopg2 throws error run command :sudo apt-get install libpq-dev python-dev


On Linux, activate/deactivate virtual environment
* workon learningspace
* deactivate

On Linux, install, upgrade or downgrade a package
* pip install _package-name_ __e.g. pip install django__
* pip install _package-name_ --upgrade __e.g. pip install django --upgrade__
* pip install _package-name_==_version-number_ __e.g. pip install django==3.1__

## Git commit conventions
* Never work on _master_ branch. Create your working branch and name it as per your name and task.
* Never merge your branch into the _master_ branch without approval of your manager.
* Always add comment for commits. Following is the comment convention.
  * "YYYYMMDD HH:MM **_detailed comment no more than 160 characters_**"
