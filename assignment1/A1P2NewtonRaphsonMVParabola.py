# ---------------------------------------------------
# Irina Khan
# SYDE 572 Assignment 1 Part 2 - Parabola Fitting
#
# Objective: 
# Fit N data points [(x1, y1), ..., (xn, yn)] 
# to a parabola (y = ax^2 + bx + c)
# ---------------------------------------------------


# ---------------------------------------------------
# Numerical Method: Newton-Raphson Multivariate
# ---------------------------------------------------

import matplotlib.pyplot as plt
import numpy as np

a0 = 1
b0 = 1
c0 = 1
tolerance = 1e-6

x = [0, 2, 1, 3]
y = [0.5, 3.5, 1.5, 7.5]

N = len(x)


def calculate_J(a, b, c, x, y, N):
    sum = 0
    for i in range(N): 
        sum += (y[i] - (a*(x[i])**2 + b*x[i] + c))**2  

    J = sum / N

    return J

def calculate_gradient(a, b, c, x, y, N):

    sumJa = 0
    sumJb = 0
    sumJc = 0

    for i in range(N):
        error = y[i] - (a*(x[i])**2 + b*x[i] + c)

        sumJa += error * x[i]**2
        sumJb += error * x[i]
        sumJc += error

    deltaJdeltaA = (-2 * sumJa) / N
    deltaJdeltaB = (-2 * sumJb) / N
    deltaJdeltaC = (-2 * sumJc) / N

    G = np.array([
        deltaJdeltaA, deltaJdeltaB, deltaJdeltaC,
        ])

    return G

def calculate_hessian(x, N):

    delta2JdeltaA2 = 0
    delta2JdeltaB2 = 0
    delta2JdeltaC2 = 2
    delta2JdeltaAdeltaB = 0
    delta2JdeltaAdeltaC = 0
    delta2JdeltaBdeltaC = 0
    

    for i in range(N):
        delta2JdeltaA2 += x[i] ** 4
        delta2JdeltaB2 += x[i] ** 2
        delta2JdeltaAdeltaB += x[i] ** 3
        delta2JdeltaAdeltaC += x[i] ** 2
        delta2JdeltaBdeltaC += x[i]

    delta2JdeltaA2 = (2*delta2JdeltaA2)/N
    delta2JdeltaB2 = (2*delta2JdeltaB2)/N
    delta2JdeltaAdeltaB = (2*delta2JdeltaAdeltaB)/N
    delta2JdeltaBdeltaC = (2*delta2JdeltaBdeltaC)/N
    delta2JdeltaAdeltaC = (2*delta2JdeltaAdeltaC)/N\

    H = np.array([
    [delta2JdeltaA2,       delta2JdeltaAdeltaB, delta2JdeltaAdeltaC],
    [delta2JdeltaAdeltaB,  delta2JdeltaB2,      delta2JdeltaBdeltaC],
    [delta2JdeltaAdeltaC,  delta2JdeltaBdeltaC, delta2JdeltaC2]
    ])
    
    return H

# ---------------------------------------------------
# Running the Newton-Raphson Multivariate Algorithm
# ---------------------------------------------------

a = a0
b = b0
c = c0

a_values_tested = [a]
b_values_tested = [b]
c_values_tested = [c]

print("Initial a: " + str(a0))
print("Initial b: " + str(b0))
print("Initial c: " + str(c0))

# Counter limits iteratoins to 100 in the while loop below!
counter = 0

while True:

    G = calculate_gradient(a, b, c, x, y, N)
    H = calculate_hessian(x, N)

    H_inverse = np.linalg.inv(H)

    
    parameters = np.array([a, b, c])

    parameters_new = parameters - H_inverse @ G

    a_new = parameters_new[0]
    b_new = parameters_new[1]
    c_new = parameters_new[2]   

    if (abs(a_new - a) < tolerance and abs(b_new - b) < tolerance and abs(c_new - c)) or (counter > 100):
        break

    a_values_tested.append(a_new)
    b_values_tested.append(b_new)
    c_values_tested.append(c_new)

    counter = counter + 1
    a = a_new
    b = b_new
    c = c_new

print("Optimized values for (a*, b*, c*): (" + str(a) + ", " + str(b) + ", " + str(c) + ")")
print("Final line equation: y = " + str(a) + "x^2 + " + str(b) + "x + " + str(c))
print("Total number of iterations = " + str(len(a_values_tested)))

# ---------------------------------------------------
# Calculating the final MSE
# ---------------------------------------------------

MSE = calculate_J(a, b, c, x, y, N)
print("The final MSE value is: " + str(MSE))

# ---------------------------------------------------
# Creating the INTERMEDIATE plot of the function, showing all lines generated
# ---------------------------------------------------

plt.figure(figsize=(8,6))
#plt.plot(x_vals, y_vals, label=f"f(x) = {m}x + {b}", color="blue", linewidth=1)

# --- Ploting all of the point from the data set: ---
for i in range(N):
    plt.scatter(x[i], y[i], color="blue", s=30, zorder=3)
    plt.annotate( f"({x[i]:.3f}, {y[i]:.3f})", (x[i], y[i]), xytext=(5, 5), textcoords="offset points")
# --- End of Plotting all data set points ---


# --- Ploting all intermediate x and y values from numerical method, in colour order from red to green: ---
cmap = plt.cm.RdYlGn
colors =  np.linspace(0, 1, len(a_values_tested))

x_vals = np.linspace(-5, 5, 500)
for i in range(len(a_values_tested)):
    y_vals = (a_values_tested[i] * x_vals**2 + b_values_tested[i] * x_vals + c_values_tested[i])
    plt.plot(x_vals, y_vals, label=f"f(x) = {a_values_tested[i]:.3f}x² + " f"{b_values_tested[i]:.3f}x + "f"{c_values_tested[i]:.3f}", color=cmap(colors[i]), alpha=0.75, zorder=5)
# --- End of Ploting all intermediate x and y values from numerical method, in colour order from red to green: ---


# --- Plotting the axes and the title of the graph ---
plt.title(f"Plot of all parabola equations tested via the Newton-Raphson Multivariate method to \n fit all points in data set", fontname="Calibri")
plt.axhline(0, color='black', linewidth=0.8, linestyle='-') # X-axis baseline
plt.axvline(0, color='black', linewidth=0.8, linestyle='-') # Y-axis baseline
plt.grid(True, linestyle=':', alpha=0.6)
# --- End of Plotting the axes and the title of the graph ---


plt.legend()
plt.show()

