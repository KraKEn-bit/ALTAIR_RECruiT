# import rclpy
# from rclpy.node import Node
# from sensor_msgs.msg import Image
# from cv_bridge import CvBridge
# import cv2

# class VideoPublisher(Node):
#     def __init__(self):
#         super().__init__('video_publisher')
#         self.publisher_ = self.create_publisher(Image, 'video_frames', 10)
#         self.br = CvBridge()
#         self.cap = cv2.VideoCapture(0)  # Webcam

#         self.timer = self.create_timer(0.03, self.publish_frame)  # ~30 FPS

#     def publish_frame(self):
#         ret, frame = self.cap.read()
#         if ret:
#             self.publisher_.publish(self.br.cv2_to_imgmsg(frame, encoding='bgr8'))

# def main(args=None):
#     rclpy.init(args=args)
#     node = VideoPublisher()
#     rclpy.spin(node)
#     node.destroy_node()
#     rclpy.shutdown()

# if __name__ == '__main__':
#     main()


#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

class VideoPublisher(Node):
    def __init__(self):
        super().__init__('video_publisher')
        self.publisher_ = self.create_publisher(Image, 'camera_frames', 10)
        self.bridge = CvBridge()

        self.cap = cv2.VideoCapture("rtsp://admin:admin@192.168.0.104:1935")
        self.cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)  # minimize buffering

        if not self.cap.isOpened():
            self.get_logger().error("Cannot open RTSP stream!")
            exit(1)

        self.timer = self.create_timer(0.03, self.timer_callback)  # ~30 FPS

    def timer_callback(self):
        ret, frame = self.cap.read()
        if not ret:
            self.get_logger().warn("No frame received, skipping...")
            return
        msg = self.bridge.cv2_to_imgmsg(frame, encoding="bgr8")
        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = VideoPublisher()
    rclpy.spin(node)
    node.cap.release()
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
