# DevOps Apprenticeship: Project Exercise

> If you are using GitPod for the project exercise (i.e. you cannot use your local machine) then you'll want to launch a VM using the [following link](https://gitpod.io/#https://github.com/CorndelWithSoftwire/DevOps-Course-Starter). Note this VM comes pre-setup with Python & Poetry pre-installed.

## System Requirements

The project uses poetry for Python to create an isolated environment and manage package dependencies. To prepare your system, ensure you have an official distribution of Python version 3.7+ and install Poetry using one of the following commands (as instructed by the [poetry documentation](https://python-poetry.org/docs/#system-requirements)):

### Poetry installation (Bash)

```bash
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | python -
```

### Poetry installation (PowerShell)

```powershell
(Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py -UseBasicParsing).Content | python -
```

## Dependencies

The project uses a virtual environment to isolate package dependencies. To create the virtual environment and install required packages, run the following from your preferred shell:

```bash
$ poetry install
```

You'll also need to clone a new `.env` file from the `.env.template` to store local configuration options. This is a one-time operation on first setup:

```bash
$ cp .env.template .env  # (first time only)
```

The `.env` file is used by flask to set environment variables when running `flask run`. This enables things like development mode (which also enables features like hot reloading when you make a file change). There's also a [SECRET_KEY](https://flask.palletsprojects.com/en/1.1.x/config/#SECRET_KEY) variable which is used to encrypt the flask session cookie.

You will also need to add your own TRELLO_API_KEY and TRELLO_API_TOKEN to the .env file as this will not be stored between sessions.

## Running the App

Once the all dependencies have been installed, start the Flask app in development mode within the Poetry environment by running:
```bash
$ poetry run flask run
```

You should see output similar to the following:
```bash
 * Serving Flask app "app" (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with fsevents reloader
 * Debugger is active!
 * Debugger PIN: 226-556-590
```
Now visit [`http://localhost:5000/`](http://localhost:5000/) in your web browser to view the app.

## Running the tests
If you are running the tests from within VS code you can use the testing tab on the left hand side to run all or some of the tests. If you want to run the tests via the terminal you can either use poetry run pytest to run all the tests or poetry run pytest a_folder_name to be more specific

## To provision a VM from an Ansible Control Node
ansible-playbook my-ansible-playbook.yml -i my-ansible-inventory
``

For Mod 4 this is in /home/ec2-user/to-do_app_setup on Ansible controller IP: 13.41.20.10 

## To build and run the Docker files
to build in prod use command 
 $ docker build --target production . --tag todoapp

 to run in prod use command
 $ docker run --env-file .env -p 5000:5000 todoapp

 To build in dev use command
 $ docker build --target development . --tag todoapp:dev
 
 To run in dev using bind mount so you can make changes and see it update use command
 $ docker run --env-file .env -p 5000:5000 --mount type=bind,source="$(pwd)"/todo_app,target=/app/todo_app todoapp:dev 

 To run docker tests
 $ docker run --env-file .env.test my-test-image

 module 8 help
 building a pipeline to run the docker file and then deploy it to docker. and then deploy it to Heroku
 docker build --target production --tag kelliep/my-todo-app .
 docker push kelliep/my-todo-app:latest

 These have been added to pipeline so when you do a push, this should run automatically. you can check in docker to see your project, and also in the github repo to see jobs running

 install heroku curl https://cli-assets.heroku.com/install-ubuntu.sh | sh
 heroku login -i work email, password in secrets file

 change the tag from docker to heroku
 docker tag kelliep/my-todo-app:latest registry.heroku.com/to-do-app-kellie/web
 push to heroku
 docker push registry.heroku.com/to-do-app-kellie/web