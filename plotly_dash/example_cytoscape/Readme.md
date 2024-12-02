
Had to get dash-cytoscape:

```bash
pip install dash plotly dash-cytoscape
```

Had to downgrade the verison using pyenv:

```bash
example_deploying % pyenv install 3.10
example_deploying % pyenv global 3.10
example_deploying % python --version
Python 3.10.15

example_deploying % python -m venv mydashenv

example_deploying % . mydashenv/bin/activate

(mydashenv) example_deploying % pip install -r src/requirements.txt
...

(mydashenv) example_deploying % pip install gunicorn

(mydashenv) mydashenvapanchul@orion example_deploying % cd src

(mydashenv) mydashenvapanchul@orion src % gunicorn app:server
[2024-11-30 11:48:47 -0500] [48928] [INFO] Starting gunicorn 21.2.0
[2024-11-30 11:48:47 -0500] [48928] [INFO] Listening at: http://127.0.0.1:8000 (48928)
[2024-11-30 11:48:47 -0500] [48928] [INFO] Using worker: sync
[2024-11-30 11:48:47 -0500] [48929] [INFO] Booting worker with pid: 48929
```

You should see something like:

![](pics/Screenshot%202024-11-30%20at%2011.52.06 AM.png)
