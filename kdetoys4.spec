%define branch 0
%{?_branch: %{expand: %%global branch 1}}

%if %branch
%define kde_snapshot svn1198704
%endif

Name: kdetoys4
Summary: K Desktop Environment - Toys and Amusements
Version: 4.6.1
Epoch: 1
URL: http://www.kde.org
%if %branch
Release: %mkrel -c %kde_snapshot 1
Source: ftp://ftp.kde.org/pub/kde/unstable/%version/src/kdetoys-%{version}%kde_snapshot.tar.bz2
%else
Release: %mkrel 1
Source: ftp://ftp.kde.org/pub/kde/unstable/%version/src/kdetoys-%{version}.tar.bz2
%endif
Group: Graphical desktop/KDE
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
License: GPL
BuildRequires: kdelibs4-devel >= 2:4.2.98
BuildRequires: kdebase4-workspace-devel >= 2:4.2.98
BuildRequires: qimageblitz-devel
Obsoletes: kworldclock < 1:4.0.74-1
Obsoletes: %{_lib}kworldclock4 < 1:4.0.74-1
Obsoletes: kde4-kworldclock < 1:4.0.68
%if %mdkversion >= 201000
Obsoletes: kdetoys < 1:3.5.10-2
Provides:  kdetoys = %epoch:%version-%release
%endif

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
%if %branch
%setup -q -n kdetoys-%{version}%kde_snapshot
%else
%setup -q -n kdetoys-%{version}
%endif

%build
%cmake_kde4
%make

%install
rm -fr %buildroot
%makeinstall_std -C build

%clean
rm -fr %buildroot
