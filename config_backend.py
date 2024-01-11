import matplotlib.pyplot as plt
import numpy as np

# Daten erstellen
x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)

# Figur und Achsen erstellen
fig, ax = plt.subplots()

# Größe des Figures in Zoll
fig.set_size_inches(4, 3)

# Plotten
ax.plot(x, y, label='sin(x)')
ax.set_facecolor('#FFFFFF') # white

# Hintergrundfarbe des Figures
fig.set_facecolor('#DCDCDC') # gainsboro

# Toolbar ausblenden
plt.gcf().canvas.toolbar.pack_forget()

# Fenstertitel vergeben
fig.canvas.manager.set_window_title('Sinusfunktion')

# Anzeigen
plt.show()
