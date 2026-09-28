# ---------------------------------------------------
# Irina Khan
# SYDE 572 Assignment 1 Part 1
#
# Objective: 
# Find the shortest distance from a point (x0, y0) 
# to a function
# ---------------------------------------------------

# ---------------------------------------------------
# First Numerical Method: Newton-Raphson Method
# ---------------------------------------------------

import matplotlib.pyplot as plt
import numpy as np
import math

# The following code functions must have the desired mathematical function written 
# out in full, including the derivative forms:

def f(x):
    return (x**2) + 5

def df(x):
    return 2*x 

def ddf(x):
    return 2

# The coordinates of the point x0, y0
x0 = 0
y0 = 0

# Implemented the Newton-Raphson method in the following code function:
def find_distance_newton(x0, y0, f, df, ddf, initial_guess=5, tolerance=1e-7, max_iter=100):

    x = initial_guess

    x_vals_array = [x]

    for _ in range(max_iter):

        print(x, type(x), np.shape(x))
        D_prime = 2 * (x - x0) + 2 * (f(x) - y0) * df(x)
        D_double_prime = 2 + 2 * (df(x)**2) + 2 * (f(x) - y0) * ddf(x)

        # Newton-Raphson update step
        next_x = x - D_prime / D_double_prime

        if abs(next_x - x) < tolerance:
            x = next_x
            break
        
        x_vals_array.append(next_x)
        x = next_x

    shortest_distance = ((x - x0)**2 + (f(x) - y0)**2)**0.5

    return shortest_distance, x, x_vals_array


# ---------------------------------------------------
# Running the first numerical method:
# ---------------------------------------------------

final_distance, x_location, tested_x_vals = find_distance_newton(x0,y0,f, df, ddf)
y_location = f(x_location)

tested_y_vals = []
for item in tested_x_vals:
    tested_y_vals.append(f(item))
    
print("The final optimized distance is: " + str(final_distance))
print("The shortest distance connects to the function at x = " + str(x_location))
print("By Newton Raphson, it took " + str(len(tested_x_vals) - 1) + " iteration(s) to find the solution.")

# ---------------------------------------------------
# Creating the INTERMEDIATE plot of the function, showing all tested x-values:
# ---------------------------------------------------

# --- Plotting the function ---
x_vals = np.linspace(-10, 10, 500)
y_vals = f(x_vals)

plt.figure(figsize=(8,6))
plt.plot(x_vals, y_vals, label=f"f(x) = $x^2 + 5$", color="blue", linewidth=1)
# --- End of Plotting the function ---


# --- Ploting point x0 and y0: ---
plt.scatter(x0, y0, color="purple", s=30, zorder=3, label=rf"$x_0,\ y_0$ = ({x0:.2f}, {y0:.2f})")
# --- End of Ploting point x0 and y0: ---


# --- Ploting all intermediate x and y values from numerical method, in colour order from red to green: ---
colors =  np.linspace(0, 1, len(tested_x_vals))
plt.scatter(tested_x_vals, tested_y_vals, s=30, zorder=5, c=colors, cmap="RdYlGn", alpha=0.75)
# Seperately plotted the x* point on the function so it is annotated in the legend:
plt.scatter(tested_x_vals[-1], tested_y_vals[-1], s=30, color="green", zorder=5, label=f"($x^*$,$y^*$) = ({x_location:.3f}, {y_location:.3f})", alpha=0.75)
# --- End of Ploting all intermediate x and y values from numerical method, in colour order from red to green: ---


# --- Plotting the axes and the title of the graph ---
plt.title(f"Plot of all tested x values via Newton-Raphson method to \n find the shortest distance between P0 (" +str(x0) + "," + str(y0) + ") and f(x) = $x^2 + 5$", fontname="Calibri")
plt.axhline(0, color='black', linewidth=0.8, linestyle='-') # X-axis baseline
plt.axvline(0, color='black', linewidth=0.8, linestyle='-') # Y-axis baseline
plt.grid(True, linestyle=':', alpha=0.6)
# --- End of Plotting the axes and the title of the graph ---


# ---- ZOOM IN CODE ----
#Following text code block zooms the plot into the area where the approximations occur!
x_range = max(tested_x_vals) - min(tested_x_vals)
y_range = max(tested_y_vals) - min(tested_y_vals)

