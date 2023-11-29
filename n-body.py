#!/usr/bin/env python3

#       Library
import numpy as np
import math as m
import matplotlib.pyplot as plt
from scipy.constants import G  # MKS N m**2/kg**2

#         Class

class Particle():
    def __init__(self, m=0.0, r = 0.0, p=[0.0,0.0,0.0], ve = 0.0, v = [0.0, 0.0, 0.0], Static=True, Acceleration = [0.0, 0.0, 0.0]):
        self.m = m # [kg]
        self.r = r # [ua] (astronomical units) Average distance to the Sun
        self.p = p # [m, m, m] Position vector 
        self.ve = ve # [m/s] Escape velocity
        self.v = v # [m/s, m/s, m/s]
        self.i = 0 # index in the n-body-system
        self.static = Static # if true, the particle is not moved
        self.acce = Acceleration
        
    def Print(self):
        print (self.i, self.p[0], self.p[1],self.p[2],self.v[0],self.v[1],self.v[2])

'''
class Particle():
    def __init__(self, m=0.0, r=[0.0,0.0,0.0], v = [0.0,0.0,0.0],Static=False):
        self.m = m # [kg]
        self.r = r # [m, m, m]
        self.v = v # [m/s, m/s, m/s]
        self.i = 0 # index in the n-body-system
        self.static = Static # if true, the particle is not moved
'''
        
    #def Print(self):
        #print (self.i,self.m, self.r[0], self.r[1],self.r[2],self.v[0],self.v[1],self.v[2])


class N_body_system():
    def __init__(self):
        self.N = 0  #number of particles
        self.p = [] # set of particles

    def add_particle(self, p):
        self.N = self.N + 1
        p.i = self.N
        self.p.append(p)

    def Print(self):
        for p in self.p:
            p.Print()

    def Header(self):
        print(self.N)
        print("#index","mass", "x","y","z","vx","vy","vz")


class Integrator():
    def __init__(self, n_body_system,dt):
        self.n_body_system = n_body_system
        self.dt = dt

    def E(self,m,r):
        #suma = 0.0
        #for p in self.n_body_system.p: #for all particles
        #    m = p.m
        #    if (p.i != n):
        #        suma = suma+ m*dt/r**3
        return (G*m)/(r**3)
                
    def U(self, r_i, r_n):
        r_x = r_i[0] - r_n[0]
        r_y = r_i[1] - r_n[1]
        r_z = r_i[2] - r_n[2]
        return [r_x, r_y, r_z]

    def norm(self, r):
        return m.sqrt(r[0]**2 + r[1]**2 + r[2]**2)
    
    def compute(self):
        #print("DEB2",self.n_body_system.N)
        for p in self.n_body_system.p: #for all particles
            if (p.static != True):
                n = p.i
                vx = 0.0
                vy = 0.0
                vz = 0.0
                for q in self.n_body_system.p: #sum
                    #print("DEB3",q.i,n)
                    if (q.i != n):
                        u = self.U(q.r,p.r)
                        r = self.norm(u)
                        vx = vx + self.E(p.m, r)*self.dt*u[0]
                        vy = vy + self.E(p.m, r)*self.dt*u[1]
                        vz = vz + self.E(p.m, r)*self.dt*u[2]
                        #print("DEB1",vx,vy,vz)
                p.v[0] = vx + p.v[0] + (p.acce[0]*self.dt)
                p.v[1] = vy + p.v[1] + (p.acce[1]*self.dt)
                p.v[2] = vz + p.v[2] + (p.acce[2]*self.dt)
            
                    
                
                
            for p in self.n_body_system.p: #for all particles
                p.r[0] = p.v[0]*self.dt + p.r[0]
                p.r[1] = p.v[1]*self.dt + p.r[1]
                p.r[2] = p.v[2]*self.dt + p.r[2]            
                
                
            return self.n_body_system

                
ANG = 7.6 # initial angular position of the rocket in radians

#        Position values

