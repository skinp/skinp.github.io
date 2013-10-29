Title: Python Tab Completion
Date: 2013-10-29
Slug: python-tab-completion
Summary: How to add primitive tab completion to the python shell

Add this to your `PYTHONSTARTUP` (ex: `~/.pythonrc.py`) file:

    ::python
    try:
        import readline
    except ImportError:
        print "Module readline not available."
    else:
        import rlcompleter
        readline.parse_and_bind("tab: complete")

then

    ::bash
    export PYTHONSTARTUP=~/.pythonrc.py
    python

or add `PYTHONSTARTUP` entry to your shell profile...
