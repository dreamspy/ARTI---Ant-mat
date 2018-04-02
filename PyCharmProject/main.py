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
    #   probability of generating totally random ants


    policies = [
                [1, 1, 0.00, 1.5, 0.5, 0.25, 0.01],
                [1, 1, 0.01, 1.5, 0.5, 0.25, 0.01],
                [2, 1, 0.01, 1.5, 0.5, 0.1, 0.01],
                [3, 1, 0.01, 1.5, 0.5, 0.1, 0.01]
                ]

    for policie in policies:
        print(policie)
        print(testPolicie(policie))

def testPolicie(policie):
    updateCrossoverSettings(policie)

    obj = [False, 0]
    chrashed = [obj] * N
    ate = [obj] * N
    eaten = 0
    counter = 0


    testEnvs = [[i, [i + j for j in range(numberOfFoods)]] for i in range(numberOfEnvs)]


    for env in testEnvs:
        angularSpeed = randomAngularSpeed()
        A = anglesFromSpeed(angularSpeed)
        X = pathsFromAngles(A)
        obsSeed = env[0]
        foodSeeds = env[1]
        foodLocations = [newFood(width, height, seed) for seed in foodSeeds]
        obs = obstacles(width, height, foodLocations, 2, 3, foodSize, obsSeed)
        chrashed = [obj] * len(X)
        ate = [obj] * len(X)

        nrOfSteps = 0

        for foodLocation in foodLocations:
            eaten = 0
            chrashed = [obj] * len(X)
            ate = [obj] * len(X)
            collisionObstacles(X, obs, chrashed, foodSize)
            eaten = collisionFood(X, ate, foodLocation, eaten)
            while eaten <= bitesPerFood:
                collisionObstacles(X, obs, chrashed, foodSize)
                eaten = collisionFood(X, ate, foodLocation, eaten)
                if nrOfSteps % drawEveryNRuns == 0:
                    rendera(index, width, height, tk, canvas, X, foodLocation, obs, foodSize, chrashed, ate, eaten)

                # calc fit
                F = fitnessAll(foodLocation, X, ate, chrashed)

                # new gen
                angularSpeed = newAngGen(angularSpeed, F)
                A = anglesFromSpeed(angularSpeed)
                X = pathsFromAngles(A)

                chrashed = [obj] * len(X)
                ate = [obj] * len(X)
                nrOfSteps += 1
                if nrOfSteps >= stepLimit:
                    print("number of steps reached limit, canceling")
                    return -1

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







