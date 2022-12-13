import random
from matplotlib import pyplot as plt

chromosomes = int(input("Enter number of chromosomes: "))

def newGen(p1, p2, prob):

    c1 = [0] * chromosomes    
    c2 = [0] * chromosomes
    for i in range(chromosomes):
        if (i%2 == 0):
            c1[i] = random.choice(p1)
        else:
            c1[i] = random.choice(p2)
    for i in range(chromosomes):
        if (i%2 == 0):
            c2[i] = random.choice(p1)
        else:
            c2[i] = random.choice(p2)
    if (random.random() < prob):
        c1[random.randrange(chromosomes)] = random.randrange(9)
    return c1 , c2

def sim(prob):

    p1 = [0] * chromosomes
    p2 = [0] * chromosomes
    
    for i in range(chromosomes):
        p1[i] = random.randrange(9)

    for i in range(chromosomes):
        p2[i] = random.randrange(9)

    generations = 0

    while (True):
        c1, c2 = newGen(p1, p2, prob)
        p1 = c1
        p2 = c2
        generations += 1
        if (c1 == c2):
            return generations
            break

def simulate(n, prob):
    trials = []
    global x
    global y
    x = []
    y = []
    for i in range(n):
        x.append(i+1)
        y.append(sim(prob))
        trials.append(sim(prob))
    return (sum(trials)/n)

numOfSims = int(input("Enter number of simulations: "))
mutationProb = float(input("Enter the probability of mutation: "))

answer = simulate(numOfSims, mutationProb)
print(" ")
print(f"The offsprings will be the exact same after {answer} generations")

lines = plt.plot(x,y)
plt.setp(lines, color = 'r', linewidth = 1)
plt.title(f"Number of generations after which both offsprings are exactly the same (Mutation Probability: {mutationProb*100}%)\n\nAverage: {answer} generations\n\n")
plt.xlabel("Simulation Number")
plt.ylabel("Number of Generations")
plt.show()
