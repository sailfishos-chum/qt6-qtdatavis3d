%global  qt_version 6.7.2

Summary: Qt6 - Qt Data Visualization component
Name:    qt6-qtdatavis3d
Version: 6.7.2
Release: 2%{?dist}

License: GPL-3.0-only WITH Qt-GPL-exception-1.0
Url:     http://www.qt.io
Source0: %{name}-%{version}.tar.bz2

BuildRequires: cmake
BuildRequires: clang
BuildRequires: ninja
BuildRequires: qt6-qtbase-devel >= %{qt_version}
BuildRequires: qt6-qtbase-private-devel
%{?_qt6:Requires: %{_qt6}%{?_isa} = %{_qt6_version}}
BuildRequires: qt6-qtdeclarative-devel >= %{qt_version}
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: openssl-devel

%description
Qt Data Visualization module provides multiple graph types to visualize data in
3D space both with C++ and Qt Quick 2.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: qt6-qtbase-devel%{?_isa}
Requires: qt6-qtdeclarative-devel%{?_isa}
%description devel
%{summary}.

%prep
%autosetup -n %{name}-%{version}/upstream -p1


%build
%cmake_qt6 \
    -DQT_BUILD_EXAMPLES:BOOL=OFF \
    -DQT_INSTALL_EXAMPLES_SOURCES=OFF

%cmake_build

%install
%cmake_install

%files
%license LICENSES/GPL*
%{_qt6_libdir}/libQt6DataVisualization.so.6*
%{_qt6_libdir}/libQt6DataVisualizationQml.so.6*
%{_qt6_qmldir}/QtDataVisualization/

%files devel
%dir %{_qt6_libdir}/cmake/Qt6DataVisualization
%dir %{_qt6_libdir}/cmake/Qt6DataVisualizationQml
%{_qt6_headerdir}/QtDataVisualization/
%{_qt6_headerdir}/QtDataVisualizationQml/
%{_qt6_libdir}/libQt6DataVisualization.so
%{_qt6_libdir}/libQt6DataVisualization.prl
%{_qt6_libdir}/libQt6DataVisualizationQml.prl
%{_qt6_libdir}/libQt6DataVisualizationQml.so
%{_qt6_libdir}/cmake/Qt6DataVisualization/*.cmake
%{_qt6_libdir}/cmake/Qt6DataVisualizationQml/*.cmake
%{_qt6_archdatadir}/mkspecs/modules/*
%{_qt6_libdir}/cmake/Qt6BuildInternals/StandaloneTests/QtDataVisualizationTestsConfig.cmake
%{_qt6_libdir}/cmake/Qt6Qml/QmlPlugins/*.cmake
%{_qt6_libdir}/qt6/modules/*.json
%{_qt6_libdir}/qt6/metatypes/qt6*_metatypes.json
%{_qt6_libdir}/pkgconfig/*.pc
