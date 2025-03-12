# Fuerza Bruta de Texto

Este proyecto implementa un algoritmo simple de fuerza bruta para generar un texto objetivo carácter por carácter. Utiliza un enfoque aleatorio para construir la cadena de texto, comparando cada carácter con el deseado hasta encontrar la coincidencia.

## Objetivo

El propósito del programa es demostrar cómo un algoritmo de fuerza bruta puede adivinar una cadena de texto sin conocerla previamente. Es un ejercicio educativo sobre la generación aleatoria y la búsqueda de coincidencias en programación.

## Cómo funciona

El programa sigue estos pasos:

1. Define un conjunto de caracteres posibles que incluyen letras mayúsculas y minúsculas, espacios y signos de puntuación.
2. Genera una cadena vacía con la misma longitud que el texto objetivo.
3. Para cada posición en la cadena, selecciona aleatoriamente caracteres hasta encontrar el correcto.
4. Imprime el progreso en tiempo real, mostrando cómo se forma la cadena gradualmente.
5. Introduce un pequeño retardo para que el proceso sea más visible.

## Requisitos

- **Python 3.x** (el script usa módulos estándar, por lo que no se requieren dependencias adicionales).

## Ejecución

1. Asegúrate de tener **Python 3.x** instalado.
2. Descarga el archivo y navega a su ubicación en la terminal.
3. Ejecuta el script con:

   ```bash
   python3 fuerza_bruta.py
    ```

    Observa cómo el programa genera el texto deseado de manera progresiva.

## Ejemplo de salida

H <br>
Ho <br>
Hol <br>
Hola <br>
Hola <br>
Hola M <br>
Hola Mu <br>
Hola Mun <br>
Hola Mund <br>
Hola Mundo <br>
Hola Mundo! <br>
Hola Mundo!!

> **Notas** 

> - El programa usa un método ineficiente basado en fuerza bruta. Para cadenas largas, el tiempo de ejecución aumenta significativamente.
> - Su propósito es puramente educativo para visualizar cómo un algoritmo de fuerza bruta encuentra una solución.