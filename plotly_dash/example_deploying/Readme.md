
This is initially from [an online tutorial](https://github.com/Coding-with-Adam)

Because of some messy dependencies, I used `pyenv` and `venv` to try it out:

Make sure your Python version is ok for the `requirements.txt` that we are about to load:

```bash
pyenv install 3.10
pyenv global 3.10
```

```bash
python -m venv mydashenv
. mydashenv/bin/activate
```
```bash
pip install -r src/requirements.txt

pip install gunicorn
```

You could use a cloud instance or http://render.com to host it. But you can just run `python app.py`, or better yet:

```bash
cd src
gunicorn app:server   # app is the name of the file, app.py
```

Here's an actual test run:

```bash
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
