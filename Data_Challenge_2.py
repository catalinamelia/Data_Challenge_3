#!/usr/bin/env python
# coding: utf-8

# # Sistemas planetarios
# 
# Es ampliamente conocido que un sistema planetario consiste principalmente en un grupo de planetas y una estrella. En este problema, necesitarás codificar las siguientes entidades utilizando el lenguaje de programación Python y el paradigma orientado a objetos. Las entidades se describirán de la siguiente manera:

# In[56]:


import csv
from astropy.constants import L_sun, M_sun, G
import numpy as np
import pyvo
import pandas as pd


# ## Estrellas

# In[57]:


class Estrella():
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


# ## Sistema Jerárquico

# In[58]:


class Sistema_Jerarquico():
    """
    Esta clase representa un sistema estelar jerárquico compuesto por múltiples estrellas.
    
    Atributos:
    estrellas: Una lista que contiene objetos de la clase Estrella.
    """
    def __init__(self, estrellas):
        """
        Esta función inicializa una nueva instancia de la clase Sistema_Jerarquico con la lista de estrellas.
        
        Parámetros:
        estrellas: Una lista de objetos de la clase Estrella que representan las estrellas en el sistema.
        """
        #Busco un sistema con dos o más estrellas
        if len(estrellas) < 2: 
            #uso raise porque es una excepción única
            raise ValueError("No es un sistema jerárquico") 
        self.estrellas = estrellas

    def orden_segun_masa(self):
        """
        Esta función ordena la lista de estrellas de acuerdo a su masa.
        
        Retorna:
        Una lista de estrellas ordenada por masa estelar.
        """
        return sorted(self.estrellas, key=lambda estrella: estrella.masa)
    
    def nombres_ordenados(self):
        """
        Esta función genera los nombres de las estrellas, seguidos de letras del alfabeto ordenadas.
        
        Retorna:
        Una cadena de texto que contiene los nombres de las estrellas seguidos de letras del alfabeto ordenadas.
        """
        return sorted(self.estrellas, key=lambda x: x[-1])


# ## Planeta

# In[59]:


class Planeta():
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


# ## Planeta Exoplanetario

# In[60]:


class Exoplaneta(Planeta):
    """
    Esta es una clase que representa un exoplaneta, la clase hereda de la clase Planeta.
    
    Atributos:
    (Todos los atributos de la clase Planeta)
    metodo_primer_descubrimiento: El método de primer descubrimiento del exoplaneta.
    similar_a_tatooine: Indica si el exoplaneta es similar a Tatooine.
    """
    def __init__(self, estrella_anfitriona, masa_planetaria, radio, a, inclinacion, excentricidad, argumento_periastron, metodo_primer_descubrimiento, sim_tatooine):
        """
        Esta función inicializa una nueva instancia de la clase Exoplaneta con los atributos dados.
        
        Parámetros:
        estrella_anfitriona: La estrella anfitriona del exoplaneta.
        masa_planetaria: La masa del exoplaneta.
        radio: El radio del exoplaneta.
        a: El radio semi mayor de la órbita del exoplaneta.
        inclinacion: La inclinación de la órbita del exoplaneta.
        excentricidad: La excentricidad de la órbita del exoplaneta.
        argumento_periastron: El argumento del periastron del exoplaneta.
        metodo_primer_descubrimiento: El método de primer descubrimiento del exoplaneta ("imagen directa", "velocidad radial" o "tránsito").
        similar_a_tatooine: Indica si el exoplaneta es similar a Tatooine. Por defecto, False.
        """
        Planeta.__init__(self, estrella_anfitriona, masa_planetaria, radio, a, inclinacion, excentricidad, argumento_periastron)
        self.metodo_primer_descubrimiento = metodo_primer_descubrimiento
        self.sim_tatooine = sim_tatooine

    def primer_descubrimiento(self):
        """
        Esta función devuelve el método de primer descubrimiento del exoplaneta.
        
        Retorna:
        El método de primer descubrimiento del exoplaneta ("imagen directa", "velocidad radial" o "tránsito").
        """
        return self.metodo_primer_descubrimiento

    def similar_tatooine(self):
        """
        Esta función determina si el exoplaneta es similar a Tatooine.
        
        Retorna:
        True si el exoplaneta es similar a Tatooine, False si no.
        """
        if self.metodo_primer_descubrimiento == "Tránsito":
            b = self._a * np.cos(self._inclinacion) / ((1 - self._excentricidad**2) * (self._estrella_anfitriona._radio * (1 + self._excentricidad * np.sin(self._argumento_periastron))))
            return 0 < b < 1
        else:
            return self.sim_tatooine


