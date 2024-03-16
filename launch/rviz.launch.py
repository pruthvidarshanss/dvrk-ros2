#!/usr/share/env python3

import os, xacro
from launch import LaunchDescription
from launch_ros.substitutions import FindPackageShare
from launch_ros.actions import Node

def generate_launch_description():

    package_name = FindPackageShare("urdf_dvrk").find("urdf_dvrk")

    xacro_path = os.path.join(package_name, "xacro", "dvrk.urdf.xacro")

    xacro_robot_description = xacro.process_file(xacro_path).toxml()

    rsp_node = Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        parameters=[{
            "robot_description": xacro_robot_description,
        }]
    )

    jsp_node = Node(
        package="joint_state_publisher_gui",
        executable="joint_state_publisher_gui",
        name="joint_state_publisher_gui",
    )

    rviz_config = os.path.join(package_name, "rviz", "rviz2.rviz")

    rviz_node = Node(
        package="rviz2",
        executable="rviz2",
        name="rviz2",
        output="screen",
        arguments=["-d", rviz_config],
    )

    return LaunchDescription([
        rsp_node,
        jsp_node,
        rviz_node,
    ])