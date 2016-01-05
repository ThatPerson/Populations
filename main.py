import random

population = []
new_population = []
average_individual = [0, 0, 0]
conditions = [600, 500, 400]
prob = []

n_ind = 5000
n_iter = 5000

for i in range(0, n_ind):
    q = []
    for i in range(0, len(conditions)):
        q.append(random.randint(0, 1000))

    population.append(q)

for q in range(0, n_iter):
    sum_individual = []
    new_population = []
    average_individual = [0,0,0]
    prob = []
    for i in range(0, len(conditions)):
        sum_individual.append(0)
    for i in range(0, len(population)):
        for p in range(0, len(conditions)):
            sum_individual[p] = sum_individual[p] + population[i][p]
    s = ""
    for i in range(0, len(conditions)):
        average_individual[i] = sum_individual[i] / len(population)
        s = s+" "+str(average_individual[i])
    print ("Generation "+str(q)+"["+s+"]") 
    for i in range(0, len(population)):
        probability = 1
        for p in range(0, len(conditions)):
           if (conditions[p] > population[i][p]):
                probability = probability + (population[i][p] / conditions[p]) # This is the issue - the likelihood of survival is too low.
           else:
                probability = probability + (1/(population[i][p] / conditions[p]))
        
        #print (probability)
        prob.append(probability)
    limit = random.randint(0, max(prob))
    for i in range(0, len(population)):
        if (prob[i] > limit):
            population[i] = average_individual
        #throw in some random mutation
        if (random.randint(0, 10) > 7):
            for p in range(0, len(population[i])):
                population[i][p] = population[i][p] + random.randint(-1, 1)
                
           #Doesn't seem to be progressing - seems to stay constant.

            
