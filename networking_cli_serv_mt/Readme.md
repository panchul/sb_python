
## Pre-requisites

```bash
    $ pip install wikipedia
    ...
    Installing collected packages: soupsieve, beautifulsoup4, wikipedia
    Successfully installed beautifulsoup4-4.9.3 soupsieve-2.1 wikipedia-1.4.0
```

## Running the server

```bash
    $ python server.py
    [STARTING] Server is starting...
    [LISTENING] Server is listening on 127.0.1.1:2345
```

## Running the client

```bash
    $ python client.py 
    [CONNECTED] Client connected to server at 127.0.1.1:2345
    > pig
    [SERVER]
    > !DISCONNECT
```

It prints whatever wikipedia response was on `pig`.
