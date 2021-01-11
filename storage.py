"""
    store: storage.py --key key_name --val value
    get: storage.py --key key_name
"""
import os
import sys
import tempfile
import json
import argparse
filename = 'storage.data'
storage_path = os.path.join(tempfile.gettempdir(), filename)
# print(storage_path)


def print_usage():
    print(f"usage: {sys.argv[0]} --key key_name [--val value]")


key_name = None
key_value = None

parser = argparse.ArgumentParser()
parser.add_argument("--key", type=str, help="key name")
parser.add_argument("--val", type=str, help="key value (optional)")
args = parser.parse_args()
if args.key is not None:
    key_name = args.key
if args.val is not None:
    key_value = args.val

# print(f"key: {key_name}, value: {key_value}")

if key_name is None:
    print_usage()
    exit(1)
if os.path.exists(storage_path):
    with open(storage_path, 'r') as f:
        storage_dict = dict(json.load(f))
else:
    # if file not exists - create empty dict
    storage_dict = {}

# get old value from dict (value is list of strings)
value = storage_dict.get(key_name, None)

if key_value is None:
    if value is not None:
        print(", ".join(value))
    else:
        print(None)
else:
    if value is None:
        value = []
    value.append(key_value)
    storage_dict[key_name] = value
    with open(storage_path, 'w') as f:
        json.dump(storage_dict, f)
