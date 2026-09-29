# ---------------------------------------------------
# Irina Khan
# SYDE 572 Assignment 1 Part 2 - Line Fitting
#
# Objective: 
# Fit N data points [(x1, y1), ..., (xn, yn)] 
# to a line (y = mx + b)
# ---------------------------------------------------


# ---------------------------------------------------
# Numerical Method: Newton-Raphson Multivariate
# ---------------------------------------------------

import matplotlib.pyplot as plt
import numpy as np

m0 = 0
b0 = 0
tolerance = 1e-6

x = [0, 2, 1, 3]
y = [0.5, 3.5, 1.5, 7.5]

N = len(x)



def calculate_J(m, b, x, y, N):
    sum = 0
    for i in range(N): 
        sum += (y[i] - (x[i]*m + b))**2  

    J = sum / N

    return J

def calculate_gradient(m, b, x, y, N):

    sumJm = 0
    sumJb = 0

    for i in range(N):
        error = y[i] - (x[i]*m + b)

        sumJm += error * x[i]
        sumJb += error

    deltaJdeltaM = (-2 * sumJm) / N
    deltaJdeltaB = (-2 * sumJb) / N

    return deltaJdeltaM, deltaJdeltaB

def calculate_hessian(x, N):

    delta2JdeltaM2 = 0
    delta2JdeltaMdeltaB = 0
    delta2JdeltaB2 = 2

    for i in range(N):
        delta2JdeltaM2 += x[i] ** 2
        delta2JdeltaMdeltaB += x[i]

    delta2JdeltaM2 = (2*delta2JdeltaM2)/N
    delta2JdeltaMdeltaB = (2*delta2JdeltaMdeltaB)/N
    
    return delta2JdeltaM2, delta2JdeltaMdeltaB, delta2JdeltaB2


# ---------------------------------------------------
# Running the Newton-Raphson Multivariate Algorithm
# ---------------------------------------------------

m = m0
b = b0

m_values_tested = [m]
b_values_tested = [b]

print("Initial m: " + str(m0))
print("Initial b: " + str(b0))

# Counter limits iteratoins to 100 in the while loop below!
counter = 0

while True:

    deltaJdeltaM, deltaJdeltaB = calculate_gradient(m, b, x, y, N)
    delta2JdeltaM2, delta2JdeltaMdeltaB, delta2JdeltaB2 = calculate_hessian(x, N)

    determinant = delta2JdeltaM2 * delta2JdeltaB2 - delta2JdeltaMdeltaB * delta2JdeltaMdeltaB
    m_new = m - (1/determinant) * (delta2JdeltaB2 * deltaJdeltaM - delta2JdeltaMdeltaB * deltaJdeltaB)
    b_new = b - (1/determinant) * (-1 * delta2JdeltaMdeltaB * deltaJdeltaM + delta2JdeltaM2* deltaJdeltaB)

    if (abs(m_new - m) < tolerance and abs(b_new - b) < tolerance) or (counter > 100):
        break

    m_values_tested.append(m_new)
    b_values_tested.append(b_new)

    counter = counter + 1
    m = m_new
    b = b_new

print("Optimized values for m*, b*: (" + str(m) + ", " + str(b) + ")")
print("Final line equation: y = " + str(m) + "x + " + str(b))
print("Total number of iterations = " + str(len(m_values_tested)))

# ---------------------------------------------------
# Calculating the final MSE
# ---------------------------------------------------

MSE = calculate_J(m, b, x, y, N)
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
colors =  np.linspace(0, 1, len(m_values_tested))

x_vals = np.linspace(-10, 10, 500)
for i in range(len(m_values_tested)):
    y_vals = m_values_tested[i] * x_vals + b_values_tested[i]
    plt.plot(x_vals, y_vals,label=f"f(x) = {m_values_tested[i]:.3f}x + {b_values_tested[i]:.3f}", color=cmap(colors[i]), alpha=0.75, zorder=5)
# --- End of Ploting all intermediate x and y values from numerical method, in colour order from red to green: ---


# --- Plotting the axes and the title of the graph ---
plt.title(f"Plot of all line equations tested via the Newton-Raphson Multivariate method to \n fit all points in data set", fontname="Calibri")
plt.axhline(0, color='black', linewidth=0.8, linestyle='-') # X-axis baseline
plt.axvline(0, color='black', linewidth=0.8, linestyle='-') # Y-axis baseline
plt.grid(True, linestyle=':', alpha=0.6)
# --- End of Plotting the axes and the title of the graph ---


plt.legend()
plt.show()

