   //////////////////////////////////////////////
  //        ARDUINO SOIL MOISTURE DEMO        //
 //                                          //
//           http://www.educ8s.tv           //
/////////////////////////////////////////////



int sensorPin = A0;  
int sensorValue = 0;  
int percent = 0;

void setup() {
  Serial.begin(9600);
}

void loop() {
  
  sensorValue = analogRead(sensorPin);
  percent = convertToPercent(sensorValue);
  printValuesToSerial();
  delay(1000);
}

int convertToPercent(int value)
{
  int percentValue = 0;
  percentValue = map(value, 1023, 465, 0, 100);
  return percentValue;
}

void printValuesToSerial()
{
  Serial.print("\n\nAnalog Value: ");
  Serial.print(sensorValue);
  Serial.print("\nPercent: ");
  Serial.print(percent);
  Serial.print("%");
}

