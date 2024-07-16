import astroscrappy
import glob

import os as os

from astropy.io import fits

"""
This is a python program to run cosmic ray removal on observations
(both science and standard frames)
"""

# THESE HAVE TO BE SET MANUALLY
gain = 0.16 # LOOK UP fitsfile[1].header['GAIN']
ron = 4.3 # LOOK UP fitsfile[1].header['RDNOISE']

# THSE CAN BE SET DIFFERENTLY AS NEEDED
frac = 0.01
objlim = 15
sigclip = 5
niter = 5

def crremoval(
    gain,
    ron,
    list,
    inp_dir = ".",
    out_dir = ".",
    frac = 0.01,
    objlim = 15,
    sigclip = 5,
    niter = 5
):



    print('Script running')
    print('\n ---Using the following parameters:---\n')
    print(f'gain = {gain}')
    print(f'ron = {ron}')
    print(f'frac = {frac}')
    print(f'objlim = {objlim}')
    print(f'sigclip = {sigclip}')
    print(f'niter = {niter}')
    print('----------------------------------------\n')
    
    for filename in list:
        fitsfile = fits.open(inp_dir + "/" + filename)
        print('Removing cosmics from file: ' + filename + '...')
            
        crmask, clean_arr = astroscrappy.detect_cosmics(fitsfile[1].data, sigclip=sigclip, sigfrac=frac, objlim=objlim, cleantype='medmask', niter=niter, sepmed=True, verbose=True)
    
    # Replace data array with cleaned image
        fitsfile[1].data = clean_arr
    
    # Try to retain info of corrected pixel if extension is present.
        try:
            fitsfile[2].data[crmask] = 16 #Flag value for removed cosmic ray
        except:
            print("No bad-pixel extension present. No flag set for corrected pixels")
    
    # Update file
        fitsfile.writeto(out_dir + "/crr"+filename, output_verify='fix', overwrite=True)
    
