"""Tests for pydantic_djmodel package."""

import pytest

from fhir.resources.medication import Medication as FHIRMedication
from pydantic_djmodel.core import pydantic_to_django


@pytest.fixture
def response_pytest() -> bool:
    """Sample pytest fixture."""
    return True


@pytest.fixture
def response_hypothesis() -> bool:
    """Sample pytest + hypothesis fixture."""
    return True


def test_import() -> None:
    """Test import."""
    import pydantic_djmodel

    assert pydantic_djmodel

    from pydantic_djmodel import core

    assert core


@pytest.mark.skip
def test_with_fhir() -> None:
    """Test with pytest + hypothesis."""
    # Generate Django model from FHIR Medication Pydantic model
    MedicationModel = pydantic_to_django(FHIRMedication, 'Medication')

    # Example usage
    print(MedicationModel.__name__)  # Output: Medication
