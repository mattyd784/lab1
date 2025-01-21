import pytest
from hello_world import hello_world

def test_hello_world():
    """Test the hello_world function."""
    assert hello_world() == "Hello, World!", "The function should return 'Hello, World!'"