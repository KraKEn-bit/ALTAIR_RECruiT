#include "motor.h"

void setup() {
  setupMotors(1, 2, 3, 4); 
}

void loop() {
  forward(200);
  delay(2000);

  stopMotors();
  delay(1000);

  backward(150);
  delay(2000);
}
