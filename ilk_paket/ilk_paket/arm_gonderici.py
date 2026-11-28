import math
import rclpy
from rclpy.node import Node
from rclpy.qos import (QoSProfile, ReliabilityPolicy,
                       DurabilityPolicy, HistoryPolicy)
from px4_msgs.msg import VehicleCommand


class ArmGonderici(Node):
    def __init__(self):
        super().__init__('arm_gonderici')

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

    def komut_yolla(self, komut, p1=0.0, p2=0.0, p7=0.0):
        msg = VehicleCommand()
        msg.timestamp = int(self.get_clock().now().nanoseconds / 1000)
        msg.command = komut
        msg.param1 = p1
        msg.param2 = p2
        msg.param7 = p7
        msg.target_system = 1
        msg.target_component = 1
        msg.source_system = 1
        msg.source_component = 1
        msg.from_external = True
        self.pub.publish(msg)

    def gonder(self):
        if self.sayac < 3:
            self.komut_yolla(
                VehicleCommand.VEHICLE_CMD_COMPONENT_ARM_DISARM, p1=1.0)
            self.get_logger().info('Arm komutu gonderildi')
        elif self.sayac == 3:
            self.komut_yolla(
                VehicleCommand.VEHICLE_CMD_NAV_TAKEOFF,
                p1=math.nan, p2=math.nan, p7=math.nan)
            self.get_logger().info('Kalkis komutu gonderildi')
        else:
            self.timer.cancel()
            self.get_logger().info('Bitti, Ctrl+C ile cikabilirsin')

        self.sayac += 1


def main(args=None):
    rclpy.init(args=args)
    node = ArmGonderici()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
