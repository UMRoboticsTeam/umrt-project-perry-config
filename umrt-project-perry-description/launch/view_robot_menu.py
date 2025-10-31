#!/usr/bin/env python3

import subprocess

# Define the available robot configs, 1 is for the rover, and 2 is for the arm
robots = {
    "1": {
        "name": "Rover",
        "description_package": "umrt-project-perry-description",
        "description_file": "diffbot.urdf.xacro",
        "rviz_config": "diffbot_view.rviz",
    },
    "2": {
        "name": "Arm",
        "description_package": "umrt-project-perry-description",
        "description_file": "project_perry.urdf.xacro",
        "rviz_config": "project_perry_view.rviz",
    },
}

# Main Function
def main():
    # UI, lists all the robots config to show on rviz
    print("=== Select Robot to View ===")
    for key, robot in robots.items():
        print(f"{key}. {robot['name']}")
    print("============================")

    choice = input("Enter your choice: ").strip()

    # Invalid
    if choice not in robots:
        print("Invalid choice.")
        return

    robot = robots[choice]
    print(f"\nLaunching {robot['name']} in RViz...")

    # Launch command
    cmd = [
        "ros2", "launch", "umrt-project-perry-description", "view_robot.launch.py",
        f"description_package:={robot['description_package']}",
        f"description_file:={robot['description_file']}",
        f"gui:=true"
    ]

    subprocess.run(cmd)

if __name__ == "__main__":
    main()
