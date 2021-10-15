"""Setup.py file"""
from setuptools import setup

setup(
    name="pytest-unittest-assertions",
    version="0.0.1",
    # the following makes a plugin available to pytest
    entry_points={"pytest11": ["unittest_assertions = pytest_unittest_assertions"]},
    # custom PyPI classifier for pytest plugins
    classifiers=["Framework :: Pytest"],
)
