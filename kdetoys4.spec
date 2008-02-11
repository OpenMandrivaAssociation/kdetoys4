Name:		kdetoys4
Summary:	K Desktop Environment - Toys and Amusements
Version:    4.0.1
Epoch:		1
URL:		ftp://ftp.kde.org/pub/kde/stable/%version/src/
Release:        %mkrel 1
Source: ftp://ftp.kde.org/pub/kde/stable/%version/src/kdetoys-%version.tar.bz2
Group:		Graphical desktop/KDE
BuildRoot:	%_tmppath/%name-%version-%release-root
License:	GPL
BuildRequires:	kdelibs4-devel >= %version

%description
Toys for the K Desktop Environment.

Software included in this package are:
	- amor: Amusing Misuse Of Resources put's comic figures above your windows
	- kteatime: system tray applet that makes sure your tea doesn't get too strong
	- ktux: Tux-in-a-Spaceship screen saver
	- kweather: plasma applet that will display the current weather outside
	- kworldclock: application and plasma applet showing daylight area on the world globe


#-------------------------------------------------------------------

%package -n kde4-kweather
Group:      Graphical desktop/KDE
Summary:    Plasma applet that will display the current weather outside 
Provides:   kweather4
Obsoletes:  %lib_name-kweather < 3.97.1-0.745233.1

%description -n kde4-kweather
Plasma applet that will display the current weather outside

%files -n kde4-kweather
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
%dir %_kde_docdir/HTML/en/kweather
%doc %_kde_docdir/HTML/en/kweather/index.cache.bz2
%doc %_kde_docdir/HTML/en/kweather/index.docbook

#-------------------------------------------------------------------

%package -n kde4-amor
Group:      Graphical desktop/KDE
Summary:    Amusing Misuse Of Resources put's comic figures above your windows
Provides:   amor4
Conflicts:  kdetoys4 < 3.97.1-0.745233.1

%description -n kde4-amor
Amusing Misuse Of Resources put's comic figures above your windows

%files -n kde4-amor
%defattr(-,root,root)
%_kde_bindir/amor
%_kde_datadir/applications/kde4/amor.desktop
%_kde_datadir/kde4/services/kcmweather.desktop
%_kde_datadir/kde4/services/kcmweatherservice.desktop
%dir %_kde_appsdir/amor
%_kde_appsdir/amor/*
%_kde_iconsdir/hicolor/*/apps/amor.png
%_datadir/dbus-1/interfaces/org.kde.amor.xml

%dir %_kde_docdir/HTML/en/amor
%doc %_kde_docdir/HTML/en/amor/*.png
%doc %_kde_docdir/HTML/en/amor/*.bz2
%doc %_kde_docdir/HTML/en/amor/*.docbook

#-------------------------------------------------------------------

%package -n kde4-ktux
Group:      Graphical desktop/KDE
Summary:    Tux-in-a-Spaceship screen saver
Provides:   ktux4
Conflicts:  kdetoys4 < 3.97.1-0.745233.1

%description -n kde4-ktux
Tux-in-a-Spaceship screen saver

%files -n kde4-ktux
%defattr(-,root,root)
%_kde_bindir/ktux
%dir %_kde_appsdir/ktux
%dir %_kde_appsdir/ktux/sprites
%_kde_appsdir/ktux/sprites/spriterc
%_kde_appsdir/ktux/sprites/*.png
%_kde_iconsdir/hicolor/*/apps/ktux.png
%_kde_datadir/kde4/services/ScreenSavers/ktux.desktop

#-------------------------------------------------------------------

%package -n kde4-kteatime
Group:      Graphical desktop/KDE
Summary:    System tray applet that makes sure your tea doesn't get too strong
Provides:   kteatime4
Conflicts:  kdetoys4 < 3.97.1-0.745233.1

%description -n kde4-kteatime
System tray applet that makes sure your tea doesn't get too strong

%files -n kde4-kteatime
%defattr(-,root,root)
%_kde_bindir/kteatime
%dir %_kde_appsdir/kteatime
%_kde_appsdir/kteatime/kteatime.notifyrc
%_kde_datadir/applications/kde4/kteatime.desktop
%_kde_iconsdir/hicolor/*/apps/kteatime.png

%dir %_kde_docdir/HTML/en/kteatime
%_kde_docdir/HTML/en/kteatime/config.png
%_kde_docdir/HTML/en/kteatime/index.cache.bz2
%_kde_docdir/HTML/en/kteatime/index.docbook

#-------------------------------------------------------------------

%package -n kde4-kworldclock
Group:      Graphical desktop/KDE
Summary:    Application and plasma applet showing daylight area on the world globe
Provides:   kworldclock4
Conflicts:  kdetoys4 < 3.97.1-0.745233.1

%description -n kde4-kworldclock
TODO

%files -n kde4-kworldclock
%defattr(-,root,root)
%_kde_bindir/kworldclock
%_kde_datadir/applications/kde4/kworldclock.desktop
%_kde_appsdir/kworldclock/maps/depths/400.jpg
%_kde_appsdir/kworldclock/maps/depths/800.jpg
%_kde_appsdir/kworldclock/maps/depths/depths.desktop
%_kde_appsdir/kworldclock/maps/flatworld/1200.jpg
%_kde_appsdir/kworldclock/maps/flatworld/1600.jpg
%_kde_appsdir/kworldclock/maps/flatworld/200.jpg
%_kde_appsdir/kworldclock/maps/flatworld/400.jpg
%_kde_appsdir/kworldclock/maps/flatworld/800.jpg
%_kde_appsdir/kworldclock/maps/flatworld/flatworld.desktop
%_kde_appsdir/kworldclock/pics/flag-blue.png
%_kde_appsdir/kworldclock/pics/flag-green.png
%_kde_appsdir/kworldclock/pics/flag-mask.xpm
%_kde_appsdir/kworldclock/pics/flag-red.png
%_kde_appsdir/kworldclock/pics/flag.png
%_kde_appsdir/kworldclock/zone.tab
%_kde_iconsdir/hicolor/*/apps/kworldclock.png


%dir %doc %_kde_docdir/HTML/en/kworldclock
%doc %_kde_docdir/HTML/en/kworldclock/index.cache.bz2
%doc %_kde_docdir/HTML/en/kworldclock/*.docbook
%doc %_kde_docdir/HTML/en/kworldclock/*.png

#-------------------------------------------------------------------



%prep
%setup -q -n kdetoys-%version


%build
%cmake_kde4

%make




%install
rm -fr %buildroot
cd build
make DESTDIR=%buildroot install


%clean
rm -fr %buildroot



