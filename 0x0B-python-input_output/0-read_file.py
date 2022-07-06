#!/usr/bin/python3
"""Module 0-read_file:
     reads a text file (UTF8) and prints it to stdout:
"""


def read_file(filename=""):
    """Reads a file and prints to stdout"""
    with open(filename) as f:
        text = f.read()
        print(text, end='')
