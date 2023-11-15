#!/usr/bin/env python3

#import numpy as np
import math

# MKS
G = 6.67e-11  #N m**2/kg**2

class Particle():
    def __init__(self, m=0.0, r=[0.0,0.0,0.0], v = [0.0,0.0,0.0],Static=False):
        self.m = m # [kg]
        self.r = r # [m, m, m]
        self.v = v # [m/s, m/s, m/s]
        self.i = 0 # index in the n-body-system
        self.static = Static # if true, the particle is not moved
        
    def Print(self):
        print (self.i,self.m, self.r[0], self.r[1],self.r[2],self.v[0],self.v[1],self.v[2])


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
        return math.sqrt(r[0]**2 + r[1]**2 + r[2]**2)
    
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
                p.v[0] = vx + p.v[0]
                p.v[1] = vy + p.v[1]
                p.v[2] = vz + p.v[2]
                
                
            for p in self.n_body_system.p: #for all particles
                p.r[0] = p.v[0]*self.dt + p.r[0]
                p.r[1] = p.v[1]*self.dt + p.r[1]
                p.r[2] = p.v[2]*self.dt + p.r[2]            
                
                
            return self.n_body_system

                
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
    
mars_mass = 6.4171e23 #Kg
jupyter_mass = 1.8982e27 #Kg


