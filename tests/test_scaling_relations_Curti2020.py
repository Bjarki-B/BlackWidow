import pytest
from BlackWidowPipeline import scaling_relations_Curti2020

@pytest.mark.parametrize(
    "diagnostic, coeffs",
    scaling_relations_Curti2020.coefficients_dic.items()
)
def test_line_ratios_at_solar_metallicity(diagnostic, coeffs):
    metallicity = 8.69  # solar metallicity
    results = scaling_relations_Curti2020.line_ratios(metallicity)

    assert diagnostic in results
    assert isinstance(results[diagnostic], float)

    expected_value = coeffs["coeffs"][0]
    assert results[diagnostic] == pytest.approx(expected_value, abs=1e-12)






