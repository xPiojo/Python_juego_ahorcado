import random

def obtener_palabra_secreta() -> str:
    """
    Selecciona una palabra secreta aleatoria de una lista predefinida.

    Returns:
        str: La palabra secreta seleccionada aleatoriamente.
    """
    palabras = ['python', 'javascript', 'angular', 'tensorflow', 'java', 'django', 'react', 'typescript', 'git', 'flask']
    return random.choice(palabras)

def mostrar_progreso(palabra_secreta: str, letras_intentadas: list) -> str:
    """
    Muestra el progreso actual del jugador revelando las letras adivinadas
    y reemplazando las no adivinadas con guiones bajos.

    Args:
        palabra_secreta (str): La palabra que se está tratando de adivinar.
        letras_intentadas (list): Letras que el jugador ha intentado hasta el momento.

    Returns:
        str: Progreso actual en forma de cadena con letras reveladas y guiones bajos.
    """
    return ' '.join([letra if letra in letras_intentadas else "_" for letra in palabra_secreta])

def juego_ahorcado():
    """
    Ejecuta el juego del ahorcado, donde el jugador tiene un número limitado de intentos
    para adivinar una palabra secreta. El juego termina cuando el jugador adivina 
    completamente la palabra o se queda sin intentos.
    """
    palabra_secreta = obtener_palabra_secreta()  # Selecciona una palabra secreta aleatoria
    letras_intentadas = []  # Lista para almacenar las letras que el usuario ha intentado
    intentos = 7  # Número de intentos disponibles
    juego_terminado = False  # Indicador para saber si el juego ha terminado

    # Introducción al juego
    print("\n¡Bienvenido al juego del ahorcado!")
    print(f"Tienes {intentos} intentos para adivinar la palabra secreta.")
    print(mostrar_progreso(palabra_secreta, letras_intentadas), f"\nLa cantidad de letras de la palabra es: {len(palabra_secreta)}")

    # Bucle principal del juego, que se repite hasta que el juego termine o se agoten los intentos
    while not juego_terminado and intentos > 0:
        adivinanza = input("\nIntroduce una letra: ").strip().lower()  # Solicita una letra y elimina espacios

        # Validaciones de la entrada del jugador
        if len(adivinanza) != 1 or not adivinanza.isalpha():
            print("Por favor introduce una letra válida (solo una letra).")
        elif adivinanza in letras_intentadas:
            print("Ya has utilizado esa letra, prueba con otra.")
        else:
            letras_intentadas.append(adivinanza)  # Agrega la letra intentada a la lista
            if adivinanza in palabra_secreta:  # Si la letra está en la palabra secreta
                print(f"¡Muy bien! Has acertado la letra '{adivinanza}'.")
            else:  # Si la letra no está en la palabra secreta
                intentos -= 1
                print(f"Lo siento, la letra '{adivinanza}' no está en la palabra secreta.")
                print(f"Te quedan {intentos} intentos.")
        
        # Mostrar el progreso actual del jugador
        progreso_actual = mostrar_progreso(palabra_secreta, letras_intentadas)
        print(f"\nProgreso actual: {progreso_actual}")
        
        # Verificar si el jugador ha ganado
        if "_" not in progreso_actual:
            juego_terminado = True
            print(f"¡Felicidades, has ganado! La palabra completa es: {palabra_secreta}.")
    
    # Si el jugador ha perdido (intentos == 0)
    if intentos == 0:
        print(f"Lo siento mucho, se te han acabado los intentos. La palabra secreta era: {palabra_secreta.capitalize()}.")

# Ejecutar el juego
if __name__ == "__main__":
    juego_ahorcado()

