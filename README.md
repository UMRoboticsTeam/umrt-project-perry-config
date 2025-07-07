# UMRT Project Perry Config
Monorepo of ROS packages for configuring the University of Manitoba Robotics Team's software to work with Project Perry.

Unlike most UMRT projects, this one deviates from the norm of one-package-per-repo.
This is because of how tightly coupled the packages here are.
Whenever a change is made to one config, it is likely to propagate into other configs, which becomes tedious to manage when they are all individually controlled and versioned.

For example, if a URDF is changed, that would affect the ros2_control configuration, the IKFast configuration, and the MoveIt configuration.
If each of these lived in separate repos, that is 4 PRs to create, 4 new versions which have to be deployed, and if one doesn't get updated somewhere it will cause major problems.
Thus, by organising these into a monorepo this is condensed to 1 PR, and 1 version to deploy/manage.

One unusual technique used in this project, which is used to avoid complicating the ros-build workflow with additional parameters, is to symlink the version file into each of the packages.

# UMRT Project Perry Description

This is the URDF and RViz files for the Project Perry robotics arm model.

# UMRT Project Perry MoveIt Config

This is the MoveIt2 config for interacting with the Project Perry robotic arm.
It was generated using the MoveIt Setup Assistant.

# UMRT Project Perry IKFast Plugin

This is the IKFast plugin MoveIt2 uses for computing inverse kinematic solutions for the Project Perry robotic arm.
Unlike other UMRT packages, the package name is separated with underscores instead of hyphens because the package is auto-generated and the generator uses underscores.
The package is generated using the moveit_kinematics auto_create_ikfast_moveit_plugin script according to the instructions [here](https://moveit.picknik.ai/main/doc/examples/ikfast/ikfast_tutorial.html).