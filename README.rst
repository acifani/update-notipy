📬 update-notipy
================

Send a notification when there is an update available for your package!
Py-port of `update-notifier <https://github.com/yeoman/update-notifier>`_.


Install
-------

``pipenv install update_notipy``

or

``pip install update_notipy``

Usage
-----

.. code-block:: python

    from update_notipy import update_notify

    update_notify(
        <pkg_name>,
        <pkg_version>,
        callback=<callback>,
        message=<message>,
        defer=<True|False>).notify()

Arguments
~~~~~~~~~

- ``pkg_name: str``: name of the package as registered on PyPI
- ``pkg_version: str``: version of the installed package, to be compared with the latest one
- ``callback: Callable``: function to be called instead of printing the standard message
- ``message: str``: custom message to be printed
- ``defer: bool``: set to ``True`` if you want to notify the user when the app closes

Examples
--------

.. code-block:: python

    from update_notipy import update_notify

    __version__ = "0.1.0"

    update_notify('pkg-info', __version__).notify()

    #    ┌───────────────────────────────────────────┐
    #    │                                           │
    #    │   Update available 0.1.0 → 0.1.2          │
    #    │   Run pip install -U pkg-info to update   │
    #    │                                           │
    #    └───────────────────────────────────────────┘

    def foo():
        four = 2 + 2
        print(four)

    update_notify('pkg-info', __version__, callback=foo).notify()

    # 4

    update_notify('pkg-info', __version__, message="Hello, world!").notify()

    # Hello, world!
