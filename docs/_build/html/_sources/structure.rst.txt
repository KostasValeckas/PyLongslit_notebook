Setting up the directory and file structure
===========================================

As for now, the software **relies strongly on a pre-determined structure of
files/directories and their naming**. We provide a correct setup in this 
tutorial, and the user should use exactly the same structure in any 
reduction. We advise to copy the tutorial directory and  then replacing/editing
relevant files for individual observations. The file structure will be broken
down in detail in the descriptions of the individual steps.

.. code-block:: bash

   ├── calibrate.py
   ├── database
   │   ├── idarc.dat
   │   ├── lapalma.dat
   │   ├── map-g04-he-1.pdf
   │   ├── map-g04-he-2.pdf
   │   ├── map-g04-ne-1.pdf
   │   ├── map-g04-ne-2.pdf
   │   └── mylines_vac.dat
   ├── extract_1d.py
   ├── extract_science_1d.py
   ├── extract_std_1d.py
   ├── identify.py
   ├── mfeige110.dat
   ├── raw
   │   ├── ALDh120176.fits
   │   ├── ALDh120177.fits
   │   ├── ALDh120178.fits
   │   ├── ALDh120179.fits
   │   ├── ALDh120217.fits
   │   ├── ALDh130384.fits
   │   ├── ALDh130385.fits
   │   ├── ALDh130386.fits
   │   ├── ALDh130387.fits
   │   ├── ALDh130388.fits
   │   ├── ALDh140211.fits
   │   ├── ALDh140219.fits
   │   ├── ALDh140230.fits
   │   ├── ALDh140238.fits
   │   ├── ALDh140351.fits
   │   ├── ALDh140352.fits
   │   ├── ALDh140353.fits
   │   ├── ALDh140354.fits
   │   ├── ALDh140355.fits
   │   ├── ALDh140356.fits
   │   ├── ALDh140357.fits
   │   ├── ALDh140358.fits
   │   ├── ALDh140359.fits
   │   ├── ALDh140360.fits
   │   └── ALDh140361.fits
   ├── rawbias
   │   ├── mkspecbias.py
   │   └── specbias.list
   ├── rawflats
   │   ├── mkspecflat.py
   │   └── specflat.list
   ├── rawscience
   │   ├── crremoval.py
   │   ├── raw_arcs.list
   │   ├── raw_science.list
   │   └── reducescience.py
   ├── rawstd
   │   ├── crremoval.py
   │   ├── raw_arcs.list
   │   ├── raw_std.list
   │   └── reducestd.py
   ├── reduceobs.py
   ├── sensfunction.py
   ├── setup.py
   └── standard.py
