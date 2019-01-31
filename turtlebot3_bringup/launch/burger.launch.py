# /*******************************************************************************
# * Copyright 2017 ROBOTIS CO., LTD.
# *
# * Licensed under the Apache License, Version 2.0 (the "License");
# * you may not use this file except in compliance with the License.
# * You may obtain a copy of the License at
# *
# *     http://www.apache.org/licenses/LICENSE-2.0
# *
# * Unless required by applicable law or agreed to in writing, software
# * distributed under the License is distributed on an "AS IS" BASIS,
# * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# * See the License for the specific language governing permissions and
# * limitations under the License.
# *******************************************************************************/

# /* Author: Darby Lim */

import os

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import ThisLaunchFileDir
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([ThisLaunchFileDir(), '/burger_state_publisher.launch.py']),
            launch_arguments={'use_sim_time': 'false'}.items(),
        ),

        Node(
            package='turtlebot3_node',
            node_executable='time_sync',
            node_name='time_sync_node',
            output='screen'),

        Node(
            package='turtlebot3_node',
            node_executable='odometry_publisher',
            node_name='odometry_publisher',
            output='screen'),

        Node(
            package='turtlebot3_node',
            node_executable='tf_publisher',
            node_name='tf_publisher',
            output='screen'),

        Node(
            package='turtlebot3_node',
            node_executable='joint_states_publisher',
            node_name='joint_states_publisher',
            output='screen'),

        Node(
            package='turtlebot3_node',
            node_executable='scan_publisher',
            node_name='scan_publisher',
            output='screen'),
    ])