import os
import shutil
from keras.utils import load_img, save_img, array_to_img, img_to_array

def get_folders_name_from(from_location, ignored_directories ):
    list_dir = os.listdir(from_location)
    folders = []
    for file in list_dir:
        temp = os.path.splitext(file)
        if temp[1] == "" and (temp not in ignored_directories):
            folders.append(temp[0])
    return folders

#maxPooling
def maxPooling(img_a_procesar):
    img_a_convulusionar = img_to_array(img_a_procesar)

    stride = 3  # 2 x 2

    img_max_pooling = []
    for filas in range(1, 497 - 1, stride):
        new_fila = []
        for columnas in range(1, 497 - 1, stride):
            max_pixel = -1
            for f_kernel in range(stride):
                for c_kernel in range(stride):
                    pixel = img_a_convulusionar[filas + f_kernel][columnas + c_kernel][0]
                    if pixel > max_pixel:
                        max_pixel = pixel
            new_fila.append([max_pixel])  # se agrega como lista para agregarlo como canal 1 (escala de grises)
        img_max_pooling.append(new_fila)
    return img_max_pooling
#kernel 1 blox blur 3 × 3
def filtro1(img_a_procesar):

    img_a_convulusionar = img_to_array(img_a_procesar)
    kernel = [
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1]
    ]
    img_convolucionada = []  # nueva imagen
    for filas in range(1, 500 - 1):
        new_fila = []
        for columnas in range(1, 500 - 1):
            pixelConvulucionado = 0
            for f_kernel in range(len(kernel)):
                for c_kernel in range(len(kernel)):
                    pixelConvulucionado += kernel[f_kernel][c_kernel] \
                                           * img_a_convulusionar[filas + (f_kernel - 1)][columnas + (c_kernel - 1)]
            pixelConvulucionado = pixelConvulucionado / 9
            new_fila.append(pixelConvulucionado)
        img_convolucionada.append(new_fila)
    return img_convolucionada
#kernel2 Identity
def filtro2(img_a_procesar):

    img_a_convulusionar = img_to_array(img_a_procesar)
    kernel = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]
    img_convolucionada = []  # nueva imagen
    for filas in range(1, 500 - 1):
        new_fila = []
        for columnas in range(1, 500 - 1):
            pixelConvulucionado = 0
            for f_kernel in range(len(kernel)):
                for c_kernel in range(len(kernel)):
                    pixelConvulucionado += kernel[f_kernel][c_kernel] \
                                           * img_a_convulusionar[filas + (f_kernel - 1)][columnas + (c_kernel - 1)]
            pixelConvulucionado = pixelConvulucionado
            new_fila.append(pixelConvulucionado)
        img_convolucionada.append(new_fila)
    return img_convolucionada
#kernel3 ridge or  edge detection
def filtro3(img_a_procesar):

    img_a_convulusionar = img_to_array(img_a_procesar)
    kernel = [
        [0, -1, 0],
        [-1, 4, -1],
        [0, -1, 0]
    ]
    img_convolucionada = []  # nueva imagen
    for filas in range(1, 500 - 1):
        new_fila = []
        for columnas in range(1, 500 - 1):
            pixelConvulucionado = 0
            for f_kernel in range(len(kernel)):
                for c_kernel in range(len(kernel)):
                    pixelConvulucionado += kernel[f_kernel][c_kernel] \
                                           * img_a_convulusionar[filas + (f_kernel - 1)][columnas + (c_kernel - 1)]
            pixelConvulucionado = pixelConvulucionado
            new_fila.append(pixelConvulucionado)
        img_convolucionada.append(new_fila)
    return img_convolucionada
#kernel4 ridge or  edge detection
def filtro4(img_a_procesar):

    img_a_convulusionar = img_to_array(img_a_procesar)
    kernel = [
        [-1, -1, -1],
        [-1, 8, -1],
        [-1, -1, -1]
    ]
    img_convolucionada = []  # nueva imagen
    for filas in range(1, 500 - 1):
        new_fila = []
        for columnas in range(1, 500 - 1):
            pixelConvulucionado = 0
            for f_kernel in range(len(kernel)):
                for c_kernel in range(len(kernel)):
                    pixelConvulucionado += kernel[f_kernel][c_kernel] \
                                           * img_a_convulusionar[filas + (f_kernel - 1)][columnas + (c_kernel - 1)]
            pixelConvulucionado = pixelConvulucionado
            new_fila.append(pixelConvulucionado)
        img_convolucionada.append(new_fila)
    return img_convolucionada

#kernel5 Sharpen
def filtro5(img_a_procesar):

    img_a_convulusionar = img_to_array(img_a_procesar)
    kernel = [
        [0, -1, 0],
        [-1, 5, -1],
        [0, -1, 0]
    ]
    img_convolucionada = []  # nueva imagen
    for filas in range(1, 500 - 1):
        new_fila = []
        for columnas in range(1, 500 - 1):
            pixelConvulucionado = 0
            for f_kernel in range(len(kernel)):
                for c_kernel in range(len(kernel)):
                    pixelConvulucionado += kernel[f_kernel][c_kernel] \
                                           * img_a_convulusionar[filas + (f_kernel - 1)][columnas + (c_kernel - 1)]
            pixelConvulucionado = pixelConvulucionado
            new_fila.append(pixelConvulucionado)
        img_convolucionada.append(new_fila)
    return img_convolucionada

