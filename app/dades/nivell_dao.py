# -*- coding: utf-8 -*-
from typing import List

from dades.helper import obtenir_connexio, commit
from logica.entitats import Nivell


def obtenir(criteri) -> List[Nivell]:
    conn = obtenir_connexio()

    cursor = conn.cursor()

    query = """
        SELECT nom, descripcio, qualificacio
        FROM Nivell
        WHERE nom_criteri = %s AND
            nom_rubrica = %s
        ORDER BY qualificacio DESC
    """

    valors = (criteri.nom, criteri.rubrica.nom)
    cursor.execute(query, valors)

    nivells = []
    resultat = cursor.fetchall()
    for r in resultat:
        r = Nivell(r[0], criteri, r[1], r[2])
        nivells.append(r)

    commit(conn, cursor)
    return nivells