sa = m.sin(ANG)
ca = m.cos(ANG)
sca = m.sin(m.pi/2+ANG)
cca = m.cos(m.pi/2+ANG)


#        Particles

# Sun 
Sun = Particle()
Sun.m = 3.95e30 # Mass
Sun.p = [0, 0, 0] # Position vector


# Mars
Mars = Particle()
Mars.m = 6.4e23 # Mass
Mars.r = 1.52  # Average distance to the Sun
Mars.ve = 5030 # Escape velocity
Mars.p = [1.52, 0, 0] # Position vector


#Saturn
Saturn = Particle()
Saturn.m = 5.683e26 # Mass 
Saturn.r = 9.5  # Average distance to the Sun 
Saturn.ve = 35500 # Escape velocity
Saturn.p = [round(Saturn.r*ca,2), round(Saturn.r*sa, 2),0] # Position vector


# Rocket
Rocket = Particle()
Rocket.m = 1e6 # Mass
Rocket.r = 1.52 # Average distance to the Sun 
Rocket.ve = 28000/3.6 # Velocity that beats Mars escape velocity (clearance site)
Rocket.p = [round( Mars.p[0] + (ca*0.03),2), round((Mars.p[1] + sa*0.03), 2),0] # Position vector 
#considering radius on a scale of e5 (0.03e5) [km]
Rocket.static = False # Not static
Rocket.acce = [16795.60,2241.01,0]


#        General information:

Re = Saturn.r *(Saturn.m*(1989e30)**0.4) # Radius of influence/gravitational forces


System = N_body_system()
System.add_particle(Sun)
System.add_particle(Mars)
System.add_particle(Saturn)
System.add_particle(Rocket)

dt = 0.01 #sec
newton = Integrator(System, dt)
System.Header()
skip = 0

for j in range(1555200000): # 1555200000 = 6 months on 0.01 secs
    two_body = newton.compute()
    if (skip % 8640000 == 0):
        two_body.Print()
    skip=skip+1



#                    Visualize

#--------------------------------------------------------------------------------------------------------
#You can see the sun and the planets Mars and Saturn with the following code
#--------------------------------------------------------------------------------------------------------

'''
# Function makesphere of: https://stackoverflow.com/questions/61048426/python-generating-3d-sphere-in-numpy:

def makesphere(x, y, z, radius, resolution=10):
    
    u, v = np.mgrid[0:2*np.pi:resolution*2j, 0:np.pi:resolution*1j]
    X = radius * np.cos(u)*np.sin(v) + x
    Y = radius * np.sin(u)*np.sin(v) + y
    Z = radius * np.cos(v) + z
    return (X, Y, Z)
    
fig = plt.figure("Spheres")
ax = fig.add_subplot(projection='3d')

X, Y, Z = makesphere(Sun.p[0], Sun.p[1], Sun.p[2], 0.6) # radius on a scale of e5 
ax.plot_surface(X, Y, Z, color="y")

X, Y, Z = makesphere(Mars.p[0], Mars.p[1], Mars.p[2],  0.03) # radius on a scale of e5 
ax.plot_surface(X, Y, Z, color="r")

X, Y, Z = makesphere(Saturn.p[0], Saturn.p[1], Saturn.p[2],  0.05) # radius on a scale of e5 
ax.plot_surface(X, Y, Z, color="b")

'''

#--------------------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------------


#m_sun = 1.98847e30 #Kg
#dt = 0.1 #sec
#p_1 = Particle(200.0, [0,0,0], [0, 0, 0])
#p_2 = Particle(200.0, [0.1,0,0], [0, 0, 0])
#two_body = N_body_system()
#two_body.add_particle(p_1)
#two_body.add_particle(p_2)
#newton = Integrator(two_body, dt)
#two_body.Header()
#skip = 0
#for j in range(3000): #300*.7 = 210 sec > 300 sec
#    two_body = newton.compute()
#    if (skip % 10 == 0):
#        two_body.Print()
#    skip=skip+1
#    mars_mass = 6.4171e23 #Kg
#    jupyter_mass = 1.8982e27 #Kg




