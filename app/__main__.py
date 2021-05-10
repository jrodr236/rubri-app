#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from dades import rubrica_dao, alumne_dao, criteri_dao, grau_dao, nivell_dao
from logica.entitats import Nivell
from presentacio.general import mostrar, escollir, demanar_comentari, capcalera


def main():
    capcalera("Nivells")
    nivells = nivell_dao.obtenir()
    mostrar(nivells)

    capcalera("Alumnes")
    alumnes = alumne_dao.obtenir()
    mostrar(alumnes)
    alumne_escollit = escollir(alumnes)

    capcalera("Rúbriques")
    rubriques = rubrica_dao.obtenir(alumne_escollit)
    mostrar(rubriques)
    rubrica_escollida = escollir(rubriques)

    capcalera("Criteris")
    criteris = criteri_dao.obtenir(rubrica_escollida)
    mostrar(criteris)
    criteri_escollit = escollir(criteris)

    capcalera("Graus")
    graus = grau_dao.obtenir(criteri_escollit)
    mostrar(graus)
    grau_escollit = escollir(graus)

    comentari = demanar_comentari()
    nou_nivell = Nivell(alumne_escollit, grau_escollit, comentari)
    nivell_dao.crear(nou_nivell)

    capcalera("Nivells")
    nivells = nivell_dao.obtenir()
    mostrar(nivells)


if __name__ == "__main__":
    main()

