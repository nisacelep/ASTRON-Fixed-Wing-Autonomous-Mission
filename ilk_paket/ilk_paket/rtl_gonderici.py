import rclpy
from rclpy.node import Node
from rclpy.qos import (QoSProfile, ReliabilityPolicy,
                       DurabilityPolicy, HistoryPolicy)
from px4_msgs.msg import VehicleCommand


class RtlGonderici(Node):
    def __init__(self):
        super().__init__('rtl_gonderici')

        qos = QoSProfile(
            reliability=ReliabilityPolicy.BEST_EFFORT,
            durability=DurabilityPolicy.TRANSIENT_LOCAL,
            history=HistoryPolicy.KEEP_LAST,
            depth=1,
        )

        self.pub = self.create_publisher(
            VehicleCommand, '/fmu/in/vehicle_command_v1', qos)

        self.sayac = 0
        self.timer = self.create_timer(1.0, self.gonder)

    def gonder(self):
        if self.sayac < 3:
            msg = VehicleCommand()
            msg.timestamp = int(self.get_clock().now().nanoseconds / 1000)
            msg.command = VehicleCommand.VEHICLE_CMD_NAV_RETURN_TO_LAUNCH
            msg.target_system = 1
            msg.target_component = 1
            msg.source_system = 1
            msg.source_component = 1
            msg.from_external = True
            self.pub.publish(msg)
            self.get_logger().info('RTL komutu gonderildi')
        else:
            self.timer.cancel()
            self.get_logger().info('Bitti, Ctrl+C ile cikabilirsin')
        self.sayac += 1


def main(args=None):
    rclpy.init(args=args)
    node = RtlGonderici()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
