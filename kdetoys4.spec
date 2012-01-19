Name: kdetoys4
Summary: K Desktop Environment - Toys and Amusements
Version: 4.8.0
Epoch: 1
URL: http://www.kde.org
Release: 1
Source: ftp://ftp.kde.org/pub/kde/unstable/%version/src/kdetoys-%{version}.tar.bz2
Group: Graphical desktop/KDE
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
License: GPL
BuildRequires: kdelibs4-devel >= 2:4.2.98
BuildRequires: kdebase4-workspace-devel >= 2:4.2.98
BuildRequires: qimageblitz-devel
Obsoletes: kworldclock < 1:4.0.74-1
Obsoletes: %{_lib}kworldclock4 < 1:4.0.74-1
Obsoletes: kde4-kworldclock < 1:4.0.68

%description
Toys for the K Desktop Environment.

Software included in this package are:
	- amor: Amusing Misuse Of Resources put's comic figures above your windows
	- kteatime: system tray applet that makes sure your tea doesn't get too strong
	- kweather: plasma applet that will display the current weather outside
    - ktux: Tux-in-a-Spaceship screen saver

#-------------------------------------------------------------------

%package -n ktux
Group:      Graphical desktop/KDE
Summary:    Tux-in-a-Spaceship screen saver
Provides:   ktux4
Conflicts:  kdetoys4 < 3.97.1-0.745233.1
Obsoletes:  kde4-ktux < 1:4.0.68
Provides:   kde4-ktux = %epoch:%version

%description -n ktux
Tux-in-a-Spaceship screen saver

%files -n ktux
%defattr(-,root,root)
%_kde_bindir/ktux
%_kde_appsdir/ktux
%_kde_iconsdir/hicolor/*/apps/ktux.png
%_kde_datadir/kde4/services/ScreenSavers/ktux.desktop

#-------------------------------------------------------------------

%package -n amor
Group:      Graphical desktop/KDE
Summary:    Amusing Misuse Of Resources put's comic figures above your windows
Provides:   amor4
Conflicts:  kdetoys4 < 3.97.1-0.745233.1
Obsoletes:  kde4-amor < 1:4.0.68
Provides:   kde4-amor = %epoch:%version

%description -n amor
Amusing Misuse Of Resources put's comic figures above your windows

%files -n amor
%defattr(-,root,root)
%_kde_bindir/amor
%_kde_datadir/applications/kde4/amor.desktop
%_kde_appsdir/amor
%_kde_iconsdir/hicolor/*/apps/amor.png
%_kde_docdir/*/*/amor
%_kde_mandir/man6/amor.6.*

#-------------------------------------------------------------------

%package -n kteatime
Group:      Graphical desktop/KDE
Summary:    System tray applet that makes sure your tea doesn't get too strong
Provides:   kteatime4
Conflicts:  kdetoys4 < 3.97.1-0.745233.1
Obsoletes:  kde4-kteatime < 1:4.0.68
Provides:   kde4-kteatime = %epoch:%version


%description -n kteatime
System tray applet that makes sure your tea doesn't get too strong

%files -n kteatime
%defattr(-,root,root)
%_kde_bindir/kteatime
%_kde_appsdir/kteatime
%_kde_datadir/applications/kde4/kteatime.desktop
%_kde_iconsdir/hicolor/*/apps/kteatime.*
%_kde_docdir/*/*/kteatime

#-------------------------------------------------------------------

%package    devel
Summary:    Header files for %name
Group:      Development/KDE and Qt
Provides:   %name-devel =  %epoch:%version-%release

%description  devel
This package includes the header files you will need to compile
applications for %name

%files devel
%defattr(-,root,root,-)
%_kde_datadir/dbus-1/interfaces/*

#-------------------------------------------------------------------

%prep
%setup -q -n kdetoys-%{version}

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

