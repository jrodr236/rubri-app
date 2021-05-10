# -*- coding: utf-8 -*-


from typing import Dict

from logica.claus import CLAU_USUARI_BASE_DE_DADES

mysql_cfg: Dict[str, str] = {'host': 'localhost',
                             'user': 'rubriUserDB',
                             'passwd': CLAU_USUARI_BASE_DE_DADES,
                             'db': 'rubriDB'}
