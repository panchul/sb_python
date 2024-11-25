
This is from the online tutorial, see this for more: https://github.com/Coding-with-Adam

Commonly:

```bash
python3 -m venv my_env
. my_env/bin/activate

pip install -r requirements.txt

pip install gunicorn
```

Can run `python app.py`, or better yet:

```bash
cd src
gunicorn app:server   # app is the name of the file, app.py
```

The demo used http://render.com hosting hub.
