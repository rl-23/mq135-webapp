
const int aqsensor = A3;  //output of mq135 connected to A0 pin of Arduino

void setup() {

  Serial.begin (9600);      //begin serial communication with baud rate of 9600
}

void loop() {

  int ppm = analogRead(aqsensor); //read MQ135 analog outputs at A0 and store it in ppm
  delay(5000);  //print message in serail monitor
  Serial.println(ppm);            //print value of ppm in serial monitor


 
}
