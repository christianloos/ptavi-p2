#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import calcoohija
import csv


if __name__ == '__main__':
    calculadora = calcoohija.CalculadoraHija()

    with open(sys.argv[1]) as fichero:
        datos = csv.reader(fichero)

        for operandos in datos:
            operacion = operandos[0]
            operandos = operandos[1:]
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
