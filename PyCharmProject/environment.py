import numpy as np

def obstacles(width, height, food, amountLong, amountTall, size):
    obs = []
    obsLong = []
    obsTall = []
    i = 0
    while i < amountLong:
        x = np.random.random() * (width - size)
        y = np.random.random() * (height - size)
        while (x > food[0] and x < (food[0] + size)) and (y > food[1] and y < (food[1] + size)):
            x = np.random.random() * (width - size)
            y = np.random.random() * (height - size)
        obj = [x, y]
        obsLong.append(obj)
        i += 1
    i = 0
    while i < amountTall:
        x = np.random.random() * (width - size)
        y = np.random.random() * (height - size)
        while (x > food[0] and x < (food[0] + size)) and (y > food[1] and y < (food[1] + size)):
            x = np.random.random() * (width - size)
            y = np.random.random() * (height - size)
        obj = [x, y]
        obsTall.append(obj)
        i += 1
    if obsLong:
        obs.append(obsLong)
    if obsTall:
        obs.append(obsTall)
    return obs

def collisionObstacles(X, obs, chrashed, size):
    num = 0
    index = 0
    for i in X:
        while index < len(i):
            for j in obs[0]:
                if i[index][0] > j[0] and i[index][0] < j[0]+size and i[index][1] > j[1] and i[index][1] < j[1]+5:
                    if chrashed[num][0] == False:
                        chrashed[num] = [True, index]
            for k in obs[1]:
                if i[index][0] > k[0] and i[index][0] < k[0] + 5 and i[index][1] > k[1] and i[index][1] < k[1] + size:
                    if chrashed[num][0] == False:
                        chrashed[num] = [True, index]
            index+=1
        index = 0
        num+=1

def collisionFood(X, ate, food, eaten):
    num = 0
    index = 0
    for i in X:
        while index < len(i):
            if i[index][0] > food[0] and i[index][0] < food[0] + 20 and i[index][1] > food[1] and i[index][1] < food[1] + 20:
                if ate[num][0] == False:
                    ate[num] = [True, index]
                    eaten+=1
            index+=1
        index = 0
        num+=1

    return eaten