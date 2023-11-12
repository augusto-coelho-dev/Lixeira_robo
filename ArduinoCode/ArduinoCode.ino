#include <Ultrasonic.h>
#include<Servo.h>
/*
 * Pass as a parameter the trigger and echo pin, respectively,
 * or only the signal pin (for sensors 3 pins), like:
 * Ultrasonic ultrasonic(13);
 */
Ultrasonic ultrasonic(12, 13);
int distance;
Servo myservo;
void setup() {
  Serial.begin(9600);
  myservo.attach(9);
}

void loop() {
  // Pass INC as a parameter to get the distance in inches
  distance = ultrasonic.read();

  delay(1000);
  if(distance<=20){
    Serial.print("objeto");
  }
  
  if (Serial.available() > 0) {
    // Verifica se há dados disponíveis na porta serial
    String mensagem = Serial.readString();  // Lê a mensagem da porta serial

    // Comparação da mensagem
    if (mensagem.equals("detectado")) {
      myservo.write(75);
      delay(3000);
    } else {
      Serial.println("Mensagem diferente de 'detectado'");
    }
  }else{
    myservo.write(0);
  }
}