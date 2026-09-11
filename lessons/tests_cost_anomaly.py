import math

from cost_anomaly_alert import probability_of_anomaly_given_alert

def test_probabilities_valid():
    positive, negative = probability_of_anomaly_given_alert()

    assert math.isclose(positive, 1)
    assert math.isclose(negative, 1)

    
    