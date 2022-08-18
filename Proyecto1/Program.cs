﻿using System;
 
class GFG{
 
// Funcion para generar numeros random
static void metodoLinealCongruencial(double Xo, double m,
                                     double a, double c,
                                     double[] randomNums,
                                     int noOfRandomNums)
{
     
    // Inicialzar con el valor semilla
    randomNums[0] = Xo;
 
    // interacion para todos los numeros requeridos
    for(int i = 1; i < noOfRandomNums; i++)
    {
         
        // seguir el metodo lineal congruencial
        randomNums[i] = (((randomNums[i - 1] * a) + c) % m) / ((randomNums[i - 1] * a) + c);
    }
}
 
// funcion main
public static void Main(String[] args)
{
     
    // Semilla
    double Xo = 6.0000;
     
    // Modulus
    double m = 80.0000;
     
    // Multiplicador
    double a = 32.0000;
     
    // Incremento
    double c = 3.0000;
     
    // Numero de numeros random
    // a generar
    int noOfRandomNums = 10;
     
    // guardar los numeros random
    double[] randomNums = new double[noOfRandomNums];
     
    // llamar la funcion
    metodoLinealCongruencial(Xo, m, a, c,
                             randomNums,
                             noOfRandomNums);
     
    // imprimir los numeros generados
    for(int i = 0; i < noOfRandomNums; i++)
    {
        Console.Write(randomNums[i] + " ");
    }
}
}