import matplotlib.pyplot as plt
import numpy as np

# Daten erstellen
x = np.linspace(0, 2 * np.pi, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.tan(x)

# Drei Plots in einer Reihe nebeneinander
#fig, axs = plt.subplots(1, 3) 

# Drei Plots in einer Spalte untereinander
fig, axs = plt.subplots(3) 

# Funktionen plotten
axs[0].plot(x, y1, 'tab:blue')
axs[0].set_title('Sinus')

axs[1].plot(x, y2, 'tab:red')
axs[1].set_title('Kosinus')

axs[2].plot(x, y3, 'tab:green')
axs[2].set_title('Tangens')

# Abstand zwischen den Plots
fig.tight_layout(h_pad=2)

# Anzeigen
plt.show()
