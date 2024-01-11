import matplotlib.pyplot as plt
import numpy as np

# Daten erstellen
x = np.linspace(0, 2 * np.pi, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.tanh(x)

# Funktionen plotten
plt.plot(x, y1, label='sin(x)')
plt.plot(x, y2, label='cos(x)')
plt.plot(x, y3, label='tanh(x)')

# Legende hinzufügen und Fig anzeigen
plt.legend()
plt.show()
