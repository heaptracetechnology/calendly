import pytest
from flask import Flask

@pytest.fixture(scope='module')
def app() -> Flask:
    from app import app  
       
    return app