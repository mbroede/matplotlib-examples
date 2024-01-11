import numpy as np
import matplotlib.pyplot as plt

# Ein Numpy-Dictionary mit mehreren Arrays erstellen
dict = {'x': np.arange(50),
        'y': np.arange(50) + 5 * np.random.randn(50),
        'color': np.random.randint(0, 50, 50),
        'dotsize': np.abs(np.random.randn(50)) * 100}

# Ein Streudiagramm erstellen
plt.scatter('x', 'y', c='color', s='dotsize', data=dict)

# Achsenbeschriftung hinzufügen
plt.xlabel('x')
plt.ylabel('y')

# Berechnung der Gleichung für die Trendlinie
c = np.polyfit(dict['x'], dict['y'], 1)
p = np.poly1d(c)

# Trendlinie zeichnen
plt.plot(dict['x'], p(dict['x']), color='red')

# Ausgabe
plt.show()

