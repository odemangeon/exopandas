from PyAstronomy import pyasl
import astropy.units as uu

from .column_info import create_empty_column_info, add_column_2_column_info, non_app, without_unit


column_info = create_empty_column_info()
column_info = add_column_2_column_info(column_info=column_info, original_column='star_name', unified_column='st_name',
                                       description='', unit=non_app)
column_info = add_column_2_column_info(column_info=column_info, original_column='name', unified_column='pl_name',
                                       description='', unit=non_app)
column_info = add_column_2_column_info(column_info=column_info, original_column='omega', unified_column='pl_omega',
                                       description='', unit=uu.deg)
column_info = add_column_2_column_info(column_info=column_info, original_column='orbital_period', unified_column='pl_per',
                                       description='', unit=uu.d)
column_info = add_column_2_column_info(column_info=column_info, original_column='orbital_period_error_min', unified_column='pl_per_err_inf',
                                       description='', unit=uu.d)
column_info = add_column_2_column_info(column_info=column_info, original_column='orbital_period_error_max', unified_column='pl_per_err_sup',
                                       description='', unit=uu.d)
column_info = add_column_2_column_info(column_info=column_info, original_column='tzero_tr', unified_column='t_tr',
                                       description='', unit=uu.d)
column_info = add_column_2_column_info(column_info=column_info, original_column='tperi', unified_column='t_peri',
                                       description='', unit=uu.d)
column_info = add_column_2_column_info(column_info=column_info, original_column='tconj', unified_column='t_ic',
                                       description='', unit=uu.d)
column_info = add_column_2_column_info(column_info=column_info, original_column='eccentricity', unified_column='pl_ecc',
                                       description='', unit=without_unit)
column_info = add_column_2_column_info(column_info=column_info, original_column='inclination', unified_column='pl_inc',
                                       description='', unit=uu.deg)
column_info = add_column_2_column_info(column_info=column_info, original_column='semi_major_axis', unified_column='pl_a',
                                       description='', unit=uu.au)
column_info = add_column_2_column_info(column_info=column_info, original_column='impact_parameter', unified_column='b',
                                       description='', unit=without_unit)
column_info = add_column_2_column_info(column_info=column_info, original_column='radius', unified_column='pl_radj',
                                       description='', unit=uu.R_jup)
column_info = add_column_2_column_info(column_info=column_info, original_column='radius_detection_type', unified_column='pl_rad_orig',
                                       description='', unit=non_app)
column_info = add_column_2_column_info(column_info=column_info, original_column='mass', unified_column='pl_massj',
                                       description='', unit=uu.M_jup)
column_info = add_column_2_column_info(column_info=column_info, original_column='mass_error_min', unified_column='pl_massj_err_inf',
                                       description='', unit=uu.M_jup)
column_info = add_column_2_column_info(column_info=column_info, original_column='mass_error_max', unified_column='pl_massj_err_sup',
                                       description='', unit=uu.M_jup)
column_info = add_column_2_column_info(column_info=column_info, original_column='mass_sini', unified_column='pl_msinij',
                                       description='', unit=uu.M_jup)
column_info = add_column_2_column_info(column_info=column_info, original_column='mass_detection_type', unified_column='pl_mass_orig',
                                       description='', unit=non_app)
column_info = add_column_2_column_info(column_info=column_info, original_column='temp_calculated', unified_column='pl_teq',
                                       description='', unit=uu.K)
column_info = add_column_2_column_info(column_info=column_info, original_column='star_radius', unified_column='st_rad',
                                       description='', unit=uu.R_sun)
column_info = add_column_2_column_info(column_info=column_info, original_column='star_mass', unified_column='st_mass',
                                       description='', unit=uu.M_sun)
column_info = add_column_2_column_info(column_info=column_info, original_column='star_teff', unified_column='st_teff',
                                       description='', unit=uu.K)
column_info = add_column_2_column_info(column_info=column_info, original_column='st_vsini', unified_column='vsini',
                                       description='', unit=uu.km / uu.s)
column_info = add_column_2_column_info(column_info=column_info, original_column='mag_v', unified_column='mag_v',
                                       description='', unit=without_unit)
column_info = add_column_2_column_info(column_info=column_info, original_column='ra', unified_column='ra',
                                       description='', unit=uu.deg)
column_info = add_column_2_column_info(column_info=column_info, original_column='dec', unified_column='dec',
                                       description='', unit=uu.deg)
column_info = add_column_2_column_info(column_info=column_info, original_column='star_sp_type', unified_column='sp_type',
                                       description='', unit=non_app)
column_info = add_column_2_column_info(column_info=column_info, original_column='radius', unified_column='pl_radj',
                                       description='', unit=uu.R_jup)
column_info = add_column_2_column_info(column_info=column_info, original_column='radius_error_min', unified_column='pl_radj_err_inf',
                                       description='', unit=uu.R_jup)
column_info = add_column_2_column_info(column_info=column_info, original_column='radius_error_max', unified_column='pl_radj_err_sup',
                                       description='', unit=uu.R_jup)

def load_db():
    """Load the database exoplanet.et as a DataFrame and return it.
    """
    return pyasl.ExoplanetEU2().getAllDataPandas()
