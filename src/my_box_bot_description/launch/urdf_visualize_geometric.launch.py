import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    urdf_file = 'box_bot_geometric.urdf'
    package_description = 'my_box_bot_description'

    print("Fetching URDF ==>")
    robot_desc_path = os.path.join(get_package_share_directory(package_description), "urdf", urdf_file)
    # Node for robot_state_publisher
    robot_state_publisher_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher_node',
        emulate_tty=True,
        parameters=[{
            'use_sim_time': True, 
            'robot_description': open(robot_desc_path).read()  # Read the URDF file directly
        }],
        output="screen"
    )

    # Path to the RViz config file
    rviz_config_dir = os.path.join(get_package_share_directory(package_description), 'rviz', 'urdf_vis.rviz')

    # Node for RViz
    rviz_node = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz_node',
        output='screen',
        parameters=[{'use_sim_time': True}],
        arguments=['-d', rviz_config_dir]
    )
    joint_state_publisher_node= Node(
    package='joint_state_publisher_gui',
    executable='joint_state_publisher_gui',
    output='screen'
    )

    return LaunchDescription([
        robot_state_publisher_node,
        rviz_node
    ])
