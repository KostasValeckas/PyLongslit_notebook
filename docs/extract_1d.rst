.. _extract_1d:


Extract 1d science/standard star spectrum
=========================================

The procedure for extracting the 1d spectrum of the science observation and the
standard star is almost the same, and therefore they will be described together. The 
scripts used for this step are `extract_science_1d.py` and `extract_std_1d.py`.
Both scripts need `extract_1d.py` in order to work. The input to these scripts
is the :ref:`setup.py <setup>` file, as well as the `ìdarc.dat` file from the
:ref:`identify <identify>` step. The relevant files and their structure is therefore:

.. code-block::  bash

    ├── arcsub.fits
    ├── arcsub_std.fits
    ├── database
    │   ├── idarc.dat
    ├── extract_1d.py
    ├── extract_science_1d.py
    ├── extract_std_1d.py
    ├── obj.fits
    ├── setup.py
    └── std.fits

To extract the 1d spectrum of the science observation and standard star, follow these steps:

1. **Run the script**: 
   In the same directory as the `extract_science_1d.py` and `extract_std_1d.py` scripts, run:

    .. code-block:: bash
    
        python3 extract_science_1d.py

    for the science observation, and:

    .. code-block:: bash
    
        python3 extract_std_1d.py

    for the standard star.

2. **Evaluate wavelength calibration**

    Firstly, the script will do a refinement of the wavelength solution, 
    and produce some quality assurance plots. These look something like this:

    .. image:: pictures/wave_qa.png
       :width: 600
       :align: center

    The image on the top left is the detector image with a wavelength colormapped
    to every pixel. The red lines are the identified lines used in production
    of the wavelentgh solution. Here we are looking for a smooth and continuous
    colormap. The dashed black lines are the lines that are plotted in the
    curve plots (these are `the cuts`). `hcut` are the horizontal lines, and `vcut` are the vertical lines.
    For horizontal lines, we are looking for a smooth, somewhat constantly growing curve.
    For the vertical lines, some wavelength change is okay 
    in vertical direction, as it can be caused by optical effects. However, these
    should be smooth and continuous. We can assume that the object spectrum will 
    roughly be placed along one `hcut`, and it therefore has the most importance 
    to us. 

    If the results of the wavelength calibration are showing flaws,
    you need to find relevant parameters and adjust them in :ref:`setup.py <setup>`.

3. **Select the sky and object**

    In the next step, you will need to help the software to identify the sky and object.
    An interactive plot window will open, where you will have to use 5 mouse left-clicks 
    to identify (approximetly):

    1. The sky background on the left side of the object - start.
    2. The sky background on the left side of the object - end.
    3. The object center
    4. The sky background on the right side of the object - start.
    5. The sky background on the right side of the object - end.
    6. Press "q" when you are done.
   
    The plot prior and after clicking should look something like this:

    .. image:: pictures/object_prior_click.png
       :width: 600
       :align: center

    .. image:: pictures/object_post_click.png
       :width: 600
       :align: center

    The rest of the script is automatic.

    In the following we provide an array of quality assesment plots with
    comments of the expected results. If the results are not as expected,
    you need to find relevant parameters and adjust them in :ref:`setup.py <setup>`.      


4. **Evaluate results for the remainder of the extraction**

    The software will now perform a fit to the sky background,
    where we are looking for a line that goes through the sky background only:

    .. image:: pictures/object_sky_fit.png
       :width: 600
       :align: center    

    , and also a fit to the object trace, where we are looking for (somewhat)
    constant FWHM and a clean fit to object trace with a random residual spread:

    .. image:: pictures/object_trace_fit.png
       :width: 600
       :align: center

    The sky is then subtracted from the object, where we want to see the object
    trace with a uniform background after the subtraction:

    .. image:: pictures/skysub.png
       :width: 600
       :align: center

    Finally, the software will extract the 1d spectrum, and plot the result:

    .. image:: pictures/spec_1d_adu.png
       :width: 600
       :align: center

A series of files are produced, and when both scripts are excecuted, 
the relevant file structure should now look like this:

.. code-block:: bash

    ├── arcsub.fits
    ├── arcsub_std.fits
    ├── database
    │   ├── idarc.dat
    ├── extract_1d.py
    ├── extract_science_1d.py
    ├── extract_std_1d.py
    ├── obj.fits
    ├── obj.ms_1d.fits
    ├── obj.ms_1dw.dat
    ├── obj.sky.fits
    ├── obj.skysub.fits
    ├── obj.variance.fits
    ├── setup.py
    ├── std.fits
    ├── std.ms_1d.dat
    ├── std.ms_1d.fits
    ├── std.sky.fits
    ├── std.skysub.fits
    └── std.variance.fits

.. note:: 
    In the tutorial data, the standard star object trace exhibits a wave-like pattern
    in the residuals. This is an unwanted effect, and is caused by a finer
    structure in the object trace. Some of this can be resolved by setting 
    the `ORDER_APTRACE` parameter in :ref:`setup.py <setup>` to a higher value,
    and lowering the `SIGMA_APTRACE` parameter.
    However, inspecting the curve plot itself, the fit seems to be 
    sufficiently correct.


