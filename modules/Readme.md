
if you invoke the interpreter as

    $ python one.py

The output will be

    top-level in one.py
    one.py is being run directly

If you run `two.py` instead:

    $ python two.py

You get

    top-level in one.py
    one.py is being imported into another module
    top-level in two.py
    func() in one.py
    two.py is being run directly

Thus, when module `one` gets loaded, its __name__ equals "one" instead of "__main__".

