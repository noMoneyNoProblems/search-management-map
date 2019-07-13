#!/usr/bin/python3

from django.contrib.gis.geos import Point, LineString, LinearRing
import numpy as np
import shapely
import math


def pt_relv(a, b):
    """ Returns a relative vector, b-a"""
    return [v - a[i] for i, v in enumerate(b)]


def pt_corner_relv(a, b, c):
    """ Takes 3 points a, b and c and returns
         u = b - a
         v = c - b """
    return [pt_relv(a, b),
            pt_relv(b, c)]


def vec_cosine_rule(u, v):
    """Returns the cosine angle between two vectors
    Where,
    cos(theta) = u . v / mag(u) / mag(v)"""
    norm = np.linalg.norm
    dot = np.dot
    acos = math.acos
    return acos(dot(u, v)/norm(u)/norm(v))


def lrng_concave_points(lrng):
    """ Takes a linear ring and
    returns all concave/reflex points in the ring """
    lcross = lrng_cross(lrng)
    cw = sum(1 for i in lcross if i < 0)
    acw = sum(1 for i in lcross if i > 0)
    zeros = sum(1 for i in lcross if i == 0)

    # The number of concave points will always be
    # smaller or equal than the number of convex points

    # Case 1: Concave points are acw, or both
    if cw >= acw:
        return [lrng[i]
                for i, cp in enumerate(lcross)
                if cp > 0 ]

    # Alternative: Concave points are cw
    else:
        return [lrng[i]
                for i, cp in enumerate(lcross)
                if cp < 0]


def lrng_cross(lrng):
    """Returns the cross product of every corner
        """
    dirl = list()

    # Ignore last element (duplicate)
    lr = [pt for pt in lrng]
    lr.pop()

    for i, pt in enumerate(lr):
        p0 = lr[i-2]
        p1 = lr[i-1]
        p2 = pt
        dirl.append(
            np.cross(
                *pt_corner_relv(p0, p1, p2)
            )
        )
    dirl.append(dirl.pop(0))
    return [float(x) for x in dirl]


def decomp(lrng):
    """Decompose an arbitrary linear ring into a set of convex linear rings."""
    ndiags = 0
    concave_points = lrng_concave_points(lrng)
    convex_points = lrng_convex_points(lrng)

    for pt1 in concave_points:
        for pt0 in convex_points:
            if cansee(pt0, pt1, lrng):
                left = sublrng(pt0, pt1, lrng)
                right = sublrng(pt1, pt0, lrng)
                tmp = decomp(left) + decomp(right)
                if (len(tmp) < ndiags or ndiags == 0):
                    min = tmp
                    ndiags = len(tmp)

    if concave_points:
        return min
    else:
        return [lrng]


def lrng_convex_points(lrng):
    " Takes a linear ring and returns all convex points"
    concave_points = lrng_concave_points(lrng)
    convex_points = [pt
                     for pt in lrng
                     if pt not in concave_points]
    convex_points.pop()
    return convex_points


def cansee(pt0, pt1, lrng):
    """ Returns true if a line can be drawn
    from pt0 to pt1 without crossing any lines in lrng.
    pt0 and pt1 must also be across and NOT next to each other."""
    line = LineString(pt0, pt1)

    if not isinstance(pt0, Point):
        pt0 = Point(pt0)
    if not isinstance(pt1, Point):
        pt1 = Point(pt1)

    intersect = list(lrng.intersection(line))
    while pt0 in intersect:
        intersect.remove(pt0)

    while pt1 in intersect:
        intersect.remove(pt1)

    if intersect:
        return False
    else:
        return True


def sublrng(pt0, pt1, lrng):
    """ Returns a LinearRing subset of lrng.
    pt0 = starting point,
    pt1 = ending point,
    lrng = original linear ring"""

    i0 = lrng.index(pt0)
    i1 = lrng.index(pt1)

    if i1 > i0:
        return LinearRing(
            lrng[i0:i1+1] + [pt0])
    else:
        return LinearRing(lrng[i0:-1] + lrng[:i1+1] + [pt0])


def creep_line(lrng, width):
    """ Return a LineString which represents
    a creeping path through a convex LinearRing """
    xmin, ymin, xmax, ymax = lrng.extent
    xdist = xmax - xmin
    ydist = width

    def stripe(y, space, ymax):
        """ Generates ycoord spaced over interval"""
        while y < ymax:
            yield y
            y = y + space
        yield ymax

    def slice(xmin, xmax, yiter):
        """ Generates LineStrings spaced over yiter"""
        for y in yiter:
            yield LineString((xmin, y), (xmax, y))

    def carve(lrng, liter):
        """
        Generates a list of points that intersect with lrng
        """
        reverse = False
        for l in liter:
            i = lrng.intersection(l)
            i.normalize()
            if isinstance(i, LineString):
                if reverse:
                    reverse = False
                    i.reverse()
                    for p in i:
                        yield p
                else:
                    reverse = True
                    for p in i:
                        yield p
            elif isinstance(i, Point):
                yield i
            else:
                raise(TypeError)

    yiter = [y for y in stripe(ymin, ydist, ymax)]
    liter = [l for l in slice(xmin, xmax, yiter)]
    pts = [p for p in carve(lrng, liter)]

    return LineString(pts)


def creep_line_at_angle(lrng, width, angle):
    pass
# TODO: Implement creep_line at angle with shapely
#       affine transformations (rotation)
