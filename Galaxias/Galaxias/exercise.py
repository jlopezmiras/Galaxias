import pandas as pd
import numpy as np
from astropy import units as u
import matplotlib.pyplot as plt

data = pd.read_csv("Disk_100pc_old.csv")

# Positions
r = data['DIST_1000'].to_numpy() * u.pc
RA = data['RA'].to_numpy() * u.deg
DEC = data['DEC'].to_numpy() * u.deg

# Proper motion and radial velocity
pmRA = data['PMRA'].to_numpy() * u.marcsec / u.year
pmDEC = data['PMDEC'].to_numpy() * u.marcsec / u.year
vr = data['RV'].to_numpy() * u.km / u.s


tRA = r * pmRA.to(u.arcsec / u.s) * np.cos(DEC.to(u.rad))




