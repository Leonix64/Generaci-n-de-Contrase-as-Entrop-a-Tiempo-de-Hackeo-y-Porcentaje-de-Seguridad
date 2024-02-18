import random
import string
import math

def generar_password(longitud):
    """Genera una contraseña aleatoria de la longitud especificada."""
    caracteres = string.ascii_letters + string.digits + string.punctuation
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

def calcular_entropia(longitud):
    """Calcula la entropía de una contraseña."""
    num_caracteres = len(string.ascii_letters + string.digits + string.punctuation)
    return longitud * math.log2(num_caracteres)

def estimar_tiempo_hackeo(entropia):
    """Estima el tiempo necesario para hackear una contraseña basado en su entropía."""
    intentos_por_segundo = 10**12  # En caso de ataque de fuerza bruta
    tiempo_segundos = 2 ** entropia / intentos_por_segundo
    return tiempo_segundos

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

def main():
    print("Generador de Contraseñas Seguras")
    longitud_password = obtener_longitud_password()
    password_generada = generar_password(longitud_password)
    print("\nLa contraseña generada es:", password_generada)

    entropia = calcular_entropia(longitud_password)
    print("Entropía de la contraseña:", entropia)

    tiempo_hackeo = estimar_tiempo_hackeo(entropia)
    print("Tiempo estimado para hackear la contraseña:", convertir_tiempo(tiempo_hackeo))

    mostrar_consejos_seguridad()

if __name__ == "__main__":
    main()

