import matplotlib.pyplot as plt
import numpy as np

# x: 10 ganze Zahlen von 0 bis 9
x = np.arange(10) 

# y: eine lineare Funktion f(x) = mx + b
y = 3 * x + 2

# Plot erstellen
fig, ax = plt.subplots()
ax.plot(x, y)

# Dialog anzeigen
plt.show()
