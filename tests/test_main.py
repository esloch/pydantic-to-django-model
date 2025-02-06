"""Tests for pydantic_to_django_model package."""
import pytest

from hypothesis import given
from hypothesis import strategies as st


@pytest.fixture
def response_pytest():
    """Sample pytest fixture."""
    return True


@pytest.fixture
def response_hypothesis():
    """Sample pytest + hypothesis fixture."""
    return True


def test_content_pytest():
    """Test with pytest."""
    assert True


@given(st.text().filter(lambda s: s != ""))
def test_content_hypothesis(response_hypothesis):
    """Test with pytest + hypothesis."""
    assert response_hypothesis
