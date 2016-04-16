Name:           ros-indigo-monocam-settler
Version:        0.10.14
Release:        0%{?dist}
Summary:        ROS monocam_settler package

Group:          Development/Libraries
License:        BSD
URL:            http://www.ros.org/wiki/monocam_settler
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-actionlib
Requires:       ros-indigo-actionlib-msgs
Requires:       ros-indigo-rosconsole
Requires:       ros-indigo-roscpp-serialization
Requires:       ros-indigo-settlerlib
Requires:       ros-indigo-std-msgs
BuildRequires:  ros-indigo-actionlib
BuildRequires:  ros-indigo-actionlib-msgs
BuildRequires:  ros-indigo-catkin >= 0.5.68
BuildRequires:  ros-indigo-rosconsole
BuildRequires:  ros-indigo-roscpp-serialization
BuildRequires:  ros-indigo-settlerlib
BuildRequires:  ros-indigo-std-msgs

%description
Listens on a ImageFeatures topic, and waits for the data to settle. This package
is experimental and unstable. Expect its APIs to change.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Sat Apr 16 2016 Vincent Rabaud <vincent.rabaud@gmail.com> - 0.10.14-0
- Autogenerated by Bloom

