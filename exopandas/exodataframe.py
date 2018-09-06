from pandas import DataFrame
from pandas.api.types import is_list_like


class ExoDataFrame(DataFrame):
    """ExoDataFrame is a pandas.DataFrame adapted to exoplanet database purposes.

    Implemantation following http://pandas.pydata.org/pandas-docs/stable/extending.html#extending-subclassing-pandas
    and inspired by https://github.com/geopandas/geopandas
    """

    ## Unified column names
    l_unified_col = [  # Names
                     'pl_name', 'st_name',
                     # Planet orbital elements
                     'pl_omega', 'pl_per', 't_ic', 't_tr', 't_peri', 'pl_inc', 'pl_a', 'pl_ecc',
                     # Planet transit parameters
                     'tr_dur', 'b', 'transiting?', 'tr_depth', 'occ_depth', 'pl_aR',
                     # Planet physical parameters
                     'pl_massj', 'pl_msinij', 'pl_mass_orig', 'pl_radj', 'pl_rad_orig',
                     'pl_g', 'pl_rhoj', 'pl_teq',
                     # Stellar physical parameters
                     'st_teff', 'sp_type', 'st_logg', 'st_metal', 'st_mass', 'st_rad', 'st_rho',
                     # Stellar RV parameter
                     'vsini',
                     # Star position in the sky
                     'dec', 'ra', 'pm_ra', 'pm_dec', 'plx',
                     # Star magnitude
                     'mag_opt', 'mag_v',
                     ]

    _metadata = ['_column_info', 'l_unified_col']

    def __init__(self, *args, **kwargs):
        super(ExoDataFrame, self).__init__(*args, **kwargs)
        self._init_column_info()
        self._convert_columns_to_unifiedname()

    @property
    def _constructor(self):
        return ExoDataFrame

    @property
    def column_info(self):
        """Return the dataframe storing the information about the columns"""
        return self._column_info

    def _init_column_info(self):
        """Initialise the DataFrame used for column name conversion and description.
        """
        # Initialise with unified columns
        self._column_info = DataFrame({"unified_colname": self.l_unified_col,
                                       "available": [False for ii in self.l_unified_col],
                                       "original_colname": ["" for ii in self.l_unified_col],
                                       "description": ["" for ii in self.l_unified_col],
                                       "unit": [None for ii in self.l_unified_col]})
        self._add_available_unified_cols()

    def _add_available_unified_cols(self):
        """Add available unified columns.

        Should be overloaded when creating a subclass.
        """
        pass

    def _add_unified_colname(self, unified_colname, original_colname, description="", unit=None):
        """Add a new unified column name to the database.

        :param string unified_colnames: Unified column name. Must be in self.l_unified_col
        :param string original_colnames: Corresponding column name in the database
        :param string description: Description of the column content
        """
        if unified_colname in self.l_unified_col:
            idx = self._get_index_in_column_info(unified_colname, "unified_colname")[0]
            self.column_info.loc[idx, "available"] = True
            self.column_info.loc[idx, "original_colname"] = original_colname
            self.column_info.loc[idx, "description"] = description
            self.column_info.loc[idx, "unit"] = unit
        else:
            raise ValueError("unified_colname {} doesn't not exist.".format(unified_colname))

    def _add_nonunified_colname(self, original_colname, description="", unit=None):
        """Add a new non unified column name to the database.

        :param string original_colnames: Corresponding column name in the database
        :param string description: Description of the column content
        """
        self._column_info = self.column_info.append({"unified_colname": "", "available": True, "original_colname": original_colname,
                                                     "description": description, "unit": unit}, ignore_index=True)

    def _get_index_in_column_info(self, val, col):
        """Return the index of the row where the value of the column col is val in column_info.

        :param val: Value to look for
        :param string col: Column name where to look for val
        :return list_indexes l_idx: list of indexes where val can be found in column col of
            column_info
        """
        return self.column_info.index[self.column_info[col] == val].tolist()

    def _convert_columns_to_unifiedname(self):
        available_original_col = self.column_info.loc[self.column_info["available"]]["original_colname"].values
        available_unified_col = self.column_info.loc[self.column_info["available"]]["unified_colname"].values
        self.rename(columns=dict(zip(available_original_col, available_unified_col)), inplace=True)

    def _get_index_colname_in_column_info(self, colname):
        idx = self._get_index_in_column_info(colname, "unified_colname")
        if len(idx) == 0:
            idx = self._get_index_in_column_info(colname, "original_colname")
        if len(idx) == 0:
            return None
        else:
            return idx[0]

    def get_unit(self, col, squeeze=True, noneifcolnotfound=True):
        """Return the unit corresponding to the columnself.

        :param str/list_of_col col: Database column name(s)
        :param bool squeeze: If true do not return a list if only one element.
        :param bool noneifcolnotfound: If True, when col is not an available column name, the
            function return None, otherwise it raise a ValueError.
        :return astropy.units/list_of_astropy.units db_u: unit corresponding to the colum name. If
            col is not an available column name then return None or raise an error depending on
            noneifcolnotfound.
        """
        if not(is_list_like(col)):
            col = [col, ]
        # Initialise output
        db_u = []
        # For each column name provided as input
        for cl in col:
            idx = self._get_index_colname_in_column_info(cl)
            if idx is None:
                if noneifcolnotfound:
                    db_u.append(idx)
                else:
                    raise ValueError("{} is not an available column name".format(cl))
            else:
                db_u.append(self.column_info.loc[idx, "unit"])
        if len(db_u) == 1 and squeeze:
            return db_u[0]
        else:
            return db_u

    def get_description(self, col, squeeze=True, noneifcolnotfound=True):
        """Return the unit corresponding to the columnself.

        :param str/list_of_col col: Database column name(s)
        :param bool squeeze: If true do not return a list if only one element.
        :param bool noneifcolnotfound: If True, when col is not an available column name, the
            function return None, otherwise it raise a ValueError.
        :return str/list_of_str db_descr: Description corresponding to the colum name. If
            col is not an available column name then return None or raise an error depending on
            noneifcolnotfound.
        """
        if not(is_list_like(col)):
            col = [col, ]
        # Initialise output
        db_descr = []
        # For each column name provided as input
        for cl in col:
            idx = self._get_index_colname_in_column_info(cl)
            if idx is None:
                if noneifcolnotfound:
                    db_descr.append(idx)
                else:
                    raise ValueError("{} is not an available column name".format(cl))
            else:
                db_descr.append(self.column_info.loc[idx, "description"])
        if len(db_descr) == 1 and squeeze:
            return db_descr[0]
        else:
            return db_descr

    def select_opt_mag(self):
        """Select according to star magnitude in the optical bands.
        """
        raise NotImplementedError()

    def is_star_in(self, star):
        """Return True if star is in the database.

        :param string star: Star name
        """
        raise NotImplementedError("You should implement this function in your child class !")

    def get_star_rows(self, star):
        """Return rows for which the host star is star.

        :param string star: Star name
        """
        raise NotImplementedError("You should implement this function in your child class !")

    def get_planet_rows(self, planet):
        """Return the row corresponding to the planet

        :param string planet: Planet name
        """
        raise NotImplementedError("You should implement this function in your child class !")
