import matplotlib.pyplot as plt
import time
import numpy as np

def plot_record(x=0, y=0):
    plt.ion()
    figure, ax = plt.subplots(figsize=(5, 5))
    line1, = ax.plot(x, y)
 
    plt.title("Bar movement", fontsize=10)
    plt.ylabel("Pixel trajectory")
 
    for i in range(50):
        min_val = i
        max_val = 50+i
        new_y = range(min_val,max_val)
        line1.set_xdata(x)
        line1.set_ydata(new_y)
        ax.set_xlim(min_val,max_val)
        figure.canvas.draw()
        figure.canvas.flush_events()
 
        time.sleep(0.1)

"""X = np.linspace(0,10,50)
Y = range(0,50)
plot_record(x=X,y=Y)"""