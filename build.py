#!/usr/bin/env python3
import subprocess
import argparse
import os


REPO = 'ejfitzgerald/linger'
PROJECT_ROOT = os.path.dirname(__file__)
HEADER = """

 _____   __
|     |_|__|.-----.-----.-----.----.
|       |  ||     |  _  |  -__|   _|
|_______|__||__|__|___  |_____|__|
                  |_____|

"""


def get_version():
    return subprocess.check_output([
        'git',
        'describe',
        '--always',
        '--tags',
        '--dirty=-wip'
    ]).decode().strip()


def parse_commandline():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--push', action='store_true', help='Push the generated image')
    return parser.parse_args()


def main():
    args = parse_commandline()

    version = get_version()

    print(HEADER)
    print(f'Version: {version}')

    subprocess.check_call([
        'docker',
        'build',
        '-t', f'{REPO}:{version}',
        PROJECT_ROOT,
    ])

    if args.push:
        subprocess.check_call([
            'docker',
            'push',
            f'{REPO}:{version}',
        ])


if __name__ == '__main__':
    main()
