import pytesseract
import datefinder
import cv2

def month_string_to_number(SS):
    #año no ingresa aqui
    valor=SS.strip(' ')
    out ="-"
    m = [ {'mes':'ENE', 'num':'-1-'}, {'mes':'FEB', 'num':'-2-'},         
          {'mes':'MAR', 'num':'-3-'}, {'mes':'ABR', 'num':'-4-'},          
          {'mes':'MAY', 'num':'-5-'}, {'mes':'JUN', 'num':'-6-'},
          {'mes':'JUL', 'num':'-7-'},{'mes':'AGO', 'num':'-8-'},
          {'mes':'SEP', 'num':'-9-'},{'mes':'OCT', 'num':'-10-'},
          {'mes':'NOV', 'num':'-11-'},{'mes':'DIC', 'num':'-12-'},       
        ]   
    
    for dic in m:
        if dic.get('mes')==valor:
            return dic.get('num')      
    return SS
    try:
        return '|'
    except:
        return '|'

def recorreCadena(txt):
    txt=txt.replace('\n', ' ').replace('\r', '')
    cadenaReparada=""
    palabra=''
    for indice in range(len(txt)):
        caracter= txt[indice]
        if caracter !=' ':
            palabra=palabra+caracter            
        else:
           cadenaReparada= cadenaReparada+" "+month_string_to_number(palabra)           
           palabra=" "
    return cadenaReparada

def devolverFecha(cadena):
    matches = list(datefinder.find_dates(cadena))
    if len(matches) > 0:
        date = matches[0]
        return date
    else:
        return 0

def getTextFromImage(image):

    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

    grayImage= cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    newImage=cv2.threshold(grayImage, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

    text = pytesseract.image_to_string(newImage,lang='spa')
    print(text)

    cadena=text
    #print('cadena',cadena)
    #print('fin cadena')

    fecha=devolverFecha(cadena)

    if fecha!=0:
        print (fecha)  
    else:    
        fecha=devolverFecha(recorreCadena(cadena))
        print(fecha)

    return fecha

