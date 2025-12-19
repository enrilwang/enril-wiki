from setuptools import setup

setup(
    name="mkdocs-backlinks-plugin",
    version="0.1",
    py_modules=["backlinks"],
    entry_points={
        "mkdocs.plugins": [
            "backlinks = backlinks:BacklinksPlugin",
        ]
    },
)

