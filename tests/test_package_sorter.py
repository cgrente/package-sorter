"""Tests for package_sorter.sort()."""
import pytest

from package_sorter import sort

## STANDARD : not bulky, not heavy

def test_small_light_package_is_standard():
    assert sort(10, 10, 10, 5) == "STANDARD"

## SPECIAL: bulky or heavy

def test_bulky_by_volume_only_is_special():
    # Arrange : 101 x 101 x 101 = 1_030_301 CM3, above the volume threshold
    # but no single side reaches 150cm and mass is light

    assert sort(101, 101, 101, 5) == "SPECIAL"

@pytest.mark.parametrize("width,height,length", [
    (150, 10, 10),
    (10, 150, 10),
    (10, 10, 150)
])
def test_bulky_by_any_single_dimension_is_special(width, height, length):
    assert sort(width, height, length, 5) == "SPECIAL"

def test_heavy_but_not_bulky_is_special():
    assert sort(10, 10, 10, 20) == "SPECIAL"

## REJECTED: bulky and heavy

def test_bulky_by_volume_and_heavy_is_rejected():
    # Arrange : 101 x 101 x 101 = 1_030_301 CM3, (bulky by volume), mass 25kg (heavy)
    assert sort(101, 101, 101, 25) == "REJECTED"

def test_bulky_by_dimension_and_heavy_is_rejected():
    # Arrange: a 200cm pole that's also heavy
    assert sort(200, 10, 10, 25) == "REJECTED"

## Boundary conditions (>= thresholds)

def test_volume_exactly_at_threshold_is_bulky():
    # Arrange: 100 x 100 x 100 = 1_000_000 cm3 exactly the bulky volume threshold
    assert sort(100, 100, 100, 5) == "SPECIAL"

def test_volume_just_below_threshold_is_not_bulky():
    # Arrange: 100 x 100 x 99 - 990_000 cm3 just under threshold
    assert sort(100, 100, 99, 5) == "STANDARD"

def test_dimension_exactly_at_threshold_is_bulky():
    # Arrange: one side exactly at 150cm volume well below 1_000_000
    assert sort(150, 10, 10, 5) == "SPECIAL"

def test_dimension_just_below_threshold_is_not_bulky():
    # Arrange: one side at 149cm volume well below the threshold
    assert sort(149, 10, 10, 5) == "STANDARD"

def test_mass_exactly_at_threshold_is_heavy():
    assert sort(10, 10, 10, 20) == "SPECIAL"

def test_mass_just_below_threshold_is_not_heavy():
    assert sort(10, 10, 10, 19.99) == "STANDARD"

## Input validation

@pytest.mark.parametrize("width,height,length", [
    (0, 10, 10),
    (10, 0, 10),
    (10, 10, 0),
    (-1, 10, 10)
])
def test_non_positive_dimension_raises_value_error(width, height, length):
    with pytest.raises(ValueError,  match="Dimension"):
        sort(width, height, length, 5)

def test_negative_mass_raises_value_error():
    with pytest.raises(ValueError, match="Mass"):
        sort(10, 10, 10, -1)

def test_zero_mass_is_allowed():
    # A massless package is unusual but not invalid per the spec
    assert sort(10, 10, 10, 0) == "STANDARD"

## Float inputs

def test_accepts_float_inputs():
    assert sort(10.5, 10.5, 10.5, 5.5) == "STANDARD"