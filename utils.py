def greedy(coins, amount):
    # TODO: Step 1 – Sort the coins in descending order
    # coins.sort(_____)

    result = []
    remaining = amount

    for coin in coins:
        pass
        # TODO: Step 2 – Use while loop to subtract coins as long as it fits
        # while _______:
        #     _______
        #     _______

    # TODO: Step 3 – Check if exact amount was made
    # if _______:
    #     print("No possible solution")
    #     return -1
    

    return result

def brute_force(coins, amount):
    # Base cases
    if amount == 0:
        return 0
    if amount < 0:
        return float('inf')  # invalid path
    
    # TODO: initialize the minimum coins variable
    # min_coins = _____

    # TODO: try each coin
    for coin in coins:
        pass
        # TODO: compute result for the remaining amount
        # res = brute_force(_____)
        
        # TODO: update min_coins if valid
        # if res != float('inf'):
        #     min_coins = _____
    
    # TODO: return the best result
    # return _____


import random

def stochastic(coins, amount):
    result = []
    while amount > 0:
        # Filter only usable coins
        valid = [c for c in coins if c <= amount]
        if not valid:
            # Cannot continue, no coin fits the remaining amount
            break
        coin = random.choice(valid)
        amount -= coin
        result.append(coin)
    return result

def trial(coins, amount, n_trials):
    best = None
    best_len = float('inf')

    for _ in range(n_trials):
        result = stochastic(coins, amount)
        # check if result is valid and better
        # if ________ and ______:
        #     ______
        #     ______

    return best