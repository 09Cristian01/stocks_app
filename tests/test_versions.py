#!/usr/bin/env python
# import pytest
from platform import python_version
from pkg_resources import get_distribution


def test_python_version():
    assert python_version() == "3.11.5"


def test_customTkinter_version():
    get_distribution("customtkinter").version == "5.2.1"


def test_mariadb_connector_version():
    get_distribution("mariadb").version == "1.1.8"


def test_dotenv_version():
    get_distribution("python-dotenv").version == "1.0.0"
