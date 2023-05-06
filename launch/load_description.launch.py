from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory

from launch_ros.descriptions import ParameterValue 
from launch.substitutions import Command

def generate_launch_description():

    return LaunchDescription([
        DeclareLaunchArgument('use_sim_time', default_value='true',description=''),
        DeclareLaunchArgument('robot_model',  default_value='hera_full',description=''),
        DeclareLaunchArgument('robot_name',   default_value='robot',description=''),
        DeclareLaunchArgument('init_pos_x',   default_value='0.0',description=''),
        DeclareLaunchArgument('init_pos_y',   default_value='0.0',description=''),
        DeclareLaunchArgument('init_pos_z',   default_value='0.0',description=''),
        DeclareLaunchArgument('init_yaw',     default_value='0.0',description=''),


        Node(
            name='spawn_entity',
            package='gazebo_ros',
            executable='spawn_entity.py',
            output='screen',
            arguments=[
                '-entity',LaunchConfiguration('robot_name'),
                '-x',LaunchConfiguration('init_pos_x'),
                '-y',LaunchConfiguration('init_pos_y'),
                '-Y',LaunchConfiguration('init_yaw'),
                # '-topic', 'robot_description'
                '-file',[get_package_share_directory('hera_description'),'/robots/',LaunchConfiguration('robot_model'),'.urdf']
            ]
        ),


        Node(
            name='robot_state_publisher',
            package='robot_state_publisher',
            executable='robot_state_publisher',
            output='screen',
            parameters=[{
                'use_sim_time': LaunchConfiguration('use_sim_time'), 
                'robot_description': ParameterValue(Command(['cat ', get_package_share_directory('hera_description'),'/robots/',LaunchConfiguration('robot_model'),'.urdf']), value_type=str),
            }],
        ),


        Node(
            name='joint_state_publisher',
            package='joint_state_publisher',
            executable='joint_state_publisher',
            output='screen',
            parameters=[
                {'use_sim_time': LaunchConfiguration('use_sim_time')}
            ]
        ),    

    ])