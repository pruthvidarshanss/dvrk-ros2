#!/usr/share/env python3

import os, xacro
from launch import LaunchDescription
from launch.actions import ExecuteProcess
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare

def generate_launch_description():
    package_name = FindPackageShare("urdf_dvrk").find("urdf_dvrk")

    world_file = os.path.join(package_name, "worlds", "config.world")

    xacro_file = os.path.join(package_name, "xacro", "dvrk.urdf.xacro")

    robot_description_raw = xacro.process_file(xacro_file).toxml()

    node_robot_state_publisher = Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        output="screen",
        arguments=["--verbose"],
        parameters=[{
            'robot_description': robot_description_raw,
            'use_sim_time': True,
        }]
    )

    jsp_node = Node(
        package="joint_state_publisher",
        executable="joint_state_publisher",
        name="joint_state_publisher",
    )

    spawn_entity = Node(
        package="gazebo_ros",
        executable="spawn_entity.py",
        output="screen",
        arguments=["-topic", "robot_description", "-entity", "dvrk"],
    )

    return LaunchDescription([
        ExecuteProcess(cmd=["gazebo", "-u", "--verbose", "-s", "libgazebo_ros_init.so", "-s", "libgazebo_ros_factory.so", world_file], output="screen"),
        jsp_node,
        node_robot_state_publisher,
        spawn_entity,
    ])