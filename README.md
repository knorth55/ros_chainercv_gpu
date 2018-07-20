# ChainerCV-ROS

The name of this project is **ChainerCV-ROS**.

Depends on https://github.com/locusrobotics/catkin_virtualenv

## Build 

```bash
mkdir catkin_ws/src -p
cd catkin_ws/src
git clone https://github.com/locusrobotics/catkin_virtualenv.git
git clone https://github.com/knorth55/catkin_pip_chainercv.git
cd ..
catkin build
```

## Run demo

Please build this using the standard build procedure of ROS.

```bash
# after build
source devel/setup.bash
rosrun chainercv python ssd_demo.py image.jpg
```
