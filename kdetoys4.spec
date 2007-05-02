# remove it when kde4 will be official kde package
%define _prefix /opt/kde4/
%define _libdir %_prefix/%_lib
%define _datadir %_prefix/share/
%define _bindir %_prefix/bin
%define _includedir %_prefix/include/
%define _iconsdir %_datadir/icons/
%define _sysconfdir %_prefix/etc/
%define _docdir %_datadir/doc/

%define branch_date 20070502

%define use_enable_final 0
%{?_no_enable_final: %{expand: %%global use_enable_final 0}}

%define compile_apidox 1
%{?_no_apidox: %{expand: %%global compile_apidox 0}}

%define unstable 1
%{?_unstable: %{expand: %%global unstable 1}}

%define branch 1
%{?_branch: %{expand: %%global branch 1}}

%define use_enable_pie 1
%{?_no_enable_pie: %{expand: %%global use_enable_pie 0}}

%if %unstable
%define dont_strip 1
%endif


%define lib_name_orig %mklibname kdetoys4
%define lib_major 1
%define lib_name %lib_name_orig%lib_major

Name:		kdetoys4
Summary:	K Desktop Environment - Toys and Amusements
Version:    	3.80.3
Release:    	%mkrel 0.%branch_date.1
Epoch:		1
URL:		ftp://ftp.kde.org/pub/kde/stable/%version/src/
Packager:	Mandriva Linux KDE Team <kde@mandriva.com>
%if %branch
Source: ftp://ftp.kde.org/pub/kde/stable/%version/src/kdetoys-%version-%branch_date.tar.bz2
%else
Source: ftp://ftp.kde.org/pub/kde/stable/%version/src/kdetoys-%version.tar.bz2
%endif



Group:		Graphical desktop/KDE
BuildRoot:	%_tmppath/%name-%version-%release-root
License:	GPL

%define mini_release %mkrel 0.%branch_date.1
BuildRequires: kdelibs4-devel >= %version-%mini_release
BuildRequires:	XFree86-devel
BuildRequires:	kdebase4-devel >= %version-%mini_release

%description
Toys for the K Desktop Environment.

Software included in this package are:
	- amor: Amusing Misuse Of Resources put's comic figures above your windows
	- eyesapplet: a kicker applet similar to XEyes
	- fifteenapplet: kicker applet, order 15 pieces in a 4x4 square by moving them
	- kmoon: system tray applet showing the moon phase
	- kodo: mouse movement meter
	- kscore: kicker applet with a sports ticker
	- kteatime: system tray applet that makes sure your tea doesn't get too strong
	- ktux: Tux-in-a-Spaceship screen saver
	- kweather: kicker applet that will display the current weather outside
	- kworldwatch: application and kicker applet showing daylight area on the world globe

%package -n %lib_name-devel
Summary:	Headers files for kdetoys
Group:		Development/KDE and Qt

Provides:	%lib_name_orig-devel = %epoch:%version-%release
Provides:	kdetoys4-devel = %epoch:%version-%release

%description -n %lib_name-devel
Headers files for kdetoys.


%package kweather
Group:      Graphical desktop/KDE
Summary:    kweather
Provides:   kweather4
Requires:	%lib_name-kweather = %epoch:%version-%release

%description kweather
kicker applet that will display the current weather outside

%package -n %lib_name-kweather
Group:      Development/KDE and Qt
Summary:    Libraries for kdetoys

%description -n %lib_name-kweather
kicker applet that will display the current weather outside



%prep

%setup -q -nkdetoys-%version-%branch_date


%build
cd $RPM_BUILD_DIR/kdetoys-%version-%branch_date
mkdir build
cd build
export QTDIR=/usr/lib/qt4/
export PATH=$QTDIR/bin:$PATH

cmake -DCMAKE_INSTALL_PREFIX=%_prefix \
%if %use_enable_final
      -DKDE4_ENABLE_FINAL=ON \
%endif
%if %use_enable_pie
      -DKDE4_ENABLE_FPIE=ON \
%endif
%if %unstable
      -DCMAKE_BUILD_TYPE=Debug \
%endif
%if "%{_lib}" != "lib"
      -DLIB_SUFFIX=64 \
%endif
        ../

%make




%install
rm -fr %buildroot
cd $RPM_BUILD_DIR/kdetoys-%version-%branch_date/build/

