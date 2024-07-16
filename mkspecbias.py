
import numpy
from astropy.io import fits

"""
This is a python program to make a BIAS frame
"""

def mkspecbias(xsize, ysize, list, inp_dir = ".", out_dir = "."):
   print('\n ---Using the following parameters for bias:---\n')
   print(f'ysize = {ysize}')
   print(f'xsize = {xsize}')
   print('----------------------------------------\n')

   #Read in the raw bias frames and subtact mean of overscan region 


   nframes = len(list)

   bigbias = numpy.zeros((nframes,ysize,xsize),float)
   #bigbias = numpy.zeros((nframes,3,3))
   for i,file in enumerate(list):
      print('Image number:', i)
      rawbias = fits.open(inp_dir + "/" + file)
      #print('Info on file:')
      #print(rawbias.info())
      data = numpy.array(rawbias[1].data)
      mean = numpy.mean(data[2066:ysize-5,0:xsize-1])
      data = data - mean
      print('Subtracted the median value of the overscan :',mean)
      bigbias[i-1,0:ysize-1,0:xsize-1] = data[0:ysize-1,0:xsize-1]

   ##Calculate bias is median at each pixel
   medianbias = numpy.median(bigbias,axis=0)

   #Write out result to fitsfile
   hdr = rawbias[0].header
   fits.writeto(out_dir +'/BIAS.fits',medianbias,hdr,overwrite=True)
