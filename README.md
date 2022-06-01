<p align = "center">
    <img src="img/itam_logo.png" />
</p>

## Parte 2 de la práctica II, Optimización 2: reimplementación de secciones de código del paquete construído para uso de niveles de BLAS, compilación a C, cómputo en paralelo, concurrente o distribuido. Preparación para la entrega de su práctica / proyecto final

## Descripción

## Divisón del equipo

| User| Equipo | Tareas | Roles |
|:---:|:---:|:---:|:---:|
AideJGC | 1 | Perfilamiento y compilación en C | Programador
pautrejo | 1 | Creación de tests y actualización de documentación | Project Manager
joelitam2021 | 1 | Perfilamiento y compilación en C | Programador
jesusmb230795 | 1 |  Perfilamiento y obtención de datos | Programador

## Trabajo

### Equipo

Se dividio el equipo para realizar cuatro tareas.

1. 2 personas que realicen perfilamiento del código.  **Aide** / **Enrique**

2. 2 personas que realicen reimplementación / adición / eliminación de secciones al código de acuerdo al perfilamiento realizado. **Aide** / **Joel**

3. 1 persona que sea *project manager* (más detalles de este rol en las notas), cree nuevos *tests* para la reimplementación / adición / eliminación de secciones al código, haga actualización de documentación hecha con *Sphinx* y *software* en las imágenes de *docker*. **Paulina**

### Individual

**Aide**: se investigó acerca de *web scraping* para obtener información de cryptomonedas. Se realizó perfilamiendo del método *bellman ford* usando diferentes métodos, asi como el perfilamiento de la función *exchange matrix* para variar el precio de las monedas en 5%. Elaboración de reporte.

**Paulina**: se diseñó la prueba para contrastar el tiempo del método original vs el método compilado en C. Se comprueba que los resultados sean idénticos y que el tiempo de ejecución sea estrictamente menor para que pueda pasar el test. La documentación se actualiza con ambas funciones tanto la original como la compilación en C y se añaden nuevas instrucciones de instalación.

**Joel** Se replicó la creación del Docker, se trabajo en la optimización con cython, realicé las ejecuciones en el ambiente AWS. se hicieron las modificaciones a la configuracion en AWS para que poder ejecutar el perfilamiento del uso del CPU (perf) 

**Enrique**: Se contruyo una función para obtener la lista de todas las monedas, asi como una función para descargar sus datos historicos. Para el preprocesamiento de la data a la creación de la red, se creo una clase para su procesamiento con apoyo del trabajo realizado por Aide. Por ultimo se hizo el perfilamiento del uso del CPU (perf).

### Documentación

 [Bellman Ford Documentation](https://optimizacion-2-2022-gh-classroom.github.io/practica-2-segunda-parte-jesusmb230795/)

### Descripción de archivos

- Carpeta [.github/workflows](https://github.com/optimizacion-2-2022-gh-classroom/practica-2-segunda-parte-jesusmb230795/tree/main/.github/workflows): Contiene los archivos *.yml* encargados de lanzar la construcción del *docker*, la documentación del paquete y el lanzamiento de los *tests*

- Carpeta [img](https://github.com/optimizacion-2-2022-gh-classroom/practica-2-segunda-parte-jesusmb230795/tree/main/aws): Contiene evidencia del uso de la infraestructura de aws,y algunas imagenes de formato.

- Carpeta [notebooks](https://github.com/optimizacion-2-2022-gh-classroom/practica-2-segunda-parte-jesusmb230795/tree/main/notebooks): Contiene las pruebas de perfilamiento y compilación en C realizadas.

- Carpeta [src](https://github.com/optimizacion-2-2022-gh-classroom/practica-2-segunda-parte-jesusmb230795/tree/main/src): Contiene el código del paquete *bellman ford*.

- Archivo [reporte_equipo_1_parte_2_practica_2.ipynb](https://github.com/optimizacion-2-2022-gh-classroom/practica-2-segunda-parte-jesusmb230795/blob/main/reporte_equipo_1_parte_1_practica_2.ipynb): reporte del perfilamiento realizado con el paquete optimizado.

- Archivo [requirements.txt](https://github.com/optimizacion-2-2022-gh-classroom/practica-2-segunda-parte-jesusmb230795/blob/main/requirements.txt): listado de paqueterías necesarias para el paquete y test.

- Archivo [setup.py](https://github.com/optimizacion-2-2022-gh-classroom/practica-2-segunda-parte-jesusmb230795/blob/main/setup.py): instalador del paquete.

- Archivo [test.py](https://github.com/optimizacion-2-2022-gh-classroom/practica-2-segunda-parte-jesusmb230795/blob/main/test.py): archivo que contiene los test al paquete.

## Comando de docker

Se cuenta con una imagen de docker que contiene preisntalado la nueva version deel paquete creado para ejecutar el método de Bellman Ford, y el en este link se puede ver el [Dockerfile](https://github.com/optimizacion-2-2022-gh-classroom/practica-2-segunda-parte-jesusmb230795/blob/main/dockerfiles/pkg/Dockerfile)

Para ejecutar el docker se usa la siguiente instrucción:

docker run --rm -v \<ruta a mi directorio\> :/datos --name jupyterlab_practica2 -p 8888:8888 -d joelitam2021/pkg_practica2_parte1:0.1

donde ***\<ruta a mi directorio\>*** deberá sustituirse por la ruta local donde desee clonar este *docker*.

Después de correr la imagen de docker en su computadora, podrá acceder al jupyterlab a través de un browser usando la siguiente dirección:

http://localhost:8888

Le pedirá una contraseña, que por defaul es qwerty.

## Botón de binder

Se cuenta con la opción de correr el paquete usando la herramienta de Binder

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/optimizacion-2-2022-gh-classroom/practica-2-segunda-parte-jesusmb230795/main)

## Referencias

* [Crypto Trading and Arbitrage Identification Strategies](https://nbviewer.org/github/rcroessmann/sharing_public/blob/master/arbitrage_identification.ipynb)
* [Video Dokerfile: example-docker-image-build-and-push](https://www.youtube.com/watch?v=wv7JGstFgrU&feature=youtu.be)
* [Dokerfile curso](https://github.com/palmoreck/dockerfiles/blob/master/jupyterlab/optimizacion_2/3.2.8/Dockerfile)
* [Video Get started with Binder](https://www.youtube.com/watch?v=owSGVOov9pQ)
* [How to share a Jupyter notebook with Binder?](https://mybinder.readthedocs.io/en/latest/introduction.html)
* [Pseudo código](https://www.simplilearn.com/tutorials/data-structure-tutorial/bellman-ford-algorithm)
* [Bellman-Ford Algorithm](https://www.sciencedirect.com/topics/computer-science/bellman-ford-algorithm).
* [bellman_ford_shortest_paths](https://www.boost.org/doc/libs/1_62_0/libs/graph/doc/bellman_ford_shortest.html)
* [An Analysis of Bellman-Ford and Dijkstra’s Algorithm](https://melitadsouza.github.io/pdf/algos.pdf)
* [6.Minikube y AWS](https://github.com/ITAM-DS/analisis-numerico-computo-cientifico/wiki/6.Minikube-y-AWS)
* [Minikube, Kubeflow y Kale 2022](https://www.youtube.com/watch?v=SusT5xQN1ro)
* [running `perf` in docker & kubernetes](https://medium.com/@geekidea_81313/running-perf-in-docker-kubernetes-7eb878afcd42)
