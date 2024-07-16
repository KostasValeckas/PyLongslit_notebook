26.06.2024
--------------
Hardcoded nframes in mkspecbias.py and mkspecflat.py made dynamic
by automatic determination based on the number of files in the list.

reducescience.py and reducestd.py made into one script,
here all input/output made dynamic so the scripts no longer
depend on pre-determined number of files or prefixes - but require a 
file name instead.
This edit allows for cosmic ray removal for standard stars also.

30.06.2024
--------------
Changed reduceobs.py to be called by wrapper scripts reducescience.py 
and reducestd.py . Same for extract_1d.py, now also called by wrapper 
scripts extract_science_1d.py and extract_std_1d.py. 

03.07.2024
--------------

standard.py made more user friendly ("animated masking and simpler commands").

05.07.2024
--------------

Better plotting in wavelength calib. assesment
