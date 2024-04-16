import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from tkinter import Tk, Label, Entry, Button


class direct_vec:
    # Class for defining a 2D vector with angle theta
    def __init__(self, theta):
        self.vx, self.vy = np.cos(theta), np.sin(theta)
        self.theta = theta

    # Rotate the vector by a given angle
    def rot(self, theta):
        return direct_vec(theta + self.theta)

    # Calculate the slope of the vector
    def slope(self):
        return self.vy / self.vx

    # Get the cosine component of the vector
    def get_cos(self):
        return self.vx

    # Get the sine component of the vector
    def get_sin(self):
        return self.vy



class point:
    # Class for defining a 2D point
    def __init__(self, x0, y0):
        self.x = x0
        self.y = y0

    # Get the coordinates of the point
    def get_point(self):
        return (self.x, self.y)

    # Set the coordinates of the point
    def set_point(self, x=None, y=None):
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    # Create a copy of the point
    def copy(self):
        return point(self.x, self.y)


# Function to plot a linear segment given a starting point, direction vector, and length
def plot_linear(point, vec, length):
    x0, y0 = point.get_point()
    x_range = np.linspace(start=x0, stop=x0 + vec.vx * length, num=20)
    plt.plot(x_range, vec.slope() * (x_range - x0) + y0)


# Function to recursively generate the Koch curve segments
def koch(p0, vec, L, n):
    p = p0.copy()
    if n < 0:
        print("error")
        return None
    if n == 0:
        # Base case: plot a linear segment
        plot_linear(p, vec, 3 * L)
        return

    koch(p, vec, L / 3, n-1)
    p.set_point(p0.x + vec.get_cos() * 2 * L, p0.y + vec.get_sin() * 2 * L)
    koch(p, vec, L / 3, n-1)

    p.set_point(p0.x + vec.get_cos() * L, p0.y + vec.get_sin() * L)
    koch(p, vec.rot(np.pi / 3), L / 3, n - 1)

    p.set_point(p0.x + vec.get_cos() * L + vec.rot(np.pi / 3).vx * L, p0.y + vec.get_sin() * L + vec.rot(np.pi / 3).vy * L)
    koch(p, vec.rot(- np.pi / 3), L / 3, n-1)


# Function to generate the outer part of the Koch curve
def koch_outer(N, p0, vec, L):
    plt.cla()

    p = p0.copy()
    rot_vec = vec.rot(np.pi / 3)
    koch(p, rot_vec, L, N)

    p.set_point(p0.x + rot_vec.get_cos() * 3 * L, p0.y + rot_vec.get_sin() * 3 * L)
    rot_vec = vec.rot(-np.pi / 3)
    koch(p, rot_vec, L, N)

    p.set_point(p0.x + vec.get_cos() * 3 * L, p0.y + vec.get_sin() * 3 * L)
    rot_vec = vec.rot(-np.pi / 3)
    koch(p, vec.rot(-np.pi), L, N)

    plt.title("Koch Curve n=" + str(N))
    plt.xlim(-L / 2, 7 * L / 2)
    plt.ylim(-L, 3 * L)


# Function to generate the Koch curve with a given depth
def generate_koch_curve(depth):
    vec = direct_vec(0)
    L = 1
    p0 = point(0, 0)
    fig = plt.figure(figsize=(10, 10))

    ani = animation.FuncAnimation(fig, koch_outer, fargs=(p0, vec, L), interval=1000, frames=depth)

    ani.save("koch_curves.gif", writer='imagemagick')

    plt.savefig(f"koch_curve_depth_{depth}.png")

    plt.show()


# Function to handle button click event for generating the Koch curve
def on_generate_button_click():
    depth = int(entry_depth.get())
    if 0 <= depth <= 11:
        generate_koch_curve(depth)
    else:
        result_label.config(text="Please enter a number between 1 and 7.")



# Create main window
root = Tk()
root.title("Koch Curves Generator")

# Create widgets
label_depth = Label(root, text="Enter the depth of the Koch curve (1 to 7 inclusive):")
label_depth.grid(row=0, column=0, padx=10, pady=10)

entry_depth = Entry(root)
entry_depth.grid(row=0, column=1, padx=10, pady=10)

generate_button = Button(root, text="Generate", command=on_generate_button_click)
generate_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

result_label = Label(root, text="")
result_label.grid(row=2, column=0, columnspan=2)


# Run the main event loop
root.mainloop()