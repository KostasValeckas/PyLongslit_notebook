Getting started
~~~~~~~~~~~~~~~

Execution of the software is highly manual. 
The software depends on "hard-coded" paths and file names, 
often relative to the location of the script.

We therefore believe that the best way to learn how the software works
is by following a tutorial. The tutorial will guide you through the reduction
of a long-slit spectrum, and will also comment on where changes should be 
made when/if you will run the software for your own data/setup.

We therefore provide a `tutorial directory <https://github.com/KostasValeckas/PyLongslit/tree/main/tutorial>`_ that contains the example data
and is prepped to have the right file and directory structure.

The example data comes from 
`ALFOSC <https://www.not.iac.es/instruments/alfosc/>`_ , and is an 
observation of the SDSSJ234034-033205 quasar, provided by
Johan Peter Uldall Fynbo.

**The tutorial describes a series of parameters that need to be 
set in various scripts to match your data. For the tutorial data, everything in the
tutorial directory has the right parameters set. This means
that you can directly execute the scripts as they are provided.**

Tutorial
----------------------------------------------------

.. note::
    The steps in this tutorial have been tested on 
    Linux Ubuntu 22.04.4 LTS (which should also cover MacOS functionality
    in broad sense) and Windows 10 Pro.

Running the software can be divided in two main parts: pre-processing and
pipeline execution. 

You have to excecute the steps exactly in the order they are presented in the
contents table below.


.. toctree:: 
   :maxdepth: 2
   :caption: Contents:

   structure
   pre_processing
   pipeline



