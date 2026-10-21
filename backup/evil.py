import os
import base64
import socket


def evil_function():
    eval("1 + 1")
    exec("print('test')")
    base64.b64decode("SGVsbG8=")
    socket.connect


if __name__ == "__main__":
    print("not a real evil file")
