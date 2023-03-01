import cv2
import time
import math

p1 = 530
p2 = 300

#declara las matrices

video = cv2.VideoCapture("bb3.mp4")

# Cargar rastreador 
tracker = cv2.TrackerCSRT_create()

# Leer el primer cuadro del video
returned, img = video.read()

# Seleccionar el cuadro delimitador en la imagen
bbox = cv2.selectROI("Rastreando", img, False)

# Inicializar el rastreador en la imagen y el cuadro delimitador
tracker.init(img, bbox)

print(bbox)


while True:
    
    check, img = video.read()   

    # Actualizar el rastreador en la imagen y el cuadro delimitador
    success, bbox = tracker.update(img)

    # Llamar a drawBox()
    if success:
        drawBox(img, bbox)
    else:
        cv2.putText(img,"Perdido",(75,90),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,255),2)

    # Lamar goal_track()
    goal_track(img, bbox)

    # Mostrar el Video
    cv2.imshow("Resultado", img)


    # Cerrar la ventana de muestra cuando la barra espaciadora sea presionada        
    key = cv2.waitKey(25)
    if key == 32:
        print("Detenido")
        break

video.release()
cv2.destroyALLwindows()
