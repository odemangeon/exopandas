from os.path import expanduser, join

from pandas import read_table
import astropy.units as uu

from .column_info import create_empty_column_info, add_column_2_column_info, non_app, without_unit


database_main_folder = expanduser("~/Data/exoplanet_database/TEPCat")


## TEPCat well-studied
column_info_WS = create_empty_column_info()
# TODO: Actually the System column is a mix of Star and planet name. Try to find a solution to this
column_info_WS = add_column_2_column_info(column_info=column_info_WS, original_column='System', unified_column='pl_name',
                                          description='', unit=non_app)
column_info_WS = add_column_2_column_info(column_info=column_info_WS, original_column='Period', unified_column='pl_per',
                                          description='', unit=uu.d)
column_info_WS = add_column_2_column_info(column_info=column_info_WS, original_column='semi_major_axis', unified_column='pl_a',
                                          description='', unit=uu.au)
column_info_WS = add_column_2_column_info(column_info=column_info_WS, original_column='R_b', unified_column='pl_radj',
                                          description='', unit=uu.R_jup)
column_info_WS = add_column_2_column_info(column_info=column_info_WS, original_column='M_b', unified_column='pl_massj',
                                          description='', unit=uu.M_jup)
column_info_WS = add_column_2_column_info(column_info=column_info_WS, original_column='rho_b', unified_column='pl_rhoj',
                                          description='', unit=uu.M_jup / uu.R_jup**3)
column_info_WS = add_column_2_column_info(column_info=column_info_WS, original_column='g_b', unified_column='pl_g',
                                          description='', unit=uu.m * uu.s**2)
column_info_WS = add_column_2_column_info(column_info=column_info_WS, original_column='dec', unified_column='dec',
                                          description='', unit=uu.deg)
column_info_WS = add_column_2_column_info(column_info=column_info_WS, original_column='Teq', unified_column='pl_teq',
                                          description='', unit=uu.K)
column_info_WS = add_column_2_column_info(column_info=column_info_WS, original_column='R_A', unified_column='st_rad',
                                          description='', unit=uu.R_sun)
column_info_WS = add_column_2_column_info(column_info=column_info_WS, original_column='M_A', unified_column='st_mass',
                                          description='', unit=uu.M_sun)
column_info_WS = add_column_2_column_info(column_info=column_info_WS, original_column='loggA', unified_column='st_logg',
                                          description='', unit="dex")
column_info_WS = add_column_2_column_info(column_info=column_info_WS, original_column='Teff', unified_column='st_teff',
                                          description='', unit=uu.K)
column_info_WS = add_column_2_column_info(column_info=column_info_WS, original_column='[Fe/H]', unified_column='st_metal',
                                          description='', unit="dex")
column_info_WS = add_column_2_column_info(column_info=column_info_WS, original_column='rho_A', unified_column='st_rho',
                                          description='', unit=uu.M_sun / uu.R_sun**3)


def load_db_WS():
    """Load the database TEPCat well-studied as a DataFrame and return it.
    """
    cols = ['System', 'Teff', 'Teff_erru', 'Teff_errd', '[Fe/H]', '[Fe/H]_erru', '[Fe/H]_errd',
            'M_A', 'M_A_erru', 'M_A_errd', 'R_A', 'R_A_erru', 'R_A_errd', 'loggA', 'loggA_erru',
            'loggA_errd', 'rho_A', 'rho_A_erru', 'rho_A_errd', 'Period', 'Period_err', 'Period_erru',
            'Period_errd', 'a(AU)', 'a(AU)_erru', 'a(AU)_errd', 'M_b', 'M_b_erru', 'M_b_errd',
            'R_b', 'R_b_erru', 'R_b_errd', 'g_b', 'g_b_erru', 'g_b_errd', 'rho_b', 'rho_b_erru',
            'rho_b_errd', 'Teq', 'Teq_erru', 'Teq_errd', 'Discovery_reference', 'Recent_reference']
    db = read_table(join(database_main_folder, "well-studied/allplanets-csv.csv"), header=None, skiprows=[0],
                    names=cols, sep=',', skipinitialspace=True)
    for col in ["System", "Discovery_reference", "Recent_reference"]:
        if col in db.columns:
            db[col] = db[col].str.strip()
    return db


## TEPCat planning
column_info_Pl = create_empty_column_info()
# TODO: Actually the System column is a mix of Star and planet name. Try to find a solution to this
column_info_Pl = add_column_2_column_info(column_info=column_info_Pl, original_column='System', unified_column='pl_name',
                                          description='', unit=non_app)
