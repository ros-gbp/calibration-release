Name:           ros-jade-calibration-estimation
Version:        0.10.14
Release:        0%{?dist}
Summary:        ROS calibration_estimation package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/calibration_estimation
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       python-matplotlib
Requires:       ros-jade-calibration-msgs
Requires:       ros-jade-python-orocos-kdl
Requires:       ros-jade-rospy
Requires:       ros-jade-rostest
Requires:       ros-jade-sensor-msgs
Requires:       ros-jade-urdfdom-py
Requires:       ros-jade-visualization-msgs
Requires:       scipy
BuildRequires:  ros-jade-catkin >= 0.5.68

%description
Runs an optimization to estimate the a robot's kinematic parameters. This
package is a generic rewrite of pr2_calibration_estimation.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/jade" \
        -DCMAKE_PREFIX_PATH="/opt/ros/jade" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/jade

%changelog
* Sun Apr 17 2016 Vincent Rabaud <vincent.rabaud@gmail.com> - 0.10.14-0
- Autogenerated by Bloom

* Sun Jan 18 2015 Vincent Rabaud <vincent.rabaud@gmail.com> - 0.10.13-0
- Autogenerated by Bloom

