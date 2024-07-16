import numpy
from astropy.io import fits

"""
This is a python program to make a specflat frame
"""


def mkspecflat(xsize, ysize, list, inp_dir = ".", out_dir = "."):
    print('\n ---Using the following parameters for flats:---\n')
    print(f'ysize = {ysize}')
    print(f'xsize = {xsize}')
    print('----------------------------------------\n')
    
    #Read in the raw flat frames and subtact mean of overscan region 
    
    nframes = len(list)
    
    bigflat = numpy.zeros((nframes,ysize,xsize),float)
    BIASframe = fits.open(out_dir + '/BIAS.fits')
    BIAS = numpy.array(BIASframe[0].data)
    
    for i,file in enumerate(list):
       print('Image number:', i)
       rawflat = fits.open(inp_dir + "/" + file)
       #print('Info on file:')
       #print(rawflat.info())
       data = numpy.array(rawflat[1].data)
       median = numpy.mean(data[2066:ysize-5,0:xsize-1])
       data = data - median
       print('Subtracted the median value of the overscan :',median)
       data = data - BIAS
       print('Subtracted the BIAS')
       bigflat[i-1,0:ysize-1,0:xsize-1] = data[0:ysize-1,0:xsize-1]
       norm = numpy.median(bigflat[i-1,100:400,100:1300])
       print('Normalised with the median of the frame :',norm)
       bigflat[i-1,:,:] = bigflat[i-1,:,:]/norm
    
    #Calculate flat is median at each pixel
    medianflat = numpy.median(bigflat,axis=0)
    
    #Normalise the flat field
    lampspec = numpy.mean(medianflat,axis=1)
    norm = medianflat*0.
    for i in range(0,xsize-1):
       medianflat[:,i] = medianflat[:,i] / lampspec[:]
    
    #Write out result to fitsfile
    hdr = rawflat[0].header
    fits.writeto(out_dir + '/Flat.fits',medianflat,hdr,overwrite=True)
