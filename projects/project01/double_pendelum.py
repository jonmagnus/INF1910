
g = 9.81

class DoublePendelum:
    def __init__(self,M1=1,L1=1,M2=1,L2=1):
        self.M1 = M1
        self.L1 = L1
        self.M2 = M2
        self.L2 = L2

    def __call__(self,t,y):
        theta1,omega1,theta2,omega2 = y
        diff_theta = theta2 - theta1

        theta1_ = omega1
        theta2_ = omega2

        omega1_ = (self.M2*self.L1*omega1**2*np.sin(diff_theta)*np.cos(diff_theta)
                   + self.M2*g*np.sin(theta2)*np.cos(diff_theta)
                   + self.M2*self.L2*omega2**2*np.sin(diff_theta)
                   - (self.M1 + self.M2)*g*np.sin(theta1)
                  )/(
                  (self.M1 + self.M2)*self.L1
                   - self.M2*self.L1*np.cos(diff_theta)**2)
        omega2_ = (self.
