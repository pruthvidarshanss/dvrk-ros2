#!/usr/share/env python3

import os, xacro
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch_ros.substitutions import FindPackageShare
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution

def generate_launch_description():

    package_name = FindPackageShare("urdf_dvrk").find("urdf_dvrk")

    ld = LaunchDescription()

    default_model_path = os.path.join(package_name, "xacro", "ecm", "ecm.urdf.xacro")
    declare_model = DeclareLaunchArgument(name="model", default_value=default_model_path, description="Absolute path to model")
    ld.add_action(declare_model)

    default_rviz_config = os.path.join(package_name, "rviz", "config.rviz")
    declare_rviz = DeclareLaunchArgument(name="rviz", default_value=default_rviz_config, description="Default RVIZ 2 config")
    ld.add_action(declare_rviz)

    gui_arg = DeclareLaunchArgument(name="gui", default_value="true", choices=["true", "false"],
                                    description="Flag to enable joint_state_publisher_gui")
    ld.add_action(gui_arg)

    ld.add_action(IncludeLaunchDescription(
        PathJoinSubstitution([FindPackageShare("urdf_launch"), "launch", "display.launch.py"]),
        launch_arguments={
            "urdf_package": "urdf_dvrk",
            "urdf_package_path": LaunchConfiguration("model"),
            "rviz_config": LaunchConfiguration("rviz"),
            "jsp_gui": LaunchConfiguration("gui")
        }.items()
    ))

    return ld