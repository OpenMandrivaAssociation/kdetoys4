Name:          kdetoys4
Summary:       K Desktop Environment - Toys and Amusements
Version:       4.0.73
Epoch:         1
URL:           ftp://ftp.kde.org/pub/kde/stable/%version/src/
Release:       %mkrel 1
Source:        ftp://ftp.kde.org/pub/kde/stable/%version/src/kdetoys-%version.tar.bz2
Group:         Graphical desktop/KDE
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-buildroot
License:       GPL
BuildRequires: kdelibs4-devel >= %version
BuildRequires: kdebase4-workspace-devel >= %version
BuildRequires: qimageblitz-devel

%description
Toys for the K Desktop Environment.

Software included in this package are:
	- amor: Amusing Misuse Of Resources put's comic figures above your windows
	- kteatime: system tray applet that makes sure your tea doesn't get too strong
	- ktux: Tux-in-a-Spaceship screen saver
	- kweather: plasma applet that will display the current weather outside
	- kworldclock: application and plasma applet showing daylight area on the
	  world globe

#-------------------------------------------------------------------

%package -n     kweather
Group:          Graphical desktop/KDE
Summary:        Plasma applet that will display the current weather outside 
Provides:       kweather4
Obsoletes:      kde4-kweather < 1:4.0.68
Provides:       kde4-kweather = %epoch:%version

%description -n kweather
Plasma applet that will display the current weather outside

%files -n kweather
%defattr(-,root,root)
%_kde_bindir/kweatherreport
%_kde_bindir/kweatherservice
%_kde_libdir/libkdeinit4_kweatherreport.so
%dir %_kde_appsdir/kweather
%_kde_appsdir/kweather/*.png
%_kde_appsdir/kweatherservice/stations.dat
%_kde_appsdir/kweatherservice/weather_stations.desktop
%_kde_iconsdir/hicolor/*/apps/kweather.png   
%_kde_datadir/kde4/services/kweatherservice.desktop
%_kde_libdir/kde4/kcm_weather.so
%_kde_libdir/kde4/kcm_weatherservice.so
%_datadir/dbus-1/interfaces/org.kde.kweather.kweather.xml
%_datadir/dbus-1/interfaces/org.kde.kweather.service.xml
%_kde_docdir/*/*/kweather

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
%_kde_datadir/kde4/services/kcmweather.desktop
%_kde_datadir/kde4/services/kcmweatherservice.desktop
%dir %_kde_appsdir/amor
%_kde_appsdir/amor/*
%_kde_iconsdir/hicolor/*/apps/amor.png
%_datadir/dbus-1/interfaces/org.kde.amor.xml
%_kde_docdir/*/*/amor

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
%dir %_kde_appsdir/ktux
%dir %_kde_appsdir/ktux/sprites
%_kde_appsdir/ktux/sprites/spriterc
%_kde_appsdir/ktux/sprites/*.png
%_kde_iconsdir/hicolor/*/apps/ktux.png
%_kde_datadir/kde4/services/ScreenSavers/ktux.desktop

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
%dir %_kde_appsdir/kteatime
%_kde_appsdir/kteatime/kteatime.notifyrc
%_kde_datadir/applications/kde4/kteatime.desktop
%_kde_iconsdir/hicolor/*/apps/kteatime.png
%_kde_docdir/*/*/kteatime

#-------------------------------------------------------------------

%package -n kworldclock
Group:      Graphical desktop/KDE
Summary:    Application and plasma applet showing daylight area on the world globe
Provides:   kworldclock4
Conflicts:  kdetoys4 < 3.97.1-0.745233.1
Obsoletes:  kde4-kworldclock < 1:4.0.68
Provides:   kde4-kworldclock = %epoch:%version

%description -n kworldclock
TODO

%files -n kworldclock
%defattr(-,root,root)
%_kde_bindir/kworldclock
%_kde_datadir/applications/kde4/kworldclock.desktop
%_kde_appsdir/kworldclock/pics
%_kde_appsdir/kworldclock/maps
%_kde_appsdir/kworldclock/zone.tab
%_kde_iconsdir/hicolor/*/apps/kworldclock.png
%_kde_docdir/*/*/kworldclock


#-------------------------------------------------------------------

%define  kworldclock_major 4
%define  libkworldclock %mklibname kworldclock %kworldclock_major

%package -n %libkworldclock
Summary:    KDE 4 core library
Group:      System/Libraries

%description -n %libkworldclock
KDE 4 core library.

%post -n   %libkworldclock -p /sbin/ldconfig
%postun -n %libkworldclock -p /sbin/ldconfig

%files -n %libkworldclock
%defattr(-,root,root)
%_kde_libdir/libkworldclock.so.%{kworldclock_major}*

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
%_kde_includedir/kworldclock
%_kde_libdir/libkworldclock.so

#-------------------------------------------------------------------

%prep
%setup -q -n kdetoys-%version

%build
%cmake_kde4

%make

%install
rm -fr %buildroot
make -C build DESTDIR=%buildroot install


%clean
rm -fr %buildroot
