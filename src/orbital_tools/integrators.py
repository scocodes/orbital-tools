def rk4_step(fun, t, y, dt, **kwargs):

    k1 = fun(t, y, **kwargs)
    k2 = fun(t + dt/2, y + dt/2 * k1,  **kwargs)
    k3 = fun(t + dt/2, y + dt/2 * k2,  **kwargs)
    k4 = fun(t + dt, y + dt * k3,  **kwargs)

    kavg = (1/6) * (k1 + 2*k2 + 2*k3 + k4)

    return y + dt * kavg