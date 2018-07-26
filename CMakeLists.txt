cmake_minimum_required(VERSION 2.8.12)
project(chainercv)

# Make sure to find-package `catkin_virtualenv`
find_package(catkin REQUIRED catkin_virtualenv)

# Must be called before catkin_generate_virtualenv
catkin_package()

# Generate the virtualenv, optionally with python 3 as the default interpreter:
catkin_generate_virtualenv(
  PYTHON_VERSION_MAJOR 2
  USE_SYSTEM_PACKAGES TRUE
  ISOLATE_REQUIREMENTS FALSE
  EXTRA_PIP_ARGS "-qq" "--no-binary=:all")
# catkin_generate_virtualenv(PYTHON3)

# Make sure your python executables are installed using `catkin_install_python`:
catkin_install_python(
  PROGRAMS
  scripts/ssd_demo.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})

install(FILES requirements.txt
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION})
