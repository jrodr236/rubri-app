# -*- coding: utf-8 -*-
from typing import List

from dades.helper import obtenir_connexio, commit
from logica.entitats import Grau


def obtenir(criteri) -> List[Grau]:
    conn = obtenir_connexio()

    cursor = conn.cursor()

    query = """
        SELECT nom, descripcio, qualificacio
        FROM Grau
        WHERE nom_criteri = %s AND
            nom_rubrica = %s
        ORDER BY qualificacio DESC
    """

    valors = (criteri.nom, criteri.rubrica.nom)
    cursor.execute(query, valors)

    graus = []
    resultat = cursor.fetchall()
    for r in resultat:
        r = Grau(r[0], criteri, r[1], r[2])
        graus.append(r)

    commit(conn, cursor)
    return graus


