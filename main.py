import random,time

#Definicion de colores
BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'

iniciar_trivia = True  # Iniciamos la variable en True
intentos = 0  # variable que almacenará el número de veces que el usuario intenta nuestra trivia.
  
# Lo primero es mostrar en pantalla el texto de bienvenida para quien juegue tu trivia
print(YELLOW+"Bienvenido a mi trivia sobre Python"+RESET)

while iniciar_trivia == True: #  Mientras iniciar_trivia sea True, repite:
  intentos += 1
  
  puntaje = 0 #Inicializamos Puntaje
  puntaje=random.randint(1,100)
  
  print("\nIntento número:", intentos)
  input("Presiona Enter para continuar")
  #BIENVENIDA =========================
  for i in range(5):
    print("...")
    time.sleep(0.)
  print(BLUE+"* "*40+RESET)
  print(BLUE+"* "*40+RESET)
  time.sleep(0.2)
  print(YELLOW+"  ####   #   #  #####  ##  ##   ###   #   #"+RESET)
  time.sleep(0.2)
  print(YELLOW+"  #   #   # #   #####  ##  ##  #   #  ##  #"+RESET)
  time.sleep(0.2)
  print(YELLOW+"  ####    ###     #    ######  #   #  # # #"+RESET)
  time.sleep(0.1)
  print(YELLOW+"  ##       #      #    ##  ##  #####  # ###"+RESET)
  time.sleep(0.1)
  print(YELLOW+"  ##       #      #    ##  ##   ###   #  ##"+RESET)
  time.sleep(0.1)
  print(BLUE+"* "*40+RESET)
  print(BLUE+"* "*40+RESET+"\n")
  print("Pondremos a prueba tus conocimientos")
  print(f"Iniciaras el juego con:  {puntaje} puntos")
  #BIENVENIDA =========================
  
  namePlayer= input("Ingrese su nombre: ")# Inicia la variable nombre de jugador
  #Validacion de nombre
  while namePlayer == "":
    print("Por favor ingrese su nombre")
    namePlayer= input("Ingrese su nombre: ")
  
  for i in range(1,5):
    print("...")
    time.sleep(0.1)
    
  print(CYAN+f"\nBienvenido {namePlayer} mucho gusto"+RESET)
  country= input("De que pais eres :")

  #Validacion de Pais
  while country == "":
    print("Por favor ingrese su Pais de origen")
    country= input("De que pais eres :")
  time.sleep(0.2)
  print(GREEN+f"\n{country} Que Hermoso Lugar!\n\n"+RESET) 
  
  # Instrucciones sobre cómo jugar
  print("Ahora responde las siguientes preguntas escribiendo la letra de la alternativa y presionando 'Enter' para enviar tu respuesta:\n ")
  
  # Pregunta 1
  print(GREEN+"1) ¿Cual de los siguientes lenguajes de programación No es interpretado?"+RESET)
  print("a) C++")
  print("b) Javascript")
  print("c) Python")
  print("d) PHP")
  # Almacenamos la respuesta del usuario en la variable "respuesta_1"
  respuesta_1 = input("\nTu respuesta: ")
  while respuesta_1 not in ("a","b","c","d","x"): 
    print("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta:")
    respuesta_1 = input("\nTu respuesta: ")
  if respuesta_1 == "b":
    print(RED+"Respuesta Incorrecta\n"+RESET)
    puntaje -= random.randint(0,20)
  elif respuesta_1 == "c":
    print(RED+"Respuesta Incorrecta\n"+RESET)
    puntaje -= random.randint(0,10)
  elif respuesta_1 == "d":
    print(RED+"Respuesta Incorrecta\n"+RESET)
    puntaje -= random.randint(0,15)
  elif respuesta_1 == "x":
    print("Descubriste la opcion Secreta. Se multiplicara tu puntaje !\n")
    puntaje *= random.randint(2,3)
  else:
    puntaje += random.randint(0,50)
    print(BLUE+"Respuesta Correcta. Muy bien"+RESET,namePlayer)
  
  print("Tienes: "+MAGENTA,puntaje,RESET+" Puntos.")
  input("Presiona Enter para continuar\n")
    
  # Pregunta 2
  print(GREEN+"2) ¿A que se debe el nombre de Python?"+RESET)
  print("a) A la serpiente piton que en ingles es \"Python\"")
  print("b) A una banda de musica ")
  print("c) A una serie de TV llamado Monty Python")
  print("d) Al nombre de La mascota del creador")
  # Almacenamos la respuesta del usuario en la variable "respuesta_2"
  respuesta_2 = input("\nTu respuesta: ")
  while respuesta_2 not in ("a","b","c","d","y"): 
    print("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta:")
    respuesta_2 = input("\nTu respuesta: ")
  if respuesta_2 == "a":
    print(RED+"Respuesta Incorrecta\n"+RESET)
    puntaje -= random.randint(0,20)
  elif respuesta_2 == "b":
    print(RED+"Respuesta Incorrecta\n"+RESET)
    puntaje -= random.randint(0,10)
  elif respuesta_2 == "d":
    print(RED+"Respuesta Incorrecta\n"+RESET)
    puntaje -= random.randint(0,15)
  elif respuesta_2 == "y":
    print("Descubriste la opcion Secreta. Se multiplicara tu puntaje !\n")
    puntaje *= random.randint(1,3)
  else:
    puntaje += random.randint(0,50)
    print(BLUE+"Respuesta Correcta. Muy bien"+RESET,namePlayer)
  print("Tienes: "+MAGENTA,puntaje,RESET+" Puntos.")
  input("Presiona Enter para continuar\n")
    
  
  # Pregunta 3
  print(GREEN+"3) ¿Quien fue el creador de python?"+RESET)
  print("a) Bill Gates")
  print("b) Guido van Rossum")
  print("c) James Gosling")
  print("d) Steve Jobs")
  
  # Almacenamos la respuesta del usuario en la variable "respuesta_3"
  respuesta_3 = input("\nTu respuesta: ")
  while respuesta_3 not in ("a","b","c","d","z"): 
    print("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta:")
    respuesta_3 = input("\nTu respuesta: ")
  if respuesta_3 == "a":
    print(RED+"Respuesta Incorrecta\n"+RESET)
    puntaje -= random.randint(0,20)
  elif respuesta_3 == "c":
    print(RED+"Respuesta Incorrecta\n"+RESET)
    puntaje -= random.randint(10,20)
  elif respuesta_3 == "d":
    print(RED+"Respuesta Incorrecta\n"+RESET)
    puntaje -= random.randint(0,15)
  elif respuesta_3 == "z":
    print("Descubriste la opcion Secreta. Se multiplicara tu puntaje !\n")
    puntaje += random.randint(10,50)
  else:
    puntaje *= random.randint(2,5)
    print(BLUE+"Respuesta Correcta. Muy bien"+RESET,namePlayer)
    
  for i in range(5):
    print("* ",end="\t")
    time.sleep(0.1)
  print("")
  print("Obtuviste: "+MAGENTA,puntaje,RESET+" Puntos.")
  input("Presiona Enter para continuar\n")
  
  #RULETA FINAL DE LA TRIVIA
  time.sleep(0.2)
  print(BLUE+"* "*22+RESET)
  time.sleep(0.2)
  print(YELLOW+"********        RULETA FINAL        ********"+RESET)
  time.sleep(0.2)
  print(BLUE+"* "*22+RESET)
  time.sleep(0.2)
  print("En esta ruleta final podras ganar un puntaje aleatorio")

  #VALIDACION entrada numerica
  while True:
    try:
      numRuleta =int(input("Ingresa Solo un numero del uno al 10: "))
      break
    except ValueError:
      print("Debes escribir un número.")
      continue
  
  puntajeRuleta = random.randint(1,100) + random.randint(numRuleta,50)
  puntaje = puntaje + puntajeRuleta
  for i in range(5):
    print("...")
    time.sleep(0.3)
  print(f"GANASTE {puntajeRuleta} Puntos Adicionales!!")
  
  print(f"Gracias {namePlayer} por jugar mi trivia de Python. "+YELLOW+f"Acumulaste {puntaje} puntos"+RESET)
  
  for i in range(5):
    print("...")
    time.sleep(0.2)
  print(MAGENTA+"\n¿Deseas intentar la trivia nuevamente?")
  repetir_trivia = input("Ingresa 'si' para repetir, o cualquier tecla para finalizar: "+RESET).lower()
  
  if repetir_trivia != "si":  # != significa "distinto"
    print(f'\nEspero que lo hayas pasado bien {namePlayer} de {country}, hasta pronto!')
    iniciar_trivia = False  # Cambiamos el valor de iniciar_trivia a False para evitar que se repita.

