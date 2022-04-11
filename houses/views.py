

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.http import FileResponse, Http404

# from .models import User
from .models import User, Apartamentos, Estadisticas

# Create your views here.
from django.http import HttpResponse
from .forms import NameForm, UploadFileForm, ImgForm
from django.core.files.storage import FileSystemStorage
import os

import cv2
import numpy as np
import time
import os, os.path

import threading

global tempsims
tempsims = 1

global temppic
temppic = 0

global original

# original = cv2.imread("images/81.jpg")

# print(compname)

actual = 0

def comparar(baseimg, area, apartmentid):
    global tempsims
    global temppic
    global actual
    global archivos
    print(actual)
    DIR = './media/catalogo/'+area+'/'
    archivos = len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])-1
    
    print(temppic)
    name = str(baseimg)
    # print(name)
    original = cv2.imread(f"./{name}")
    actual = actual + 1
    compname = str(actual)+".jpg"
    image_to_compare = cv2.imread("./media/catalogo/"+area+"/"+compname+"")
    print("./media/catalogo/"+area+"/"+compname+"")

    # if original.shape[1] > 2800 or original.shape[0] > 2800:
    #     scale_percent = 10
    # elif original.shape[1] > 2000 or original.shape[0] > 2000:
    #     scale_percent = 25
    # elif original.shape[1] > 1500 or original.shape[0] > 1500:
    #     scale_percent = 50
    # else:
    #     scale_percent = 100


    width = int(image_to_compare.shape[1] * 100 / 100)
    height = int(image_to_compare.shape[0] * 100 / 100)
    dim = (width, height)
    
    # resize image
    resized = cv2.resize(original, dim, interpolation = cv2.INTER_AREA)

    # image_to_compare = cv2.resize(image_to_compare, dim, interpolation = cv2.INTER_AREA)
    print('Resized Dimensions : ',resized.shape)
    # 1) Check if 2 images are equals
    
    
    if resized.shape == image_to_compare.shape:
        # print("The images have same size and channels")
        difference = cv2.subtract(resized, image_to_compare)
        b, g, r = cv2.split(difference)

        if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0:
            print("The images are completely Equal")
        else:
            print("The images are NOT equal")
            
    # 2) Check for similarities between the 2 images
    # time.sleep(1)

    # surf = cv2.xfeatures2d.SIFT_create(400)
    # kp_1, desc_1 = surf.detectAndCompute(resized, None)
    # kp_2, desc_2 = surf.detectAndCompute(image_to_compare, None)

    sift = cv2.xfeatures2d.SIFT_create()
    kp_1, desc_1 = sift.detectAndCompute(resized, None)
    kp_2, desc_2 = sift.detectAndCompute(image_to_compare, None)

    index_params = dict(algorithm=0, trees=5)
    search_params = dict()
    flann = cv2.FlannBasedMatcher(index_params, search_params)

    matches = flann.knnMatch(desc_1, desc_2, k=2)

    good_points = []
    ratio = 0.6
    finalurl = "hola"
    for m, n in matches:
        if m.distance < ratio*n.distance:
            good_points.append(m)
    if actual != archivos:
        if len(good_points) > tempsims:
            print(len(good_points))
            result = cv2.drawMatches(resized, kp_1, image_to_compare, kp_2, good_points, None)
            tempsims = len(good_points)
            temppic = compname
            print(temppic, tempsims)
            del image_to_compare
            del resized
            del original
            comparar(str(baseimg), area, apartmentid)
        else:
            del image_to_compare
            del resized
            del original
            comparar(str(baseimg), area, apartmentid)
    else:
        final = cv2.imread("media/catalogo/"+area+"/"+temppic+"")
        # finaltemp = temppic
        result = temppic
        to_edit = Apartamentos.objects.get(id=apartmentid)
        print(f"El resultado es: {result}")
        if area == "ktc":
            to_edit.ktc_new = result
            to_edit.save()
        elif area == "hall":
            to_edit.hall_new = result
            to_edit.save()
        elif area == "bath":
            to_edit.bath_new = result
            to_edit.save()
        elif area == "room":
            to_edit.room_new = result
            to_edit.save()

        actual = 0
        tempsims = 0
        temppic = 0
    



