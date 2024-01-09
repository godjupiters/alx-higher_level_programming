#!/usr/bin/python3
"""Pascal's Triangle function Defined."""


def pascal_triangle(n):
    """Pascal's Triangle Rep of size "n".
    """
    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        t = triangles[-1]
        tmpo = [1]
        for o in range(len(t) - 1):
            tmpo.append(t[o] + t[o + 1])
        tmpo.append(1)
        triangles.append(tmpo)
    return triangles
