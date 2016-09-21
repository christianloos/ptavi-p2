#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

class CalculadoraHija(Calculadora):

    def __init__(self, op1, op2):
        self.op1 = op1
        self.op2 = op2

    def multiply(self, op1, op2):
        return op1 * op2
    
    def divide(self, op1, op2):
        return op1 / op2

if __name__ == "__main__":
    Calculadora = CalculadoraHija(op1,op2)

    try: 
        operando1 = int(sys.argv[1])
        operando2 = int(sys.argv[3])
    except ValueError:
        sys.exit("Error: Non numerical parameters")

    if sys.argv[2] == "multiplica":
        result = hija.multiply(operando1, operando2)
    elif sys.argv[2] == "divide":
        result = hija.divide(operando1, operando2)

    else:
        sys.exit('Operación sólo puede ser sumar, restar, multiplicar o dividir')

    print(result)

    

