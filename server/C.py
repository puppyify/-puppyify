import getopt
import hashlib
import json
import os
import sys
import uuid

PUPPYIFY_PATH = '../puppyify' if not os.getenv("PUPPYIFY_PATH") else os.getenv("PUPPYIFY_PATH")
WORKSPACE_PATH = f'{PUPPYIFY_PATH}/workspace'
SOFT_PATH = f'{PUPPYIFY_PATH}/soft'


def mkdirs(path):
    if not os.path.exists(path):
        print("mkdirs: path=" + path)
        os.makedirs(path)
    return path


def md5(param: str, len=32) -> str:
    if type(param) != 'str':
        param = json.dumps(param)
    return hashlib.md5(param.encode()).hexdigest()[0:len]


def code(len=16) -> str:
    return md5(str(uuid.uuid4()), len)


def load_token():
    global TOKEN
    help_info = """fast.py -t <token>"""
    argv = sys.argv[1:]
    token = None
    try:
        opts, args = getopt.getopt(argv, "ht:", ["token="])
    except getopt.GetoptError:
        print(help_info)
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print(help_info)
            sys.exit()
        elif opt in ("-t", "--token"):
            token = arg
    if not token:
        token = 'rUzf0Y861xaNJES1'
    TOKEN = token
    if not token:
        print(help_info)


def init():
    load_token()
    print('TOKEN', TOKEN)
    print('PUPPYIFY_PATH', PUPPYIFY_PATH)
    print('WORKSPACE_PATH', WORKSPACE_PATH)
    print('SOFT_PATH', SOFT_PATH)
    print()
    print()


def check_token(token):
    return TOKEN == token
