# UMRT Project Perry Config
Monorepo of ROS packages for configuring the University of Manitoba Robotics Team's software to work with Project Perry.

Unlike most UMRT projects, this one deviates from the norm of one-package-per-repo.
This is because of how tightly coupled the packages here are.
Whenever a change is made to one config, it is likely to propagate into other configs, which becomes tedious to manage when they are all individually controlled and versioned.

For example, if a URDF is changed, that would affect the ros2_control configuration, the IKFast configuration, and the MoveIt configuration.
If each of these lived in separate repos, that is 4 PRs to create, 4 new versions which have to be deployed, and if one doesn't get updated somewhere it will cause major problems.
Thus, by organising these into a monorepo this is condensed to 1 PR, and 1 version to deploy/manage.