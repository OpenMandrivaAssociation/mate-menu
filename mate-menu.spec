Summary:	An Advanced Menu for the MATE Desktop 
Name:		mate-menu
Version:	22.04.2
Release:	1
License:	GPLv2+ and MIT
Group:		Graphical desktop/Other
Url:		https://github.com/ubuntu-mate/%{name}
Source0:	https://github.com/ubuntu-mate/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:	intltool
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(python-distutils-extra)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	desktop-file-utils

Requires:	mate-menus
Requires:	mate-panel
Requires:	mozo
Requires:	python%{pyver}dist(configobj)
Requires:	python%{pyver}dist(pygobject)
Requires:	python%{pyver}dist(pyxdg)
Requires:	python%{pyver}dist(python-xlib)
Requires:	python%{pyver}dist(setproctitle)
Requires:	python%{pyver}dist(unidecode)
Requires:	xdg-utils

BuildArch:	noarch

%description
An advanced menu for MATE. Supports filtering, favorites,
auto-session, and many other features.
This menu originated in the Linux Mint distribution and has
been ported to other distributions that ship the MATE Desktop
Environment.

%files -f %{name}.lang
%license COPYING
%doc README.md
%{_bindir}/%{name}
%{_usr}/lib/%{name}/
%{py_puresitedir}/mate_menu/
%{py_puresitedir}/mate_menu-*.*-info/
%{_datadir}/%{name}/
%{_datadir}/glib-2.0/schemas/org.mate.mate-menu*.gschema.xml
%{_datadir}/mate-panel/applets/org.mate.panel.MateMenuApplet.mate-panel-applet
%{_datadir}/dbus-1/services/org.mate.panel.applet.MateMenuAppletFactory.service
%{_mandir}/man1/mate-menu.1.*

#-----------------------------------------------------------------------

%prep
%autosetup -p1

%build
%py_build

%install
%py_install

# locales
%find_lang %{name} --with-gnome --all-name

