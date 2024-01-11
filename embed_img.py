import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, y)

# Neues Axes-Objekt hinzufügen
# Parameter: x,y linke untere Ecke, B x H des Images
ax = fig.add_axes([0.6, 0.6, 0.25, 0.25])
img = mpimg.imread(r'c:\projects\py\matplotlib-examples\chart_123x95.png')
ax.imshow(img)

# Ausblenden aller anderen ax-Artists
ax.set_xticklabels([])
ax.set_yticklabels([])
ax.set_xticks([])
ax.set_yticks([])
for spine in ax.spines.values():
    spine.set_visible(False)

# Anzeigen
plt.show()
