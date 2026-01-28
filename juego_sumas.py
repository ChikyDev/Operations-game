'''Juego de operaciones'''

#Para usar este juego deberas de tener instalado python en tu ordenador
# 1. paso, abrir Simbolo del sistema
# 2. paso, buscamos el archivo donde se haya guardado
# 3. paso, ejecutamos con python3 juego_sumas.py o si tienes una version mas antigua de python usaremos, python2 o python juego_sumas.py#



import random #Importamos la libreria random, ya que queremos que se generen numeros aleatorios para este juego
import sys #Importamos la librearia de sys para poder finalizar y controlar los bucles, asi sabremos cuando sale del programa


vida = 5 #Datos del juego tanto vidas como nivel
nivel = 1

while True: #Bucle que se encarga de mandar la pregunta hasta que se acierte el resultado

    print('Este juego se debera adivinar el numero sumando la cantidad que marque, tendras 5 vidas y hay 6 niveles, buena suerte ​🤗​')
    inicio = input('Empezamos?: ')

    inicio = inicio.lower()

    if inicio in ['si', 'venga','okay']:
        print('Buena suerte ​😎​')
        break #El bucle se cierra aqui ya que el usuario confirma si decide jugar o no
    elif inicio == 'no':
        print('Lo dejamos para otra vez 🫡​')
        sys.exit() #Mismo bucle que se cierra, solo que esta vez es si el usuario decide no jugar
        
    #SUMA ⬇️

while True:
    num1 = random.randint(1, 1000) #Variable con librería random, del 1 al 1000
    num2 = random.randint(1, 100) # Variable co valor de 1 a 100 por terminos de logica

    print(f'\nNivel {nivel}') #Esto lo que muestra es el nivel en el que se encuentra el usuario
    print(f'Cuanto es {num1} + {num2}?') #Esta es la pregunta que le sale al usuario, para sumar los dos numeros 

    respuesta = input('Cual es el resultado: ')

    if not respuesta.isdigit(): ##Lo que pasa aqui es que esta diciendo el programa, que si no hay ningun valor introducido, salta la alerta sin romper el bucle 
        print('Introduce un numero valido ❌​')
        continue

    respuesta = int(respuesta) #La respuesta debe de ser un numero entero

    if respuesta == num1 + num2: #Esta indicando que si la respuesta es igual a la suma de num1 y num2, pasa al siguiente nivel
        print('Correcto! empiezas muy bien ​✅​')
        nivel += 1 #Suma un nivel a la variable de Nivel
        break #Esto rompe el bucle, cuando el usuario acierta correctamente
    else: #Esto es lo que indica cuando el usuario escribe la respuesta mal
        vida -= 1 #De 5 vidas que empieza el usuario se le resta 1 y asi sucesivamente si sigue fallando
        print('Es incorrecto ❌​')
        print(f'Te quedan {vida} vidas') #Aqui se muestran las vidas restantes usando un f string
    if vida == 0:
        print('🔴​ Game over 🔴​')
        break #Este bucle termina cuando llega a 0 vidas cuando vida = 0, y vuelta a empezar si el usuario decide comenzar una partida nueva

    #RESTAS⬇️​

while True:

    num1 = random.randint(100,1000)
    num2 = random.randint(1,100)

    print(f'\nNivel {nivel}')
    print(f'Cuanto es {num1} - {num2}')

    respuesta_2 = input('Cual es el resultado: ')

    if not respuesta_2.isdigit():
        print('Introduce un numero valido  ❌​')
        continue

    respuesta_2 =  int(respuesta_2)

    if respuesta_2 == num1 - num2:
        print('Tomaya! que crack eres ​😎​')
        nivel += 1
        break
    else:
        vida -= 1
        print('Es incorrecto ❌')
        print(f'Te quedan {vida} vidas')
    if vida == 0:
        print('🔴 Game over 🔴')
        break

    #MULTIPLICACIONES ⬇️

while True:
    num1 = random.randint(1,1000)
    num2 = random.randint(1,100)

    print(f'\nNivel {nivel}')
    print(f'Cuanto es {num1} x {num2}')

    respuesta_3 = input('Cual es el resultado: ')

    if not respuesta_3.isdigit():
        print('Introduce un numero valido ❌​')
        continue

    respuesta_3 = int(respuesta_3)

    if respuesta_3 == num1 * num2:
        print('Si señor! estas hecho un genio 😉​')
        nivel += 1
        break
    else:
        vida -= 1
        print('Es incorrecto ❌')
        print(f'Te quedan {vida} vidas')
    if vida == 0:
        print('🔴 Game over 🔴')
        break

    #DIVISION ⬇️

while True:
    num1 = random.randint(1,1000) 
    num2 = random.randint(1,100)

    print(f'\nNivel {nivel}')
    print(f'Cuanto es {num1} / {num2}? (2 decimales)')

    respuesta_4 = input('Cual es el resultado: ')

    try: #El try sirve para que si el usuario pone un numero con decimal, python prueba el cambio a decimal junto al except que se encarga de exentar el error ValueError
        respuesta_4 = float(respuesta_4)
    except ValueError:
        print('Introduce un numero valido ❌')
        continue

    resultado = round(num1 / num2, 2) #Esto se encarga de que la respuesta introducida por el usuario sea redondeada para que no tenga que escribirse el valor entero

    if round(respuesta_4, 2) == resultado:
        print('Que crack!! estas hecho un/a genio 😇​')
        break
    else:
        vida -= 1
        print('Respuesta incorrecta ⚠️​')
        print(f'Te quedan {vida} vidas❗​')

    if vida == 0:
        print('🚨​ Game over 🚨​')
        break

    #Final del juego 

