from numpy import where
from pandas import DataFrame
from pandas.api.types import is_list_like

from .databases.exoplaneteu import column_info as column_info_EU
from .databases.exoplaneteu import load_db as load_db_EU
from .databases.exoplanetarchive import column_info as column_info_EA
from .databases.exoplanetarchive import load_db as load_db_EA
from .databases.sweetcat import column_info as column_info_SC
from .databases.sweetcat import load_db as load_db_SC
from .databases.tepcat import column_info_WS, column_info_Pl, column_info_LS, column_info_HM, column_info_HP, column_info_Ob
from .databases.tepcat import load_db_WS, load_db_Pl, load_db_LS, load_db_HM, load_db_HP, load_db_Ob

dico_databases = {"exoplaneteu": {"column_info": column_info_EU, "load_db": load_db_EU},
                  "exoplanetarchive": {"column_info": column_info_EA, "load_db": load_db_EA},
                  "sweetcat": {"column_info": column_info_SC, "load_db": load_db_SC},
                  "tepcat well-studied": {"column_info": column_info_WS, "load_db": load_db_WS},
                  "tepcat planning": {"column_info": column_info_Pl, "load_db": load_db_Pl},
                  "tepcat little-studied": {"column_info": column_info_LS, "load_db": load_db_LS},
                  "tepcat homogeneous-meas": {"column_info": column_info_HM, "load_db": load_db_HM},
                  "tepcat homogeneous-phys": {"column_info": column_info_HP, "load_db": load_db_HP},
                  "tepcat obliquity": {"column_info": column_info_Ob, "load_db": load_db_Ob},
                  }


