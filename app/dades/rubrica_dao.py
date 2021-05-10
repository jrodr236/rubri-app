# -*- coding: utf-8 -*-
from dades.helper import obtenir_connexio, commit

from typing import List

from logica.entitats import Rubrica

def obtenir(alumne) -> List[Rubrica]:
    conn = obtenir_connexio()

    cursor = conn.cursor()

    query = """
        SELECT a.nom_rubrica, r.descripcio
        FROM Avalua a
            INNER JOIN Rubrica r
            ON r.nom = a.nom_rubrica
        WHERE a.cognoms_alumne = %s
            AND a.nom_alumne = %s     
    """

    valors = (alumne.cognoms, alumne.nom)
    cursor.execute(query, valors)

    rubriques = []
    resultat = cursor.fetchall()
    for r in resultat:
        rub = Rubrica(r[0], r[1])
        rubriques.append(rub)

    commit(conn, cursor)
    return rubriques
