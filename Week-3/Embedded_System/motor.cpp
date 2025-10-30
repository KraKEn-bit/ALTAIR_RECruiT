#include "motor.h"

int leftPin1;
int leftPin2;
int rightPin1;
int rightPin2;

void setupMotors(int lp1, int lp2, int rp1, int rp2) {
  leftPin1=lp1;
  leftPin2=lp2;
  rightPin1=rp1;
  rightPin2=rp2;

  pinMode(leftPin1, OUTPUT);
  pinMode(leftPin2, OUTPUT);
  pinMode(rightPin1, OUTPUT);
  pinMode(rightPin2, OUTPUT);
}
void forward(int pwm) {
  analogWrite(leftPin1, pwm);
  analogWrite(leftPin2, 0);
  analogWrite(rightPin1, pwm);
  analogWrite(rightPin2, 0);
}
void backward(int pwm) {
  analogWrite(leftPin1, 0);
  analogWrite(leftPin2, pwm);
  analogWrite(rightPin1, 0);
  analogWrite(rightPin2, pwm);
}

void stopMotors() {
  analogWrite(leftPin1, 0);
  analogWrite(leftPin2, 0);
  analogWrite(rightPin1, 0);
  analogWrite(rightPin2, 0);
}
