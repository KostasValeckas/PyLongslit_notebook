import numpy as np

def append_list(file_names, input_dir):
    return [input_dir + file for file in file_names]

#Weight function for optimal extraction
def gaussweight(x, mu, sig):
    return np.exp(-0.5*(x-mu)**2/sig**2) / (np.sqrt(2.*np.pi)*sig)

#For setting up the output fits-spectra
def fake_multispec_data(arrlist):
   # takes a list of 1-d numpy arrays, which are
   # to be the 'bands' of a multispec, and stacks them
   # into the format expected for a multispec.  As of now
   # there can only be a single 'aperture'.
   return np.expand_dims(np.array(arrlist), 1)