
See more at [Python.md#web-related](https://github.com/panchul/workspace/blob/master/doc/Python.md#web-related)

---

Quick and simple HTTP server, this is to serve the folder where you run it:

    $ python -m http.server --cgi

More at https://docs.python.org/3/library/http.server.html

By default, the server uses the current directory. The option -d/--directory specifies a directory to which it should serve the files. For example, the following command uses a specific directory:

    $ python -m http.server --directory /tmp/

---
