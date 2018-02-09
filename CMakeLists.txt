cmake_minimum_required(VERSION 2.8.12)
project(chainercv)

find_package(catkin REQUIRED COMPONENTS catkin_pip)

# defining current package as a package that should be managed by pip (not catkin - even though we make it usable with workspaces)
catkin_pip_package_virtualenv(${PROJECT_NAME})
# CAREFUL : all projects for test here will share the same workspace. pip might have conflicts...

# # We need to install the project pip dependencies in the devel workspace being created
# catkin_pip_requirements(${CMAKE_CURRENT_SOURCE_DIR}/requirements.txt)
