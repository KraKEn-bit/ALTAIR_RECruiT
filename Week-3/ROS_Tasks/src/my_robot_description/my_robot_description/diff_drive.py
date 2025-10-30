#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from sensor_msgs.msg import JointState

class DiffDrive(Node):
    def __init__(self):
        super().__init__('diff_drive')
        self.publisher_ = self.create_publisher(JointState, '/joint_states', 10)
        self.subscription = self.create_subscription(
            Twist,
            '/cmd_vel',
            self.cmd_vel_callback,
            10
        )
        self.wheel_separation = 0.3   # distance between left and right wheels
        self.wheel_radius = 0.08
        self.joint_state = JointState()
        self.joint_state.name = ['left_wheel_joint', 'right_wheel_joint']
        self.joint_state.position = [0.0, 0.0]

    def cmd_vel_callback(self, msg):
        linear = msg.linear.x
        angular = msg.angular.z

        # wheel velocities
        v_l = (2*linear - angular*self.wheel_separation)/2
        v_r = (2*linear + angular*self.wheel_separation)/2

        # velocity to rotation (assuming timestep ~0.1s)
        dt = 0.1
        self.joint_state.header.stamp = self.get_clock().now().to_msg()
        self.joint_state.position[0] += v_l / self.wheel_radius * dt
        self.joint_state.position[1] += v_r / self.wheel_radius * dt

        self.publisher_.publish(self.joint_state)

def main(args=None):
    rclpy.init(args=args)
    node = DiffDrive()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
