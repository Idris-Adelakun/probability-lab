import math


while True:
    try:
        base_rate = float(
            input(
                "Base rate - probability that a genuine anomaly occurs "
                "e.g. 0.88 for 88%):\n"
            ))
        if base_rate <= 0 or base_rate > 1:
                    print("This value must be between 0 and 1")
                    continue

        true_rate = float(
            input(
                "True positive rate - probability the detector raises an alert: "
            ))
        if true_rate <= 0 or true_rate > 1:
                    print("This value must be between 0 and 1")
                    continue
                    
        false_rate = float(
            input(
                "False positive rate - probability the detector raises an alert "
                    ))
        if false_rate <= 0 or false_rate > 1:
            print("This value must be between 0 and 1")
            continue
        else: 
            break
    except ValueError as error:
        print("Please enter a value between 0 and 1")




def probability_of_anomaly_given_alert(
        base_rate,
        true_positive_rate,
        false_positive_rate
):
    P_A  = base_rate
    P_Ac = 1 - P_A

    P_Ap = true_positive_rate # P(+ | A)
    P_An = 1 - true_positive_rate # P(- | A)

    P_Acp = false_positive_rate # P(+ | Ac)
    P_Acn = 1 - false_positive_rate # P(- | Ac)

    P_positive = P_A * P_Ap + P_Ac * P_Acp # P(+)
    P_negative = P_A * P_An + P_Ac * P_Acn # P(-)

    assert math.isclose(P_positive + P_negative, 1) # Debug check; should equal 1

    prob_alert_positive = (P_Ap * P_A)/ P_positive
    prob_alert_negative = (P_An * P_A)/ P_negative

    return prob_alert_positive, prob_alert_negative


positive, negative = probability_of_anomaly_given_alert(base_rate, true_rate, false_rate)

print(f"Probability of anomaly given positive alert: {positive:.3%}")
print(f"Probability of anomaly given negative alert: {negative:.3%}")