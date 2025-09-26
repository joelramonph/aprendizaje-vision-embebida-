import cv2


cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: No se puede abrir la cámara.")
    exit()

while True:
    ret, frame = cap.read()

    if not ret:
        print("No se pudo recibir el frame. Saliendo...")
        break


    cv2.imshow("Mi camra en vivo", frame)
    if cv2.waitKey(1) == ord("q"):
        break

cap.release()
cv2.destroyAllWindows() 

print("Recursos liberados y programa finalizado.")