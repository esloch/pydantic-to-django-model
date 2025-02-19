"""Tests for pydantic_to_django_model package."""

import pytest

from hypothesis import given
from hypothesis import strategies as st


@pytest.fixture
def response_pytest() -> bool:
    """Sample pytest fixture."""
    return True


@pytest.fixture
def response_hypothesis() -> bool:
    """Sample pytest + hypothesis fixture."""
    return True


def test_content_pytest() -> None:
    """Test with pytest."""
    assert True is True


@given(st.text().filter(lambda s: s != ''))
def test_content_hypothesis(response_hypothesis: bool) -> None:
    """Test with pytest + hypothesis."""
    assert response_hypothesis
