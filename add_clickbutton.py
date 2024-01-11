import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Button

fig, ax = plt.subplots()

# Unten Platz für den Button lassen
plt.subplots_adjust(bottom=0.2)

# Beispieldaten erstellen
x = np.arange(10)
y = x

# Plotten
line, = plt.plot(x, y)

# Klasse für Datenänderung + Aktualisierung
class ReDraw:
    m = 1
    b = 0

    def update(self, event):
        self.m = -1 if self.m > 0 else 1
        self.b += 1    
        line.set_ydata(self.m * x + self.b)
        ax.relim()
        ax.autoscale_view()
        plt.draw()

# Klasse instanziieren
onclick = ReDraw()

# Button implementieren
axbtn = plt.axes([0.7, 0.02, 0.15, 0.08])
btn = Button(axbtn, 'Update', color='skyblue')
btn.on_clicked(onclick.update)

# Anzeigen
plt.show()

