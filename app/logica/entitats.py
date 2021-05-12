# -*- coding: utf-8 -*-

class Alumne:

    def __init__(self, cognoms : str, nom: str):
        self.cognoms = cognoms
        self.nom = nom

    def __str__(self):
        return "{}, {}".format(self.cognoms, self.nom)


class Rubrica:
    def __init__(self, nom : str, descripcio : str):
        self.nom = nom
        self.descripcio = descripcio

    def __str__(self):
        return "{} ({})".format(self.nom, self.descripcio)


class Criteri:
    def __init__(self, nom : str, rubrica : Rubrica, descripcio : str, pes : int):
        self.nom = nom
        self.rubrica = rubrica
        self.descripcio = descripcio
        self.pes = pes

    def __str__(self):
        return "{} ({}). Pes={}".format(self.nom, self.descripcio, self.pes)


class Nivell:
    def __init__(self, nom : str, criteri : Criteri, descripcio : str, qualificacio : int):
        self.nom = nom
        self.criteri = criteri
        self.descripcio = descripcio
        self.qualificacio = qualificacio

    def __str__(self):
        return "{} ({}). Qualificacio={}".format(self.nom, self.descripcio, self.qualificacio)


class AlumneNivell:
    def __init__(self, alumne : Alumne, nivell : Nivell, comentari : str):
        self.alumne = alumne
        self.nivell = nivell
        self.comentari = comentari

    def __str__(self):
        return "{}\n" \
               "     {}\n" \
               "     {}\n" \
               "     {}\n" \
               "     ({})".format(self.alumne, self.nivell.criteri.rubrica, self.nivell.criteri, self.nivell, self.comentari)
