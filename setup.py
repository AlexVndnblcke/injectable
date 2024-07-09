from os.path import join, dirname
import re

from setuptools import setup, find_packages


def read(*names, **kwargs):
    with open(
        join(dirname(__file__), *names), encoding=kwargs.get("encoding", "utf8")
    ) as fh:
        return fh.read()


readme = re.compile("^.. start-badges.*^.. end-badges", re.M | re.S).sub(
    "", read("README.rst")
)
changelog = re.sub(":[a-z]+:`~?(.*?)`", r"``\1``", read("CHANGELOG.rst"))

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

with open("requirements.dev.txt") as f:
    dev_requirements = f.read().splitlines()

setup(
    name="injectable",
    version="4.0.0",
    packages=find_packages(
        exclude=(
            "tests",
            "examples",
            "docs",
            ".eggs",
            ".github",
            ".pytest_cache",
            ".tox",
            "build",
            "dist",
            "htmlcov",
            "injectable.egg-info",
        )
    ),
    url="https://github.com/roo-oliv/injectable",
    license="MIT",
    author="Rodrigo Oliveira",
    author_email="oliveira.rodrigo.m@gmail.com",
    description="Dependency Injection for Humans™",
    long_description=f"{readme}\n{changelog}",
    keywords=(
        "injection inject injectable injectables autowiring autowire autowired"
        " dependency dependency-injection DI SOLID lazy lazy-initialization"
        " circular circular-dependency cyclic cyclic-dependency"
        " inversion-of-control ioc container spring guice fixture for-humans humans"
    ),
    python_requires=">=3.9",
    install_requires=requirements,
    setup_requires=[],
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: MacOS",
        "Operating System :: POSIX",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: Implementation :: CPython",
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
        "Typing :: Typed",
    ],
)
