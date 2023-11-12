import serial
import threading
import cv2
import time
import time

# Pausa a execução do programa por 2 segundos

camera = cv2.VideoCapture(0)
classificador = cv2.CascadeClassifier(r'cascade/cokelogoorigfullds.xml')

porta = 'COM4'
velocidadeBaud = 9600

try:
    SerialArduino = serial.Serial(porta, velocidadeBaud, timeout=0.2)
except Exception as e:
    print("Verificar porta serial ou religar Arduino:", str(e))

def handle_data(data):
    print("Recebi: " + data)
    if data.strip() == "objeto":
        # Ativar a detecção de objeto por 5 segundos
        print("Ativando detecção de objeto por 5 segundos...")
        start_time = time.time()
        while time.time() - start_time < 5:
            check, img = camera.read()
            imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            objetos = classificador.detectMultiScale(imgGray)

            for x, y, l, a in objetos:
                cv2.rectangle(img, (x, y), (x + l, y + a), (255, 0, 0), 2)
                # Enviar mensagem "detectado" para o Arduino
                SerialArduino.write('detectado'.encode())
                time.sleep(2)

            cv2.imshow('Imagem', img)
            cv2.waitKey(1)
        print("Detecção de objeto desativada.")

def read_from_port(ser):
    while True:
        reading = ser.readline().decode()
        if reading != "":
            handle_data(reading)

lerSerialThread = threading.Thread(target=read_from_port, args=(SerialArduino,))
lerSerialThread.start()

while True:
    pass
