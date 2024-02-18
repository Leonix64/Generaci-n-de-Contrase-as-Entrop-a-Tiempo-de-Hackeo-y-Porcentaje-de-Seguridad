import random
import string
import math

def generar_password(longitud):
    """Genera una contraseña aleatoria de la longitud especificada."""
    caracteres = string.ascii_letters + string.digits
    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contraseña

def obtener_longitud_password():
    """Obtiene la longitud deseada de la contraseña del usuario."""
    while True:
        try:
            longitud_password = int(input("Ingresa la longitud de la contraseña: "))
            if longitud_password < 8:
                print("La longitud mínima recomendada es 8 caracteres.")
            else:
                return longitud_password
        except ValueError:
            print("Por favor, ingresa un número entero válido.")

def obtener_cantidad_password():
    """Obtiene la cantidad de contraseñas a generar."""
    while True:
        try:
            cantidad_contraseñas = int(input("Ingresa la cantidad de contraseñas a generar: "))
            if cantidad_contraseñas < 1:
                print("Debe ingresar al menos una contraseña.")
            else:
                return cantidad_contraseñas
        except ValueError:
            print("Porfavor, ingresa un numero entero valido.")

def calcular_entropia(longitud):
    """Calcula la entropía de una contraseña."""
    num_caracteres = len(string.ascii_letters + string.digits)
    return longitud * math.log2(num_caracteres)

def estimar_tiempo_hackeo(entropia):
    """Estima el tiempo necesario para hackear una contraseña basado en su entropía."""
    intentos_por_segundo = 10**12  # En caso de ataque de fuerza bruta
    tiempo_segundos = 2 ** entropia / intentos_por_segundo
    return tiempo_segundos

def nivel_dificultad(tiempo_hackeo):
    """Determina el nivel de dificultad basado en el tiempo estimado de hackeo."""
    if tiempo_hackeo <= 3600:  # Menos de una hora
        return "Bajo"
    elif tiempo_hackeo <= 157784630:  # Menos de 5 años
        return "Medio"
    else:
        return "Alto"

def convertir_tiempo(tiempo_segundos):
    """Convierte el tiempo de segundos a una forma más legible."""
    unidades = [('año', 60 * 60 * 24 * 365), ('mes', 60 * 60 * 24 * 30), ('semana', 60 * 60 * 24 * 7),
                ('día', 60 * 60 * 24), ('hora', 60 * 60), ('minuto', 60), ('segundo', 1)]
    resultado = []
    for nombre, segundo_valor in unidades:
        valor = tiempo_segundos // segundo_valor
        if valor:
            resultado.append("{} {}".format(int(valor), nombre + ('' if valor == 1 else 's')))
        tiempo_segundos %= segundo_valor
    return ', '.join(resultado)

def mostrar_consejos_seguridad():
    """Muestra algunos consejos de seguridad para contraseñas."""
    print("\n¡Recuerda estos consejos para mantener tu contraseña segura!")
    print("1. Utiliza una combinación de letras (mayúsculas y minúsculas), números y símbolos.")
    print("2. Evita usar información personal o fácilmente adivinable.")
    print("3. No reutilices contraseñas entre diferentes cuentas.")
    print("4. Considera el uso de un gestor de contraseñas para generar y almacenar contraseñas seguras.")

def generar_multiples_contraseñas():
    """Genera la cantidad de contraseñas y muestre sus detalles."""
    cantidad_contraseñas = obtener_cantidad_password()
    longitud_password = obtener_longitud_password()

    print("\nGenerando {} contraseñas con longitud de {} digitos...".format(cantidad_contraseñas, longitud_password))

    for i in range(cantidad_contraseñas):
        password_generada = generar_password(longitud_password)
        print("\nContraseña {}:".format(i+1))
        print("Contraseña Generada:",password_generada)

        entropia = calcular_entropia(longitud_password)
        print("Entropia de la contraseña:", entropia)

        tiempo_hackeo = estimar_tiempo_hackeo(entropia)
        print("Tiempo estimado para Hackear la contraseña:", convertir_tiempo(tiempo_hackeo))

        dificultad = nivel_dificultad(tiempo_hackeo)
        print("Nivel de dificultad:", dificultad)

def main():
    print("Generador de Contraseñas Seguras")
    generar_multiples_contraseñas()
    mostrar_consejos_seguridad()

if __name__ == "__main__":
    main()
