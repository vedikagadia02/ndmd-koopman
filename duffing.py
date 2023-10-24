import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib import rc
from scipy.integrate import odeint, quad

def deriv(X, t, lamda, mu):
    """Return the derivatives dx1/dt and dx2/dt"""
    x1, x2 = X
    x1dot = mu*x1
    x2dot = lamda*(x2-x1**2) 
    return x1dot, x2dot

def solve_equation(tmax, dt_per_period, t_trans, x1_0, x2_0, lamda, mu):

    dt = 2*np.pi/ dt_per_period
    t = np.arange(0, tmax, dt)
    """initial conditions x1_0 and x2_0"""
    X0 = [x1_0, x2_0]
    X = odeint(deriv, X0, t, args=(lamda, mu))
    idx = int(t_trans / dt)
    return t[idx:], X[idx:], dt

if __name__=='__main__':
    x1_0, x2_0 = -5,5
    tmax, t_trans = 1, 0
    lamda, mu = 1, -0.05
    dt_per_period = 1000

    # Switch fonts
    mpl.rcParams['font.family'] = ['serif'] # default is sans-serif
    rc('text', usetex=True)
    plt.close("all")
    fig, ax = plt.subplots(1, 1, figsize=(4, 4))

    x1_data = []
    x2_data = []
    t_data = []

    for x1_0 in np.arange(0, 5, 0.25):
        for x2_0 in np.arange(0, 5, 0.25):
            t, X, dt = solve_equation(tmax, dt_per_period, t_trans, x1_0, x2_0, lamda, mu)
            x1, x2 = X.T
            x1_data.append(x1)
            x2_data.append(x2)
            t_data.append(t)

    cmap = plt.get_cmap("viridis")
    dotColors = cmap(np.linspace(0,1,len(x2)))
    # for i in range(0,len(xdot)-1):
    #     ax[0].plot(x[i:i+2], xdot[i:i+2], color=dotColors[i])
    ax.scatter(x1, x2, c=dotColors, s=0.5, alpha=0.8) 

    data = np.stack([np.array(x1_data), np.array(x2_data), np.array(t_data)], axis=2)
    print('data-size', data.shape)
    # print(data)
    print(np.load('duffing-test.npy').shape)
    np.save('duffing.npy', data)
