import pytest
from BlackWidowPipeline import scaling_relations_Curti2020 as Curti2020

def test_line_ratios_zero_metallicity():
    metallicity = 0
    results = Curti2020.line_ratios(metallicity)

    # 1. Check that the result is a dictionary
    assert isinstance(results, dict)

    # 2. Check that all expected diagnostics are present
    expected_diagnostics = [
        "R2", "R3", "O3O2", "R23", "N2", "O3N2", "S2", "RS32", "O3S2"
    ]
    for diag in expected_diagnostics:
        assert diag in results

    # 3. Check that all values are floats
    for val in results.values():
        assert isinstance(val, float)





