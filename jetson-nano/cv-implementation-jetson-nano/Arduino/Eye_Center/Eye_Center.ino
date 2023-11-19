#include <Servo.h>


// create servo object to control a servo
Servo myservoLR;                 // left-right
Servo myservoUD;                 // up-down

int angle = 0;

void setup() {
  myservoLR.attach(9);  // attaches the servo object to pin 9
  myservoUD.attach(10);

  myservoLR.write(10);
//    delay(100);
    myservoUD.write(10);
}

void loop() {

//  // for centering the servos
 myservoLR.write(90);
 myservoUD.write(90);

//  // for trying out the range, with the assembly setup
//  // for left right range
//  // delays are just to help us visualize, 
//  // not to give time to servo to move before the next command
//  myservoLR.write(90+35);
//  delay(1000);
//  myservoLR.write(90);
//  delay(1000);
//  myservoLR.write(90-35);
//  delay(1000);
//  myservoLR.write(90);
//  delay(1000);

//   // for the Up down range
//   myservoUD.write(90+45);
//   delay(1000);
//   myservoUD.write(90);
//   delay(1000);
//   myservoUD.write(90-45);
//   delay(1000);
//   myservoUD.write(90);
//   delay(1000);
//   for (angle = 0; angle <= 180; angle += 1){
//    myservoLR.write(angle);
//   delay(100);
//   }
//    myservoLR.write(90);
//    delay(100);
//    myservoUD.write(90);

}
