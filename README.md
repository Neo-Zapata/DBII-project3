# DBII-project3
# **Integrantes**
* Neo Marcelo Zapata Gallegos
* Harold Canto Vidal
* Christian Rojas Rojas
* Eros Carhuancho Espejo

# Tabla de contenido
- [Cuadro de Actividades](#Cuadro-de-Actividades)
- [Cuadro de Participación](#Cuadro-de-Participación)
- [Introducción](#Introducción)
- [Librerías](#Librerías)
    * [Face Recognition](#Face-Recognition)
    * [Rtree](#Rtree)
    * [KD-Tree](#KD-Tree)
- [Implementación](#Implementación)
    * [Backend](#Backend)
    * [Frontend](#Frontend)
    * [Experimentación](#Experimentación)

Procedimiento general:
    - Extracción de caracteristicas
    - Indexacion de vectores caracteristicos para busquedas eficientes
    - Algoritmo de búsqueda KNN
    
    
# Cuadro de Actividades:

<table>
  <tbody>
    <tr>
      <th>Lista de actividades realizadas</th>
      <th align="center">Responsable</th>
    </tr>
    <tr>
      <td>Implementación de la función range_search y knn para el Rtree </td>
      <td align="center">Harold Canto Vidal</td>
    </tr>
    <tr>
      <td>Implementación de la función preprocesamiento</td>
      <td align="center">Neo Marcelo Zapata Gallegos</td>
    </tr>
    <tr>
      <td>Implementación de la función score</td>
      <td align="center">Christian Rojas Rojas y Neo Marcelo Zapata Gallegos</td>
    </tr>
    <tr>
      <td>Implementación de la función range_search y knn secuencial</td>
      <td align="center">Neo Marcelo Zapata Gallegos</td>
    </tr>
    <tr>
      <td>Implementación del Frontend</td>
      <td align="center">Christian Rojas Rojas</td>
    </tr>
    <tr>
      <td>Escritura del informe</td>
      <td align="center">Eros Carhuancho y Harold Canto</td>
    </tr>
    <tr>
      <td>Implementación de la función knn para el KDtree </td>
      <td align="center">Eros Carhuancho</td>
    </tr>
  </tbody>
</table>

# Cuadro de Participación:

<table>
  <tbody>
    <tr>
      <th>Integrantes</th>
      <th align="center">Participación</th>
    </tr>
    <tr>
      <td>Neo Marcelo Zapata Gallegos</td>
      <td align="center">100%</td>
    </tr>
    <tr>
      <td>Harold Canto Vidal</td>
      <td align="center">100%</td>
    </tr>
    <tr>
      <td>Christian Rojas Rojas</td>
      <td align="center">100%</td>
    </tr>
    <tr>
      <td>Eros Carhuancho Espejo</td>
      <td align="center">100%</td>
    </tr>
  </tbody>
</table>


# Introducción:
El reconocimiento facial es una forma de identificar o confirmar la identidad de una persona en función de su rostro. Los sistemas de reconocimiento facial se pueden utilizar para identificar personas en fotos, videos o en tiempo real. En este proyecto con ayuda de librerías especializadas en el procesamiento de imágenes crearemos un programa que reconozca el rostro de una imagen y devuelva los rostros más parecidos a partir de una base de datos. 

# Librerías:
## Face Recognition
Esta librería nos podrá dar las herramientas de representación para los rostros de una imagen. Con la ayuda de la función load_image_file podremos representar toda la imagen en un vector de números. Posteriormente con la ayuda de la función face_encodings podremos reconocer un rostro de la imagen anteriormente procesada y generar un vector característico de 128 dimensiones, el cual es la representación matemática de un rostro. En el proyecto usaremos este vector característico para poder comparar con otros vectores de otras imágenes y así reconocer la similitud de rostros


## Rtree
Esta librería implementa un RTree el cual indexa los vectores característicos de las imágenes. La estructura implementada en esta librería está optimizada para poder resolver el problema de encontrar los vecinos más cercanos.

## KD-Tree
El KD-Tree es una estructura de datos de partición espacial para poder organizar puntos en un espacio k-dimensional. Este árbol es útil para aplicaciones como búsqueda por rango y la búsqueda del vecino más cercano, el cual es parte del objetivo de nuestro proyecto. Con ayuda de la librería sklearn podremos llamar a nuestra estructura de datos KDTree. Con la función query(imagen,k) podremos saber los k vecinos más cercanos a la imagen dada. Todo esto comparando las 128 dimensiones antes representadas con la librería face_recognition. 

# Implementación
## Backend
## Frontend
## Experimentación


ANOTACIONES:
    ES NECESARIO CARGAR EL DIRECTORIO DE IMAGENES CON EL NOMBRE "dataset" DENTRO DE LA CARPETA "/backend".
    backend -
             |_ dataset
             |_ processed_data (automatically created)
             |_ main.py
             |_ README.md
