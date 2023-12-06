#!/usr/bin/env python3

import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

with open('data_1.txt') as f:
    lines = f.readlines()

N = int(lines[0])
i = 0
j = 0
fig = plt.figure()
ax = fig.add_subplot(111)
x = []
y = []
z = []
for data in lines[2:]:
    coordinates = data.split()
    x.append(float(coordinates[1]))
    y.append(float(coordinates[2]))
    i = i+1
    if (i==N):
        i = 0
        ax.scatter(x[0],y[0], s=60000, color = "#EDB120")
        ax.scatter(x[1],y[1], s=3000, color = "#A2142F")
        ax.scatter(x[2],y[2], s=5000, color = "#0072BD")
        ax.scatter(x[3],y[3], color = "g")

        plt.title( "Rocket's Path From Mars to Saturn" )
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        legend_elements= [Line2D([0], [0], label='Sun', marker='o', color="#EDB120", markersize=10, 
          linestyle=''),
                  Line2D([0], [0], label='Mars', marker='o', color="#A2142F", markersize=10, 
          linestyle=''),
                  Line2D([0], [0], label='Saturn', marker='o', color="#0072BD", markersize=10, 
          linestyle=''),
                  Line2D([0], [0], label='Rocket', marker='o', color="g", markersize=10, 
          linestyle=''),]
        ax.legend(handles=legend_elements, loc='upper left')
        
        plt.savefig("frame-"+str(j)+".png")
        plt.cla()
        j = j+1
        x = []
        y = []
        z = []
