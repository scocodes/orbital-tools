import numpy as np

class Dynamics:
     
    def __init__(self, atmosphere=None, B=100):
         self.atm = atmosphere
         self.B = 100

    def two_body_rhs(self, t, y):
            r = y[0:3]
            v = y[3:6]

            rmag = np.linalg.norm(r)
            alt_km = (rmag-self.atm.r_earth) / 1e3

            agrav = -self.atm.mu_earth*(r/rmag**3)
            rho = self.atm.density(alt_km)
            vmag = np.linalg.norm(v)
            if vmag > 0:
                adrag = -1/(2*self.B) * (rho*v*vmag)
            else:
                adrag = np.zeros(3)
            
            atotal = adrag + agrav
            dydt = np.zeros_like(y)

            dydt[0:3] = v
            dydt[3:6] = atotal
            return dydt
    
