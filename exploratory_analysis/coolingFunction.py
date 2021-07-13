import h5py, numpy as np, glob, string, os, pdb, time
import os
from numpy import log10 as log
import scipy
import scipy.stats
from scipy import interpolate

Z_solar = 0.0129
def LambdaFunc(z,tables_dir,Y):
    fns = np.array(glob.glob(tables_dir+'z_?.???.hdf5'))
    zs = np.array([float(fn[-10:-5]) for fn in fns])
    fn = fns[zs.argsort()][searchsortedclosest(sorted(zs), z)]
    
    f=h5py.File(fn,'r')
    iHe = searchsortedclosest(f['Metal_free']['Helium_mass_fraction_bins'][:],Y)    
    H_He_Cooling  = f['Metal_free']['Net_Cooling'][iHe,...]
    Tbins         = f['Metal_free']['Temperature_bins'][...]
    nHbins        = f['Metal_free']['Hydrogen_density_bins'][...]
    Metal_Cooling = f['Total_Metals']['Net_cooling'][...] 
    
    f_H_He = interpolate.RegularGridInterpolator((log(Tbins), log(nHbins)),
                                                    H_He_Cooling, 
                                                    bounds_error=False, fill_value=None)
    f_Z = interpolate.RegularGridInterpolator((log(Tbins), log(nHbins)),
                                                    Metal_Cooling, 
                                                    bounds_error=False, fill_value=None)
    
    
    return lambda T,nH,Z2Zsun,f_H_He=f_H_He,f_Z=f_Z: (
        f_H_He((log(T), log(nH))) + f_Z((log(T), log(nH))) * Z2Zsun )


def searchsortedclosest(arr, val):
    assert(arr[0]!=arr[1])
    if arr[0]<arr[1]:
        ind = np.searchsorted(arr,val)
        ind = minarray(ind, len(arr)-1)
        return maxarray(ind - (val - arr[maxarray(ind-1,0)] < arr[ind] - val),0)        
    else:
        ind = np.searchsorted(-arr,-val)
        ind = minarray(ind, len(arr)-1)
        return maxarray(ind - (-val + arr[maxarray(ind-1,0)] < -arr[ind] + val),0)        


def maxarray(arr, v):
    return arr + (arr<v)*(v-arr)
def minarray(arr, v):
    return arr + (arr>v)*(v-arr)
