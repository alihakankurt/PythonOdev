import numpy
import pandas
import matplotlib.pyplot as plt

MIN_VALUE: int = 0
MAX_VALUE: int = 1000
POINT_COUNT: int = 1000
GRID_SIZE: int = 100
GROUP_COUNT: int = MAX_VALUE // GRID_SIZE

if __name__ == "__main__":
    points = numpy.random.randint(MIN_VALUE, MAX_VALUE, size=(POINT_COUNT, 2))

    df = pandas.DataFrame(points, columns=["X", "Y"])
    df.to_excel("points.xlsx", index=False)

    fig, ax = plt.subplots()
    ax.set_title("Points")

    ax.set_xlabel("X")
    ax.set_xticks(numpy.arange(MIN_VALUE, MAX_VALUE + 1, GRID_SIZE))

    ax.set_ylabel("Y")
    ax.set_yticks(numpy.arange(MIN_VALUE, MAX_VALUE + 1, GRID_SIZE))

    ax.grid(True)

    groups = [[[] for _ in range(GROUP_COUNT)] for _ in range(GROUP_COUNT)]
    for point in points:
        x, y = point
        x //= GRID_SIZE
        y //= GRID_SIZE
        groups[x][y].append(point)

    colors = numpy.random.rand(GROUP_COUNT, GROUP_COUNT, 3)
    for x in range(GROUP_COUNT):
        for y in range(GROUP_COUNT):
            for point in groups[x][y]:
                ax.scatter(point[0], point[1], color=colors[x][y])

    plt.show()
