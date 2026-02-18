
# Probability of rolling a 4 on a fair die

favorable = 1
total_outcomes = 6
probability = favorable / total_outcomes
print(probability)


# Independent events example

p_rain = 0.3
p_traffic = 0.2
p_both = p_rain * p_traffic
print(p_both)


# Conditional probability example

p_A_and_B = 0.1
p_B = 0.4
p_A_given_B = p_A_and_B / p_B
print(p_A_given_B)


# Bayes' theorem example

p_disease = 0.01
p_positive_given_disease = 0.9
p_positive = 0.05

p_disease_given_positive = (p_positive_given_disease * p_disease) / p_positive
print(p_disease_given_positive)


#The Sample Space Map

import random

actions = ["Click", "Scroll", "Exit"]

sample_space = [(a, b) for a in actions for b in actions]

print("Sample Space S:")
print(sample_space)
print("Total outcomes:", len(sample_space))
print()

event_E = [outcome for outcome in sample_space if "Click" in outcome]

prob_E = len(event_E) / len(sample_space)

print("Event E (At least one Click):")
print(event_E)
print("Probability of at least one Click =", prob_E)
print()

trials = 1000
count_sum_7 = 0

for _ in range(trials):
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    if die1 + die2 == 7:
        count_sum_7 += 1
experimental_probability = count_sum_7 / trials

print("Experimental Probability of sum = 7 after 1000 trials:")
print(experimental_probability)


#The Logic Of Dependency

P_heads = 1/2

P_six = 1/6

P_independent = P_heads * P_six

print("Independent Events:")
print("Probability of Heads AND rolling a 6 =", P_independent)
print()

P_first_red = 5/10

P_second_red = 4/9

P_dependent = P_first_red * P_second_red

print("Dependent Events:")
print("Probability that both marbles are Red =", P_dependent)
print()

print("Reflection:")
print("The denominator changed because one marble was removed.")
print("Total marbles reduced from 10 to 9, so the probability changed.")
print("This is called dependent probability.")


#The Bayseian Filter

P_spam = 0.1                 
P_ham = 1 - P_spam           

P_free_given_spam = 0.9      
P_free_given_ham = 0.05      

P_free = (P_free_given_spam * P_spam) + (P_free_given_ham * P_ham)

P_spam_given_free = (P_free_given_spam * P_spam) / P_free

print("P(Free) =", P_free)
print("P(Spam | Free) =", P_spam_given_free)
