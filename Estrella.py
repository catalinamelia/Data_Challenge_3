class Estrella:
    """
    Esta clase representa una estrella y proporciona métodos para calcular su luminosidad total y luminosidad de la secuencia principal.
    
    Atributos principales:
    nombre: Nombre de la estrella.
    masa: Masa de la estrella.
    radio: Radio de la estrella.
    temperatura_superficial: Temperatura superficial de la estrella.
    distancia: Distancia de la estrella a la Tierra.
    movimiento_propio: Movimiento propio de la estrella.
    """
    def __init__(self, nombre, masa, radio, temperatura_superficial, distancia, movimiento_propio):
        """
        Esta función inicializa una nueva instancia de la clase Estrella con los atributos dados.
        
        Parámetros:
        nombre: Nombre de la estrella.
        masa: Masa de la estrella.
        radio: Radio de la estrella.
        temperatura_superficial: Temperatura superficial de la estrella.
        distancia: Distancia de la estrella a la Tierra.
        movimiento_propio: Movimiento propio de la estrella.
        """
        self.nombre = nombre #Este atributo es público, por lo que no es necesario poner un _ antes del nombre
        self._masa = masa
        self._radio = radio
        self._temperatura_superficial = temperatura_superficial
        self._distancia = distancia
        self._movimiento_propio = movimiento_propio
    def luminosidad_total(self):
        """
        Esta función calcula la luminosidad total de la estrella.
        
        Retorna:
        La luminosidad total de la estrella (con retorno del tipo flotante).
        """
        #Para que retorne del tipo flotante empleo float()
        return float(4 * np.pi * (self._radio**2) * (self._temperatura_superficial)) 
    def luminosidad_de_la_secuencia_principal(self):
        """
        Esta función calcula la luminosidad de la secuencia principal de la estrella.
        
        Retorna:
        La luminosidad de la secuencia principal de la estrella (con retorno del tipo flotante).
        """
        return float(L_sun * (self._masa / M_sun)**3.5)
    def velocidad_escape(self):
        """
        Esta función calcula la velocidad de escape de la estrella.
        
        Retorna:
        La velocidad de escape de la estrella (con retorno del tipo flotante).
        """
        G = 6.674e-11  # Constante gravitacional
        velocidad = np.sqrt((2 * G * self._masa) / self._radio)
        return velocidad
