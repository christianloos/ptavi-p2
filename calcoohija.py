#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import calcoo

class CalculadoraHija(Calculadora):

    def __init__(self, op1, op2):
        self.op1 = op1
        self.op2 = op2

    def multiply(self, op1, op2):
        return op1 * op2
    
    def divide(self, op1, op2):
        return op1 / op2

if __name__ == "__main__":
    CalculadoraHija = CalculadoraHija()

    try: 
        operando1 = int(sys.argv[1])
        operando2 = int(sys.argv[3])
    except ValueError:
        sys.exit("Error: Non numerical parameters")

    if sys.argv[2] == "suma":
        result = CalculadoraHija.plus(operando1, operando2)
    elif sys.argv[2] == "resta":
        result = CalculadoraHija.minus(operando1, operando2)
    elif sys.argv[2] == "multiplica":
        result = CalculadoraHija.multiply(operando1, operando2)
    elif sys.argv[2] == "divide":
        try:        
            result = CalculadoraHija.divide(operando1, operando2)
        except ZeroDivisionError:
            sys.exit("Division by zero is not allowed")

    else:
        sys.exit('Operación sólo puede ser sumar, restar, multiplicar o dividir')

    print(result)

    

