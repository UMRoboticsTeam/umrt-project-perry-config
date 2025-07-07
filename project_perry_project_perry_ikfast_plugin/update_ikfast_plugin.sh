search_mode=OPTIMIZE_MAX_JOINT
srdf_filename=project_perry.srdf
robot_name_in_srdf=project_perry
moveit_config_pkg=project_perry_moveit_config
robot_name=project_perry
planning_group_name=project_perry
ikfast_plugin_pkg=project_perry_project_perry_ikfast_plugin
base_link_name=base_link
eef_link_name=gripper_link
ikfast_output_path=/ws2/ik/project_perry_project_perry_ikfast_plugin/src/project_perry_project_perry_ikfast_solver.cpp

rosrun moveit_kinematics create_ikfast_moveit_plugin.py\
  --search_mode=$search_mode\
  --srdf_filename=$srdf_filename\
  --robot_name_in_srdf=$robot_name_in_srdf\
  --moveit_config_pkg=$moveit_config_pkg\
  $robot_name\
  $planning_group_name\
  $ikfast_plugin_pkg\
  $base_link_name\
  $eef_link_name\
  $ikfast_output_path