base_location = './'
source_folder = ('JuarezRamos')
destination_folder = 'Anie'
ignored_directories = ['.idea', '.DS_Store'] #or other folders

name_folders = get_folders_name_from(base_location + source_folder, ignored_directories)  # custom location
print(name_folders)


for folder in name_folders:
    try:
        ##read content - source location
        rutaImagen = base_location + source_folder + "/" + folder
        imgs = [archivo for archivo in os.listdir(rutaImagen) if archivo.endswith(".jpeg")]

        ##write content - destination location
        exists = os.path.exists(base_location + destination_folder + '/' + folder)
        if exists:
            shutil.rmtree(base_location + destination_folder + '/' + folder) #remove folder and subfolders

        #create a new folder...
        os.mkdir(base_location + destination_folder + '/' + folder)

        for k in range(5): #tot_kernels
            ruta = base_location + destination_folder + '/' + folder + "/Kernel_" + str(k)
            os.mkdir(ruta)
            for imagen in imgs:
                rutaImagenActual = rutaImagen + "/" + imagen
                img_a_procesar = load_img(rutaImagenActual, target_size=(500, 500), color_mode="grayscale")
                #######################################################################################################
                ##Aplica kernel "k" y guarda la imagen en ruta + nombre
                match k:
                    case 0:
                        img_convolucionada = filtro1(img_a_procesar)  ## se debe cambiar....
                        img = img_to_array(img_convolucionada)
                        rutaToSave = ruta + "/" + imagen[0:imagen.index(".")] + "_conFiltro_" + str(k) + ".jpeg"
                        save_img(rutaToSave, img)
                        ##Aplica maxPooling al kernel "k" y guarda la imagen en ruta + nombre
                        img_convolucionada_MX = maxPooling(img_convolucionada)  ## se debe cambiar....
                        imgMP = img_to_array(img_convolucionada_MX)
                        rutaToSave = ruta + "/" + imagen[0:imagen.index(".")] + "_conMaxPooling_" + str(k) + ".jpeg"
                        save_img(rutaToSave, imgMP)

                    case 1:
                        img_convolucionada = filtro2(img_a_procesar)  ## se debe cambiar....
                        img = img_to_array(img_convolucionada)
                        rutaToSave = ruta + "/" + imagen[0:imagen.index(".")] + "_conFiltro_" + str(k) + ".jpeg"
                        save_img(rutaToSave, img)
                        img_convolucionada_MX = maxPooling(img_convolucionada)  ## se debe cambiar....
                        imgMP = img_to_array(img_convolucionada_MX)
                        rutaToSave = ruta + "/" + imagen[0:imagen.index(".")] + "_conMaxPooling_" + str(k) + ".jpeg"
                        save_img(rutaToSave, imgMP)

                    case 2:
                        img_convolucionada = filtro3(img_a_procesar)  ## se debe cambiar....
                        img = img_to_array(img_convolucionada)
                        rutaToSave = ruta + "/" + imagen[0:imagen.index(".")] + "_conFiltro_" + str(k) + ".jpeg"
                        save_img(rutaToSave, img)
                        img_convolucionada_MX = maxPooling(img_convolucionada)  ## se debe cambiar....
                        imgMP = img_to_array(img_convolucionada_MX)
                        rutaToSave = ruta + "/" + imagen[0:imagen.index(".")] + "_conMaxPooling_" + str(k) + ".jpeg"
                        save_img(rutaToSave, imgMP)

                    case 3:
                        img_convolucionada = filtro4(img_a_procesar)  ## se debe cambiar....
                        img = img_to_array(img_convolucionada)
                        rutaToSave = ruta + "/" + imagen[0:imagen.index(".")] + "_conFiltro_" + str(k) + ".jpeg"
                        save_img(rutaToSave, img)
                        ##Aplica maxPooling al kernel "k" y guarda la imagen en ruta + nombre
                        img_convolucionada_MX = maxPooling(img_convolucionada)  ## se debe cambiar....
                        imgMP = img_to_array(img_convolucionada_MX)
                        rutaToSave = ruta + "/" + imagen[0:imagen.index(".")] + "_conMaxPooling_" + str(k) + ".jpeg"
                        save_img(rutaToSave, imgMP)

                    case 4:
                        img_convolucionada = filtro5(img_a_procesar)  ## se debe cambiar....
                        img = img_to_array(img_convolucionada)
                        rutaToSave = ruta + "/" + imagen[0:imagen.index(".")] + "_conFiltro_" + str(k) + ".jpeg"
                        save_img(rutaToSave, img)
                        ##Aplica maxPooling al kernel "k" y guarda la imagen en ruta + nombre
                        img_convolucionada_MX = maxPooling(img_convolucionada)  ## se debe cambiar....
                        imgMP = img_to_array(img_convolucionada_MX)
                        rutaToSave = ruta + "/" + imagen[0:imagen.index(".")] + "_conMaxPooling_" + str(k) + ".jpeg"
                        save_img(rutaToSave, imgMP)
                        #######################################################################################################

    except Exception as ex:
        print('-----> ERROR!!!   ', ex)
    finally:
        pass