def price(area):
    talla = None

    if area < 50:
        talla = "XS"
    elif area >= 50 and area < 70:
        talla = "S"
    elif area >= 70 and area < 100:
        talla = "M"
    elif area >= 100 and area < 120:
        talla = "L"
    elif area >= 120 and area < 150:
        talla = "XL"
    else:
        talla = "XXL"

    print(f"La talla del apartamento es: {talla} ({area}m2)")

    prices = {"XS" : 1650000, "S" : 1600000, "M" : 1500000, "L" : 1400000, "XL" : 1250000, "XXL" : 1200000}

    preciofinal = area * prices[talla]

    return preciofinal

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():

            # print(request.POST['fullname'])

            tipo = None
            cliente = None
            if request.POST['type'] == 1:
                tipo = "vendedor"
            elif request.POST['type'] == 2:
                tipo = "comprador"
            else:
                tipo = "remodelador"

            if request.POST['customer'] == 1:
                cliente = "persona"
            else:
                cliente = "empresa"
                

            user = User(nombre = request.POST['fullname'], correo = request.POST['email'], telefono = request.POST['phone'], type = tipo, customer = cliente)
            user.save()

            print(user.id)
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect(f'/houses/newhouse/?name={user.nombre}&uid={user.id}')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'houses/index.html', {'form': form})

def createhouse(request):
    return render(request, 'houses/houseinfo.html', {'name': (request.GET['name']).split()[0], 'uid': request.GET['uid']})

def newhouse(request):
    if request.method == 'POST':
        # check whether it's valid:
            if request.POST['area'] and request.POST['price']:
                priceremo = price(int(request.POST['area']))
                print(priceremo)
                pricetotal = priceremo + int(request.POST['price'])
                print(pricetotal)

                apartment = Apartamentos(userid = request.GET['uid'], direccion = request.POST['neighborhood'], area = request.POST['area'], precio = request.POST['price'], precio_nuevo = pricetotal, precio_remo = priceremo, estrato = "Not defined", comodidades = request.POST['comodities'])
                apartment.save()

                # process the data in form.cleaned_data as required
                # ...
                # redirect to a new URL:
                # compare()
                return HttpResponseRedirect(f'/houses/newhouse/images/?id={apartment.id}&area=ktc')
            else: 
                return render(request, 'houses/houseinfo.html', {'error': "Te falta completar algunos campos"})
    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'houses/houseinfo.html', {'form': form})


import unidecode
def uploadimgs(request):
    # print("AAAA") 
    print(request.GET['area'])
    if request.method == 'POST':
        uid = request.GET['id']
        area = request.GET['area']
        uploaded_file = request.FILES['document']

        to_edit = Apartamentos.objects.get(id=int(uid))

        fs = FileSystemStorage()
        new_string = unidecode.unidecode(uploaded_file.name)
        defstr = new_string.replace(" ", "")
        name = fs.save(defstr, uploaded_file)

        url = fs.url(name)

        if request.GET['area'] == "ktc":
            to_edit.ktc = url
            to_edit.save()
            return HttpResponseRedirect(f'/houses/newhouse/images/?id={uid}&area=hall')
        elif request.GET['area'] == "hall":
            to_edit.hall = url
            to_edit.save()
            return HttpResponseRedirect(f'/houses/newhouse/images/?id={uid}&area=bath')
        elif request.GET['area'] == "bath":
            to_edit.bath = url
            to_edit.save()
            return HttpResponseRedirect(f'/houses/newhouse/images/?id={uid}&area=room')
        elif request.GET['area'] == "room":
            to_edit.room = url
            to_edit.save()
            return HttpResponseRedirect(f'/houses/newhouse/final/?id={uid}')

        
    area = request.GET['area']

    return render(request, 'houses/images.html', {'area': area})

from .mail import sendMail

