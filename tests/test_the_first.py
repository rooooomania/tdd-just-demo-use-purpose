# app.py
from app import app

def test_always_passes():
    assert True
    
def x_test_always_fails():
    assert False
    

def test_hello_world():
    with app.test_client() as client:
        response = client.get('/')
        assert response.data == b'Hello, World!'
        assert response.status_code == 200
