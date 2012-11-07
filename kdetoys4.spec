Name:		kdetoys4
Version: 4.9.3
Release: 1
Epoch:		1
Summary:	K Desktop Environment - Toys and Amusements
Group:		Graphical desktop/KDE
License:	GPL
URL:		http://www.kde.org
Source:		ftp://ftp.kde.org/pub/kde/stable/%{version}/src/kdetoys-%{version}.tar.xz
BuildRequires:	kdelibs4-devel
BuildRequires:	kdebase4-workspace-devel
BuildRequires:	pkgconfig(qimageblitz)

%description
Toys for the K Desktop Environment.

Software included in this package are:
	- amor: Amusing Misuse Of Resources put's comic figures above your windows
	- kteatime: system tray applet that makes sure your tea doesn't get too strong
	- kweather: plasma applet that will display the current weather outside
	- ktux: Tux-in-a-Spaceship screen saver

#-------------------------------------------------------------------

%package -n ktux
Group:		Graphical desktop/KDE
Summary:	Tux-in-a-Spaceship screen saver
Provides:	ktux4
Provides:	kde4-ktux = %{EVRD}

%description -n ktux
Tux-in-a-Spaceship screen saver

%files -n ktux
%{_kde_bindir}/ktux
%{_kde_appsdir}/ktux
%{_kde_iconsdir}/hicolor/*/apps/ktux.png
%{_kde_services}/ScreenSavers/ktux.desktop

#-------------------------------------------------------------------

%package -n amor
Group:		Graphical desktop/KDE
Summary:	Amusing Misuse Of Resources put's comic figures above your windows
Provides:	amor4
Provides:	kde4-amor = %{EVRD}

%description -n amor
Amusing Misuse Of Resources put's comic figures above your windows

%files -n amor
%{_kde_bindir}/amor
%{_kde_applicationsdir}/amor.desktop
%{_kde_appsdir}/amor
%{_kde_iconsdir}/hicolor/*/apps/amor.png
%{_kde_docdir}/*/*/amor
%{_kde_mandir}/man6/amor.6.*

#-------------------------------------------------------------------

%package -n kteatime
Group:		Graphical desktop/KDE
Summary:	System tray applet that makes sure your tea doesn't get too strong
Provides:	kteatime4
Provides:	kde4-kteatime = %{EVRD}


%description -n kteatime
System tray applet that makes sure your tea doesn't get too strong

%files -n kteatime
%{_kde_bindir}/kteatime
%{_kde_appsdir}/kteatime
%{_kde_applicationsdir}/kteatime.desktop
%{_kde_iconsdir}/hicolor/*/apps/kteatime.*
%{_kde_docdir}/*/*/kteatime

#-------------------------------------------------------------------

%package devel
Summary:	Header files for %{name}
Group:		Development/KDE and Qt
Provides:	%{name}-devel = %{EVRD}

%description devel
This package includes the header files you will need to compile
applications for %{name}

%files devel
%{_kde_datadir}/dbus-1/interfaces/*

#-------------------------------------------------------------------

%prep
%setup -q -n kdetoys-%{version}

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

