#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist


# class DrawCircleNode(Node):

#     def __init__(self):
#         super().__init__("Circle")
#         self.cmd_vel_pub = self.create_publisher(Twist, "/turtle1/cmd_vel",10) 
#         self.timer = self.create_timer(0.5,self.send_velocity_command)
#         self.get_logger().info("Draw cicle node has started Bruh!!")

#     def send_velocity_command(self):
#         msg = Twist()
#         msg.linear.x = 2.0
#         msg.angular.z = 1.0
#         self.cmd_vel_pub.publish(msg)

# def main(args=None):
#     rclpy.init(args=args)
#     node = DrawCircleNode()
#     rclpy.spin(node)
#     rclpy.shutdown()


class DrawCircleNode(Node):

    def __init__(self):
        super().__init__("Circle")
        self.cmd_vel_pub = self.create_publisher(Twist, "/turtle1/cmd_vel",10) 
        self.timer = self.create_timer(0.5, self.send_velocity_command)

        self.mode = input("Enter A(circle) / B(square) / C(spiral): ").strip().upper()
        self.counter = 0
        self.spiral_speed = 0.5

        self.get_logger().info("Draw cicle node has started Bruh!!")

    def send_velocity_command(self):
        msg = Twist()

        # Circle
        if self.mode == "A":
            msg.linear.x = 2.0
            msg.angular.z = 1.0

        # Square
        elif self.mode == "B":
            if self.counter < 3:             
                msg.linear.x = 1.5
                msg.angular.z = 0.0
            elif self.counter < 5:           
                msg.linear.x = 0.0
                msg.angular.z = 1.57
            else:
                self.counter = 0

            self.counter += 1


        # Outward Spiral
        elif self.mode == "C":
            msg.linear.x = self.spiral_speed
            msg.angular.z = 1.0
            self.spiral_speed += 0.1

        else:
            self.get_logger().warn("Invalid Selection! Use A / B / C!")

        self.cmd_vel_pub.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    node = DrawCircleNode()
    rclpy.spin(node)
    rclpy.shutdown()