make DESTDIR=%buildroot install


# Create LMDK menu entries
install -d %buildroot/%_menudir/


mandriva-add-xdg-categories.pl %buildroot/%_datadir/applications/kde4/amor.desktop "More Applications/Games/Toys" 
mandriva-add-xdg-categories.pl %buildroot/%_datadir/applications/kde4/kteatime.desktop "More Applications/Games/Toys" kde
mandriva-add-xdg-categories.pl %buildroot/%_datadir/applications/kde4/kworldclock.desktop "More Applications/Games/Toys"


%post
/sbin/ldconfig
%update_icon_cache hicolor

%postun
/sbin/ldconfig
%clean_icon_cache hicolor


%post kweather -p /sbin/ldconfig


%postun kweather -p /sbin/ldconfig

%post -n %lib_name-kweather -p /sbin/ldconfig


%postun -n %lib_name-kweather -p /sbin/ldconfig


%clean
rm -fr %buildroot


%files 
%defattr(-,root,root)

#
%_bindir/amor
%_bindir/kteatime
%_bindir/ktux
%_bindir/kworldclock

#
#
%_libdir/kde4/eyes_panelapplet.so
%_libdir/kde4/fifteen_panelapplet.so
%_libdir/kde4/kmoon_panelapplet.so
#
#
%_datadir/applications/kde4/*.desktop
#
#
%dir %_datadir/apps/
%dir %_datadir/apps/amor/
%_datadir/apps/amor/billyrc
%_datadir/apps/amor/blobrc
%_datadir/apps/amor/bsdrc
%_datadir/apps/amor/eyesrc
%_datadir/apps/amor/nekorc
%_datadir/apps/amor/ghostrc
%_datadir/apps/amor/pingurc
%_datadir/apps/amor/taorc
%_datadir/apps/amor/tips-en
%_datadir/apps/amor/tuxrc
%_datadir/apps/amor/wormrc
%_datadir/apps/amor/bonhommerc
#

%dir %_datadir/apps/amor/pics/animated/blob/
%_datadir/apps/amor/pics/animated/blob/*.png

%dir %_datadir/apps/amor/pics/animated/bonhomme/
%_datadir/apps/amor/pics/animated/bonhomme/*.png

%dir %_datadir/apps/amor/pics/animated/eyes/
%_datadir/apps/amor/pics/animated/eyes/*.png

%dir %_datadir/apps/amor/pics/animated/ghost/
%_datadir/apps/amor/pics/animated/ghost/*.png

%dir %_datadir/apps/amor/pics/animated/neko/
%_datadir/apps/amor/pics/animated/neko/*.png

%dir %_datadir/apps/amor/pics/animated/pingu/
%_datadir/apps/amor/pics/animated/pingu/*.png

%dir %_datadir/apps/amor/pics/animated/tao/
%_datadir/apps/amor/pics/animated/tao/*.png

%dir %_datadir/apps/amor/pics/animated/worm/
%_datadir/apps/amor/pics/animated/worm/*.png

%dir %_datadir/apps/amor/pics/preview/
%_datadir/apps/amor/pics/preview/*.png

%dir %_datadir/apps/amor/pics/static/
%_datadir/apps/amor/pics/static/*.png

#
#
%dir %_datadir/apps/kicker/
%dir %_datadir/apps/kicker/applets/
%_datadir/apps/kicker/applets/eyesapplet.desktop
%_datadir/apps/kicker/applets/kfifteenapplet.desktop
#
#
%dir %_datadir/apps/kmoon/
%dir %_datadir/apps/kmoon/pics/
%_datadir/apps/kmoon/pics/*.png
#
#
#
#
%dir %_datadir/apps/ktux/
%dir %_datadir/apps/ktux/sprites/
%_datadir/apps/ktux/sprites/spriterc
%_datadir/apps/ktux/sprites/*.png
#
#
%dir %_datadir/apps/kworldclock/
%_datadir/apps/kworldclock/zone.tab
#
%dir %_datadir/apps/kworldclock/pics/
%_datadir/apps/kworldclock/pics/*.png
%_datadir/apps/kworldclock/pics/*.xpm

%dir %_datadir/apps/kworldclock/maps/flatworld/
%_datadir/apps/kworldclock/maps/flatworld/*.jpg
%_datadir/apps/kworldclock/maps/flatworld/*.desktop
#
%dir %_datadir/apps/kworldclock/maps/
%dir %_datadir/apps/kworldclock/maps/depths/
%_datadir/apps/kworldclock/maps/depths/*.desktop
%_datadir/apps/kworldclock/maps/depths/*.jpg
#
#
%dir %_datadir/apps/kicker/
%dir %_datadir/apps/kicker/applets/
%_datadir/apps/kicker/applets/kmoonapplet.desktop

%dir %_datadir/apps/kteatime/
%_datadir/apps/kteatime/kteatime.notifyrc
%_datadir/apps/kteatime/crystalsvg/22x22/actions/mug.png
%_datadir/apps/kteatime/crystalsvg/22x22/actions/tea_anim1.png
%_datadir/apps/kteatime/crystalsvg/22x22/actions/tea_anim2.png
%_datadir/apps/kteatime/crystalsvg/22x22/actions/tea_not_ready.png
%_datadir/apps/kteatime/hicolor/16x16/apps/kteatime.png
%_datadir/apps/kteatime/hicolor/32x32/apps/kteatime.png
%_datadir/apps/kteatime/hicolor/48x48/apps/kteatime.png


%_datadir/icons/crystalsvg/16x16/apps/fifteenpieces.png
%_datadir/icons/crystalsvg/22x22/apps/fifteenpieces.png
%_datadir/icons/crystalsvg/32x32/apps/fifteenpieces.png
%_datadir/icons/crystalsvg/48x48/apps/fifteenpieces.png
%_datadir/icons/crystalsvg/scalable/apps/fifteenpieces.svgz
%_datadir/kde4/services/ScreenSavers/ktux.desktop


#
%_datadir/icons/hicolor/16x16/apps/*.png

%_datadir/icons/hicolor/22x22/apps/*.png

%_datadir/icons/hicolor/32x32/apps/*.png

%_datadir/icons/hicolor/48x48/apps/*.png

%dir %_docdir/HTML/en/amor/
%doc %_docdir/HTML/en/amor/*.png
%doc %_docdir/HTML/en/amor/*.bz2
%doc %_docdir/HTML/en/amor/*.docbook
%dir %_docdir/HTML/en/kmoon/
%doc %_docdir/HTML/en/kmoon/*.bz2
%doc %_docdir/HTML/en/kmoon/*.docbook
%dir %_docdir/HTML/en/kodo/
%doc %_docdir/HTML/en/kodo/*.png
%doc %_docdir/HTML/en/kodo/*.bz2
%doc %_docdir/HTML/en/kodo/*.docbook
%dir %_docdir/HTML/en/kteatime/
%doc %_docdir/HTML/en/kteatime/*.png
%doc %_docdir/HTML/en/kteatime/*.bz2
%doc %_docdir/HTML/en/kteatime/*.docbook
%dir %_docdir/HTML/en/kweather/
%doc %_docdir/HTML/en/kweather/*.bz2
%doc %_docdir/HTML/en/kweather/*.docbook
%dir %_docdir/HTML/en/kworldclock/
%doc %_docdir/HTML/en/kworldclock/*.bz2
%doc %_docdir/HTML/en/kworldclock/*.docbook
%doc %_docdir/HTML/en/kworldclock/*.png




%files -n %lib_name-devel
%defattr(-,root,root,-)
%_datadir/dbus-1/interfaces/org.kde.amor.xml

%files kweather
%defattr(-,root,root,-)
%_datadir/apps/kweather/*.png
%_datadir/apps/kweatherservice/*.dat
%_datadir/apps/kweatherservice/*.desktop
%_datadir/kde4/services/kcmweather.desktop
%_datadir/kde4/services/kcmweatherservice.desktop
%_datadir/kde4/services/kweatherservice.desktop
%_bindir/kweatherreport
%_bindir/kweatherservice
%_libdir/kde4/kcm_weather.so
%_libdir/kde4/kcm_weatherservice.so
%_libdir/kde4/weather_panelapplet.so
%_datadir/apps/kicker/applets/kweather.desktop


%files -n %lib_name-kweather
%defattr(-,root,root,-)
%_libdir/libkdeinit_kweatherreport.so

%_datadir/dbus-1/interfaces/org.kde.kweather.kweather.xml
%_datadir/dbus-1/interfaces/org.kde.kweather.service.xml


