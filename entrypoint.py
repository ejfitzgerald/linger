#!/usr/bin/env python3
import argparse
import re
import os
import sys
import subprocess
import time


HEADER = """

 _____   __
|     |_|__|.-----.-----.-----.----.
|       |  ||     |  _  |  -__|   _|
|_______|__||__|__|___  |_____|__|
                  |_____|

"""


def _host_port(text: str):
    match = re.match(r'^(.*?):(\d+)$', text)
    if match is None:
        print(f'Invalid host:port pair -> {text}')
        sys.exit(1)

    return match.group(1), int(match.group(2))


def parse_commandline() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'targets',
        metavar='HOST:PORT',
        type=_host_port,
        nargs='+',
        help='The set of hosts and ports that we should linger for'
    )
    return parser.parse_args()


def wait_for_host(host: str, port: int):
    with open(os.devnull, 'w') as nullfile:

        idx = 0
        while True:
            if idx >= 1:
                print(f'waiting for connection to {host}:{port}... (retry: {idx})')
            else:
                print(f'waiting for connection to {host}:{port}...')

            status = subprocess.call(
                ['nc', '-z', host, str(port)],
                stdout=nullfile,
                stderr=subprocess.STDOUT
            )

            if status == 0:
                break

            time.sleep(5)
            idx += 1

    print(f'waiting for connection to {host}:{port}...complete')


def main():
    args = parse_commandline()

    print(HEADER)

    for host, port in args.targets:
        wait_for_host(host, port)


if __name__ == '__main__':
    main()
