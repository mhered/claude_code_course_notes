import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Create figure and axis
fig, ax = plt.subplots(figsize=(10, 10), facecolor='black')
ax.set_facecolor('black')
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.axis('off')

# Parameters for the spiral
n_points = 1000
theta = np.linspace(0, 8 * np.pi, n_points)

# Create multiple spirals with different parameters
spirals = []
colors = ['#FF006E', '#FB5607', '#FFBE0B', '#8338EC', '#3A86FF']

for i, color in enumerate(colors):
    offset = i * 2 * np.pi / len(colors)
    r = theta / (8 * np.pi) * 1.5
    x = r * np.cos(theta + offset)
    y = r * np.sin(theta + offset)
    line, = ax.plot([], [], color=color, linewidth=2, alpha=0.7)
    spirals.append((line, x, y))

# Animation function
def animate(frame):
    for line, x, y in spirals:
        # Rotate the spiral
        angle = frame * 0.02
        x_rot = x * np.cos(angle) - y * np.sin(angle)
        y_rot = x * np.sin(angle) + y * np.cos(angle)
        line.set_data(x_rot, y_rot)
    return [line for line, _, _ in spirals]

# Create animation
anim = FuncAnimation(fig, animate, frames=200, interval=50, blit=True, repeat=True)

plt.title('Rotating Spiral Galaxy', color='white', fontsize=20, pad=20)
plt.tight_layout()

# Save as GIF
print("Creating GIF... this may take a moment...")
anim.save('spiral_galaxy.gif', writer='pillow', fps=20, dpi=80)
print("Done! Saved as spiral_galaxy.gif")
