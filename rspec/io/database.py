from collections import MutableMapping
import logging
import os.path
from os.path import expanduser, join

import numpy as np
import pandas as pd
from sqlalchemy import create_engine, inspect

logger = logging.getLogger(__name__)

class Database(MutableMapping):
    def __init__(self, path=None):
        if not path:
            path = os.path.join(expanduser("~"), "compounds.db")
        self._path = path

        self._conn = None
        self._spectrum = dict()

    def __delitem__(self):
        pass

    def __enter__(self):
        engine = create_engine("sqlite:///{}".format(self._path))
        self._conn = engine.connect()

        inspector = inspect(engine)
        compounds = inspector.get_table_names()
        logger.info(
            "found {} compound(s) in the database".format(len(compounds))
        )
        for compound in compounds:
            self._spectrum[compound] = pd.read_sql_table(compound, self._conn)
        
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        self._conn.close()

    def __getitem__(self, key):
        return self._spectrum[key]

    def __iter__(self):
        return iter(self._spectrum)

    def __len__(self):
        return len(self._spectrum)

    def __setitem__(self, key, value):
        if key in self._spectrum:
            raise KeyError("compound \"{}\" exists".format(key))
        elif not isinstance(value, pd.DataFrame):
            raise ValueError("not a DataFrame")

        # save to in-memory database
        self._spectrum[key] = value
        # save to file
        value.to_sql(key, self._conn, if_exists='fail')

    