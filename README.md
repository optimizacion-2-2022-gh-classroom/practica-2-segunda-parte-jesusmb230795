<p align = "center">
    <img src="img/itam_logo.png" />
</p>

## Parte 2 de la práctica II, Optimización 2: reimplementación de secciones de código del paquete construído para uso de niveles de BLAS, compilación a C, cómputo en paralelo, concurrente o distribuido. Preparación para la entrega de su práctica / proyecto final


## Descripción



## Divisón del equipo

| User| Equipo | Tareas | Roles |
|:---:|:---:|:---:|:---:|
AideJGC | 1 | | 
pautrejo | 1 |  | 
joelitam2021 | 1 | | 
jesusmb230795 | 1 |  | 

## Trabajo

### Equipo




### Individual



### Documentación


### Descripción de archivos



## Comando de docker

Se cuenta con una imagen de docker que contiene preisntalado la nueva version deel paquete creado para ejecutar el método de Bellman Ford, y el en este link se puede ver el [Dockerfile](https://github.com/optimizacion-2-2022-gh-classroom/practica-2-primera-parte-joelitam2021/blob/main/dockerfiles/pkg/Dockerfile)

Para ejecutar el docker se usa la siguiente instrucción:

docker run --rm -v \<ruta a mi directorio\> :/datos --name jupyterlab_practica2 -p 8888:8888 -d joelitam2021/pkg_practica2_parte1:0.1

donde ***\<ruta a mi directorio\>*** deberá sustituirse por la ruta local donde desee clonar este *docker*.

Después de correr la imagen de docker en su computadora, podrá acceder al jupyterlab a través de un browser usando la siguiente dirección:

http://localhost:8888

Le pedirá una contraseña, que por defaul es qwerty.

## Botón de binder

Se cuenta con la opción de correr el paquete usando la herramienta de Binder

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/optimizacion-2-2022-gh-classroom/practica-2-primera-parte-joelitam2021.git/main)

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
