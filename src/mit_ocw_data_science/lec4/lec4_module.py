import random

def roll_die():
    """Returns a random int between 1 and 6"""
    return random.choice([1, 2, 3, 4, 5, 6])

def run_sim(goal, num_trials, txt):
    """
    Simulates rolling a die multiple times to estimate the probability of getting a specific sequence. And prints the actual and estimated probabilities of achieving the target sequence.
    """
    total = 0
    for i in range(num_trials):
        result = ''
        for j in range(len(goal)):
            result += str(roll_die())
        if result == goal:
            total += 1
    print('Actual probability of', txt, '=',
          round(1/(6**len(goal)), 8))
    est_probability = round(total/num_trials, 8)
    print('Estimated Probability of', txt, '=',
          round(est_probability, 8))

def same_date(num_people, num_same):
    """
    Checks if there are people sharing the same birthdate among a group of people. Returns True if there are 'num_same' people sharing the same birthdate, False otherwise.
    """
    possible_dates = range(366)
    # possible_dates = 4*list(range(0, 57)) + [58]\
    #                 + 4*list(range(59, 366))\
    #                 + 4*list(range(180, 270))
    birthdays = [0] * 366
    for p in range(num_people):
        birth_date = random.choice(possible_dates)
        birthdays[birth_date] += 1
    return max(birthdays) >= num_same

def birthday_prob(num_people, num_same, num_trials):
    """
     Estimates the probability of at least 'num_same' people sharing the same birthdate in a group. And returns the estimated probability of 'num_same' people sharing the same birthdate.
    """
    num_hits = 0
    for t in range(num_trials):
        if same_date(num_people, num_same):
            num_hits += 1
    return num_hits / num_trials

