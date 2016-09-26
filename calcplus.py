#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import calcoohija

if __name__ == '__main__':
    
    fichero = open('operaciones', 'r')
    
    lineas = fichero.readlines()
    
    calculadora = calcoohija.CalculadoraHija()
    
    diccionario = {'suma': calculadora.plus, 'resta': calculadora.minus, 'multiplica': calculadora.multiply, 'divide': calculadora.divide}
    
    for linea in lineas:
    
        elementos_lista = linea.split(',') #separamos la lista mediante comas
        operandos = elementos_lista [1:] #seleccionamos los operandos
        operandos[-1] = operandos[-1][:-1] #eliminamos \n
        operacion = elementos_lista[0] #seleccionamos la operacion
        
        
        
        
        
        
