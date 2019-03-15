from pandas import DataFrame
import astropy.units as uu

without_unit = "w/o unit"
non_app = "N/A"


def create_empty_column_info():
    """Create an empty column_info DataFrame to be used to define the column of a database.
    """
    return DataFrame({"original_column": [], "unified_column": [], "description": [], "unit": []})


def add_column_2_column_info(column_info, original_column, unified_column="", description="", unit=""):
    """Add a column description on the column_info DataFrame.

    :param DataFrame column_info: Column info DataFrame
    :param str original_column: Original name of the column in the database
    :param str unified_column: Unified name of the column in the database. If this is not provided,
        the column will not be considered an unified column.
    :param str description: Description of the content of the column (without description of the unit).
        If unified column is provided you should not provide this description, since the description
        of the unified column will be used.
    :param str/astropy.Unit unit: Unit of the value in the column. If the values are not number and
        thus do not have units put "N/A". If the values are number without unit put "w/o unit". Not
        providing any unit will prevent proper merging of similar columns.
    """
    if unified_column != "":
        if unified_column not in unified_cols['column'].unique():
            raise ValueError("{} is not the name of a unified column.".format(unified_column))
        idx = unified_cols.index[unified_cols["column"] == unified_column].tolist()
        if len(idx) > 1:
            raise ValueError("There is several occurence of column {} in unified_cols, check it!"
                             "".format(unified_column))
        else:
            idx = idx[0]
        if description != "":
            print("WARNING: For column {} you provided a unified column name, the description provided will be"
                  "ignored and the unified column description will be used instead".format(original_column))
        description = unified_cols.loc[idx, 'description']
        if unit != unified_cols.loc[idx, 'unit']:
            print("WARNING: (column {}) The unit of the unified column in this database is different that it unit "
                  "in the unified_cols dataframe. Right now the unit conversion is not implemented."
                  "".format(original_column))
    return column_info.append({'original_column': original_column, 'unified_column': unified_column,
                               'description': description, 'unit': unit},
                              ignore_index=True)


def create_empty_unified_cols():
    """Create an empty unified_cols DataFrame to be used to define the unified columns.
    """
    return DataFrame({"column": [], "description": [], "unit": []})


def add_column_2_unified_cols(unified_info, column, description, unit):
    """Add a column description on the column_info DataFrame.

    :param DataFrame unified_info: Unified column info DataFrame
    :param str original_column: Original name of the column in the database
    :param str unified_column: Unified name of the column in the database. If this is not provided,
        the column will not be considered an unified column.
    :param str description: Description of the content of the column (without description of the unit).
        If unified column is provided you should not provide this description, since the description
        of the unified column will be used.
    :param str/astropy.Unit unit: Unit of the value in the column. If the values are not number and
        thus do not have units put "N/A". If the values are number without unit put "w/o unit". Not
        providing any unit will prevent proper merging of similar columns.
    """
    return unified_info.append({'column': column, 'description': description, 'unit': unit},
                               ignore_index=True)


