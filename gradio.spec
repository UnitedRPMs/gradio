%global     commit     17b9e8bcb5fcbbd9863fd610f3e4109093017494
%global     githash    %(c=%{commit}; echo ${c:0:7})
%global     gitdate    20160801

Name:       gradio
Version:    4.0.1
Release:    2.%{gitdate}git%{githash}%{?dist}
Summary:    Internet radio app for Gnome users

Group:      Applications/Internet
License:    GPLv3
URL:        https://github.com/haecker-felix/gradio
Source:     https://github.com/haecker-felix/%{name}/archive/%{commit}/%{name}-v%{version}-%{githash}.tar.gz

BuildRequires:  vala
BuildRequires:  cmake
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.18
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(libsoup-2.4)
BuildRequires:  intltool desktop-file-utils libappstream-glib

Requires:       dconf


%description
A GTK3 app for finding and listening to internet radio stations.

%prep -n
%setup -q -n %{name}-%{commit}

%build
cmake -DCMAKE_INSTALL_PREFIX=/usr
make %{?_smp_mflags}

%install
%make_install
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
%find_lang %{name}

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

%files -f %{name}.lang
%{_bindir}/%{name}
%{_datadir}/glib-2.0/schemas/*
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.svg
%{_datadir}/%{name}/style/style.css

%changelog
* Fri Aug 05 2016 Pavlo Rudyi <paulcarroty at riseup> -  4.0.1-2
- Update to the latest git snapshot 
