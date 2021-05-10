# -*- coding: utf-8 -*-
from typing import List

from dades.helper import obtenir_connexio, commit
from logica.entitats import Nivell, Rubrica, Criteri, Grau, Alumne


def crear(nivell : Nivell) -> None:
    conn = obtenir_connexio()

    cursor = conn.cursor()

    query = """
        INSERT INTO Nivell(cognoms_alumne, nom_alumne, nom_grau, nom_criteri, nom_rubrica, comentari)
        VALUES (%s, %s, %s, %s, %s, %s)
    """
    valors = (nivell.alumne.cognoms, nivell.alumne.nom, nivell.grau.nom, nivell.grau.criteri.nom, nivell.grau.criteri.rubrica.nom, nivell.comentari)

    cursor.execute(query, valors)

    commit(conn, cursor)


def obtenir() -> List[Nivell]:
    conn = obtenir_connexio()

    cursor = conn.cursor()

    query = """
        SELECT n.cognoms_alumne, n.nom_alumne, n.nom_grau, g.descripcio, g.qualificacio, n.nom_criteri, c.descripcio, 
            c.pes, n.nom_rubrica, r.descripcio, n.comentari
        FROM Nivell n
        LEFT JOIN Grau g
            ON g.nom = n.nom_grau
        LEFT JOIN Criteri c
            ON c.nom = n.nom_criteri
        LEFT JOIN Rubrica r
            ON r.nom = n.nom_rubrica
    """

    cursor.execute(query)  # , valors)

    nivells = []
    resultat = cursor.fetchall()
    for r in resultat:
        rubrica = Rubrica(r[8], r[9])
        criteri = Criteri(r[5], rubrica, r[6], r[7])
        grau = Grau(r[2], criteri, r[3], r[4])
        alumne = Alumne(r[0], r[1])
        nivell = Nivell(alumne, grau, r[10])
        nivells.append(nivell)

    commit(conn, cursor)
    return nivells
