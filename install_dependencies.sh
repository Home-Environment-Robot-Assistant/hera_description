#!/bin/bash

distribution=${1:-noetic} 

apt-get install -y ros-$distribution-joint-state-publisher-gui
