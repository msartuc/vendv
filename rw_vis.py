import matplotlib.pyplot as plt
from random_walk import RandomWalk

rw = RandomWalk()
rw.fill_walk()

#plot the points in the walk
plt.style.use('classic')
fig, ax = plt.subplots(figsize = (15,9))
point_numbers = range(rw.num_points)
ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
edgecolors='none', s=10)

#ax.scatter(rw.x_values, rw.y_values, s=15)
ax.set_aspect('equal')
# Emphasize the first and last points.
ax.scatter(0, 0, c='green', edgecolors='none', s=100)
ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none',
s=100)
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)
plt.show()