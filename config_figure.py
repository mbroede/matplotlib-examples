import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import FormatStrFormatter

x = np.arange(-2, 3, 0.1)
y = -2 * x ** 2 + 7

fig, ax = plt.subplots()
fig.set_size_inches(6, 7)
ax.plot(x, y, color='green', linestyle='--', linewidth=3)

# Verschieben der Achsen
ax.spines['left'].set_position('zero')
ax.spines['left'].set_color('blue')
ax.spines['bottom'].set_position('zero')

# Verstecken der rechten und oberen Achse
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

# Beschriftung der Axen
plt.xlabel('X', fontsize=16, loc='right')
plt.ylabel('Y', fontsize=16, loc='top')

# Vom Gitter nur die x-Linien aktivieren
plt.grid(True, axis='x')
plt.grid(False, axis='y')

# Major-Ticks Labelfarbe einstellen
ax.tick_params(axis='y', which='major', labelcolor='red')

# Minor-Ticks hinzufügen aber auf der x-Achse ausblenden
ax.minorticks_on()
ax.tick_params(axis='x', which='minor', bottom=False)
ax.tick_params(axis='y', which='minor', bottom=True, labelsize=6, labelcolor='blue')
ax.yaxis.set_minor_formatter(FormatStrFormatter("%.1f"))

# Annotation
ax.annotate('max y-value', xy=(0, 7), xytext=(0.5, 7.5), color='red',
            arrowprops=dict(facecolor='white', shrink=0.05))

# Titel mit speziellen Font
font = {'family':'serif', 'color':'green', 'weight':'bold', 'size':16 }
ax.set_title("Eine Parabel", pad=30, fontdict=font)

# Figure anzeigen
plt.show()
