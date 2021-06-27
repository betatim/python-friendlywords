from setuptools import setup, find_packages
import pathlib


here = pathlib.Path(__file__).parent.resolve()

long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="py-friendlywords",
    # match the upstream project, use postX for our versioning
    version="1.2.0.post2",
    description="Curated lists of friendly words, as used in project names and elsewhere on glitch.com",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/betatim/python-friendlywords",
    author="Tim Head",
    packages=find_packages(),
    package_data={
        "friendlywords": [
            "collections.txt",
            "objects.txt",
            "predicates.txt",
            "teams.txt",
        ],
    },
    python_requires=">=3.7",
)
