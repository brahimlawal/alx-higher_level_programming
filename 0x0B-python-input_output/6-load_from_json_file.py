#!/usr/bin/python3
"""Defines a JSON file-reading function."""
import json


def load_from_json_file(filename):
    """Creates a Python object from JSON file"""
    with open(filename, mode='r', encoding='utf-8') as file:
        return json.load(file)
