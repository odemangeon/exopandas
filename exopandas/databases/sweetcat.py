import astropy.units as uu
from PyAstronomy.pyasl import SWEETCat

from .column_info import create_empty_column_info, add_column_2_column_info, non_app, without_unit


column_info = create_empty_column_info()
column_info = add_column_2_column_info(column_info=column_info, original_column='star', unified_column='st_name',
                                       description='', unit=non_app)
column_info = add_column_2_column_info(column_info=column_info, original_column='mass', unified_column='st_mass',
                                       description='', unit=uu.M_sun)
column_info = add_column_2_column_info(column_info=column_info, original_column='teff', unified_column='st_teff',
                                       description='', unit=uu.K)
column_info = add_column_2_column_info(column_info=column_info, original_column='metal', unified_column='st_metal',
                                       description='', unit='dex')
column_info = add_column_2_column_info(column_info=column_info, original_column='logg', unified_column='st_logg',
                                       description='', unit='dex')
column_info = add_column_2_column_info(column_info=column_info, original_column='vmag', unified_column='mag_v',
                                       description='', unit=without_unit)
column_info = add_column_2_column_info(column_info=column_info, original_column='ra', unified_column='ra',
                                       description='', unit=uu.deg)
column_info = add_column_2_column_info(column_info=column_info, original_column='dec', unified_column='dec',
                                       description='', unit=uu.deg)
column_info = add_column_2_column_info(column_info=column_info, original_column='par', unified_column='plx',
                                       description='', unit=uu.mas)


def load_db():
    """Load the database exoplanet.et as a DataFrame and return it.
    """
    return SWEETCat().data
