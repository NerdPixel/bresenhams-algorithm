import numpy as np
def calcDelta(fP ,sP):
    return np.subtract(sP, fP)


if __name__ == '__main__':
    fP = np.array([101, 5])
    sP = np.array([107, 9])
    delta = calcDelta(fP, sP)
    E = 2 * delta[1] - delta[0]

    while not np.allclose(fP, sP):
        if E <= 0:
            fP[0] += 1
            E = E + 2*calcDelta(fP, sP)[1]
            print("right")
        else:
            fP += 1
            delta = calcDelta(fP, sP)
            E = E + 2*delta[1]-2*delta[0]
            print("right & up")
        print(fP)
