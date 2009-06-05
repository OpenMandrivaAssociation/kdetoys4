%define branch 0
%{?_branch: %{expand: %%global branch 1}}

%if %branch
%define kderevision svn973768
%endif

Name:          kdetoys4
Summary:       K Desktop Environment - Toys and Amusements
Version:       4.2.90
Epoch:         1
URL:           ftp://ftp.kde.org/pub/kde/unstable/%version/src/
Release:       %mkrel 1
%if %branch
Source:        ftp://ftp.kde.org/pub/kde/unstable/%version/src/kdetoys-%{version}%kderevision.tar.bz2
%else
Source:        ftp://ftp.kde.org/pub/kde/unstable/%version/src/kdetoys-%{version}.tar.bz2
%endif
Group:         Graphical desktop/KDE
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-buildroot
License:       GPL
BuildRequires: kdelibs4-devel >= %version
BuildRequires: kdebase4-workspace-devel >= %version
BuildRequires: qimageblitz-devel

Obsoletes:     kworldclock < 1:4.0.74-1
Obsoletes:     %{_lib}kworldclock4 < 1:4.0.74-1
Obsoletes:     kde4-kworldclock < 1:4.0.68

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

#-----------------------------------------------------------------

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
%_kde_appsdir/kweather
%_kde_appsdir/kweatherservice
%_kde_iconsdir/hicolor/*/apps/kweather.png   
%_kde_datadir/kde4/services/kweatherservice.desktop
%_kde_libdir/kde4/kcm_weather.so
%_kde_libdir/kde4/kcm_weatherservice.so
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
%if %branch
%setup -q -n kdetoys-%{version}%kderevision
%else
%setup -q -n kdetoys-%{version}
%endif

%build
%cmake_kde4
%make

%install
rm -fr %buildroot
make -C build DESTDIR=%buildroot install

%clean
rm -fr %buildroot
