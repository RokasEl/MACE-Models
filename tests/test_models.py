import pytest
from ase.build import molecule

import mace_models


@pytest.mark.parametrize("name", ["ani500k_small", "medium_spice", "small_spice"])
def test_load_model(name):
    model = mace_models.load(name)
    assert model.name == name

    water = molecule("H2O")
    water.calc = model.get_calculator()
    assert isinstance(water.get_potential_energy(), float)
