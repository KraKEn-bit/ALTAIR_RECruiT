#ifndef MOTOR_H
#define MOTOR_H

#include <Arduino.h>

void setupMotors(int lp1, int lp2, int rp1, int rp2);
void forward(int pwm);
void backward(int pwm);
void stopMotors();

#endif
