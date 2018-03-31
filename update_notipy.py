import atexit
from typing import Callable

from boxing import boxing
from pkg_info import get_pkg_info
from semver import compare


class update_notify(object):
    def __init__(self, name: str, version: str, **opts):
        self.name: str = name
        self.version: str = version
        self.is_updated: bool = self.is_latest_version()
        self.callback: Callable = opts.get('callback')
        self.message: str = opts.get('message')
        self.defer: bool = bool(opts.get('defer', False))

    def is_latest_version(self) -> bool:
        pkg = get_pkg_info(self.name)
        self.latest = pkg.version
        return True if compare(self.version, self.latest) >= 0 else False

    def notify(self) -> None:
        if self.is_updated:
            return
        if self.callback and callable(self.callback):
            action, arg = self.callback, None
        elif self.message:
            action, arg = print, self.message
        else:
            action, arg = print, self.default_message()
        if self.defer:
            atexit.register(action, arg) if arg else atexit.register(action)
        else:
            action(arg) if arg else action()

    def default_message(self) -> str:
        return boxing(f'Update available {self.version} → {self.latest}\n' +
                      f'Run pip install -U {self.name} to update')
