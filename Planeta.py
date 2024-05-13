﻿class Planeta:
    """
    Esta clase representa un planeta que orbita alrededor de una estrella anfitriona.
    
    Atributos:
    estrella_anfitriona: La estrella alrededor de la cual orbita el planeta.
    masa_planetaria: La masa del planeta.
    radio: El radio del planeta.
    a: El radio semi mayor de la órbita del planeta.
    inclinacion: La inclinación de la órbita del planeta.
    excentricidad: La excentricidad de la órbita del planeta.
    argumento_periastron: El argumento del periastron del planeta.
    """
    def __init__(self, estrella_anfitriona, masa_planetaria, radio, a, inclinacion, excentricidad, argumento_periastron):
        """
        Esta función inicializa una nueva instancia de la clase Planeta con los atributos dados.
        
        Parámetros:
        estrella_anfitriona: La estrella alrededor de la cual orbita el planeta.
        masa_planetaria: La masa del planeta.
        radio: El radio del planeta.
        a: El radio semi mayor de la órbita del planeta.
        inclinacion: La inclinación de la órbita del planeta.
        excentricidad: La excentricidad de la órbita del planeta.
        argumento_periastron: El argumento del periastron del planeta.
        """
        self._estrella_anfitriona = estrella_anfitriona
        self._masa_planetaria = float(masa_planetaria)
        self._radio = float(radio)
        self._a = float(a)
        self._inclinacion = float(inclinacion)
        self._excentricidad = float(excentricidad)
        self._argumento_periastron = float(argumento_periastron)

    def periodo_de_rotacion_kepleriana(self):
        """
        Esta función calcula y devuelve el período de rotación kepleriana del planeta.
        
        Retorna:
        El período de rotación kepleriana del planeta (del tipo flotante).
        """
        G = G 
        M = self._estrella_anfitriona._masa  
        a = self._a  

        periodo = 2 * np.pi * (np.sqrt(a**3 / (G*M)))
        return float(periodo)
