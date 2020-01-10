
#include <Servo.h>
#include <EEPROM.h>
#include <SoftwareSerial.h>
#define OUVERT 1
#define FERME 2

SoftwareSerial mySerial(10, 11); // RX, TX

Servo servo;
char state;

void setup() {
  // put your setup code here, to run once:
  servo.attach(7);
  pinMode(LED_BUILTIN, OUTPUT);

  EEPROM.write(0,1);
  Serial.begin(9600);
  
  while (!Serial) {
    ; // attente de connexion
  }

  if(EEPROM.read(0) == OUVERT) // 
  {                       
    servo.write(70); // tourne le moteur 
    delay(200);
  }
  else if(EEPROM.read(0) == FERME)
  {
    servo.write(120); // tourne le moteur 
    delay(200);
  }

  mySerial.begin(9600);
  
}

void loop() {

  if(mySerial.available() > 0)
  {
    char data;
    data = mySerial.read(); //stocage varriable recue par l'application android
    Serial.print(data);
    switch(data)
    {
      case '1': 
        if(EEPROM.read(0) == OUVERT) // EEPROM = 1 quand le verrou est ouvert
        {
          EEPROM.write(0, 2); // ecrit 2 pour retourner 0 à EEPROM. cette valeur va etre utilisée par arduino pour se rappeller le dernier etat dans lequel etait le loquet 
          mySerial.print("3"); 
          digitalWrite(LED_BUILTIN, HIGH);
          delay(200);
          digitalWrite(LED_BUILTIN, LOW);
          delay(200);
          for(int a = 70; a <= 120; a++) // ferme le loquet
          {
            servo.write(a);
            delay(15);
            mySerial.println(servo.read());
          }
        }
        else if(EEPROM.read(0) == FERME) 
        {
          EEPROM.write(0, 1); // ecrit 1 pour adresser 0 à EEPROM. meme fonction que si-dessus;
          mySerial.print("4"); // envoi le nombre 4 à l'application ce nombre sera utilisé pour mettre à jour la position du loquet
          for(int x = 120; x >= 70; x--) //ouvre le loquet
          {
            servo.write(x);
            delay(15);
          }
        }
        break;
      case '3': 
      // l'application demande à arduino de donner l'état actuel du loquet pour pouvoir changer l'icone fermée ou ouvert de l'application . 
        if(EEPROM.read(0) == OUVERT)
        {
          mySerial.print("4");
        }
        else if(EEPROM.read(0) == FERME)
        {
          mySerial.print("3");
        }
        break;
    }
  }
  
}
