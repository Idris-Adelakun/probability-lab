
import lessons.counting_and_sets.counting as lcs

cpkh  = lcs.calculate_prob_k_heads
tde = lcs.two_dice_experiment


def main():

    heads = 10
    tosses = 100

    # print(cpkh(heads,tosses))

    while True:
        try:
            target_sum = int(input("Please enter the sum of the dice:\n"))
        except ValueError:
            print("Please enter a whole number")
            continue

        if target_sum < 2 or target_sum > 12:
            print("Your value must be greater than 2 and less than 12")
            continue
        break


    probability = tde(target_sum)

    print(f"The probability of getting {target_sum} is {probability:.3%}")














if __name__ == "__main__":
    main()