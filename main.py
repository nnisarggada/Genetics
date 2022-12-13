
def newGen(p1, p2, prob):
    c1 = [0] * 4        
    c2 = [0] * 4        
    for i in range(4):
        if (i%2 == 0):
            c1[i] = random.choice(p1)
        else:
            c1[i] = random.choice(p2)
    for i in range(4):
        if (i%2 == 0):
            c2[i] = random.choice(p1)
        else:
            c2[i] = random.choice(p2)
    if (random.random() < prob):
        c1[random.randrange(4)] = random.randrange(9)
    return c1 , c2


def sim(prob):
    p1 = [1, 2, 3, 4]
    p2 = [5, 6, 7, 8]
    generations = 0

    while (True):
        c1, c2 = newGen(p1, p2, prob)
        # print(c1)
        # print(c2)
        # print(" ")
        p1 = c1
        p2 = c2
        generations += 1
        if (c1 == c2):
            return generations
            break

def simulate(n, prob):
    trials = []
    for i in range(n):
        trials.append(sim(prob))
    return (sum(trials)/n)

print(simulate(100, 0.0))
