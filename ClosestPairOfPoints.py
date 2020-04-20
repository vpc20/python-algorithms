import sys
from math import sqrt


# Euclidean distance
# The distance between points p1 (x1, y1) and p2 (x2, y2) is
# sqrt((x1-x2)^2 + (y1-y2)^2)
def distance(p1, p2):
    return sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


def brute_cp(pts):
    """
    Brute force algorithm for closest pair of points.
    Points are represented by tuple (x, y)

    :param pts: array of points
    :return: a tuple with a pair of points and the distance between the two points
    :rtype: (tuple, tuple, float)
    """
    min_dist = sys.maxsize
    # p1, p2 = (), ()
    for i in range(len(pts)):
        for j in range(i + 1, len(pts)):
            dist = distance(pts[i], pts[j])
            if dist < min_dist:
                min_dist = dist
                p1 = pts[i]
                p2 = pts[j]
    return p1, p2, min_dist


def closest_pair_recur(px, py):
    """
    Find the closest pair of points

    :param px: set of points sorted by x coordinate
    :param py: set of points sorted by y coordinate
    :return: a tuple with a pair of points and the distance between the two points
    """
    min_dist = sys.maxsize
    p1, p2 = (), ()
    if len(px) <= 3:
        return brute_cp(px)
    midx = len(px) // 2
    pxl = px[:midx]
    pxr = px[midx:]

    # mid = px[midx][0]
    # pyl, pyr = [], []
    # for pt in py:
    #     if pt[0] < mid:
    #         pyl.append(pt)
    #     else:
    #         pyr.append(pt)
    pyl, pyr = [], []
    for pt in py:
        if pt in pxl:
            pyl.append(pt)
        else:
            pyr.append(pt)

    # get min distance from left and right
    p1l, p2l, min_distl = closest_pair_recur(pxl, pyl)
    # print('left')
    # print(p1l, p2l, min_distl)
    p1r, p2r, min_distr = closest_pair_recur(pxr, pyr)
    # print('right')
    # print(p1r, p2r, min_distr)
    if min_distl < min_distr:
        min_dist = min_distl
        p1 = p1l
        p2 = p2l
    else:
        min_dist = min_distr
        p1 = p1r
        p2 = p2r

    # process points which lie in both py and px
    pylr = [pt for pt in py if px[midx][0] - min_dist <= pt[0] <= px[midx][0] + min_dist]
    for i in range(len(pylr)-1):
        for j in range(i+1, min(i + 7, len(pylr))):
            d = distance(pylr[i], pylr[j])
            if d < min_dist:
                min_dist = d
                p1 = pylr[i]
                p2 = pylr[j]

    return p1, p2, min_dist


def closest_pair(pts):
    px = sorted(pts, key=lambda e: e[0])  # sorted by x coordinate
    py = sorted(pts, key=lambda e: e[1])  # sorted by y coordinate
    return closest_pair_recur(px, py)


if __name__ == '__main__':
    # print(distance((0, 0), (0, 1)))
    # print(distance((0, 0), (0, 2)))
    # print(distance((0, 0), (0, -1)))
    # print(distance((0, 0), (0, -2)))
    # print(distance((0, 0), (1, 0)))
    # print(distance((0, 0), (2, 0)))
    # print(distance((0, 0), (-1, 0)))
    # print(distance((0, 0), (-2, 0)))
    # print(distance((0, 0), (1, 1)))
    # print(distance((0, 0), (1, -1)))
    # print(distance((0, 0), (-1, -1)))
    # print(distance((0, 0), (-1, 1)))
    #
    # print(brute_cp([(0, 0), (0, 1)]))
    # print(brute_cp([(0, 0), (0, 1), (1, 1)]))
    # print(brute_cp([(0, 0), (5, 1), (1, 1)]))
    #
    # # print(closest_pair([(0, 2), (2, 3), (1, 1)]))
    # print(brute_cp([(10, 5),
    #                 (9, 4),
    #                 (8, 3),
    #                 (7, 2),
    #                 (6, 1),
    #                 (5, 10),
    #                 (4, 9),
    #                 (3, 8),
    #                 (2, 7),
    #                 (1, 6)]))
    # print(closest_pair([(10, 5),
    #                     (9, 4),
    #                     (8, 3),
    #                     (7, 2),
    #                     (6, 1),
    #                     (5, 10),
    #                     (4, 9),
    #                     (3, 8),
    #                     (2, 7),
    #                     (1, 6)]))

    # print(brute_cp([(78, 71), (49, -48), (26, -59), (-45, -76)]))
    # print(closest_pair([(78, 71), (49, -48), (26, -59), (-45, -76)]))
    print(brute_cp([(73, 91), (76, -52), (25, -11), (67, -34)]))
    print(closest_pair([(73, 91), (76, -52), (25, -11), (67, -34)]))
