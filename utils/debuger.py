# -*- coding: utf-8 -*-
__author__ = 'SolPie'
from deco import singleton
import logging


@singleton
class Log():
# Map echo settings to logger levels
    _echo_map = {
        None: logging.NOTSET,
        False: logging.NOTSET,
        True: logging.INFO,
        'debug': logging.DEBUG,
    }

    def __init__(self):
        self.logger = logging.getLogger('Tagreat')
        console = logging.StreamHandler()
        self.logger.addHandler(console)
        pass

    def log(self, level, msg, *args, **kwargs):
        """Delegate a log call to the underlying logger.

        The level here is determined by the echo
        flag as well as that of the underlying logger, and
        logger._log() is called directly.

        """

        # inline the logic from isEnabledFor(),
        # getEffectiveLevel(), to avoid overhead.

        # if self.logger.manager.disable >= level:
        #     return

        # selected_level = self._echo_map[self.echo]
        # if selected_level == logging.NOTSET:
        #     selected_level = self.logger.getEffectiveLevel()
        #
        # if level >= selected_level:
        self.logger._log(level, msg, args, **kwargs)

    def debug(self, msg, *args, **kwargs):
        """Delegate a debug call to the underlying logger."""

        self.log(logging.DEBUG, msg, *args, **kwargs)

    def debug(self, *args):
        print args

    def info(self, msg, *args, **kwargs):
        """Delegate an info call to the underlying logger."""

        self.log(logging.INFO, msg, *args, **kwargs)

    def warning(self, msg, *args, **kwargs):
        """Delegate a warning call to the underlying logger."""

        self.log(logging.WARNING, msg, *args, **kwargs)

    def error(self, msg, *args, **kwargs):
        """
        Delegate an error call to the underlying logger.
        """
        self.log(logging.ERROR, msg, *args, **kwargs)
        pass
