def find_runner_up():
    players = int(input("Enter the number of participants: "))
    scores = list(map(int, input("Enter the scores of the participants separated by spaces: ").split()))
    if players != len(scores):
        print("The number of scores entered does not match the number of participants.")
        return
    unique_scores = list(set(scores))  # list has at least 2 unique Scores .
    if len(unique_scores) < 2:
        print("Not enough unique scores to determine a runner-up.")
        return
    unique_scores.sort(reverse=True)  # descending sorted
    runner_up = unique_scores[1]  # Final Runners-Up Score

    print("The runner-up score is:", runner_up)


find_runner_up()
