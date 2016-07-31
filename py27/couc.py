#!/usr/bin/env python


def line_length(clen, line):
    ''' Line length by Pythagoras theorem '''
    return clen + (
        (line[1][0] - line[0][0])**2 +
        (line[1][1] - line[0][1])**2
    )**.5

def pl_length(polyline):
    ''' Gets polyline length by adding up segment lengths '''
    return reduce(
        line_length,
        [(s, e) for s, e in zip(polyline[:-1], polyline[1:])], 0)

def get_quad_area(q):
    '''
    Gets the area of a regular quadilateral defined by 2 line segments.
    If area is zero, the line segments are colinear (and probably overlap)
    '''
    return abs((
        (q[0][0]*q[1][1] - q[0][1]*q[1][0]) + \
        (q[1][0]*q[2][1] - q[1][1]*q[2][0]) + \
        (q[2][0]*q[3][1] - q[2][1]*q[3][0]) + \
        (q[3][0]*q[0][1] - q[3][1]*q[0][0])
    )/2)

def get_overlap_start(line1, line2):
    '''
    checks if the area of the quad defined by both lines
    is zero (implying both lines are projections of each other)
    then see if they overlap by checking if start/end points
    of one line lie within the other.
    If the above are met, sort the points list smallest first
    and return the overlap start which should be at index 2 in the
    sorted list.
    '''
    quad = list(line1 + line2)
    if not get_quad_area(quad) and \
        (line1[0] <= line2[0] <= line1[1] or
         line1[0] <= line2[1] <= line1[1] or
         line2[0] <= line1[0] <= line2[1] or
         line2[0] <= line1[1] <= line2[1]):
        quad.sort()
        return quad[1]
    return False

def get_overlap(ad, bc):
    '''
    Gets overlap polyline (common to ad & bc)
    '''
    overlap = []

    bc_iterator = iter(zip(bc[:-1], bc[1:]))

    for ad_seg in zip(ad[:-1], ad[1:]):
        while not overlap:
            # continue search for overlap start
            try:
                bc_seg = next(bc_iterator)
                os = get_overlap_start(ad_seg, bc_seg)
                overlap = [os,] if os else []
            except StopIteration:
                bc_iterator = iter(zip(bc[:-1], bc[1:]))
                break

        if overlap:
            try:
                if ad_seg[1] != bc_seg[1]:
                    endpoints = [ad_seg[1], bc_seg[1]]
                    endpoints.sort()
                    overlap.append(endpoints[0])
                    return overlap
                else:
                    overlap.append(ad_seg[1])
                bc_seg = next(bc_iterator)
            except StopIteration:
                pass
    else:
        return overlap


def get_detour_ratio(**kwargs):
    ''' works out the "detour ratio" from all geo-polyline lengths '''
    ad = kwargs.get('ad', [])
    bc = kwargs.get('bc', [])

    ad_bc_overlap = get_overlap(ad, bc)

    return round((pl_length(ad_bc_overlap)*2)/(pl_length(ad)+pl_length(bc)), 4)

if __name__ == '__main__':
    pass
