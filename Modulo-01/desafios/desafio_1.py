import cv2


cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: No se puede abrir la cámara.")
    exit()

while True:
    ret, frame = cap.read()
    cv2.putText(frame, "En vivo", (10, 50), cv2.FONT_HERSHEY_SIMPLEX,1, (0, 255, 0), 2, cv2.LINE_AA)
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