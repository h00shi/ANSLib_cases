import numpy as np
import matplotlib.pyplot as plt

def change_axis_color(ax, color, axis_name='y', spine_loc=None):
    """ Change the color of x or y axis 

    https://stackoverflow.com/questions/4761623/changing-the-color-of-the-axis-ticks-and-labels-for-a-plot-in-matplotlib?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa
    """
    if   ( axis_name == 'y' ):
        ax.get_yaxis().get_label().set_color(color=color)
        ax.tick_params('y', colors=color)
    elif ( axis_name == 'x' ):
        ax.get_xaxis().get_label().set_color(color=color)
        ax.tick_params('x', colors=color)
        
    if(spine_loc is not None):
        ax.spines[spine_loc].set_color(color)
    

def add_axis_twinx(ax, offset=0, color=None):
    """Add a twin axis for overplotting.

* Input:

    ch, the convergence history object
    ax, axis to plot on
    plt_options, dictionary of options to be passed to matplotlib

* Axis with colors:

    https://matplotlib.org/examples/api/two_scales.html

* More than three axis:

    https://matplotlib.org/examples/axes_grid/demo_parasite_axes2.html

    https://stackoverflow.com/questions/9103166/multiple-axis-in-matplotlib-with-different-scales?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa
    """
    twin = ax.twinx()

    if( color is not None):
        change_axis_color(twin, color, 'y', 'right')
    
    # right, left, top, bottom
    twin.spines['right'].set_position(('outward', offset))      
    # no x-ticks                 
    # twin.xaxis.set_ticks([])
    # Sometimes handy, same for xaxis
    #par2.yaxis.set_ticks_position('right')

    return twin
