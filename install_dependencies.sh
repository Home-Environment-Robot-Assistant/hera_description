#!/bin/bash
# rode o comando 'apt-get update' antes de chamar esse script

apt-get install -y --no-install-recommends \
    apt-utils \
    ros-$ROS_DISTRO-xacro \
    ros-$ROS_DISTRO-joint-state-publisher-gui
