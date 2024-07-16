import matplotlib._pylab_helpers

from astropy.io import fits

import numpy as np

from matplotlib import pyplot as plt

get_new_line = True

def standard(out_dir = ".", star_file_path = None):

    #The equivalent of "standard" in IRAF/onedspec
    #https://astro.uni-bonn.de/~sysstw/lfa_html/iraf/noao.onedspec.standard.html

    #Open file for output
    f = open(out_dir + '/stdinfo', 'w')

    #name of standard star
    #tdnm = 'gd71'
    stdnm = 'feige110'
    #stdnm = 'bd33d2642'

    #get information from header
    std_file = fits.open(out_dir + '/std.fits')
    hdr = std_file[0].header
    exptime = hdr['EXPTIME']
    airmass = hdr['AIRMASS']

    #read in the standard star measurements
    std_data = np.loadtxt(out_dir + '/std.ms_1d.dat')
    lam = std_data[:,0]
    stdcounts = std_data[:,1]

    f.write("%s  %s  %s\n" % ('#', stdnm, 'std.ms_1d.dat'))
    f.write("%5.1f %4.3f\n" % (exptime, airmass))
    f.close

    #Read the file with the flux measurements
    #SET .Z.UNITS = "micro-Janskys"
    #SET .Z.LABEL = "Flux"
    #SET .TABLE.BANDWIDTH = 40
    std_ref_data = np.loadtxt(star_file_path)
    reflam = std_ref_data[:,0]
    refflux = std_ref_data[:,1]
    bandwidth = 40.

    #Plot measured standard spectrum
    fig, _ = plt.subplots()
    plt.xlim(3300,9500)
    plt.ylim(0,np.amax(stdcounts)*1.2)
    plt.xlabel('lambda i Å')
    plt.ylabel('Counts')
    plt.xlabel('Observed wavelength [Å]')
    plt.ylabel('Counts per sec')
    plt.plot(lam,stdcounts, lw = 1, label='1d extracted standard star spectrum')
    plt.legend()

    plt.title("Click on a part of a spectrum that you want to mask\n"
                "Press q to quit")
    plt.draw()
    plt.pause(0.001)


    #hack to only show legend once, TODO: fix this
    legend_bool = True

    deleted = list()

    # A hack to prevent q exit hack
    # and infinte loop. 
    # TODO: fix this to remove the global variable
    def exit_on_q(event):

        if event.key == 'q':
            global get_new_line
            get_new_line = False
            plt.close("all")

    fig.canvas.mpl_connect('key_press_event', exit_on_q)

    global get_new_line

    while get_new_line:

        plt.title("Click on a part of a spectrum that you want to mask\n"
                "Press q to quit")
        plt.pause(0.001)


        # this  loop manually checks if the window has been closed by corner "x"
        while True:

            points = plt.ginput(n=1, timeout=3, mouse_add = 1)
            
            # the long condition is how man matplotlib windows are open
            if len(points) != 1 and len(matplotlib._pylab_helpers.Gcf.get_all_fig_managers()) == 0:
                get_new_line = False
                plt.close("all")
                break

            if len(points) == 1:
                plt.pause(0.001)
                break


        if len(points) == 1 and get_new_line:

            pix_ref, _ = points[0]
            select = np.abs(reflam - pix_ref) < bandwidth/2
            
            for wl in (reflam[select]):

                if not get_new_line:
                    break

                deleted.append(wl)
                window = (lam > wl-0.5*bandwidth) & (lam < wl+0.5*bandwidth)
                maxflux = np.amax(stdcounts[window])
                minflux = np.amin(stdcounts[window])
                if legend_bool:
                    plt.vlines(wl, minflux, maxflux, color='r', linewidth=1, label = 'Masked regoin')
                    legend_bool = False
                else: 
                    plt.vlines(wl, minflux, maxflux, color='r', linewidth=1)
                plt.legend()
                plt.title("Masking out wavelength %.1f, please wait..." % wl)
                plt.draw()
                plt.pause(0.001)
    
        else:
            get_new_line = False
            plt.close("all")
    plt.show()

    get_new_line = True

    #Write to file

    # CHANGE UNITS HERE TO FIT YOUR REFERENCE FILE
    #Convert micro-Jansky to erg/s/cm/AA (https://en.wikipedia.org/wiki/AB_magnitude)
    #print("ASSUMING THAT THE REFERENCE FILE IS IN MICRO-JANSKY")
    #flam = refflux/1.e6/3.34e4/reflam**2

    #Convert AB magnitude to erg/s/cm/AA:
    print("ASSUMING THAT THE REFERENCE FILE IS IN AB MAGNITUDE")
    flam = 2.998e18*10**(-(refflux+48.6)/2.5)/reflam**2


    f = open(out_dir + '/stddata', 'w')
    for n in range(0,len(reflam)):
        wl = reflam[n]
        if (wl > np.amin(lam)) & (wl < np.amax(lam)) & (wl not in deleted):
            window = (lam > wl-0.5*bandwidth) & (lam < wl+0.5*bandwidth)
            f.write("%.0f   %.3e   %.2f    %.1f\n" %(wl,flam[n],bandwidth,np.mean(stdcounts[window])))
    print('Output files stdinfo and stddata have been written to the output directory.')

    f.close