unified_cols = create_empty_unified_cols()
# Names
unified_cols = add_column_2_unified_cols(unified_cols, column='st_name', description='Host star name', unit='N/A')
unified_cols = add_column_2_unified_cols(unified_cols, column='pl_name', description='Planet name', unit='N/A')
# Planet orbital elements
unified_cols = add_column_2_unified_cols(unified_cols, column='pl_per', description='Planetary orbital period', unit=uu.d)
unified_cols = add_column_2_unified_cols(unified_cols, column='pl_per_err_inf', description='Inferior error bar on the planetary orbital period', unit=uu.d)
unified_cols = add_column_2_unified_cols(unified_cols, column='pl_per_err_sup', description='Superior error bar on the planetary orbital period', unit=uu.d)
unified_cols = add_column_2_unified_cols(unified_cols, column='pl_omega', description='*Stellar* orbital argument of periastron corresponding to the planetary one', unit=uu.deg)
unified_cols = add_column_2_unified_cols(unified_cols, column='t_ic', description='Planetary time of inferior conjunction', unit=uu.d)
unified_cols = add_column_2_unified_cols(unified_cols, column='t_tr', description='Planetary transit time', unit=uu.d)
unified_cols = add_column_2_unified_cols(unified_cols, column='t_peri', description='Planetary periastron passage', unit=uu.d)
unified_cols = add_column_2_unified_cols(unified_cols, column='pl_inc', description='Planet orbital inclination', unit=uu.deg)
unified_cols = add_column_2_unified_cols(unified_cols, column='pl_a', description='Planet orbital semi-major axis', unit=uu.au)
unified_cols = add_column_2_unified_cols(unified_cols, column='pl_ecc', description='Planetary orbital eccentricity', unit='w/o unit')
# Planet transit parameters
unified_cols = add_column_2_unified_cols(unified_cols, column='tr_dur', description='Planetary transit duration', unit=uu.d)
unified_cols = add_column_2_unified_cols(unified_cols, column='b', description='Planetary impact parameter', unit='w/o unit')
unified_cols = add_column_2_unified_cols(unified_cols, column='transiting?', description='Planet Transit Flag', unit='N/A')
unified_cols = add_column_2_unified_cols(unified_cols, column='tr_depth', description='Planetary transit depth', unit=uu.percent)
unified_cols = add_column_2_unified_cols(unified_cols, column='occ_depth', description='Planetary occultation depth', unit=uu.percent)
unified_cols = add_column_2_unified_cols(unified_cols, column='pl_aR', description='Planetary orbital semi-major axis over the stellar radius', unit='w/o unit')
# Planet physical parameters
unified_cols = add_column_2_unified_cols(unified_cols, column='pl_massj', description='Planetary mass', unit=uu.M_jup)
unified_cols = add_column_2_unified_cols(unified_cols, column='pl_massj_err_inf', description='Inferior error bar on the planetary mass', unit=uu.M_jup)
unified_cols = add_column_2_unified_cols(unified_cols, column='pl_massj_err_sup', description='Superior error bar on the planetary mass', unit=uu.M_jup)
unified_cols = add_column_2_unified_cols(unified_cols, column='pl_msinij', description='Planetary mass multiplied by the sin of the orbital inclination', unit=uu.M_jup)
unified_cols = add_column_2_unified_cols(unified_cols, column='pl_mass_orig', description='Origin of the planetary mass', unit='N/A')
unified_cols = add_column_2_unified_cols(unified_cols, column='pl_radj', description='Planetary radius', unit=uu.R_jup)
unified_cols = add_column_2_unified_cols(unified_cols, column='pl_radj_err_inf', description='Inferior error bar on planetary radius', unit=uu.R_jup)
unified_cols = add_column_2_unified_cols(unified_cols, column='pl_radj_err_sup', description='Superior error bar on planetary radius', unit=uu.R_jup)
unified_cols = add_column_2_unified_cols(unified_cols, column='pl_rad_orig', description='Origin of the planetary radius', unit='N/A')
unified_cols = add_column_2_unified_cols(unified_cols, column='pl_g', description='Planetary surface gravity', unit=uu.m * uu.s**2)
unified_cols = add_column_2_unified_cols(unified_cols, column='pl_rhoj', description='Planetary mean density', unit=uu.M_jup / uu.R_jup**3)
unified_cols = add_column_2_unified_cols(unified_cols, column='pl_teq', description='Planetary equilibrium temperature', unit=uu.K)
# Stellar physical parameters
unified_cols = add_column_2_unified_cols(unified_cols, column='st_teff', description='Stellar effective temperature', unit=uu.K)
unified_cols = add_column_2_unified_cols(unified_cols, column='sp_type', description='Stellar spectral type', unit='N/A')
unified_cols = add_column_2_unified_cols(unified_cols, column='st_logg', description='Stellar log of the surface gravity', unit='dex')
unified_cols = add_column_2_unified_cols(unified_cols, column='st_metal', description='Stellar metallicity', unit='dex')
unified_cols = add_column_2_unified_cols(unified_cols, column='st_mass', description='Stellar mass', unit=uu.M_sun)
unified_cols = add_column_2_unified_cols(unified_cols, column='st_rad', description='Stellar radius', unit=uu.R_sun)
unified_cols = add_column_2_unified_cols(unified_cols, column='st_rho', description='Stellar mean density', unit=uu.M_sun / uu.R_sun**3)
# Stellar RV parameter
unified_cols = add_column_2_unified_cols(unified_cols, column='vsini', description='Stellar radial velocity rotational broadning', unit=uu.km / uu.s)
# Star position in the sky
unified_cols = add_column_2_unified_cols(unified_cols, column='ra', description='Stellar right ascencion (J2000)', unit=uu.deg)
unified_cols = add_column_2_unified_cols(unified_cols, column='dec', description='Stellar declination (J2000)', unit=uu.deg)
unified_cols = add_column_2_unified_cols(unified_cols, column='pm_ra', description='Stellar proper motion in right ascencion', unit=uu.mas / uu.yr)
unified_cols = add_column_2_unified_cols(unified_cols, column='pm_dec', description='Stellar proper motion in declination', unit=uu.mas / uu.yr)
unified_cols = add_column_2_unified_cols(unified_cols, column='plx', description='Stellar parralaxe', unit=uu.mas)
# Star magnitude
unified_cols = add_column_2_unified_cols(unified_cols, column='mag_v', description='Stellar magnitude in the V band', unit=without_unit)
