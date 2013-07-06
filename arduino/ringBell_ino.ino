/* door bell ringer for arduino. 
   xtal@hackeriet.no, 2012-10-13 */

int outPin = 8;

int incomingByte = 0;
char inLetter = 'A';

void setup()
{
  Serial.begin(9600);  
  pinMode(outPin, OUTPUT);
  digitalWrite(outPin, LOW);
}

void loop()
{
  if (Serial.available() > 0) {
     incomingByte = Serial.read();
     inLetter = incomingByte;
     if (inLetter == 'R') {
       ring();
     }
     else if (inLetter == 'Z') {
       alarm();
     }
     Serial.println(inLetter);
  }
}

void ring()
{
  Serial.println("ringing");
  digitalWrite(outPin, HIGH);
  delay(200);
  digitalWrite(outPin, LOW);
  delay(50);
}

void alarm()
{
  int i;
  int times = 20;
  Serial.println("alarming");
  for(i=0;i<=times;i++) {
    digitalWrite(outPin, HIGH);
    delay(50);
    digitalWrite(outPin, LOW);
    delay(50);
  }
}



