
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import numpy as np 
import time
import math
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
def ab(a,b):
    absulute  = float(math.sqrt((a[0]-b[0])**2+(a[1]-b[1])**2+(a[2]-b[2])**2))
    return float(absulute**3) 
class body():
    def __init__(self,mass,position,first1,secound1,first_mass,secound_mass):
        self.velocity = 0 #it mabe change later 
        self.mass = mass 
        self.position = position 
        self.dt  = 0.1
        self.first_mass = first_mass
        self.secound_mass = secound_mass
        self.G = 10
        self.first_postion = first1
        self.secound_postion = secound1
        self.acs = -self.G*self.first_mass*((self.position-self.first_postion)/float(ab(self.position,self.first_postion))) - self.G*self.secound_mass*((self.position-self.secound_postion)/float(ab(self.position,self.secound_postion)))
    def update_velocity(self):
        self.velocity = self.velocity + self.dt*self.acs

    def update_position(self,first,secound):
        self.position = self.position + self.dt*self.velocity
        self.first_postion = first
        self.secound_postion = secound
        self.acs = -self.G*self.first_mass*((self.position-self.first_postion)/float(ab(self.position,self.first_postion))) - self.G*self.secound_mass*((self.position-self.secound_postion)/float(ab(self.position,self.secound_postion)))
        
positions = np.random.uniform(low = -20,high =20,size=(3,3))
pos1 = positions[0]
pos2 = positions[1]
pos3 = positions[2]
mass1 = 10
mass2 = 17
mass3 = 2.3
body1 = body(mass1,pos1,pos2,pos3,mass2,mass3)
body2 = body(mass2,pos2,pos1,pos3,mass1,mass3)
body3 = body(mass3,pos3,pos2,pos1,mass2,mass1)
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
while True:
    z = np.array([body1.position[2],body2.position[2],body3.position[2]])
    y = np.array([body1.position[1],body2.position[1],body3.position[1]]) 
    x = np.array([body1.position[0],body2.position[0],body3.position[0]])
    ax.plot(x,y,z)
    plt.pause(0.001)
    body1.update_velocity()
    body2.update_velocity()
    body3.update_velocity()
    body1.update_position(body2.position,body3.position)
    body2.update_position(body1.position,body3.position)
    body3.update_position(body2.position,body1.position)
    time.sleep(0.01)
plt.show()
