def rk4_step(fun, t, y, dt, **args):

    k1 = fun(t, y, args)
    k2 = fun(t + dt/2, y + dt/2 * k1, args)
    k3 = fun(t + dt/2, y + dt/2 * k2, args)
    k4 = fun(t + dt, y + dt * k3, args)

    kavg = (1/6) * (k1 + 2*k2 + 2*k3 + k4)

    return y + dt * kavg