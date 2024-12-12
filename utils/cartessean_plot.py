import numpy as np
import matplotlib.pyplot as plt

def cartesean_plot(funcs:list, lim, num=200):
    x_values = np.linspace(-lim, lim, num=num)
    
    temp_arr = []
    
    for func in funcs:
        temp_arr.append({"values":[func['func'](x) for x in x_values], "title": func['title']})
    fig, ax = plt.subplots()
    ax.set_ylim(ymin=-lim, ymax=lim)
    ax.set_xlim(xmin=-lim, xmax=lim)
    
    for arr in temp_arr:
        plt.plot(x_values, arr['values'], label=arr['title'])
    plt.grid(linestyle='-', linewidth=0.5)
    plt.legend(loc='upper left')

    plt.show()