def iniciarComp(apartmentid):
    areas = ["ktc", "hall", "bath", "room"]
    
    render(request, 'houses/base.html')
    for a in areas:
        to_edit = Apartamentos.objects.get(id=int(apartmentid))
        if a == "ktc":
                comparar(to_edit.ktc, "ktc", int(apartmentid))
            
        elif a == "hall":

            comparar(to_edit.hall, "hall", int(apartmentid))
        elif a == "bath":
            comparar(to_edit.bath, "bath", int(apartmentid))
        elif a == "room":
            comparar(to_edit.room, "room", int(apartmentid))

    ap = Apartamentos.objects.get(id=int(apartmentid))
    uid = ap.userid

    user = User.objects.get(id=int(uid))
    email = user.correo
    print(f"Enviando correo a {email}")
    finalMail(int(apartmentid), email)
    
    
    return HttpResponseRedirect(f'/newhouse/final/pdf/?id={apartmentid}')

def finalview(request):
    areas = ["ktc", "hall", "bath", "room"]
    apartmentid = request.GET['id']
    
    # render(request, 'houses/base.html')
    compare = threading.Thread(target=iniciarComp, name="Downloader", args=(apartmentid,))
    compare.start()

    ap = Apartamentos.objects.get(id=int(apartmentid))
    uid = ap.userid

    user = User.objects.get(id=int(uid))
    email = user.correo

    return render(request, 'houses/final.html', {'email': email})

import numpy as np
from fpdf import FPDF
import time
# from matplotlib.ticker import ScalarFormatter

# id=43&area=ktc

import os.path
from os import path

def finalMail(apartmentid, email):
    ap = Apartamentos.objects.get(id=int(apartmentid))

    if path.exists(f"./media/{apartmentid}.pdf"):
        print("Ya existe")
    else:

        pdf = FPDF('P', 'mm', (216, 279.4))
        pdf.add_page()
        pdf.set_font('Helvetica', '', 10)
        pdf.set_text_color(0, 0, 0)
        pdf.image('./media/0001.jpg', x = 0, y = 0, w = 216, h = 279.4)

        pdf.text(57, 26, ap.direccion) # BARRIO
        pdf.text(75, 26, ap.area) #AREA

        pdf.text(185, 49, ap.direccion) # BARRIO
        pdf.text(185, 39, ap.area) #AREA

        # pdf.text(77, 112, "X") #HABITACIÓN
        # pdf.text(103, 112, "X") #BAÑOS
        # pdf.text(127.8, 112, "X") #PARQUEADERO

        precio = "${:,.2f}".format(int(ap.precio))
        precio_remo = "${:,.2f}".format(int(ap.precio_remo))
        precio_nuevo = "${:,.2f}".format(int(ap.precio_nuevo))


        pdf.set_fill_color(0, 0, 0)
        pdf.set_xy(15, 36)
        pdf.cell(41, 10, precio, 0, 1, 'C') # PRECIO INICIAL
        pdf.set_xy(15, 54)
        pdf.cell(42, 10, precio_remo, 0, 1, 'C') # PRECIO REMO
        pdf.set_text_color(255, 255, 255)
        pdf.set_font('Helvetica', 'B', 10)
        pdf.set_xy(15, 71)
        pdf.cell(42, 10, precio_nuevo, 0, 1, 'C') # PRECIO FINAL

        pdf.image(f"./media/catalogo/ktc/{ap.ktc_new}", x = 64, y = 35, w = 45) # img 1
        pdf.image(f"./media/catalogo/room/{ap.room_new}", x = 112, y = 35, w = 45) # img 2


        pdf.image(f".{ap.ktc}", x = 41, y = 99, w = 48) # Cocina ant
        pdf.image(f"./media/catalogo/ktc/{ap.ktc_new}", x = 135, y = 99, w = 48) # Cocina desp

        pdf.image(f".{ap.hall}", x = 41, y = 160, w = 48) # Sala ant
        pdf.image(f"./media/catalogo/hall/{ap.hall_new}", x = 135, y = 160, w = 48) # Sala desp
        # # 67
        pdf.image(f".{ap.bath}", x = 41, y = 221, w = 48) # Baño ant
        pdf.image(f"./media/catalogo/bath/{ap.bath_new}", x = 135, y = 221, w = 48) # Baño desp


        pdf.add_page()

        pdf.set_font('Helvetica', '', 10)
        pdf.set_text_color(0, 0, 0)
        pdf.image('./media/0002.jpg', x = 0, y = 0, w = 216, h = 279.4)

        pdf.image(f".{ap.room}", x = 41, y = 15, w = 48) # Room ant
        pdf.image(f"./media/catalogo/room/{ap.room_new}", x = 135, y = 15, w = 48) # Room desp
        pdf.output(f'./media/{apartmentid}.pdf')

    sendMail(email, apartmentid)
    


