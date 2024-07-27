import random
def gambler(stake, goal, trials):
    wins = 0
    bets = 0

    for _ in range(trials):
        cash = stake
        while cash > 0 and cash < goal:
            bets += 1
            if random.random() < 0.5:
                cash += 1
            else:
                cash -= 1
        if cash == goal:
            wins += 1
    print(f"number of wins: {wins}")
    print(f"win percentage: {(wins / trials) * 100}%")
    print(f"loss percentage: {((trials - wins) / trials) * 100}%")

stake = int(input("enter the stake: "))
goal = int(input("enter the goal: "))
trials = int(input("enter the number of trials: "))
gambler(stake, goal, trials)
