#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import calcoohija


if __name__ == '__main__':

    calculadora = calcoohija.CalculadoraHija()

    fichero = open(sys.argv[1], 'r')
    lineas = fichero.readlines()

    for linea in lineas:
        operandos = linea.split(',')
        operacion = operandos[0]
        operandos = operandos[1:]
        operandos[-1] = operandos[-1][:-1]
        result = int(operandos[0])
        operandos = operandos[1:]

        for operando in operandos:
            if operacion == "suma":
                result = calculadora.plus(result, int(operando))
            elif operacion == "resta":
                result = calculadora.minus(result, int(operando))
            elif operacion == "multiplica":
                result = calculadora.multiply(result, int(operando))
            elif operacion == "divide":
                try:
                    result = calculadora.divide(result, int(operando))
                except ZeroDivisionError:
                    sys.exit("Division by zero is not allowed")
            else:
                sys.exit('Operación sólo puede ser sumar, restar,'
                         'multiplicar o dividir')
        print(result)
