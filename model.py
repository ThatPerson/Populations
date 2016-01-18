# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 22:35:03 2016

@author: ben
"""
import math
import random


def f(maxi, spread, value):
    mean = maxi/2
    coeff = 1/(spread * math.sqrt(2*math.pi))
    expv = -((value - mean)**2)/(2*spread*spread)
    return coeff * math.exp(expv)


class Individual:
    age = 0
    genes = []
    max_age = 0
    alive = 1
    food_stored = 0
    def __init__(self, genes):
        self.genes = genes
        self.max_age_c()
    def max_age_c(self):
        self.max_age = abs(math.sin(self.genes[0]/10) * math.cos(self.genes[1]/10)) * 2000
    def spread(self):
        q = abs(math.sin(self.genes[1]/10) * math.cos(self.genes[0]/10)) * 1000
        if q == 0:
            q=10
            self.alive = 0

        return q
    def reproduce(self, max_age_m):
        sex_age = self.max_age/2
        probability = f(self.max_age, self.spread(), self.age) * 100
        prob_fac = random.randint(0, 100)
        self.age = self.age + 1
        if (self.age > (self.max_age * max_age_m)):
            self.alive = 0

        if (prob_fac < probability * 3):
            # Reproduction cycle

            return 1
        else:
            return 0



class Population:
    population = []
    max_population = 500000
    food_remaining = 0
    def __init__(self, population, max_population, food):
        self.population = population
        self.max_population = max_population
        self.food_remaining = food
    def age_multiplier(self):
        pop_size = len(self.population)
        #return 1 - (math.pow(pop_size, 3) / math.pow(self.max_population,3))
        return 1
    def pop_age(self, num_years):
        for i in self.population:
            s = i.reproduce(self.age_multiplier())
            if (s == 1):
                # Food required is i.genes[2]
                if (self.food_remaining >= i.genes[2]):
                    self.food_remaining = self.food_remaining - i.genes[2]
                    i.food_stored = i.food_stored + i.genes[2]
                    # Move food across.
                    new_genes = i.genes
                    for cs in range(0, len(new_genes)):
                        new_genes[cs] = new_genes[cs] + (random.random() / 10)-0.05
                    ss = Individual(new_genes)
                    self.population.append(ss)
                else:
                    i.alive = 0



            if (i.alive == 0):
                self.food_remaining = self.food_remaining + i.food_stored
                self.population.remove(i)
        return len(self.population)
    def average_genes(self):
        average_gene = []
        if (len(self.population) > 0):
            n = len(self.population[0].genes)
            for i in range(0, n):
                average_gene.append(0)
            for i in self.population:
                for p in range(0, len(i.genes)):
                    average_gene[p] = average_gene[p] + i.genes[p]
            for i in range(0, n):
                average_gene[i] = average_gene[i] / len(self.population)
        else:
            average_gene = [0, 0]
        return average_gene


pop_members = []
for i in range(0, 800):
    # Create founder population
    c = Individual([random.randint(0, 10), random.randint(0, 10), random.randint(0, 100)])
    pop_members.append(c)

pop = Population(pop_members, 5000, 10000)
out = ""
for i in range(0, 10000):
    l = pop.pop_age(1)
    ge = pop.average_genes()
    out = out + str(i) + ", " + str(l) + ", " + str(ge[0]) + ", " + str(ge[1]) + ", " + str(pop.food_remaining) + ", " + str(ge[2]) + "\n"
    print str(i) + ": " + str(l)

q = open('test_stage.csv', 'r+')
q.write(out)
q.close()
