# VSISA - Vivvidero Software Image Similarity Application

*Lee este archivo en otros lenguajes: [English](README.md), [Español](README_ES.md)

###### Bienvenido lector, mediante este documento te estaremos explicando la anatomía de VSISA.

![2](https://user-images.githubusercontent.com/63880943/164364813-32a9ba10-1e65-4569-b97d-e3aa936109d4.jpg)

## Version

La versión actual es v1.0 Beta

*Revisa nuestro: [documento de versiones](VERSIONS.md)

## ¿Que es VSISA?

Vivvidero Software Image Similarity Application es un software especializado en comparativa de imagenes, el objetivo es comparar una imagen subida por un usuario 
con un catalogo especializado de renders arquitectonicos con fin de acelerar el proceso de remodelación de una apartamento, tanto para vendedor como para uso interno de Vivvidero©.

## ¿Como funciona?

Se desarrolló una interfaz de usuario, desde la cual se creará cada usuario, se añadirá la información del apartamento, las imagenes, y posteriormente se iniciará el procesamiento de las mismas con OpenCV,
una vez terminado el procesamiento de imagenes se enviará el correo correspondiente con un archivo PDF adjunto.

## Algoritmo

Se utilizaron 2 algoritmos distintos para realizar la comparativa, SIFT y SURF, ambos vienen con OpenCV. Además se complementó con Instance Segmentation para identificar
mejor cada objeto, sin embargo esta última característica sigue en revisión a la fecha de la última versión.

## Manejo de archivos

En cada carpeta encontrará un archivo readme, en dicho documento se consignará la información de los archivos almacenados en dicho directorio

## Dependencias

  Utilizamos las siguientes dependencias:
  
  - Django (Web framework)
  - FPDF (PDF development)
  - OpenCV (Image processing Lib)
  - Pillow (Image management software)
  - Numpy (Numeric calculations software)

## Instalación

  - Verifica que tengas todas las **Dependencias** instaladas
  - Haz las migraciones correspondientes, para ello debes ejecutar el siguiente comando:
  
    ```
    py manage.py makemigrations
    ```
  - Una vez verificada las migraciones necesarias se puede arrancar un servidor de desarrollo:
  
    ```
    py manage.py runserver
    ```
    - En caso de llegar a necesitar abrirlo al público puedes usar el comando: (El puerto 8000 debe estar abierto en firewall y en el router)
    
      ```
      py manage.py runserver 0.0.0.0:8000
      ```
      
  - Listo! El proyecto es accesible desde la dirección 127.0.0.1:8000 en caso de ser local. Para remoto puedes revisar la documentación de [Django](https://docs.djangoproject.com/en/4.0/)


    
    
  
  


 

