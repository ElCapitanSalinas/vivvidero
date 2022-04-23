# VSISA - Vivvidero Software Image Similarity Application


###### File management
On this kind of files you'll see the information about the files inside the folder.

## Houses

This is the main django app.

Django adds the capability for adding multiple applications into one project, the main project is called vivvidero.

All the urls settings are managed from urls.py, and the functions associated to those urls are stored on views.py.

## Views.py

This is the file where we init and interact with the functions. When someone requests some information from an url we need to interact with the functions stored on this file.

# Django official docs description

"In Django, web pages and other content are delivered by views. Each view is represented by a Python function (or method, in the case of class-based views). Django will choose a view by examining the URL that’s requested (to be precise, the part of the URL after the domain name)."