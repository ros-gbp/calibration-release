Name:           ros-jade-calibration-launch
Version:        0.10.14
Release:        0%{?dist}
Summary:        ROS calibration_launch package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/calibration_launch
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-jade-interval-intersection
Requires:       ros-jade-joint-states-settler
Requires:       ros-jade-laser-cb-detector
Requires:       ros-jade-monocam-settler
Requires:       ros-jade-urdfdom-py
BuildRequires:  ros-jade-catkin

%description
This package contains a collection of launch files that can be helpful in
configuring the calibration stack to run on your robot.

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

