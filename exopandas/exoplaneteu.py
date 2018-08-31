import astropy.units as uu

from PyAstronomy import pyasl

from .exodataframe import ExoDataFrame


## Pyastronomy ExoplanetEU2 object
v = pyasl.ExoplanetEU2()


class ExoplanetEU(ExoDataFrame):

    def __init__(self, *args, **kwargs):
        if len(args) == 0:
            args = [pyasl.ExoplanetEU2().getAllDataPandas()]
        super(ExoplanetEU, self).__init__(*args, **kwargs)

    @property
    def _constructor(self):
        return ExoplanetEU

    def _add_available_unified_cols(self):
        # Names
        self._add_unified_colname('st_name', 'star_name', description="")
        self._add_unified_colname('pl_name', 'name', description="")  # Planet name
        # Planet orbital elements
        self._add_unified_colname('pl_omega', 'omega', description="*Stellar* orbital argument of periastron (in degrees)", unit=uu.deg)
        self._add_unified_colname('pl_per', 'orbital_period', description="Planetary orbital period (in days)", unit=uu.d)
        self._add_unified_colname('t_tr', 'tzero_tr', description="Planetary transit time (in days)", unit=uu.d)
        self._add_unified_colname('t_peri', 'tperi', description="Planetary periastron passage (in days)", unit=uu.d)
        self._add_unified_colname('t_ic', 'tconj', description="Planetary time of inferior conjunction (in days)", unit=uu.d)
        self._add_unified_colname('pl_ecc', 'eccentricity', description="Planetary orbital eccentricity")
        self._add_unified_colname('pl_inc', 'inclination', description="Planet orbital inclination (in degrees)", unit=uu.deg)
        self._add_unified_colname('pl_a', 'semi_major_axis', description="Planet orbital semi-major axis (in AU)", unit=uu.au)
        # Planet transit parameter
        self._add_unified_colname('b', 'impact_parameter', description="Planetary impact parameter")
        # Planet parameters
        self._add_unified_colname('pl_radj', 'radius', description="Planetary radius (in R_jup)", unit=uu.R_jup)
        self._add_unified_colname('pl_massj', 'mass', description="Planetary mass (in M_jup)", unit=uu.M_jup)  # Planet mass in Mjup
        self._add_unified_colname('pl_teq', 'temp_calculated', description="Planetary calculated equilibrium temperature (in K)", unit=uu.K)  # Pl equilibrium temp [K]
        # Stellar Parameters
        self._add_unified_colname('st_rad', 'star_radius', description="Stellar radius (in R_sun)", unit=uu.R_sun)
        self._add_unified_colname('st_mass', 'star_mass', description="Stellar mass (in M_sun)", unit=uu.M_sun)
        self._add_unified_colname('st_teff', 'star_teff', description="Stellar effective temperature (in K)", unit=uu.K)  # Stellar effective temperature in K
        # self.col['vsini'] = 'st_vsini'
        self._add_unified_colname('vsini', 'st_vsini', description="")
        # self.column_conv['mag_opt'] = ["mag_v",]
        self._add_unified_colname('mag_v', 'mag_v', description="")
        self._add_unified_colname('pl_rad_orig', 'radius_detection_type', description="")
        self._add_unified_colname('dec', 'dec', description="Stellar declination (J2000, in degrees)", unit=uu.deg)  # in degrees
        self._add_unified_colname('ra', 'ra', description="Stellar right ascencion (J2000, in degrees)", unit=uu.deg)  # in degrees
        self._add_unified_colname('pl_mass_orig', 'mass_detection_type', description="")  # Planet mass origin
        self._add_unified_colname('sp_type', 'star_sp_type', description="")  # Spectral type
        self._add_unified_colname('pl_msinij', 'mass_sini', description="")  # in mass in jupiter mass
