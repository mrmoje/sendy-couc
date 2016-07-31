# Sendy-COUC
A solution for a sample combo-geo-polyline detour problem (from Sendy's
Combined Orders Use Case challenge)

### The problem/challenge:-
Given two geo-polylines AD and BC, come up with an algorithm to determine
the "detour" associated with their combined geo-polyline and further determine
if the detour is negligible enough for one to traverse the combined geo-polyline.

### This Solution:-
The detour can be expressed as the ratio of twice the length of common or
overlapping sections to the sum of both the polyline lengths, i.e
`2*len(ol)/(len(ad)+len(bc))` where `ol` is the overlapping segment polyline
and `ad` & `bc` are the given geo-polylines.
The acceptable detour can be specified as a detour ratio threshold.

### Assumptions

- There should be only one set of overlapping segments.
- Overlapping segments will have the same points save for the first and last
points of the overlapping polyline.

#### The algorithm
The first (intuitive) algorithm that comes to mind is of a "brute force"
kind where algorithm that goes a little something like this:-

  ----

  1. initialize ad polyline from user input
  2. initialize bc polyline from user input
  3. initialize overlap polyline to empty points list

  4. for each segment in ad
        while overlap polyline is empty
            fetch next bc segment
            if ad and bc segments overlap
                add starting overlap point to overlap polyline
            if at end of bc list

        if overlap is not empty
            if ad and bc segment endpoints differ
                add the least
            else
                add ad segment endpoint to overlap
            fetch next bc segment

  4. get overlap length
  5. get ad length
  6. get bc length
  7. return => overlap_length x 2 / (ad_length + bc_length )... aka detour ratio as defined above

  ---

The algorithm takes worst case O(ad * bc) time.

### Implementation:-
#### Python
Implementation resides in <py27/couc.py>. Run it like so:-

`./test.py -ad "[[1,2],[17,2]]" -bc "[[3,2],[14,2]] -d 80 -r"`

Where `-ad` and `-bc` are your polylines expressed as json arrays of 2 element
arrays (or tuples if you like) and `-d` is your acceptable "detour ratio"
threshold with valid i/p from 0-1. The `-r` toggles.

Test cases reside in the <py27/test.py>. Takes no arguments. Run like so:-
`./test.py` (or `test.py` on Windows).
