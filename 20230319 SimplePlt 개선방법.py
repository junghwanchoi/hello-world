
# legend 창 선 클릭시 어떤일 할때

#(출처) https://stackoverflow.com/questions/66423508/matplotlib-legend-picking-with-pandas-dataframe-doesnt-work

# Firstly, you need to extract all line2D objects on the figure. You can get them by using ax.get_lines(). Here the example:

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

ts = pd.Series(np.random.randn(1000), index=pd.date_range("1/1/2000", periods=1000))
ts = ts.cumsum()
df = pd.DataFrame(np.random.randn(1000, 4), index=ts.index, columns=list("ABCD"))
df = df.cumsum()
fig, ax = plt.subplots()
df.plot(ax=ax)
lines = ax.get_lines()
leg = ax.legend(fancybox=True, shadow=True)
lined = {}  # Will map legend lines to original lines.
for legline, origline in zip(leg.get_lines(), lines):
    legline.set_picker(True)  # Enable picking on the legend line.
    lined[legline] = origline

def on_pick(event):
    #On the pick event, find the original line corresponding to the legend
    #proxy line, and toggle its visibility.
    legline = event.artist
    origline = lined[legline]
    visible = not origline.get_visible()
    origline.set_visible(visible)
    #Change the alpha on the line in the legend so we can see what lines
    #have been toggled.
    legline.set_alpha(1.0 if visible else 0.2)
    fig.canvas.draw()

fig.canvas.mpl_connect('pick_event', on_pick)
plt.show()




# 그래프창에서 선 클릭시 어떤일 할때

# (출처) https://stackoverflow.com/questions/22201869/matplotlib-event-handling-line-picker

# Are you wanting something like this? When a line is clicked, it will be hidden, and when the "empty" location is clicked again, it will be shown.

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)

fig, ax = plt.subplots()
for i in range(1, 10):
    ax.plot(x, i * x + x, picker=5)

def on_pick(event):
    event.artist.set_visible(not event.artist.get_visible())
    fig.canvas.draw()

fig.canvas.callbacks.connect('pick_event', on_pick)
plt.show()




