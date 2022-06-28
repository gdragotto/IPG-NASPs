from Instances import *
# get optimization software
import gurobipy as grb
import numpy as np


#######################################################
##        COMPUTE INITIAL SET OF STRATEGIES          ##
## Generate initial strategies: monopoly strategies  ##
#######################################################

# INPUT
# G : game class (see Instances.py)

# OUTPUT
# S = list of strategies
# U_p = individial profit for each player and each strategy in S
# Best_m = list of the players best reaction models

def InitialStrategies(G, opt_solver=1):
    ### for each player produce the optimal strategy if she was alone in the game ###
    S = [[[]] for p in range(G.m())]  # list of strategies
    U_p = [[[]] for p in range(G.m())]  # associated individual profit
    # Profile is the profile of strategies
    Profile = [np.array([0 for k in range(G.n_I()[p] + G.n_C()[p])]) for p in range(G.m())]
    Profile[G.m()-1][0]=150
    # Best reaction models
    Best_m = [None for i in range(G.m())]
    for p in range(G.m()):
        S[p][0], U_p[p][0], Model_p = BestReactionGurobiNASP(G.name(), G.m(), G.c()[p], G.Q()[p], Profile, p, False,
                                                             Best_m[p])
        Best_m.append(Model_p)
    return S, U_p, Best_m


# Compute Best Reaction of player against the strategy 'Profile'
def BestReactionGurobiNASP(name, m, c_p, Q_p, Profile, p, create, m_p=None, CE_verify=False):
    m_p = grb.Model("BR_"+str(m))
    m_p.setParam('OutputFlag', False)
    m_p = grb.read(name + "_" + str(p) + ".mps")
    m_p.setParam('OutputFlag', False)
    m_p.setParam("Threads", 2)
    m_p.ModelSense = grb.GRB.MAXIMIZE

    # variables
    x = np.array(m_p.getVars())

    # Objective
    xk_Qkp = sum(np.dot(Profile[k], Q_p[k]) for k in range(m) if k != p)  # np.array
    objective = grb.LinExpr(np.dot(c_p, x) + np.dot(x, xk_Qkp))
    m_p.setObjective(objective)

    # warm start
    for j, aux_var in enumerate(m_p.getVars()):
        aux_var.start = Profile[p][j]

    m_p.optimize()
    # Shadow price
    try:
        sol = []
        value = 0
        if p == m - 1:
            delta = xk_Qkp[0]
            price = Profile[p][0]
            if delta > 0:
                price = Profile[p][0] + 1
            else:
                price = Profile[p][0] - 1

            sol = [price]
            if delta < 1 and price < 2:
                price = 180
                value = -1000
            else:
                value = round(-abs(delta)*price)
            print("Trying to clear", delta)
            print("\tSetting the price to", price, " -- value of", round(value))
        else:
            sol = [i.x for i in m_p.getVars()]
            value = m_p.ObjVal

        return sol, value, m_p

    except:
        print("Wow! The best reaction problem has no feasible solution. The status code is: ", m_p.status)
