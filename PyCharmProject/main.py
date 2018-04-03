import stateMachine
from settings import *
from tkinter import *
from stateMachine import *
from environment import *
from render import *


def main():

    ### Policies structure
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
    policies = [
                [1, 1, 0.05, 0.25, 0.5, 0.05, 0.05],
                [1, 1, 0.05, 0.50, 0.5, 0.05, 0.05],
                [1, 1, 0.05, 1.50, 0.5, 0.05, 0.05],
                [1, 1, 0.05, 3.00, 0.5, 0.05, 0.05],
                ]

    policies2 = [
                [2, 1, 0.05, 1.50, 0.5, 0.05, 0.05],
                [2, 1, 0.05, 1.50, 0.5, 0.05, 0.05],
                [2, 1, 0.05, 1.50, 0.5, 0.05, 0.05],
                [2, 1, 0.05, 1.50, 0.5, 0.05, 0.05],
                [2, 1, 0.05, 1.50, 0.5, 0.05, 0.05],
                [2, 1, 0.05, 1.50, 0.5, 0.05, 0.05],
                [2, 1, 0.05, 1.50, 0.5, 0.05, 0.05],
                [2, 1, 0.05, 1.50, 0.5, 0.05, 0.05],
                [2, 1, 0.05, 1.50, 0.5, 0.05, 0.05],
                [2, 1, 0.05, 1.50, 0.5, 0.05, 0.05],
    ]
    policies1 = [
                [1, 1, 0.05, 1.50, 0.5, 0.05, 0.05],
                [1, 1, 0.05, 1.50, 0.5, 0.05, 0.05],
                [1, 1, 0.05, 1.50, 0.5, 0.05, 0.05],
                [1, 1, 0.05, 1.50, 0.5, 0.05, 0.05],
                [1, 1, 0.05, 1.50, 0.5, 0.05, 0.05],
                [1, 1, 0.05, 1.50, 0.5, 0.05, 0.05],
                [1, 1, 0.05, 1.50, 0.5, 0.05, 0.05],
                [1, 1, 0.05, 1.50, 0.5, 0.05, 0.05],
                [1, 1, 0.05, 1.50, 0.5, 0.05, 0.05],
                [1, 1, 0.05, 1.50, 0.5, 0.05, 0.05],
                ]

    print("2 obstacles")
    print("Policie")
    for policie in policies:
        print(policie)
        testPolicie(policie)

    print("Policie1")
    score = 0
    for policie in policies1:
        print(policie)
        score += stestPolicie(policie)
        average = score / len(policies1)
    print("Average score = ", average)

    print("Policie2")
    score = 0
    for policie in policies2:
        print(policie)
        score += stestPolicie(policie)
        average = score / len(policies1)
    print("Average score = ", average)

    return


def testPolicie(policie):
    updateCrossoverSettings(policie)

    obj = [False, 0]
    chrashed = [obj] * N
    ate = [obj] * N
    eaten = 0
    counter = 0

    testEnvs = [[i, [i + j for j in range(numberOfFoods)]] for i in range(numberOfEnvs)]


    envNr = 0
    totalNrOfSteps = 0
    for env in testEnvs:
        angularSpeed = randomAngularSpeed()
        A = anglesFromSpeed(angularSpeed)
        X = pathsFromAngles(A)
        obsSeed = env[0]
        foodSeeds = env[1]
        foodLocations = [newFood(width, height, seed) for seed in foodSeeds]
        obs = obstacles(width, height, foodLocations, nrOfHorizObstacles, nrOfVertObstacles, obsSize, obsSeed)
        chrashed = [obj] * len(X)
        ate = [obj] * len(X)

        nrOfSteps = 0
        foodNr = 0
        for foodLocation in foodLocations:
            # print("        rendering")
            rendera(index, width, height, tk, canvas, X, foodLocation, obs, obsSize, chrashed, ate, eaten)
            eaten = 0
            chrashed = [obj] * len(X)
            ate = [obj] * len(X)
            # print("        collisionObstacles first")
            collisionObstacles(X, obs, chrashed, obsSize)
            # print("        collisionFood first")
            eaten = collisionFood(X, ate, foodLocation, eaten)
            while eaten <= bitesPerFood:
                # print("        collision")
                collisionObstacles(X, obs, chrashed, obsSize)
                eaten = collisionFood(X, ate, foodLocation, eaten)
                # if nrOfSteps % drawEveryNRuns == 0:
                #     rendera(index, width, height, tk, canvas, X, foodLocation, obs, obsSize, chrashed, ate, eaten)

                # calc fit
                # print("        fitness")
                F = fitnessAll(foodLocation, X, ate, chrashed)

                # new gen
                # print("        newAngGen")
                angularSpeed = newAngGen(angularSpeed, F)
                # print("        calc A")
                A = anglesFromSpeed(angularSpeed)
                # print("        cald X")
                X = pathsFromAngles(A)

                chrashed = [obj] * len(X)
                ate = [obj] * len(X)
                nrOfSteps += 1
                totalNrOfSteps += 1
                maxFit = np.max(F)
                # print("        finished while round")
                # if debug: print("    envNr: ", envNr,  " foodNr: ", foodNr , " eaten: ", '%3i' % eaten, " steps: ", '%3i' % nrOfSteps, " totalSteps: ", '%4i' % totalNrOfSteps, " maxFit: ", maxFit)
                if nrOfSteps >= stepLimit:
                    print("number of steps reached limit, canceling")
                    return -1
            # if debug: print("    envNr: ", envNr,  " foodNr: ", foodNr , " steps: ", '%3i' % nrOfSteps, " totalSteps: ", '%4i' % totalNrOfSteps)
            foodNr += 1
        envNr += 1
    print("Total number of steps: ", totalNrOfSteps)

    return nrOfSteps

def pShape(X):
    print(np.array(X).shape)

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







