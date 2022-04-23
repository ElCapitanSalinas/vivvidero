# VSISA - Vivvidero Software Image Similarity Application

*Read this file in other languages: [English](README.md), [Español](README_ES.md)

###### Welcome reader, on this document we will explain you the anatomy of VSISA.

![2](https://user-images.githubusercontent.com/63880943/164364813-32a9ba10-1e65-4569-b97d-e3aa936109d4.jpg)


## ¿What VSISA is?

Vivvidero Software Image Similarity Application is an image comparative software, the main objective is compare an image uploaded by the user with an arquitectonic renders stock
to improve the redesign process for the apartments, for sellers and inside use for Vivvidero©.

## ¿How does it works?

We developed an User Interface, there will be created every user, then the user will sign all the apartment information and upload the images, after that
we will start the image processing, once finished the software will send an email with the process pdf.

## Algorithm

We’ve used 2 algorithms for the comparison, SIFT and SURF, both of them came with OpenCV. And we've added a basic instance segmentation to improve 
the objects detection, this feature is still being tested for the last version.

## Dependencies

  We used this libraries:
  
  - Django (Web framework)
  - FPDF (PDF development)
  - OpenCV (Image processing Lib)
  - Pillow (Image management software)
  - Numpy (Numeric calculations software)

## Installation

  - Verify all the **Dependencies**
  - Do the project migrations, you must execute the following command:
  
    ```
    py manage.py makemigrations
    ```
  - Once done the migrations you can start the development server:
  
    ```
    py manage.py runserver
    ```
    - In case that you need remote access you must use the command: (For this example the port 8000 TCP must be opened in your firewall and router)
    
      ```
      py manage.py runserver 0.0.0.0:8000
      ```
      
  - Done! The project is remotely joinable from the url 127.0.0.1:8000 if its local. For remote you must check the [Django documentation](https://docs.djangoproject.com/en/4.0/)


    
    
  
  


 

