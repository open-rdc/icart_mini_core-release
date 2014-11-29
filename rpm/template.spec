Name:           ros-indigo-icart-mini-driver
Version:        0.0.1
Release:        1%{?dist}
Summary:        ROS icart_mini_driver package

Group:          Development/Libraries
License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-controller-manager
Requires:       ros-indigo-hardware-interface
Requires:       ros-indigo-hokuyo-node
Requires:       ros-indigo-joy
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-teleop-twist-joy
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-controller-manager
BuildRequires:  ros-indigo-hardware-interface
BuildRequires:  ros-indigo-joy
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-teleop-twist-joy

%description
The icart_mini_driver package

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
* Tue Nov 25 2014 Daiki Maekawa <method_aspect_card@yahoo.co.jp> - 0.0.1-1
- Autogenerated by Bloom

* Tue Nov 25 2014 Daiki Maekawa <method_aspect_card@yahoo.co.jp> - 0.0.1-0
- Autogenerated by Bloom

