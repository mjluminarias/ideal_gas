import matplotlib.pyplot as plt
import numpy as np

import matplotlib
matplotlib.use('TkAgg')



# Constants
num_particles = 1000 #n
container_size = 10 #V
time_steps = 1000
particles_speed = 0.5 # T function

# Initial positions and velocitiesof particles
positions = np.random.rand(num_particles, 2)* container_size
velocities = np.random.rand(num_particles, 2)* particles_speed

# Creating our plot
fig, ax = plt.subplots()
scatter = ax.scatter(positions[:, 0], positions[:, 1], marker='o', c='black')
ax.set_xlim(0, container_size)
ax.set_ylim(0, container_size)
plt.gca().set_aspect('equal', adjustable='box')


# Simulation Loop
collisions_array = []
for step in range(time_steps):
    positions += velocities
    n_collision = 0
    for i in range(num_particles):
        for j in range(2):
            if positions[i,j] < 0 or positions[i,j] > container_size:
                # Collisions
                velocities[i,j] *= -1
                n_collision += 1
                
    collisions_array = np.append(collisions_array, n_collision)
    
    print(f"N of collisions: {n_collision} - On average: {np.average(collisions_array):.2f}", end='\r')
    
    if not plt.fignum_exists(fig.number):
        break
                
    scatter.set_offsets(positions)
    plt.pause(0.001)

plt.show()