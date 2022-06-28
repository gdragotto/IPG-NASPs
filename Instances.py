# from numpy import *
import glob, os

import numpy as np
import gurobipy as grb
import pyarma as pa


class Game(object):
    r"""Create instances in a standard format.

    Parameters:
    ----------
    type: string with Knapsack or LotSizing
    m: number of players (optional),
    n: number of items for Knapsack, number of period for LotSizing (optional), number of vertices KEG
    ins: number associated with the instance (Knapsack only), must be <numb_ins
    numb_ins: number of instances (Knapsack only)
    K: maximum cycle length allowed (KEG only)
    Returns:
    -------
    m: number of players
    n_I: list of number of binary variables for each player i=0,..,m-1
    n_C: list of number of continuous variables for each player i=0,..,m-1
    n_constr: list of number of constraints for each player i=0,..,m-1
    c: list of coeficients for the linear part of the obj function,
        for each player i=0,..,m-1
    Q: list of matrices for the bilinear part of the obj function,
        for each player i=0,..,m-1
    A: list of constraint matrices for each player i=0,..,m-1
    b: list of vectors with the rhs  for the constraints of each player i=0,..,m-1
    """

    def __init__(self, type, m=2, n=10, ins=0, numb_ins=10, K=0, NASPfile=""):
        if type == 'NASP':
            m, n_I, n_C, n_constr, c, Q, A, b = NASP(NASPfile)
            self.__name = NASPfile
        elif type == "empty":
            m = 0
            n_I = []
            n_C = []
            n_constr = []
            c, Q, A, b = [], [], [], []
        else:
            print("Not valid instance")
            raise NameError('Give a proper type to the game')
        self.__m = m
        self.__n_I = n_I
        self.__n_C = n_C
        self.__n_constr = n_constr
        self.__c = c
        self.__Q = Q
        self.__A = A
        self.__b = b
        self.__type = type
        self.__ins = ins
        self.__numb_ins = numb_ins

    # give parameters of a player
    def Player_n_I(self, p):
        if p > self.__m:
            raise NameError('That player does not exist')
        else:
            return self.__n_I[p]

    def Player_n_C(self, p):
        if p > self.__m:
            raise NameError('That player does not exist')
        else:
            return self.__n_C[p]

    def Player_n_constr(self, p):
        if p > self.__m:
            raise NameError('That player does not exist')
        else:
            return self.__n_constr[p]

    def Player_c(self, p):
        if p > self.__m:
            raise NameError('That player does not exist')
        else:
            return self.__c[p]

    def Player_Q(self, p):
        if p > self.__m:
            raise NameError('That player does not exist')
        else:
            return self.__Q[p]

    def Player_A(self, p):
        if p > self.__m:
            raise NameError('That player does not exist')
        else:
            return self.__A[p]

    def Player_b(self, p):
        if p > self.__m:
            raise NameError('That player does not exist')
        else:
            return self.__b[p]

    def Numb_players(self):
        return self.__m

    def type(self):
        return self.__type

    def name(self):
        return self.__name

    def ins(self):
        return self.__ins

    def numb_ins(self):
        return self.__numb_ins

    def b(self):
        return self.__b

    def A(self):
        return self.__A

    def Q(self):
        return self.__Q

    def c(self):
        return self.__c

    def n_constr(self):
        return self.__n_constr

    def n_C(self):
        return self.__n_C

    def n_I(self):
        return self.__n_I

    def m(self):
        return self.__m

    def Save_Game(self, m=2, n=10, ins=0):
        # save file with instance
        filename = 'Instances/' + self.__type + "/Game_" + str(m) + "_" + str(n) + "_" + str(ins) + ".npy"
        with open(filename, "wb") as f:
            np.save(f, self.__m)
            np.save(f, self.__n_I)
            np.save(f, self.__n_C)
            np.save(f, self.__n_constr)
            np.save(f, self.__c)
            np.save(f, self.__Q)
            if self.__type == "KEG":  # then number of restrictions can vary an numpy raises an error if we save A all together
                aux = [self.__A[p] for p in range(self.__m)]
                finalc = np.empty(len(aux), dtype=object)
                finalc[:] = aux
                np.save(f, finalc)
            else:
                np.save(f, self.__A)
            np.save(f, self.__b)
            np.save(f, self.__type)
            np.save(f, self.__ins)
            np.save(f, self.__numb_ins)

    def Read_Game(self, filename):
        if self.__type == "empty":
            with open(filename, "rb") as f:
                self.__m = int(np.load(f))
                self.__n_I = list(np.load(f))
                self.__n_C = list(np.load(f))
                self.__n_constr = list(np.load(f))
                self.__c = list(np.load(f, allow_pickle=True))
                self.__Q = list(np.load(f, allow_pickle=True))
                self.__A = list(np.load(f, allow_pickle=True))
                self.__b = list(np.load(f))
                self.__type = str(np.load(f))
                self.__ins = int(np.load(f))
                self.__numb_ins = int(np.load(f))
        else:
            raise NameError("It is not an empty game")

    # create game manually
    def Create(self, m, n_I, n_C, n_constr, c, Q, A, b, type="empty", ins=1, numb_ins=1):
        self.__m = m
        self.__n_I = n_I
        self.__n_C = n_C
        self.__n_constr = n_constr
        self.__c = c
        self.__Q = Q
        self.__A = A
        self.__b = b
        self.__type = type
        self.__ins = ins
        self.__numb_ins = numb_ins

    # recover info on lot sizing game
    def A_market(self):
        if self.__type == "LotSizing":  # recover A_market
            T = self.__n_I[0]  # number of periods equal to number of binary variables
            # market size: part of linear objective
            return list(self.__c[0][2 * T:3 * T])

    def B(self):
        if self.__type == "LotSizing":  # recover B
            T = self.__n_I[0]  # number of periods equal to number of binary variables
            # market slope: part of quadratic objective
            return [int(-0.5 * self.__Q[0][0][2 * T + i, 2 * T + i]) for i in range(T)]

    def F(self):
        if self.__type == "LotSizing":  # recover F
            T = self.__n_I[0]  # number of periods equal to number of binary variables
            # F : setup costs
            return [list(self.__c[p][:T]) for p in range(self.__m)]

    def H(self):
        if self.__type == "LotSizing":  # recover H
            T = self.__n_I[0]  # number of periods equal to number of binary variables
            # H : inventory costs
            return [list(self.__c[p][3 * T:4 * T]) for p in range(self.__m)]

    def C(self):
        if self.__type == "LotSizing":  # recover C
            T = self.__n_I[0]  # number of periods equal to number of binary variables
            # C : production costs
            return [list(self.__c[p][T:2 * T]) for p in range(self.__m)]

    def M(self):
        if self.__type == "LotSizing":  # recover M
            T = self.__n_I[0]  # number of periods equal to number of binary variables
            # M : production capacity per period
            return [[self.__A[p][2 * T + i, i] for i in range(T)] for p in range(self.__m)]

    def __str__(self):
        return self.__type + " game"


