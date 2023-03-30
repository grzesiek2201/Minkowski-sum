import numpy as np
import matplotlib.pyplot as plt
from minkowskisum import minkowskisum, sort_vertices


def main():
    # create two polygons
    polygon1 = np.array([[-4, 2], [-3, 1], [-2, 2]])
    polygon2 = np.array([[2, 1], [4, 1], [4, 3], [2, 3]])

    # calculate minkowski sum
    msum = minkowskisum(polygon1, polygon2)

    # plot the polygons
    polygon1 = sort_vertices(polygon1)
    polygon2 = sort_vertices(polygon2)
    plt.figure(figsize=(7, 4))
    plt.fill(polygon1[:, 0], polygon1[:, 1], color='gray')
    plt.fill(polygon2[:, 0], polygon2[:, 1], color='darkgray')
    plt.fill(msum[:, 0], msum[:, 1])
    ax = plt.gca()
    ax.set_aspect('equal')
    ax.set_axisbelow(True)
    ax.grid()
    plt.show()


if __name__ == '__main__':
  main()
