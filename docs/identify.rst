.. _identify:

Identify
========

In this step, we manually identify the lines in the arc-lamp spectrum, and fit
a polynomial function for describing wavelength as a function of pixel
(this function is called a **wavelength solution**). This later allows
us to calibrate the pixel values of the science and standard star frames
to wavelength values.
The identification is done in an interactive plotting window/GUI. 

**This step is by far the most time-consuming for the user, as 
a fair amount of user work is needed. Excpect this to be challenging
at first, if you have not tried this type of routine before.**

To run this script, you will need the `arcsub.fits` file from the 
:ref:`pre-processing <pre_processing>` step. You will also need a 
list with the arc lines for your specific setup. This list should
be called `mylines_vac.dat` or `ThAr_linelist.dat` and should be 
located in the `database` directory. For this tutorial, we provide the
list for the HeNe lamp used for the tutorial data.
As one will need a referrence spectrum with emission lines tagged with wavelentghs
to manually identify the lines (also called a **arc lamp map**), this also needs to be aquired. 
For this tutorial, we provide such reference spectra for the
HeNe lamp used with the g04 grating for `ALFOSC <https://www.not.iac.es/instruments/alfosc/>`_ in 4 PDF files in the 
`database` directory. 
These have been downloaded from the `ALFOSC website <https://www.not.iac.es/instruments/alfosc/lamps/>`_ .

Therefore, the relevant files and directories for this step are:

.. code-block:: bash

    ├── arcsub.fits
    ├── database
    │   ├── map-g04-he-1.pdf
    │   ├── map-g04-he-2.pdf
    │   ├── map-g04-ne-1.pdf
    │   ├── map-g04-ne-2.pdf
    │   └── mylines_vac.dat
    ├── identify.py

In the following, we provide a step-by-step guide on how to execute
the line identification:

1. **Run the script**: 
   In the same directory as the `identify.py` script, run:

    .. code-block:: bash
    
        python3 identify.py

    When the script is excecuted, a GUI/interactive plot window will open.
    You have to manually load the arc spectrum by clicking on the `Load Spectrum`
    button, and finding the `arcsub.fits` file. This will also load the 
    pre-existing line list `mylines_vac.dat` into the GUI. Your window should
    look something like this:

    .. image:: pictures/id_post_loading.png
       :width: 600
       :align: center

2. **Identifying the lines**: 
   In this step, you have to use the reference spectra provided in the `databse`
   directory (or downloaded elswhere for your own setup) to identify the
   wavelentghs of the lines in the arc spectrum. This is done by clicking on the
   `Add Line` button, and then clicking on the arc spectrum where you think a line
   is, and then manually typing in the wavelength of the line. Below is an 
   example for a small Helium portion of the spectrum, with a zoom in of the corresponding 
   reference spectrum:

    .. image:: pictures/id_post_first.png
       :width: 600
       :align: center

    .. image:: pictures/id_post_first_ref.png
       :width: 600
       :align: center

   (here there is a small offset in wavelentghs between the reference spectrum 
   (lowest picture) and the line list (upper left corner) - we have used the linelist,
   since the software will rely on the list later)

   After you have found a handfull of lines, you can click on the `Fit` button to
   make a polynomial fit for a function that describes wavelength as a function of
   pixel. You can use the `Residual/Data` button to change displays between the
   fit curve and the residuals of the fit in order to evaluate the fit quality. 
   For the small amount of lines shown above, this looks like this:

      .. image:: pictures/id_fit_first.png
         :width: 600
         :align: center

      .. image:: pictures/id_res_first.png
         :width: 600
         :align: center

   When you have obtained a fit, and try to `Add Line` again, the program will
   use the fit to extrapolate the wavelength of the line you are trying to add,
   and look for it in the linelist. If it finds a match, it will automatically
   add it. If it does not find a match, it will show a message indicating so,
   but it will still add the line - you will then have to correct it manually.
   If your fit does not seem to be good, you can click on the `Clear fit` button
   to remove it, and then add more lines manually. You can also selectively remove
   one or all lines.

   From here on, you have to obtain the best possible fit by trial and error:

   1. Add lines manually
   2. Fit
   3. Use the fit to add more lines
   4. Refit - correct outlies - come back to 1. or 2. and repeat until you are satisfied with the fit.

   Remember that the calbrated 1d-spectrum will be flux as a function of wavelength - 
   therefore the quality of your fit will affect the quality of the final
   results significantly (as it will be used to determine wavelength, 
   and therefore the whole x-axis of your calibrated 1d-spectrum). 
   Even though this step is by far the most time-consuming, it 
   should not be rushed. However, you will very likely be unable to identify
   all lines, and the ones that causes uncertainty should be left out.
   This said, make sure you identify lines in all parts of the spectrum.

   5. **Saving the line list**: 
   When you are satisfied with the fit, you need to save the pixel table.
   Press `File` -> `Save PixTable` and save the file as `idarc.dat` **in the 
   database directory**. It is important that you follow the naming and 
   placement exactly.

   Your end result should look like this:

      .. code-block:: bash

            ├── arcsub.fits
            ├── database
            │   ├── idarc.dat
            │   ├── map-g04-he-1.pdf
            │   ├── map-g04-he-2.pdf
            │   ├── map-g04-ne-1.pdf
            │   ├── map-g04-ne-2.pdf
            │   └── mylines_vac.dat
            ├── identify.py
 


.. note::
   For this tutorial, we already pre-made an `idarc.dat` file, so you have 
   a starting point to work with. You can inspect the file by pressing 
   `File` -> `Load PixTable`. To proceed in the tutorial, 
   you can either try to improve our fit, or move on directly using it. 