class ExoDataFrame(DataFrame):
    """ExoDataFrame is a pandas.DataFrame adapted to exoplanet database purposes.

    Implemantation following http://pandas.pydata.org/pandas-docs/stable/extending.html#extending-subclassing-pandas
    and inspired by https://github.com/geopandas/geopandas
    """

    _metadata = ['_column_info', '_databases_included']

    def __init__(self, *args, **kwargs):
        self._init_column_info()
        self._databases_included = []
        super(ExoDataFrame, self).__init__(*args, **kwargs)

    @property
    def _constructor(self):
        return ExoDataFrame

    @property
    def column_info(self):
        """Dataframe storing the information about the columns"""
        return self._column_info

    @property
    def databases_included(self):
        """List of all database included in this ExoDataFrame"""
        return self._databases_included

    def _init_column_info(self):
        """Initialise the DataFrame used for column name conversion and description.
        """
        # Initialise with unified columns
        self._column_info = DataFrame({"column": [],
                                       "description": [],
                                       "unit": [],
                                       "unified": []})

    def add_column_info(self, column, description, unit, unified):
        """Add the information regarding of a column

        TODO: Check that the types of the unit, description, unified

        :param string column: Column name (must be in self.columns)
        :param string description: Corresponding column name in the database
        :param string/astropy.Unit unit: Description of the column content
        :param bool unified: If True the column is a unified column
        """
        if column not in self.columns:
            raise ValueError("{} is not an existing column !".format(column))
        if column in self.column_info["column"].unique():
            raise ValueError("{} is already in column_info !".format(column))
        self._column_info = self.column_info.append({'column': column, 'description': description, 'unit': unit,
                                                     'unified': unified}, ignore_index=True)

    def _get_index_in_column_info(self, val, col):
        """Return the index of the row where the value of the column col is val in column_info.

        :param val: Value to look for
        :param string col: Column name where to look for val
        :return list_indexes l_idx: list of indexes where val can be found in column col of
            column_info
        """
        return self.column_info.index[self.column_info[col] == val].tolist()

    def _get_index_colname_in_column_info(self, colname):
        idx = self._get_index_in_column_info(colname, "column")
        if len(idx) == 0:
            return None
        else:
            return idx[0]

    def load(self, database, unify=True):
        """Load a database in the current exopandas.

        :param str database: Name of the database you want to load
        :param bool unify: If True the name of the column which can be unified are changed and the
            values are convert in the correct units if necessary/possible
        """
        if len(self) > 0:
            raise ValueError("The instance is not empty, you cannot use the load function. "
                             "Use merge.")
        if database in dico_databases:
            super(ExoDataFrame, self).__init__(dico_databases[database]["load_db"]())
            column_info_db = dico_databases[database]["column_info"]
            array_column_w_info = column_info_db["original_column"].values
            if unify:
                idx = where(column_info_db["unified_column"] != "")[0]
                l_original = list(column_info_db.iloc[idx]["original_column"])
                l_new = list(column_info_db.iloc[idx]["unified_column"])
                if len(idx) > 0:
                    self.rename(columns=dict(zip(l_original, l_new)), inplace=True)
                    array_column_w_info[idx] = l_new
            for column in self.columns:
                if column not in array_column_w_info:
                    self.add_column_info(column=column, description="", unit="", unified=False)
                else:
                    if unify and (column in column_info_db["unified_column"].unique()):
                        idx = column_info_db.index[column_info_db["unified_column"] == column].tolist()[0]
                        unified = True
                    else:
                        idx = column_info_db.index[column_info_db["original_column"] == column].tolist()[0]
                        unified = False
                    self.add_column_info(column=column, description=column_info_db.loc[idx, "description"],
                                         unit=column_info_db.loc[idx, "unit"], unified=unified)
        else:
            raise ValueError("{} is not an existing database.".format(database))
        self._databases_included.append(database)

    def merge(self, database, unify=True, kwargs_merge_db={}, kwargs_merge_col={}):
        """Include the data from another database.

        :param str database: Name of the database you want to add
        :param bool unify: If True the name of the column which can be unified are changed and the
            values are convert in the correct units if necessary/possible
        :param dict kwargs_merge_db: Dictionary of keyword arguments passed to the pandas.merge function
        :param dict kwargs_merge_col: Dictionary of keyword which define the behavior of the overlapping
            column merging
        """
        # Provide some default values for some of the kwargs_merge_db arguments.
        if ((kwargs_merge_db.get("on", None) is None) and (kwargs_merge_db.get("left_on", None) is None) and
           not(kwargs_merge_db.get("left_index", False))):
            kwargs_merge_db["on"] = 'pl_name'
        kwargs_merge_db["how"] = kwargs_merge_db.get("how", "outer")
        # Check that you are not trying to include a database which is already there.
        if database in self.databases_included:
            raise ValueError("database {} is already included in the ExoDataFrame.".format(database))
        # Load the other database
        db = ExoDataFrame()
        db.load(database, unify=unify)
        # Merge the two databases
        res = super(ExoDataFrame, self).merge(db, **kwargs_merge_db)
        # Merge the two column_info
        suffixes = kwargs_merge_db.get("suffixes", ('_x', '_y'))
        res._column_info = self.column_info.merge(db.column_info, on="column", how="outer", suffixes=suffixes)
        res._databases_included = self._databases_included + db._databases_included
        # TODO:
        # Merge columns of the column_info and the databases
        # The merging process of the column_info should tell you if you can merge the column of the
        # database. For example if pl_radj exist in both database and unit has the same value, then
        # then can safely be merged in one column. Otherwise you should create two lines column_info
        # with the two different suffixes.
        # If think that you only need to compare the unit, because if the name is the same, the descriptions
        # should be the same. So don't check and use the description of the current database.
        # If pl_radj exist but with different units then you should merge them is you can performe
        # the unit convertion.
        # If pl_radj exist only in one database, then the merging trivialself.
        # Once you know which column can be merge, you need to define what the rules of the database
        # column merging. 1. If you need a unit conversion: do you want to perform the conversion, or
        # keep the two columns with their different unit. If you which to perform the unit conversion,
        # which unit to use: You can decise to use the left or right database unit or specify it on a case by case.
        # Then when a mergin of columns should be made and the two columns have at least one row with
        # two different values, what do you do ?: keep the two columns  from the two databases or use
        # one database over the other.
        return res

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
