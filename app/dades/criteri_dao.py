# -*- coding: utf-8 -*-
from typing import List

from dades.helper import obtenir_connexio, commit
from logica.entitats import Criteri


def obtenir(rubrica) -> List[Criteri]:
    conn = obtenir_connexio()

    cursor = conn.cursor()

    query = """
        SELECT nom, descripcio, pes
        FROM Criteri
        WHERE nom_rubrica = %s
    """

    valors = (rubrica.nom, )
    cursor.execute(query, valors)

    criteris = []
    resultat = cursor.fetchall()
    for r in resultat:
        r = Criteri(r[0], rubrica, r[1], r[2])
        criteris.append(r)

    commit(conn, cursor)
    return criteris


