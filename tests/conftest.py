from flask import Flask
from src import create_app
import pytest

@pytest.fixture()
def app():
    
    app = create_app()
    
    yield app

@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()

