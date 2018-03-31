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
