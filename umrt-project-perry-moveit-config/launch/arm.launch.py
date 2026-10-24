from launch import LaunchDescription
from launch.actions import (
    DeclareLaunchArgument,
    IncludeLaunchDescription,
)
from launch.launch_description_sources import PythonLaunchDescriptionSource

from launch_ros.actions import Node
from moveit_configs_utils.launch_utils import (
    add_debuggable_node,
    DeclareBooleanLaunchArg,
)

from moveit_configs_utils import MoveItConfigsBuilder

def generate_launch_description():
    moveit_config = MoveItConfigsBuilder("project_perry", package_name="umrt-project-perry-moveit-config").to_moveit_configs()
    launch_package_path = moveit_config.package_path

    ld = LaunchDescription()
    ld.add_action(
        DeclareBooleanLaunchArg(
            "db",
            default_value=False,
            description="By default, we do not start a database (it can be large)",
        )
    )
    ld.add_action(
        DeclareBooleanLaunchArg(
            "debug",
            default_value=False,
            description="By default, we are not in debug mode",
        )
    )

    # Fake joint driver
    ld.add_action(
        Node(
            package="controller_manager",
            executable="ros2_control_node",
            parameters=[
                moveit_config.robot_description,
                str(moveit_config.package_path / "config/ros2_controllers.yaml"),
            ],
        )
    )

    ld.add_action(
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                str(launch_package_path / "launch/spawn_controllers.launch.py")
            ),
        )
    )

    # Gripper (can-ppm): bridge ROS <-> CAN for the PPM gateway, and spawn its controller on the same
    # controller_manager as the arm so both run together
    ld.add_action(
        Node(
            package="ros2_j1939_babbler",
            executable="static_bridge",
            parameters=[{"sensor_name": "arm/babbler"}],
            output="both",
            remappings=[("/from_can_bus", "/arm/from_can_bus"), ("/to_can_bus", "/arm/to_can_bus")],
        )
    )
    ld.add_action(
        Node(
            package="controller_manager",
            executable="spawner",
            arguments=["can_ppm_controller", "--controller-manager", "/controller_manager"],
        )
    )
    return ld