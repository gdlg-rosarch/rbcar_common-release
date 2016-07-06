Name:           ros-indigo-rbcar-common
Version:        1.0.4
Release:        0%{?dist}
Summary:        ROS rbcar_common package

Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/rbcar_common
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-indigo-rbcar-description
Requires:       ros-indigo-rbcar-pad
BuildRequires:  ros-indigo-catkin

%description
The rbcar_common package. It contains RBCAR common packages

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
* Wed Jul 06 2016 Román Navarro <rnavarro@robotnik.es> - 1.0.4-0
- Autogenerated by Bloom

* Tue Jul 05 2016 Carlos Villar <cvillar@robotnik.es> - 1.0.3-0
- Autogenerated by Bloom

* Mon Jul 04 2016 Carlos Villar <cvillar@robotnik.es> - 1.0.2-0
- Autogenerated by Bloom

* Mon Jul 04 2016 Carlos Villar <cvillar@robotnik.es> - 1.0.1-0
- Autogenerated by Bloom