def verpdf(request):
    context = {
        
    }

    apartmentid = request.GET['id']
    ap = Apartamentos.objects.get(id=int(apartmentid))

    if path.exists(f"./media/{apartmentid}.pdf"):
        return FileResponse(open(f'./media/{apartmentid}.pdf', 'rb'), content_type='application/pdf')
    else:
        pdf = FPDF('P', 'mm', (216, 279.4))
        pdf.add_page()
        pdf.set_font('Helvetica', '', 10)
        pdf.set_text_color(0, 0, 0)
        pdf.image('./0001.jpg', x = 0, y = 0, w = 216, h = 279.4)

        pdf.text(57, 26, ap.direccion) # BARRIO
        pdf.text(75, 26, ap.area) #AREA

        pdf.text(185, 49, ap.direccion) # BARRIO
        pdf.text(185, 39, ap.area) #AREA

        # pdf.text(77, 112, "X") #HABITACIÓN
        # pdf.text(103, 112, "X") #BAÑOS
        # pdf.text(127.8, 112, "X") #PARQUEADERO

        precio = "${:,.2f}".format(int(ap.precio))
        precio_remo = "${:,.2f}".format(int(ap.precio_remo))
        precio_nuevo = "${:,.2f}".format(int(ap.precio_nuevo))


        pdf.set_fill_color(0, 0, 0)
        pdf.set_xy(15, 36)
        pdf.cell(41, 10, precio, 0, 1, 'C') # PRECIO INICIAL
        pdf.set_xy(15, 54)
        pdf.cell(42, 10, precio_remo, 0, 1, 'C') # PRECIO REMO
        pdf.set_text_color(255, 255, 255)
        pdf.set_font('Helvetica', 'B', 10)
        pdf.set_xy(15, 71)
        pdf.cell(42, 10, precio_nuevo, 0, 1, 'C') # PRECIO FINAL

        pdf.image(f"./media/catalogo/ktc/{ap.ktc_new}", x = 64, y = 35, w = 45) # img 1
        pdf.image(f"./media/catalogo/room/{ap.room_new}", x = 112, y = 35, w = 45) # img 2


        pdf.image(f".{ap.ktc}", x = 41, y = 99, w = 48) # Cocina ant
        pdf.image(f"./media/catalogo/ktc/{ap.ktc_new}", x = 135, y = 99, w = 48) # Cocina desp

        pdf.image(f".{ap.hall}", x = 41, y = 160, w = 48) # Sala ant
        pdf.image(f"./media/catalogo/hall/{ap.hall_new}", x = 135, y = 160, w = 48) # Sala desp
        # # 67
        pdf.image(f".{ap.bath}", x = 41, y = 221, w = 48) # Baño ant
        pdf.image(f"./media/catalogo/bath/{ap.bath_new}", x = 135, y = 221, w = 48) # Baño desp


        pdf.add_page()

        pdf.set_font('Helvetica', '', 10)
        pdf.set_text_color(0, 0, 0)
        pdf.image('./0002.jpg', x = 0, y = 0, w = 216, h = 279.4)

        pdf.image(f".{ap.room}", x = 41, y = 15, w = 48) # Room ant
        pdf.image(f"./media/catalogo/room/{ap.room_new}", x = 135, y = 15, w = 48) # Room desp
        pdf.output(f'./media/{apartmentid}.pdf')
        time.sleep(2)
        return FileResponse(open(f'./media/{apartmentid}.pdf', 'rb'), content_type='application/pdf')



# def index(request):
#     context = {
        
#     }
#     return render(request, 'houses/index.html', context)


