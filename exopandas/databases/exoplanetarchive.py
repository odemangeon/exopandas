from os.path import expanduser

from pandas import read_csv
import astropy.units as uu

from .column_info import create_empty_column_info, add_column_2_column_info, non_app, without_unit


column_info = create_empty_column_info()
column_info = add_column_2_column_info(column_info=column_info, original_column='pl_hostname', unified_column='st_name',
                                       description='', unit=non_app)
column_info = add_column_2_column_info(column_info=column_info, original_column='pl_name', unified_column='pl_name',
                                       description='', unit=non_app)
column_info = add_column_2_column_info(column_info=column_info, original_column='pl_orbper', unified_column='pl_per',
                                       description='', unit=uu.d)
column_info = add_column_2_column_info(column_info=column_info, original_column='tzero_tr', unified_column='t_tr',
                                       description='', unit=uu.d)
column_info = add_column_2_column_info(column_info=column_info, original_column='tperi', unified_column='t_peri',
                                       description='', unit=uu.d)
column_info = add_column_2_column_info(column_info=column_info, original_column='pl_tranmid', unified_column='t_ic',
                                       description='', unit=uu.d)
column_info = add_column_2_column_info(column_info=column_info, original_column='pl_orbincl', unified_column='pl_inc',
                                       description='', unit=uu.deg)
column_info = add_column_2_column_info(column_info=column_info, original_column='pl_orbsmax', unified_column='pl_a',
                                       description='', unit=uu.au)
column_info = add_column_2_column_info(column_info=column_info, original_column='pl_tranflag', unified_column='transiting?',
                                       description='', unit=non_app)
column_info = add_column_2_column_info(column_info=column_info, original_column='pl_trandur', unified_column='tr_dur',
                                       description='', unit=uu.d)
column_info = add_column_2_column_info(column_info=column_info, original_column='pl_trandep', unified_column='tr_depth',
                                       description='', unit=uu.percent)
column_info = add_column_2_column_info(column_info=column_info, original_column='pl_occdep', unified_column='occ_depth',
                                       description='', unit=uu.percent)
column_info = add_column_2_column_info(column_info=column_info, original_column='pl_imppar', unified_column='b',
                                       description='', unit=without_unit)
column_info = add_column_2_column_info(column_info=column_info, original_column='pl_ratdor', unified_column='pl_aR',
                                       description='', unit=without_unit)
column_info = add_column_2_column_info(column_info=column_info, original_column='pl_radj', unified_column='pl_radj',
                                       description='', unit=uu.R_jup)
column_info = add_column_2_column_info(column_info=column_info, original_column='radius_detection_type', unified_column='pl_rad_orig',
                                       description='', unit=non_app)
column_info = add_column_2_column_info(column_info=column_info, original_column='pl_massj', unified_column='pl_massj',
                                       description='', unit=uu.M_jup)
column_info = add_column_2_column_info(column_info=column_info, original_column='mass_sini', unified_column='pl_msinij',
                                       description='', unit=uu.M_jup)
column_info = add_column_2_column_info(column_info=column_info, original_column='pl_bmassprov', unified_column='pl_rad_orig',
                                       description='', unit=non_app)
column_info = add_column_2_column_info(column_info=column_info, original_column='pl_eqt', unified_column='pl_teq',
                                       description='', unit=uu.K)
column_info = add_column_2_column_info(column_info=column_info, original_column='st_rad', unified_column='st_rad',
                                       description='', unit=uu.R_sun)
column_info = add_column_2_column_info(column_info=column_info, original_column='st_mass', unified_column='st_mass',
                                       description='', unit=uu.M_sun)
column_info = add_column_2_column_info(column_info=column_info, original_column='st_teff', unified_column='st_teff',
                                       description='', unit=uu.K)
column_info = add_column_2_column_info(column_info=column_info, original_column='st_vsini', unified_column='vsini',
                                       description='', unit=uu.km / uu.s)
column_info = add_column_2_column_info(column_info=column_info, original_column='st_spstr', unified_column='sp_type',
                                       description='', unit=non_app)
column_info = add_column_2_column_info(column_info=column_info, original_column='st_vj', unified_column='mag_v',
                                       description='', unit=without_unit)
column_info = add_column_2_column_info(column_info=column_info, original_column='ra', unified_column='ra',
                                       description='', unit=uu.deg)
column_info = add_column_2_column_info(column_info=column_info, original_column='dec', unified_column='dec',
                                       description='', unit=uu.deg)
column_info = add_column_2_column_info(column_info=column_info, original_column='st_plx', unified_column='plx',
                                       description='', unit=uu.mas)
column_info = add_column_2_column_info(column_info=column_info, original_column='st_pmra', unified_column='pm_ra',
                                       description='', unit=uu.mas / uu.yr)
column_info = add_column_2_column_info(column_info=column_info, original_column='st_pmdec', unified_column='pm_dec',
                                       description='', unit=uu.mas / uu.yr)


def load_db():
    """Load the database exoplanet.et as a DataFrame and return it.
    """
    return read_csv(expanduser("~/Data/exoplanet_database/exoplanet_archive/planets.csv"),
                    comment="#")
