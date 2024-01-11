import matplotlib.pyplot as plt
from matplotlib.widgets import Button

fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.2)  # Platz für den Button lassen

# Einige Daten zum Plotten
t = [0, 1, 2, 3, 4]
s = [0, 1, 2, 3, 4]
l, = plt.plot(t, s)

class Index:
    idx = 0

    def next(self, event):
        self.idx += 1
        i = self.idx % len(t)
        ydata = s[i]
        l.set_ydata(ydata)
        plt.draw()

callback = Index()
axprev = plt.axes([0.7, 0.05, 0.1, 0.075])
bnext = Button(axprev, 'Next')
bnext.on_clicked(callback.next)

plt.show()