# ## Sistema Planetario

# In[61]:


class Sistema_Planetario():
    """
    Esta clase representa un sistema planetario.
    
    Atributos:
    planetas: Lista de objetos de la clase Planeta que conforman el sistema planetario.
    """
    def __init__(self, planetas):
        """
        Esta función inicializa una nueva instancia de la clase Sistema_Planetario con los planetas dados.
        
        Parámetros:
        planetas: Lista de objetos de la clase Planeta que conforman el sistema planetario.
        """
        self.planetas = planetas

    def numero_de_planetas(self):
        """
        Esta función devuelve el número de planetas en el sistema planetario.
        
        Retorna:
        El número de planetas en el sistema planetario.
        """
        return len(self.planetas) #Empleo len para que me devuelva del tipo entero

    def lista_orden_segun_radio(self):
        """
        Esta función devuelve la lista de planetas ordenada según su radio semi mayor de la órbita (a).
        
        Retorna:
        Una lista de objetos de la clase Planeta ordenados según su radio semi mayor de la órbita.
        """
        #La función sorted() es para ordenar y devolver una lista
        planetas_ordenados = sorted(self.planetas, key=lambda planeta: planeta.a )
        return planetas_ordenados


# ## Programa Principal

# In[71]:


#Descarga, filtración y lectura de archivo
planetas= pyvo.dal.TAPService("http://voparis-tap-planeto.obspm.fr/tap")
filtro= "SELECT target_name, detection_type, mass, radius, semi_major_axis, eccentricity, periastron\
    inclination, star_name, star_distance, star_mass, star_radius, star_teff, ra,dec FROM exoplanet.epn_core"
data= pd.DataFrame(np.array(planetas.search(filtro).to_table()))

estrellas = {} #Creo estos diccionarios vacíos para que la información sea de fácil acceso
sis_planetarios = {}

for index, row in planets.iterrows():
    star_name = row['star_name']
    if star_name not in estrellas:
        estrellas[star_name] = Estrella(star_name, row['star_mass'], row['star_radius'], row['star_teff'], row['star_distance'], (row['ra'], row['dec']))
        sis_planetarios[star_name] = []
    planeta = Planeta(row['target_name'], row['mass'], row['radius'], row['semi_major_axis'], row['eccentricity'], row['inclination'], row[13])
    sis_planetarios[star_name].append(planeta)

for star_name, planet_list in sis_planetarios.items():
    print(f"Sistema planetario alrededor de la estrella {star_name}:")
    for planeta in planet_list:
        print(f"Planeta: {planeta._estrella_anfitriona}")
        print(f"Masa: {planeta._masa_planetaria}, Júpiter")
        print(f"Radio: {planeta._radio}, radios terrestres")
        print(f"Excentricidad: {planeta._excentricidad}")
        print(f"Inclinación: {planeta._inclinacion}")
        print(f"Argumento del periastron: {planeta._argumento_periastron}")
        print()

#Acá imprimo la suma de los valores nulos, mostrándome la cantidad de datos faltantes de cada parámetro
p_faltantes = planets.isnull().sum()
print("Parámetros faltantes:")
print(p_faltantes)


# In[ ]:




