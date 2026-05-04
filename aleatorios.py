"""
Fichero: aleatorios.py
Alumno: Ainhoa Dumitru
Descripción: Implementación de generadores de números pseudoaleatorios 
mediante el algoritmo de congruencia lineal (LGC).
"""

class Aleat:
    """
    Clase que implementa un generador de números aleatorios usando LGC.

    Atributos:
        m (int): Módulo.
        a (int): Multiplicador.
        c (int): Incremento.
        x (int): Estado actual (semilla o último número generado).

    Métodos:
        __init__: Inicializa los parámetros (obligatorios por clave).
        __next__: Calcula y devuelve el siguiente número.
        __iter__: Devuelve el objeto como iterador.
        __call__: Reinicia la secuencia con una nueva semilla (posicional).

    Pruebas unitarias:
    >>> rand = Aleat(m=32, a=9, c=13, x0=11)
    >>> for _ in range(4):
    ...     print(next(rand))
    16
    29
    18
    15
    >>> rand(29)
    >>> for _ in range(4):
    ...     print(next(rand))
    18
    15
    20
    1
    """

    def __init__(self, *, m=2**48, a=25214903917, c=11, x0=1212121):
        self.m = m
        self.a = a
        self.c = c
        self.x = x0

    def __iter__(self):
        return self

    def __next__(self):
        # Aplicación de la fórmula x = (a*x + c) % m
        self.x = (self.a * self.x + self.c) % self.m
        return self.x

    def __call__(self, x0, /):
        self.x = x0


def aleat(*, m=2**48, a=25214903917, c=11, x0=1212121):
    """
    Función generadora de números aleatorios usando yield y send.

    Argumentos:
        m (int): Módulo (por defecto POSIX).
        a (int): Multiplicador (por defecto POSIX).
        c (int): Incremento (por defecto POSIX).
        x0 (int): Semilla inicial.

    Yields:
        int: El siguiente número pseudoaleatorio.

    Pruebas unitarias:
    >>> rand = aleat(m=64, a=5, c=46, x0=36)
    >>> for _ in range(4):
    ...     print(next(rand))
    34
    24
    38
    44
    >>> rand.send(24)
    38
    >>> for _ in range(4):
    ...     print(next(rand))
    44
    10
    32
    14
    """
    x = x0
    while True:
        x = (a * x + c) % m
        # yield devuelve el valor y 'recibido' captura lo que envíe .send()
        recibido = yield x
        if recibido is not None:
            x = recibido


if __name__ == "__main__":
    import doctest
    # Ejecuta las pruebas definidas en los docstrings
    doctest.testmod(verbose=True)
