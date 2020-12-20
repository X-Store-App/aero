import argparse
import os
from utilities.getconfig import get_config
import importlib.util

def __main__():
    # CLI
    parser = argparse.ArgumentParser()
    parser.add_argument("task", nargs="?")
    parser.parse_args()
    args = parser.parse_args()
    if args.task is None:
        args.task = 'default'
    # Execute task
    spec = importlib.util.spec_from_file_location('', get_config())
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    func = getattr(module, args.task)
    func()


if __name__ == "__main__":
    __main__()
