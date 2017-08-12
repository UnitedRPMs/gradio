%global     commit     d5767082123e66968da1cdd924023ce5fc602b1d
%global     githash    %(c=%{commit}; echo ${c:0:7})
%global     gitdate    20170809

Name:       gradio
Version:    5.9
Release:    1.%{gitdate}%git%{githash}%{?dist}
Summary:    Internet radio app for Gnome users

Group:      Applications/Internet
License:    GPLv3
URL:        https://github.com/haecker-felix/gradio
Source:     https://github.com/haecker-felix/%{name}/archive/%{commit}/%{name}-v%{version}-%{githash}.tar.gz

BuildRequires:  vala
BuildRequires:  meson
BuildRequires:  ninja-build
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.14
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(libsoup-2.4)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(gstreamer-pbutils-1.0)
BuildRequires:  pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires:  intltool desktop-file-utils
BuildRequires:  libappstream-glib-devel
BuildRequires:  libappstream-glib-builder-devel
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(sqlite3)

Requires:       dconf
Requires:       gstreamer1-plugins-base-tools
Requires:       gstreamer1-plugins-base
Requires:       libappstream-glib
Requires:       sqlite-libs

%description
A GTK3 app for finding and listening to internet radio stations.

%prep -n
%setup -q -n %{name}-%{commit}

%build
mkdir build
cd build
meson .. --prefix /usr
%ninja_build

%install
cd build
%ninja_install
desktop-file-install --add-category=GTK %{buildroot}%{_datadir}/applications/de.haeckerfelix.%{name}.desktop

%find_lang gradio

%clean
rm -rf %{buildroot}

%post
%{_bindir}/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :

%postun
if [ $1 -eq 0 ]
then
    %{_bindir}/touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    %{_bindir}/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
    %{_bindir}/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :
fi

%posttrans
%{_bindir}/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :
%{_bindir}/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :

%files
%license LICENSE
%{_bindir}/%{name}
%{_datadir}/glib-2.0/schemas/*
%{_datadir}/applications/de.haeckerfelix.%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/de.haeckerfelix.gradio.*
%{_datadir}/icons/hicolor/symbolic/apps/de.haeckerfelix.gradio-symbolic.svg
%{_datadir}/appdata/de.haeckerfelix.gradio.appdata.xml
%{_datadir}/locale/*/LC_MESSAGES/%{name}.*

%changelog
* Sat Aug 12 2017 Pavlo Rudyi <paulcarroty at riseup.net> -  5.9-1
- Update to the latest snapshot
- New UI and search engine

* Mon Jan 02 2017 Pavlo Rudyi <paulcarroty at riseup.net> -  5.0.0-4
- Update to the latest snapshot

* Tue Nov 07 2016 Pavlo Rudyi <paulcarroty at riseup.net> -  5.0.0-2
- Update to 5.0.0b2

* Tue Sep 27 2016 Pavlo Rudyi <paulcarroty at riseup.net> -  5.0.0-1
- Update to the latest 5.0.0 beta 1

* Tue Sep 06 2016 Pavlo Rudyi <paulcarroty at riseup.net> -  4.0.1-3
- Update to the latest git snapshot

* Fri Aug 05 2016 Pavlo Rudyi <paulcarroty at riseup> -  4.0.1-2
- Update to the latest git snapshot
