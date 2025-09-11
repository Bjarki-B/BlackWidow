import pytest
from BlackWidowPipeline import scaling_relations_Curti2020

@pytest.mark.parametrize(
    "diagnostic, coeffs", 
    scaling_relations_Curti2020.coeffitients_dic.items()
)

def test_line_ratios_at_solar_metallicity(diagnostic, coeffs):
    metallicity = 8.69 # solar metallicity
    results = scaling_relations_Curti2020.line_ratios(metallicity)

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
        
    # 4. Check that all values are (approximately) c0 at solar metallicity
    expected_value = coeffs["coeffs"][0]

    assert diagnostic in results
    assert isinstance(results[diagnostic], float)
    assert results[diagnostic] == pytest.approx(expected_value, abs=1e-12)