################################################
##################### NASP #####################
################################################
def NASP(instanceName):

    followers = []
    with open(instanceName + ".txt") as f:
        lines = f.readlines()
        followers = np.array(lines[0].split())
        followers = [int(i) for i in followers]

    m = len(followers) + 1
    n_I = []
    n_C = []
    c = []
    Q = []
    n_constr = []
    n_vars = []
    n_vars_original = []

    for p in range(m - 1):
        model = grb.read(instanceName + "_" + str(p) + ".mps")
        i = 0
        cnt = 0
        nvar = len(model.getVars())
        for v in model.getVars():
            if v.getAttr(grb.GRB.Attr.VType) == grb.GRB.CONTINUOUS:
                cnt = cnt + 1
            else:
                i = i + 1
        n_I.append(i)
        n_C.append(cnt)
        n_constr.append(0)
        c_ = pa.mat()
        c_.load(instanceName + "-clin_" + str(p) + ".mat")
        n_vars.append(nvar)
        n_vars_original.append(len(c_))
        c_ = -np.concatenate((np.array(c_), np.zeros((nvar - len(c_), 1))), axis=0)
        c.append(np.squeeze(np.asarray(c_)))

    # Fictious player
    n_I.append(0)
    n_C.append(1)  # clearing price
    n_vars.append(1)
    n_vars_original.append(1)
    c.append(np.array([0]))

    for i in range(m):
        Qi = []
        Q_read = pa.mat()
        C_read = pa.mat()
        if i != m - 1:
            Q_read.load(instanceName + "-Q_" + str(i) + ".mat")
            C_read.load(instanceName + "-C_" + str(i) + ".mat")
        previous = 0
        # print(C_read, Q_read)
        for j in range(m):
            # Qii is always empty, the rest is just the price times export/imports
            Qij = np.zeros((n_vars[i], n_vars[j]))
            # If different player
            if i != j and i != m - 1:
                for k in range(n_vars_original[i]):  # variable of i
                    for l in range(n_vars_original[j]):  # variable of j
                        Qij[k][l] = C_read[k, previous + l]
                        if C_read[k, previous + l] > 0:
                            print("Interaction among", i, j, " on variables", k, l, "is", C_read[k, previous + l])
                previous = n_vars_original[j]
                # Shadow player
                if j == m - 1:
                    #Qij[followers[i]][0] = 1  # Net Imports
                    Qij[followers[i] + 1][0] = 1  # Net Exports
                    for z in range(m-2):
                        Qij[followers[i] + 2 +z][0] = -1 # Imports from other countries
            if i == m - 1 and i != j:
                # Shadow player
                Qij[0][followers[j]] = 1 # Net Imports
                Qij[0][followers[j] + 1] = -1  # Net Exports

            Qi.append(np.transpose(Qij))
        Q.append(Qi)

    # Create shadow model
    shadow = grb.Model()
    shadow.addVar(lb=100, ub=700, vtype="C", name="price")
    shadow.write(instanceName + "_" + str(m - 1) + ".mps")

    # Dummy constraints
    A = [np.zeros((1, n_vars[p])) for p in range(m)]
    b = [0 for p in range(m)]

    print("Loaded ", instanceName, " with", m, "players with numVars", n_vars_original)
    print("Followers", followers)

    return m, n_I, n_C, n_constr, c, Q, A, b


if __name__ == "__main__":
    np.random.seed(1)
    print("Loading instance file ./Instances/NASP/Instance_1")
    NASP = Game('NASP', NASPfile="./Instances/NASP/Instance_1")
