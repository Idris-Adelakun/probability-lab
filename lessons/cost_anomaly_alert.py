
def probability_of_anomaly_given_alert(
        base_rate,
        true_positive_rate,
        false_positive_rate
):
    P_A  = base_rate
    P_Ac = 1 - P_A
    P_Ap = true_positive_rate
    P_An = false_positive_rate

    P_positive = P_A*P_Ap + P_Ac*P_Ap
    P_negative = P_A*P_An + P_Ac*P_An


