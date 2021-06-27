import importlib.resources
import os

from functools import partialmethod


def __getattr__(name):
    # This is what makes `friendlywords.teams` and `friendlywords.predicates`
    # work. We only have to add the special/magic words because __getattr__
    # will only be called if the normal lookup mechanism fails.
    if name not in ("collections", "objects", "predicates", "teams"):
        raise AttributeError()

    else:
        return getattr(_words, name)


def __dir__():
    return [
        "WordLists",
        "__builtins__",
        "__cached__",
        "__doc__",
        "__file__",
        "__getattr__",
        "__loader__",
        "__name__",
        "__package__",
        "__path__",
        "__spec__",
        "collections",
        "objects",
        "predicates",
        "teams",
    ]


class WordLists:
    def __init__(self, directory=None):
        """Manage access to several word lists

        If `directory` is passed it should be a path on the filesystem that
        contains one or more collections of words. By default the word lists
        from this module are used.
        """
        self.directory = directory
        self.cache = {}

    def words(self, name):
        """Return all the words for the collection `name`"""
        if name not in self.cache:
            if self.directory is not None:
                fname = os.path.join(self.directory, f"{name}.txt")
                with open(fname) as f:
                    words = set(f.read().split())

            else:
                with importlib.resources.open_text("friendlywords", f"{name}.txt") as f:
                    words = set(f.read().split())

            self.cache[name] = words

        return self.cache[name]

    @property
    def collections(self):
        return self.words("collections")

    @property
    def objects(self):
        return self.words("objects")

    @property
    def predicates(self):
        return self.words("predicates")

    @property
    def teams(self):
        return self.words("teams")


# "global" instance used to manage access to the default word lists
_words = WordLists()
