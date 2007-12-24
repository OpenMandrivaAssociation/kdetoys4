%define revision 750618

%define branch 1
%{?_branch: %{expand: %%global branch 1}}

%define lib_name_orig %mklibname kdetoys4
%define lib_major 1
%define lib_name %lib_name_orig%lib_major

Name:		kdetoys4
Summary:	K Desktop Environment - Toys and Amusements
Version:    	3.97.1
Epoch:		1
URL:		ftp://ftp.kde.org/pub/kde/stable/%version/src/
%if %branch
Release:        %mkrel 0.%revision.1
Source: ftp://ftp.kde.org/pub/kde/stable/%version/src/kdetoys-%version.%revision.tar.bz2
%else
Release:        %mkrel 1
Source: ftp://ftp.kde.org/pub/kde/stable/%version/src/kdetoys-%version.tar.bz2
%endif
Group:		Graphical desktop/KDE
License:	GPL
BuildRequires:	kdebase4-devel >= %version
BuildRequires:  kdebase4-workspace-devel
%description
Toys for the K Desktop Environment.

Software included in this package are:
	- amor: Amusing Misuse Of Resources put's comic figures above your windows
	- eyesapplet: a plasma applet similar to XEyes
	- fifteenapplet: Plasma applet, order 15 pieces in a 4x4 square by moving them
	- kmoon: system tray applet showing the moon phase
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
%_kde_appsdir/kicker/applets/kweather.desktop
%dir %_kde_appsdir/kweather
%_kde_appsdir/kweather/*.png
%_kde_appsdir/kweatherservice/stations.dat
%_kde_appsdir/kweatherservice/weather_stations.desktop
%_kde_iconsdir/hicolor/*/apps/kweather.png   
%_kde_datadir/kde4/services/kweatherservice.desktop


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
%_kde_libdir/kde4/kcm_weather.so
%_kde_libdir/kde4/kcm_weatherservice.so
%_kde_libdir/kde4/weather_panelapplet.so
%dir %_kde_appsdir/amor
%_kde_appsdir/amor/billyrc
%_kde_appsdir/amor/blobrc
%_kde_appsdir/amor/bonhommerc
%_kde_appsdir/amor/bsdrc
%_kde_appsdir/amor/eyesrc
%_kde_appsdir/amor/ghostrc
%_kde_appsdir/amor/nekorc
%_kde_appsdir/amor/pingurc
%_kde_appsdir/amor/taorc
%_kde_appsdir/amor/tips-en
%_kde_appsdir/amor/tuxrc
%_kde_appsdir/amor/wormrc
%dir %_kde_appsdir/amor/pics
%dir %_kde_appsdir/amor/pics/animated
%dir %_kde_appsdir/amor/pics/animated/blob
%_kde_appsdir/amor/pics/animated/blob/*.png
%dir %_kde_appsdir/amor/pics/animated/bonhomme
%_kde_appsdir/amor/pics/animated/bonhomme/*.png
%dir %_kde_appsdir/amor/pics/animated/eyes
%_kde_appsdir/amor/pics/animated/eyes/*.png
%dir %_kde_appsdir/amor/pics/animated/tao
%_kde_appsdir/amor/pics/animated/tao/*.png
%dir %_kde_appsdir/amor/pics/animated/worm
%_kde_appsdir/amor/pics/animated/worm/*.png
%dir %_kde_appsdir/amor/pics/animated/pingu
%_kde_appsdir/amor/pics/animated/pingu/*.png
%dir %_kde_appsdir/amor/pics/preview
%_kde_appsdir/amor/pics/preview/*.png
%dir %_kde_appsdir/amor/pics/animated/ghost
%_kde_appsdir/amor/pics/animated/ghost/*.png
%dir %_kde_appsdir/amor/pics/animated/neko
%_kde_appsdir/amor/pics/animated/neko/*.png
%dir %_kde_appsdir/amor/pics/static
%_kde_appsdir/amor/pics/static/*.png
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

%package -n kde4-kmoon
Group:      Graphical desktop/KDE
Summary:    System tray applet showing the moon phase
Provides:   kmoon4
Conflicts:  kdetoys4 < 3.97.1-0.745233.1

%description -n kde4-kmoon
System tray applet showing the moon phase

%files -n kde4-kmoon
%defattr(-,root,root)
%_kde_libdir/kde4/kmoon_panelapplet.so
%_kde_appsdir/kicker/applets/kmoonapplet.desktop
%dir %_kde_appsdir/kmoon
%dir %_kde_appsdir/kmoon/pics
%_kde_appsdir/kmoon/pics/*.png
%_kde_iconsdir/hicolor/*/apps/kmoon.png

%dir %_kde_docdir/HTML/en/kmoon
%_kde_docdir/HTML/en/kmoon/index.cache.bz2
%_kde_docdir/HTML/en/kmoon/index.docbook

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
%_kde_appsdir/kteatime/hicolor
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
%_kde_appsdir/kdesktop/programs/kdeworld.desktop
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
%_kde_libdir/kde4/ww_panelapplet.so
%_kde_appsdir/kicker/applets/kwwapplet.desktop
%_kde_iconsdir/hicolor/*/apps/kworldclock.png


%dir %doc %_kde_docdir/HTML/en/kworldclock
%doc %_kde_docdir/HTML/en/kworldclock/index.cache.bz2
%doc %_kde_docdir/HTML/en/kworldclock/*.docbook
%doc %_kde_docdir/HTML/en/kworldclock/*.png

#-------------------------------------------------------------------

%package -n kde4-eyesapplet
Group:      Graphical desktop/KDE
Summary:    A plasma applet similar to XEyes
Provides:   eyesapplet4
Conflicts:  kdetoys4 < 3.97.1-0.745233.1

%description -n kde4-eyesapplet
A plasma applet similar to XEyes

%files -n kde4-eyesapplet
%defattr(-,root,root)
%_kde_libdir/kde4/eyes_panelapplet.so
%_kde_appsdir/kicker/applets/eyesapplet.desktop

#-------------------------------------------------------------------

%package -n kde4-fifteenpieces
Group:      Graphical desktop/KDE
Summary:    Plasma applet, order 15 pieces in a 4x4 square by moving them
Provides:   fifteenpieces4
Conflicts:  kdetoys4 < 3.97.1-0.745233.1

%description -n kde4-fifteenpieces
Plasma applet, order 15 pieces in a 4x4 square by moving them

%files -n kde4-fifteenpieces
%defattr(-,root,root)
%_kde_libdir/kde4/fifteen_panelapplet.so
%_kde_appsdir/kicker/applets/kfifteenapplet.desktop
%_kde_iconsdir/hicolor/*/*/fifteenpieces.*

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



