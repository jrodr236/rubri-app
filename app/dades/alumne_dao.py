# -*- coding: utf-8 -*-
from dades.helper import obtenir_connexio, commit

from typing import List

from logica.entitats import Alumne


def obtenir() -> List[Alumne]:
    conn = obtenir_connexio()

    cursor = conn.cursor()

    query = """
        SELECT cognoms, nom
        FROM Alumne 
    """

    cursor.execute(query)  # , valors)

    alumnes = []
    resultat = cursor.fetchall()
    for r in resultat:
        a = Alumne(r[0], r[1])
        alumnes.append(a)

    commit(conn, cursor)
    return alumnes
