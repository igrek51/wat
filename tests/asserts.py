import re
import sys
from io import StringIO
from typing import Optional
import logging

from nuclear.sublog import init_logs
from nuclear.utils.strings import strip_ansi_colors


class StdoutCap:
    def __init__(self):
        init_logs()
        logger = logging.getLogger('nuclear.sublog')
        logger.setLevel(logging.DEBUG)
        logger.propagate = False
        self.extra_handler = logging.getLogger().handlers[0]
        self.extra_handler.setLevel(logging.DEBUG)
        formatter = logging.getLogger().handlers[0].formatter
        self.extra_handler.setFormatter(formatter)
        logger.addHandler(self.extra_handler)

        # mock output
        self.new_out, self.new_err = StringIO(), StringIO()
        self.old_out, self.old_err = sys.stdout, sys.stderr

        # capture output from loggers
        self.old_handler, self.new_handler = None, None
        self.logger = logger
        handler = get_logger_handler(self.logger)
        if handler is not None:
            self.old_handler = handler
            self.new_handler = logging.StreamHandler(self.new_out)
            self.new_handler.setLevel(self.old_handler.level)
            self.new_handler.setFormatter(self.old_handler.formatter)

    def __enter__(self):
        sys.stdout, sys.stderr = self.new_out, self.new_err
        if self.old_handler is not None:
            self.logger.removeHandler(self.old_handler)
            self.logger.addHandler(self.new_handler)
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        sys.stdout, sys.stderr = self.old_out, self.old_err
        sys.stdout.write(self.output())
        if self.old_handler is not None:
            self.logger.removeHandler(self.new_handler)
            self.logger.addHandler(self.old_handler)
        self.logger.removeHandler(self.extra_handler)

    def output(self) -> str:
        return self.new_out.getvalue() + self.new_err.getvalue()

    def stripped(self) -> str:
        return self.output().strip()

    def uncolor(self) -> str:
        matcher = re.compile(r'\x1b\[[0-9]+(;[0-9]+)?m')
        return matcher.sub('', self.output())


def assert_multiline_match(text: str, regex_pattern: str):
    regex_lines = regex_pattern.strip().splitlines()
    text_lines = strip_ansi_colors(text).strip().splitlines()

    if len(text_lines) < len(regex_lines):
        assert False, f'Actual text has {len(regex_lines) - len(text_lines)} less lines than a pattern.\nActual text:\n{text}'
    
    if len(text_lines) > len(regex_lines):
        assert False, f'Actual text has {len(text_lines) - len(regex_lines)} more lines than a pattern.\nActual text:\n{text}'

    for index, (regex_line, text_line) in enumerate(zip(regex_lines, text_lines)):
        match = re.fullmatch(regex_line, text_line)
        assert match, f'Actual Line #{index+1}:\n{text_line}\n does not match the Regex pattern:\n{regex_line}'


def get_logger_handler(logger: logging.Logger) -> Optional[logging.Handler]:
    c = logger
    while c:
        if c.handlers:
            return c.handlers[0]
        if not c.propagate:
            return None
        else:
            c = c.parent
    return None
