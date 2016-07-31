#!/usr/bin/env python

import unittest

import couc


class CoucTestCase(unittest.TestCase):

    def setUp(self):
        self.test_dat = {
            'function': {
                'example1': {
                    'ad': [(1,1), (17,1)],
                    'bc': [(3,1), (14,1)],
                    'detour': .8148,
                    'overlap_start': (3,1)
                },
                'example2': {
                    'ad': [(1,1), (17,1)],
                    'bc': [(3,3), (3,1), (23,1)],
                    'detour': .7368,
                    'overlap_start': (3,1)
                },
                'example3': {
                    'ad': [(1,11), (1,7), (11,7)],
                    'bc': [(3,11), (3,7), (4,7), (4,2)],
                    'detour': .0833,
                    'overlap_start': (3,7)
                },
            },
            'line_length': [
                { 'points': ((3, 11), (3, 7)), 'length': 4},
                { 'points': ((3, 7), (4, 7)), 'length': 1},
                { 'points': ((8, 12), (5, 8)) , 'length': 5},
                { 'points': ((12, 8), (8, 5)) , 'length': 5}
            ],
            'pl_length': [
                { 'points': [(3,3), (3,1), (17,1)], 'length': 16},
                { 'points': [(3,11), (3,7), (4,7), (4,2)], 'length': 10},
                { 'points': [(1,11), (1,7), (11,7)], 'length': 14}
            ],
            'quad_area': [
                { 'points': ((7,4), (12,6), (14,3), (8,2)), 'area': 16},
                { 'points': ((7,4), (11,2), (7,2), (3,3)), 'area':8},
                { 'points': ((7,2), (11,2), (7,2), (3,2)), 'area':0},
            ],
            'overlap': [
                {
                    'ad': [(1,1), (17,1)],
                    'bc': [(3,1), (14,1)],
                    'overlap_start': (3,1)
                },
                {
                    'ad': [(3,7), (4,7)],
                    'bc': [(1,7), (11,7)],
                    'overlap_start': (3,7)
                },
                {
                    'ad': [(1,7), (11,7)],
                    'bc': [(3,11), (3,7)],
                    'overlap_start': False
                },
            ],
        }

    def test_line_length(self):
        test_dat = self.test_dat.get('line_length')
        for line in test_dat:
            self.assertEqual(couc.line_length(0, line.get('points')),
                    line.get('length'))

    def test_pl_length(self):
        test_dat = self.test_dat.get('pl_length')

        for polyline in test_dat:
            self.assertEqual(couc.pl_length(polyline.get('points')),
                    polyline.get('length'))

    def test_get_quad_area(self):
        test_dat = self.test_dat.get('quad_area')

        for quad in test_dat:
            self.assertEqual(couc.get_quad_area(quad.get('points')),
                    quad.get('area'))

    def test_get_overlap_start(self):
        test_dat = self.test_dat.get('overlap')
        for case in test_dat:
            ol_start = couc.get_overlap_start(case.get('ad'), case.get('bc'))
            self.assertEqual(ol_start, case.get('overlap_start'))

    # And finally our function test with test data drawn
    # from the examples
    def test_get_detour_ratio(self):
        test_dat = self.test_dat.get('function')
        for tc in test_dat.itervalues():
            detour = couc.get_detour_ratio(**tc)
            self.assertEqual(detour, tc.get('detour'))


if __name__ == '__main__':
    unittest.main()