plt.xlim(min(tested_x_vals) - 0.1*x_range, max(tested_x_vals) + 0.1*x_range)
plt.ylim(min(tested_y_vals) - 0.1*y_range, max(tested_y_vals) + 0.1*y_range)
# ---- ZOOM IN CODE ----

# --- Plotting the shortest distance between function & point AND x-axis tick as dotted lines---
x_distance = np.linspace(x0, x_location, 500)
if (x_location - x0 == 0):
    y_distance = np.linspace(y0, f(x_location), 500)
else:
    slope = (f(x_location)-y0)/(x_location - x0)
    b = y0 - slope*(x0)
    y_distance = b + slope*x_distance
    axis_pointer = np.linspace(0, f(x_location), 500)
    # Plotting a line that points to the x-axis where the described function is the closest to the point (x0, y0)
    plt.plot(np.linspace(x_location, x_location, 500), axis_pointer, color="grey", linestyle='dashed', linewidth=1)

# Plotting a line between the point (x0, y0) and the point on the function that yields the shortest distance
plt.plot(x_distance, y_distance, color="grey", linestyle='dashed', linewidth=1)

for x, y in zip(tested_x_vals, tested_y_vals):
    plt.annotate(
        f"({x:.3f}, {y:.3f})",
        (x, y),
        xytext=(5, 5),
        textcoords="offset points"
    )

plt.legend()
plt.show()


# ---------------------------------------------------
# Creating the FINAL plot of the function, point and distance:
# ---------------------------------------------------

# --- Plotting the function ---
x_vals = np.linspace(-9, 9, 500)
y_vals = f(x_vals)

plt.figure(figsize=(8,6))
plt.plot(x_vals, y_vals, label=f"f(x) = $x^2 + 5$", color="blue", linewidth=1)
# --- End of Plotting the function ---


# --- Ploting point x0 and y0: ---
plt.scatter(x0, y0, color="purple", s=30, zorder=3, label=rf"$x_0,\ y_0$ = ({x0:.2f}, {y0:.2f})")
# --- End of Ploting point x0 and y0: ---


# --- Ploting the final optimized point x* and y*: ---
plt.scatter(tested_x_vals[-1], tested_y_vals[-1], s=30, color="green", zorder=5, label=f"($x^*$,$y^*$) = ({x_location:.3f}, {y_location:.3f})", alpha=0.75)
# --- End of Ploting the final optimized point ---


# --- Plotting the axes and the title of the graph ---
plt.title(f"Shortest distance between P0 (" +str(x0) + "," + str(y0) + ") and f(x) = $x^2 + 5$", fontname="Calibri")
plt.axhline(0, color='black', linewidth=0.8, linestyle='-') # X-axis baseline
plt.axvline(0, color='black', linewidth=0.8, linestyle='-') # Y-axis baseline
plt.grid(True, linestyle=':', alpha=0.6)
# --- End of Plotting the axes and the title of the graph ---


# --- Plotting the shortest distance between function & point AND x-axis tick as dotted lines---
x_distance = np.linspace(x0, x_location, 500)
if (x_location - x0 == 0):
    y_distance = np.linspace(y0, f(x_location), 500)
else:
    slope = (f(x_location)-y0)/(x_location - x0)
    b = y0 - slope*(x0)
    y_distance = b + slope*x_distance
    axis_pointer = np.linspace(0, f(x_location), 500)
    # Plotting a line that points to the x-axis where the described function is the closest to the point (x0, y0)
    plt.plot(np.linspace(x_location, x_location, 500), axis_pointer, color="grey", linestyle='dashed', linewidth=1)

# Plotting a line between the point (x0, y0) and the point on the function that yields the shortest distance
plt.plot(x_distance, y_distance, color="grey", linestyle='dashed', linewidth=1)

# Labeling the line between the function to the x-axis
plt.annotate(f"x ~= {x_location:.3f}", xy=(x_location, 0), xytext=(5, 5), textcoords="offset points")
# Labelling the distance line using a pair from the middle of the line coordinates (250 out of 500 points)
plt.annotate(f"Distance ~= {final_distance:.3f}", xy=(x_distance[250], y_distance[250]), xytext=(5, 5), textcoords="offset points")
# --- End of Plotting the shortest distance between function & point AND x-axis tick as dotted lines---


plt.legend()
plt.show()