#!/usr/bin/env python3
from livekey import animate_commands


commands = [
    'python',
    'x = {7}',
    'from wat import wat',
    'wat / x',
]


if __name__ == '__main__':
    animate_commands(commands, key_delay=0.1, line_delay=1.0)
