import stateMachine
from settings import *
from tkinter import *
from stateMachine import *
from environment import *
from render import *


def main():

    ### Policies Documentation
    #
    # [crossOverMethod, randomMethod, explorationProbability, explorationVariance, \
    #  randomCrossOverFactor, normalVariance, totallyRandomProbability]
    #
    # crossOverMethod:
    #   0 = average over angular acceleration
    #   1 = splice parents at random location
    #   2 = randomly weighted average
    #   3 = average over angular speed
    #
    # randomMethod:
    #   -1 = no random added
    #    0 = add random path to whole path
    #    1 = add random small turn at random location for all ants
    #
    # explorationProbability:
    #   probability of adding a random drastic turn at random location
    #   constriant: 0 < explorationProbability <= 1
    #
    # explorationVariance:
    #   variance of random turn in radians
    #
    # randomCrossOverFactor:
    #   control amount of randomness in random method 0
    #
    # normalVariance:
    #   variance of random turn size in random method 1
    #
    # totallyRandomProbability:
    #   probability of generating a totally random ant during crossOver


               #crM raM expP expV r0fct r1var tranP
    policie11 = [1, 1, 0.15, 1.50, 0.5, 0.05, 0.15]
    policie12 = [1, 1, 0.15, 1.50, 0.5, 0.05, 0.30]
    policie13 = [1, 1, 0.30, 1.50, 0.5, 0.05, 0.15]
    policie14 = [1, 1, 0.30, 1.50, 0.5, 0.05, 0.30]

    policie21 = [2, 1, 0.15, 1.50, 0.5, 0.05, 0.15]
    policie22 = [2, 1, 0.15, 1.50, 0.5, 0.05, 0.30]
    policie23 = [2, 1, 0.30, 1.50, 0.5, 0.05, 0.15]
    policie24 = [2, 1, 0.30, 1.50, 0.5, 0.05, 0.30]

# LEIÐBEININAR: Keyrðu eina printAverageScore í hverri keyrslu
    printAverageScore("Policie11", policie11, 10)
    # printAverageScore("Policie12", policie12, 10)
    # printAverageScore("Policie13", policie13, 10)
    # printAverageScore("Policie14", policie14, 10)
    # printAverageScore("Policie21", policie21, 10)
    # printAverageScore("Policie22", policie22, 10)
    # printAverageScore("Policie23", policie23, 10)
    # printAverageScore("Policie24", policie24, 10)

    return

# run simulation on policie nrOfRuns times
def printAverageScore(policieName, policie, nrOfRuns):
    print(policieName)
    print(policie)
    nrOfFinishedRuns = 0
    score = 0
    for i in range(nrOfRuns):
        print("    run: ", i)
        newScore = runSimulation(policie)
        if newScore != -1:
            score += newScore
            nrOfFinishedRuns += 1
    if nrOfFinishedRuns != 0:
        average = score / nrOfFinishedRuns
    print("Average score = ", average)
    print("Succeded runs: ", nrOfFinishedRuns, "/", nrOfRuns)


# run a simulation with parameters from policie
def runSimulation(policie):
    updateCrossoverSettings(policie)

    #initialize varaibles
    obj = [False, 0]
    chrashed = [obj] * N
    ate = [obj] * N
    eaten = 0
    counter = 0

    # create test environments with foods
    testEnvs = [[i, [i*10 + j for j in range(numberOfFoods)]] for i in range(numberOfEnvs)]
    # fix for unplayable environments
    i = numberOfEnvs + 1
    testEnvs[4] = [i, [i*10 + j for j in range(numberOfFoods)]]
    i = numberOfEnvs + 2
    testEnvs[9] = [i, [i*10 + j for j in range(numberOfFoods)]]

    envNr = 0
    totalNrOfSteps = 0
    for env in testEnvs:
        # calculate initial random paths
        angularSpeed = randomAngularSpeed()
        A = anglesFromSpeed(angularSpeed)
        X = pathsFromAngles(A)

        # generate obstacles and food locations from seeds
        obsSeed = env[0]
        foodSeeds = env[1]
        foodLocations = [newFood(width, height, seed) for seed in foodSeeds]
        obs = obstacles(width, height, foodLocations, nrOfHorizObstacles, nrOfVertObstacles, obsSize, obsSeed)

        # initialize counters
        nrOfSteps = 0
        foodNr = 0

        for foodLocation in foodLocations:
            #initialize
            nrOfStepsCurrentFood = 0
            eaten = 0
            chrashed = [obj] * len(X)
            ate = [obj] * len(X)

            # calculate collision with obstacles and food
            collisionObstacles(X, obs, chrashed, obsSize)
            eaten = collisionFood(X, ate, foodLocation, eaten)

            # eat food until eaten
            while eaten <= bitesPerFood:
                collisionObstacles(X, obs, chrashed, obsSize)
                eaten = collisionFood(X, ate, foodLocation, eaten)

                F = fitnessAll(foodLocation, X, ate, chrashed)

                if nrOfSteps % drawEveryNRuns == 0:
                    rendera(index, width, height, tk, canvas, X, foodLocation, obs, obsSize, chrashed, ate, eaten)
                if nrOfStepsCurrentFood >= maxNrOfStepsPerFood:
                    angularSpeed = randomAngularSpeed()
                else:
                    angularSpeed = newAngGen(angularSpeed, F)

                # generate paths
                A = anglesFromSpeed(angularSpeed)
                X = pathsFromAngles(A)

                #initialize
                chrashed = [obj] * len(X)
                ate = [obj] * len(X)

                #increment counters
                nrOfSteps += 1
                nrOfStepsCurrentFood += 1
                totalNrOfSteps += 1

                if debug:
                    maxFit = np.max(F)
                    print("    envNr: ", envNr,  " foodNr: ", foodNr , " eaten: ", '%3i' % eaten, " steps: ", '%3i' % nrOfSteps, " totalSteps: ", '%4i' % totalNrOfSteps, " maxFit: ", maxFit)

                if nrOfSteps >= stepLimit:
                    print("number of steps reached limit, canceling")
                    return -1
            if debug: print("    envNr: ", envNr,  " foodNr: ", foodNr , " steps: ", '%3i' % nrOfSteps, " totalSteps: ", '%4i' % totalNrOfSteps)
            foodNr += 1
        envNr += 1
    return totalNrOfSteps

def pShape(X):
    print(np.array(X).shape)

# update settings for crossover methods and random methods
def updateCrossoverSettings(s):
    stateMachine.crossOverMethod = s[0]
    stateMachine.randomMethod = s[1]
    stateMachine.explorationProbability = s[2]
    stateMachine.explorationVariance = s[3]
    stateMachine.randomCrossOverFactor = s[4]
    stateMachine.normalVariance = s[5]
    stateMachine.totallyRandomProbability = s[6]

if __name__ == "__main__":
    main()







