import math
import rclpy
from rclpy.node import Node
from rclpy.qos import (QoSProfile, ReliabilityPolicy,
                       DurabilityPolicy, HistoryPolicy)
from px4_msgs.msg import VehicleStatus, VehicleLocalPosition


class IlkDinleyici(Node):
    def __init__(self):
        super().__init__('ilk_dinleyici')

        qos = QoSProfile(
            reliability=ReliabilityPolicy.BEST_EFFORT,
            durability=DurabilityPolicy.TRANSIENT_LOCAL,
            history=HistoryPolicy.KEEP_LAST,
            depth=1,
        )

        self.create_subscription(
            VehicleStatus,
            '/fmu/out/vehicle_status_v5',
            self.durum_geldi,
            qos,
        )

        self.create_subscription(
            VehicleLocalPosition,
            '/fmu/out/vehicle_local_position_v1',
            self.konum_geldi,
            qos,
        )

    def durum_geldi(self, msg):
        self.get_logger().info(
            f'DURUM arming={msg.arming_state} '
            f'nav_state={msg.nav_state} '
            f'vehicle_type={msg.vehicle_type}',
            throttle_duration_sec=1.0,
        )

    def konum_geldi(self, msg):
        irtifa = -msg.z  # PX4'te z asagi dogru pozitif (NED)
        hiz = math.sqrt(msg.vx ** 2 + msg.vy ** 2)
        self.get_logger().info(
            f'KONUM irtifa={irtifa:.1f} m  '
            f'yer_hizi={hiz:.1f} m/s  '
            f'x={msg.x:.1f} y={msg.y:.1f}',
            throttle_duration_sec=1.0,
        )


def main(args=None):
    rclpy.init(args=args)
    node = IlkDinleyici()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
