# based on this image from the 'Sensitivity and Specificity' wikipedia page
# https://en.wikipedia.org/wiki/Sensitivity_and_specificity#/media/File:Sensitivity_and_specificity_1.01.svg

import numpy as np
from random import uniform
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# custom legend
red = mpatches.Patch(color='red', label='true negative')
lightcoral = mpatches.Patch(color='lightcoral', label='false positive')
lightgreen = mpatches.Patch(color='lightgreen', label='false negative')
green = mpatches.Patch(color='green', label='true positive')

# observation boundaries
LEFT = (-2, 0)
RIGHT = (0, 2)
HEIGHT = (-1.5, 1.5)


def in_circle(x, y):
    return (x**2) + (y**2) < 1


def at_origin(x, y):
    return x == 0 and y == 0


def out_of_circle(x, y):
    return (x**2) + (y**2) > 1 or at_origin(x, y)


def cmplot(cm):
    # draw a vertical line at x=0
    # https://www.statology.org/matplotlib-vertical-line/
    plt.axvline(x=0)

    # draw unit circle
    # https://stackoverflow.com/questions/63984168/how-to-draw-a-circle-with-matplotlib-pyplot
    theta = np.linspace(0, 2*np.pi, 100)
    plt.plot(np.cos(theta), np.sin(theta))
    plt.axis('equal')

    # get metrics
    tn, fp, fn, tp = cm.ravel()

    # group metrics with their display properties
    # (metric, constraints, position, color)
    metrics = [
        (tn, in_circle, RIGHT, 'red'),
        (fp, out_of_circle, RIGHT, 'lightcoral'),
        (fn, in_circle, LEFT, 'lightgreen'),
        (tp, out_of_circle, LEFT, 'green')
    ]

    for metric, constraint, pos, col in metrics:
        X = []
        Y = []
        for _ in range(metric):
            # initialise point at origin
            x, y = 0, 0
            # randomly move point until its in the right spot
            while constraint(x, y):
                x = uniform(*pos)
                y = uniform(*HEIGHT)
            X.append(x)
            Y.append(y)
        # plot metric
        plt.scatter(X, Y, color=col)

    # add legend
    plt.legend(
        handles=[red, lightcoral, lightgreen, green],
        bbox_to_anchor=(0.5, -0.05)
    )

    plt.tight_layout()
    plt.show()
