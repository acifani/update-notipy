📬 update-notipy
================

Update notifications for your python app! Py-port of `update-notifier <https://github.com/yeoman/update-notifier>`_.


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
        message=<message>).notify()


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
