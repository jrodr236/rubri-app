# -*- coding: utf-8 -*-

def mostrar(llista):
    for i, elem in enumerate(llista):
        print("- {}. {}".format(i+1, elem))


def escollir(llista):
    posicio_escollida = int(input("Escull: "))
    item_escollit = llista[posicio_escollida - 1]
    print("Has escollit: {}".format(item_escollit))
    return item_escollit


def demanar_comentari() -> str:
    return input("Comentari: ")


def capcalera(concepte):
    print("\n{}".format(concepte))
    print("-----------------------------")
