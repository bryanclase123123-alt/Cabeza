x= int(input ("Introduce un numero"));
y= int(input ("Introduce otro numero"));
operacion = '1';
while (operacion != '0'):
    print ("Seleeciona una operacion:");
    print ("1. Suma");
    print ("2. Resta");
    print ("3. Multiplicacion");
    print ("4. Division");
    print ("0. Salir");
    operacion = input ("Ingresa el numero de la operacion: ");

    if (operacion == '1'):
        # Operacion Suma
        suma = x + y;
        print ("Total = ", suma);
    elif (operacion == '2'):
        #Operacion Resta
        resta = x - y;
        print ("Total resta =", resta);
    elif (operacion == '3'):
        #Operacion Multiplicacion
        multiplicacion = x * y;
        print ("Total multiplicacion", multiplicacion);
    elif (operacion == '4'):
        #Operacion Division
        division = x / y;
        print ("Total division = ", division);