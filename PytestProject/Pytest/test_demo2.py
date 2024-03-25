import pytest
def test_m7():
    assert True

def test_m8():
    assert 100==100
@pytest.mark.login
def test_m9():
    assert "KUMAR"=="KUMAR"
@pytest.mark.login
def test_login_Insta():
    assert "admin" == "admin123"