column_info_Pl = add_column_2_column_info(column_info=column_info_Pl, original_column='Period', unified_column='pl_per',
                                          description='', unit=uu.d)
column_info_Pl = add_column_2_column_info(column_info=column_info_Pl, original_column='T0 (HJD or BJD)', unified_column='t_tr',
                                          description='', unit=uu.d)
column_info_Pl = add_column_2_column_info(column_info=column_info_Pl, original_column='length', unified_column='tr_dur',
                                          description='', unit=uu.d)


def load_db_Pl():
    """Load the database TEPCat planning as a DataFrame and return it.
    """
    cols = ['System', 'Type', 'RA_h', 'RA_m', 'RA_s', 'Dec_d', 'Dec_m', 'Dec_s', 'V_mag', 'K_mag',
            'length', 'depth', 'T0 (HJD or BJD)', 'T0_err', 'Period(day)', 'Period_err', 'Ephemeris_reference']
    db = read_table(join(database_main_folder, "obs_planning/observables.csv"), header=None, skiprows=[0],
                    names=cols, sep=',', skipinitialspace=True)
    for col in ["System", "Discovery_reference", "Recent_reference"]:
        if col in db.columns:
            db[col] = db[col].str.strip()
    return db


## TEPCat little-studied

column_info_LS = create_empty_column_info()


def load_db_LS():
    """Load the database TEPCat little-studied as a DataFrame and return it.
    """
    # TODO: Not Sure the this list of Columns is the good one.
    cols = ['System', 'Teff', 'Teff_erru', 'Teff_errd', '[Fe/H]', '[Fe/H]_erru', '[Fe/H]_errd',
            'M_A', 'M_A_erru', 'M_A_errd', 'R_A', 'R_A_erru', 'R_A_errd', 'loggA', 'loggA_erru',
            'loggA_errd', 'rho_A', 'rho_A_erru', 'rho_A_errd', 'Period', 'Period_err', 'Period_erru',
            'Period_errd', 'a(AU)', 'a(AU)_erru', 'a(AU)_errd', 'M_b', 'M_b_erru', 'M_b_errd',
            'R_b', 'R_b_erru', 'R_b_errd', 'g_b', 'g_b_erru', 'g_b_errd', 'rho_b', 'rho_b_erru',
            'rho_b_errd', 'Teq', 'Teq_erru', 'Teq_errd', 'Discovery_reference', 'Recent_reference']
    db = read_table(join(database_main_folder, "well-studied/kepplanets-csv.csv"), header=None, skiprows=[0],
                    names=cols, sep=',', skipinitialspace=True)
    for col in ["System", "Discovery_reference", "Recent_reference"]:
        if col in db.columns:
            db[col] = db[col].str.strip()
    return db


## TEPCat homogeneous-meas

column_info_HM = create_empty_column_info()


def load_db_HM():
    """Load the database TEPCat homogeneous-meas as a DataFrame and return it.
    """
    # TODO: Do list of columns
    cols = None
    db = read_table(join(database_main_folder, "homogeneous/homogeneous-input-csv.csv"), header=None, skiprows=[0],
                    names=cols, sep=',', skipinitialspace=True)
    for col in ["System", "Discovery_reference", "Recent_reference"]:
        if col in db.columns:
            db[col] = db[col].str.strip()
    return db


## TEPCat homogeneous-phys

column_info_HP = create_empty_column_info()


def load_db_HP():
    """Load the database TEPCat homogeneous-phys as a DataFrame and return it.
    """
    # TODO: Do list of columns
    cols = None
    db = read_table(join(database_main_folder, "homogeneous/homogeneous-par-csv.csv"), header=None, skiprows=[0],
                    names=cols, sep=',', skipinitialspace=True)
    for col in ["System", "Discovery_reference", "Recent_reference"]:
        if col in db.columns:
            db[col] = db[col].str.strip()
    return db


## TEPCat obliquity

column_info_Ob = create_empty_column_info()


def load_db_Ob():
    """Load the database TEPCat obliquity as a DataFrame and return it.
    """
    # TODO: Do list of columns
    cols = None
    db = read_table(join(database_main_folder, "obliquity/obliquity.csv"), header=None, skiprows=[0],
                    names=cols, sep=',', skipinitialspace=True)
    for col in ["System", "Discovery_reference", "Recent_reference"]:
        if col in db.columns:
            db[col] = db[col].str.strip()
    return db
