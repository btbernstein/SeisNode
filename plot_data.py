import matplotlib.pyplot as plt

def plot(t ):

    plt.show(block=True)

    fig,ax = plt.subplots(4,1,figsize=(16,10))
    ax[0].plot(times_v,voltages)
    ax[0].set_title("Geophone Readings: n=%i Data Points" % len(voltages), fontsize=16, fontweight="bold")
    ax[0].set_xlabel("Time (seconds)", fontsize=14, fontweight="bold")
    ax[0].set_ylabel("Voltage", fontsize=14, fontweight="bold")
    
    ax[1].errorbar(times_g,lats,yerr=lat_err)
    ax[1].set_title("Latitude: n=%i Data Points" % len(lats), fontsize=16, fontweight="bold")
    ax[1].set_xlabel("Time", fontsize=14, fontweight="bold")
    ax[1].set_ylabel("Latitude (Decimal$^\circ$)", fontsize=14, fontweight="bold")
    ax[0,1].xaxis.set_ticks(times_g[::4], rotation=45)
    
    ax[2].errorbar(times_g,lons,yerr=lon_err)
    ax[2].set_title("Longitude: n=%i Data Points" % len(lons), fontsize=16, fontweight="bold")
    ax[2].set_xlabel("Time", fontsize=14, fontweight="bold")
    ax[2].set_ylabel("Longitude (Decimal$^\circ$)", fontsize=14, fontweight="bold")
    
    ax[3].errorbar(times_g,alts,yerr=alt_err)
    ax[3].set_title("Altitude: n=%i Data Points" % len(alts), fontsize=16, fontweight="bold")
    ax[3].set_xlabel("Time", fontsize=14, fontweight="bold")
    ax[3].set_ylabel("Altitude (meters)", fontsize=14, fontweight="bold")

    for axi in ax.flat:
        if axi != ax[0]:
          plt.setp(axi.xaxis.get_majorticklabels(),rotation=20)
        axi.xaxis.set_major_locator(plt.MaxNLocator(5))

    plt.tight_layout()
    plt.savefig("all")

    plt.subplots_adjust(hspace=0.5)    
    plt.show(block=True)
