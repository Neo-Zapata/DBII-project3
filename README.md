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
- [Maldición de la dimensionalidad](#Maldición-de-la-dimensionalidad)

- [Experimentación](#Experimentación)
   * [Análisis y discusión](#Análisis-y-discusión)
   * [ANOTACIONES](#ANOTACIONES)

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

## Sequential
   Para el **`range_search()`**, se utilizó comparaciones con las distancias euclidianas obtenidas por **`numpy.linalg.norm()`**, con una busqueda secquencial en todas las imagenes procesadas de la colección.
   Para el **`knn_search()`**, se utilizó una cola de prioridad. En la que insertamos todos los elementos de la colección (ordenandolos por su distancia) y seleccionamos los K elementos con las distancias más pequeñas a la imagen de entrada. (query)

## R-tree
 Para el optimo uso del R-tree de  python se usan  **`idx.intersect`** y   **`idx.nearest`** para la busqueda por rango y el knn respectivamente idx es el indice que se maneja para su correcto uso.
 Para los vecinos más cercanos retornamos el path de la imagen y un dist que representa el vector caracteristico de la imagen.
 Para el caso de la busqeuda por rango con el Rtree su implementacion no es directa , ya que se tiene que crear un MBR para restar y sumar las 128 dimensiones 
 
## KDtree
   mmm

## Frontend

# Maldición de la dimensionalidad
Al aumentar el número de dimensiones se pueden agravar notablemente muchos de los problemas que ya pueden aparecer en dimensiones menores, esto es lo que se conoce como la maldición de la dimensionalidad sobre todo ocurre en casos cuando evaluamos los KNN vecinos más cercanos, ya que los valores se pueden parecer por las distancias que se genera. 
Una de las maneras de erradicarla es teniendo mayor cantidad de datos y quitando dimensiones.

# Experimentación
Para testear las implementaciones, se usa una imagen de Salma_Hayeks como query. Mostraremos el tiempo que demora para 100,200,400,800,1600,3200,6400,12800 datos.

![Image text](https://github.com/Neo-Zapata/DBII-project3/blob/main/Grafico.png)

## Análisis y discusión
Las pruebas muestran que las consultas indexadas en Rtree y KDTree son mucho más eficientes que las consultas secuenciales, es decir, no nos afecta la maldición del dimensionalidad en comparación con las implementaciones secuenciales. Finalmente, pudimos implementar el proyecto que devuelve las personas más similares en nuestra base de datos para cualquier consulta dada.

## ANOTACIONES
    ES NECESARIO CARGAR EL DIRECTORIO DE IMAGENES CON EL NOMBRE "dataset" DENTRO DE LA CARPETA "/backend".
    backend -
             |_ dataset
             |_ processed_data (automatically created)
             |_ main.py
             |_ README.md
