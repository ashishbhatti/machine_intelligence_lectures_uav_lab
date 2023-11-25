/*
   Control brightness of multiple LEDs
   Author: Ashish Kumar
   Date: Nov 20, 2023
   Venue: UAV Lab, IIT Kanpur
*/


#define numOfValsRec 2                                        // The number of values we are receiving, to define array       
#define digitsPerValRec 3


int valsRec[numOfValsRec];                                     // array to store the values received
int stringLength = numOfValsRec * digitsPerValRec + 1;         // 1 is for dollar sign, example string '$055255'
int counter = 0;                                              // for reading the elements of array string
bool counterStart = false;                                    // to check if counter started
String receivedString;


void setup() {
  // put your setup code here, to run once:
  // here using only 1 LED that too internal, but receiving vals for 2 LEDs
  pinMode(13, OUTPUT);                                        
  Serial.begin(9600);                                         // This value should match the python script
}  


void receiveData() {
  /*
     Creating receivedString variable,
     reading one element at a time from serial.
     Directly changing the receivedString, so no return required.
  */
  while (Serial.available()) {
    char c = Serial.read();
    if (c == '$') {
      counterStart = true;
    }
    if (counterStart) {

      // read the data till the number of characters read is less than stringlength
      if (counter < stringLength) {
        receivedString = String(receivedString + c);
        counter++;
      }

      // parse the read data and convert them to ints
      if (counter >= stringLength) {
        for (int i = 0; i < numOfValsRec; i++) {
          int num = i * digitsPerValRec + 1;
          valsRec[i] = receivedString.substring(num, num + digitsPerValRec).toInt();                       // start at 2nd index, break at 5th index
        }

        // reset the params
        receivedString = "";
        counter = 0;
        counterStart = false;
      }
    }
  }
}

void loop() {
  // put your main code here, to run repeatedly:

  receiveData();

  // LED on-off depending on the values received
  if (valsRec[1] == 255) {
    digitalWrite(13, HIGH);
  }
  else {
    digitalWrite(13, LOW);
  }
}
