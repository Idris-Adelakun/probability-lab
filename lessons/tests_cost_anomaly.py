import math

from cost_anomaly_alert import probability_of_anomaly_given_alert

def test_probabilities_valid():
    positive, negative = probability_of_anomaly_given_alert()

    assert 0 <= positive <=1
    assert 0 <= negative <=1

def test_known_case():
    positive, negative = probability_of_anomaly_given_alert(
        0.02,
        0.88,
        0.06
    )
    expected =  (0.88 * 0.02) / (0.88 * 0.02) + (0.06 * 0.98)

    assert math.isclose(positive, expected)