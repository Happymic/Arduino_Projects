#include <Arduino.h>
/***
 * L298N 驱动
//  IN1 IN2 ->  左轮（OUT1，OUT2）
IN1   IN2   马达状态
0     0     制动
0     1     正转
1     0     反转
1     1     制动

//  IN3 IN4 ->  左轮（OUT3，OUT4）
IN3   IN4   马达状态
0     0     制动
0     1     正转
1     0     反转
1     1     制动
***/

void forward(int IN1, int IN2, int IN3, int IN4)
{
  digitalWrite(IN1, LOW);
  digitalWrite(IN2, HIGH);
  digitalWrite(IN3, LOW);
  digitalWrite(IN4, HIGH);
}

void backward(int IN1, int IN2, int IN3, int IN4)
{
  digitalWrite(IN1, HIGH);
  digitalWrite(IN2, LOW);
  digitalWrite(IN3, HIGH);
  digitalWrite(IN4, LOW);
}

void left(int IN1, int IN2, int IN3, int IN4)
{
  digitalWrite(IN1, HIGH);
  digitalWrite(IN2, LOW);
  digitalWrite(IN3, LOW);
  digitalWrite(IN4, HIGH);
}

void right(int IN1, int IN2, int IN3, int IN4)
{
  digitalWrite(IN1, LOW);
  digitalWrite(IN2, HIGH);
  digitalWrite(IN3, HIGH);
  digitalWrite(IN4, LOW);
}

void stop(int IN1, int IN2, int IN3, int IN4)
{
  digitalWrite(IN1, HIGH);
  digitalWrite(IN2, HIGH);
  digitalWrite(IN3, HIGH);
  digitalWrite(IN4, HIGH);
}
