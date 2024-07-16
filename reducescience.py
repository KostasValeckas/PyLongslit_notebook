"""
A wrapper to call reduceobs.reduce_obs for a science object reduction.
"""

import sys
import os

sys.path.append(os.getcwd() + '/..')

from reduceobs import reduce_obs

# THESE HAVE TO BE SET MANUALLY
ysize = 2102
xsize = 500

# The x-coordinates of the object centers. 
# Must be same length number of exposures, and sorted to match
# the exposure frames in alphabetical order.
centers = [250, 273] 

if __name__ == '__main__':
    reduce_obs(ysize, xsize, centers, standard_star_reduction = False)