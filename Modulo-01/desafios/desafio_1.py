import cv2


cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: No se puede abrir la cámara.")
    exit()

while True:
    ret, frame = cap.read()
    text = "En vivo"
    position = (10, 50)
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 1
    font_color = (0, 255, 0)
    thickness = 2
    
    cv2.putText(frame, text, position, font, font_scale, font_color, thickness, cv2.LINE_AA)
    frameGris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    if not ret:
        print("No se pudo recibir el frame. Saliendo...")
        break


    cv2.imshow("Mi camra en vivo", frameGris)
    if cv2.waitKey(1) == ord("q"):
        break

cap.release()
cv2.destroyAllWindows() 

print("Recursos liberados y programa finalizado.")