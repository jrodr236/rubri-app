# -*- coding: utf-8 -*-
from typing import List

from dades.helper import obtenir_connexio, commit
from logica.entitats import AlumneNivell, Rubrica, Criteri, Nivell, Alumne


def crear(alumne_nivell : AlumneNivell) -> None:
    conn = obtenir_connexio()

    cursor = conn.cursor()

    query = """
        INSERT INTO Alumne_Nivell(cognoms_alumne, nom_alumne, nom_nivell, nom_criteri, nom_rubrica, comentari)
        VALUES (%s, %s, %s, %s, %s, %s)
    """
    valors = (alumne_nivell.alumne.cognoms, alumne_nivell.alumne.nom, alumne_nivell.nivell.nom, alumne_nivell.nivell.criteri.nom, alumne_nivell.nivell.criteri.rubrica.nom, alumne_nivell.comentari)

    cursor.execute(query, valors)

    commit(conn, cursor)


def obtenir() -> List[AlumneNivell]:
    conn = obtenir_connexio()

    cursor = conn.cursor()

    query = """
        SELECT an.cognoms_alumne, an.nom_alumne, an.nom_nivell, n.descripcio, n.qualificacio, an.nom_criteri, c.descripcio, 
            c.pes, an.nom_rubrica, r.descripcio, an.comentari
        FROM Alumne_Nivell an
        LEFT JOIN Nivell n
            ON n.nom = an.nom_nivell
        LEFT JOIN Criteri c
            ON c.nom = n.nom_criteri
        LEFT JOIN Rubrica r
            ON r.nom = an.nom_rubrica
    """

    cursor.execute(query)  # , valors)

    llista_alumne_nivell = []
    resultat = cursor.fetchall()
    for r in resultat:
        rubrica = Rubrica(r[8], r[9])
        criteri = Criteri(r[5], rubrica, r[6], r[7])
        nivell = Nivell(r[2], criteri, r[3], r[4])
        alumne = Alumne(r[0], r[1])
        nivell = AlumneNivell(alumne, nivell, r[10])
        llista_alumne_nivell.append(nivell)

    commit(conn, cursor)
    return llista_alumne_nivell
