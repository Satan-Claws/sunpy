"""
====================================
Blending Plots using mplcairo
====================================

This example will go through how you can blend two plots from SunPY
using mplcairo

"""

import matplotlib; matplotlib.use("module://mplcairo.qt")
import matplotlib.pyplot as plt
from mplcairo import operator_t

import astropy.units as u

import sunpy.map
import sunpy.data.sample
from sunpy.coordinates import Helioprojective

###############################################################################
# Let's Import two plots we want to blend together

a171 = sunpy.map.Map(sunpy.data.sample.AIA_171_IMAGE)
a131 = sunpy.map.Map(sunpy.data.sample.AIA_131_IMAGE)
with Helioprojective.assume_spherical_screen(a171.observer_coordinate):
    a131 = a131.reproject_to(a171.wcs)

###############################################################################
# Now, using matplotlib and mplcairo, blend the two


fig = plt.figure()
ax = fig.add_subplot(projection=a171)

_ = a171.plot(clip_interval=(1, 99.9995)*u.percent)
im131 = a131.plot(clip_interval=(1, 99.95)*u.percent)

operator_t.SCREEN.patch_artist(im131)

###############################################################################
# Plot the result we get


ax.set_title('mplcairo composite using screen blending')

plt.show()
