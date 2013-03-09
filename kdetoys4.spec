Name:		kdetoys4
Version:	4.10.1
Release:	1
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
Provides:	ktux4 = %{EVRD}
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
Provides:	amor4 = %{EVRD}
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
Provides:	kteatime4 = %{EVRD}
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

%changelog
* Sat Mar 09 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.1-1
- New version 4.10.1

* Thu Feb 07 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.0-1
- New version 4.10.0
- Make all Provides versioned

* Wed Dec 05 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.9.4-1
- New version 4.9.4

* Wed Nov 07 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.9.3-1
- New version 4.9.3

* Thu Oct 04 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.9.2-1
- New version 4.9.2

* Sat Sep 08 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.9.1-1
- New version 4.9.1

* Wed Aug 08 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.9.0-1
- New version 4.9.0

* Mon Jul 16 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.8.97-1
- New version 4.8.97
- Convert BuildRequires to pkgconfig style
- Make better usage of KDE4 path macros

* Fri Jun 29 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.8.95-1
- Update to 4.8.95

* Fri Jun 08 2012 Arkady L. Shane <arkady.shane@rosalab.ru> 1:4.8.4-1
- update to 4.8.4

* Thu May 10 2012 Arkady L. Shane <arkady.shane@rosalab.ru> 1:4.8.3-1
- update to 4.8.3

* Sun Mar 11 2012 Arkady L. Shane <arkady.shane@rosalab.ru> 1:4.8.2-1
- update to 4.8.2

* Sun Mar 11 2012 Arkady L. Shane <arkady.shane@rosalab.ru> 1:4.8.1-1
- update to 4.8.1

* Thu Jan 19 2012 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.8.0-1
+ Revision: 762521
- New upstream tarball

* Fri Jan 06 2012 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.7.97-1
+ Revision: 758110
- New upstream tarball

* Tue Jan 03 2012 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.7.95-1
+ Revision: 748795
- New version

* Fri Dec 09 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.7.90-1
+ Revision: 739375
- New upstream tarball

* Sat Nov 19 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.7.80-1
+ Revision: 731898
- New upstream tarball 4.7.80

* Fri Sep 30 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.7.41-1
+ Revision: 702071
- New version 4.7.41

* Mon Jun 13 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.6.4-1
+ Revision: 684411
- New version 4.6.4

* Fri May 13 2011 Funda Wang <fwang@mandriva.org> 1:4.6.3-1
+ Revision: 674036
- new version 4.6.3

* Tue Apr 05 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.6.2-1
+ Revision: 650782
- Remove mkrel
- New version 4.6.2

* Mon Feb 28 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.6.1-1
+ Revision: 640734
- New version 4.6.1

* Wed Jan 26 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.6.0-1
+ Revision: 632971
- New version KDE 4.6 Final

* Thu Jan 06 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.5.95-1mdv2011.0
+ Revision: 629127
- New version KDE 4.6 RC2

* Thu Dec 23 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.5.90-1mdv2011.0
+ Revision: 624071
- New upstream tarball

* Wed Dec 08 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.5.85-1mdv2011.0
+ Revision: 616351
- New upstream tarball

* Sat Nov 27 2010 Funda Wang <fwang@mandriva.org> 1:4.5.80-1mdv2011.0
+ Revision: 601667
- new version 4.5.80 (aka 4.6 beta1)

* Sat Nov 20 2010 Funda Wang <fwang@mandriva.org> 1:4.5.77-0.svn1198704.1mdv2011.0
+ Revision: 599200
- new snapshot 4.5.77

* Thu Oct 28 2010 Funda Wang <fwang@mandriva.org> 1:4.5.74-0.svn1190490.1mdv2011.0
+ Revision: 589664
- new snapshot 4.5.74

* Fri Sep 17 2010 Funda Wang <fwang@mandriva.org> 1:4.5.68-1mdv2011.0
+ Revision: 579189
- new version 4.5.68

* Tue Sep 07 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.5.67-1mdv2011.0
+ Revision: 576543
- New version 4.5.67

* Fri Aug 06 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.5.0-1mdv2011.0
+ Revision: 566575
- New upstream tarball
- Update to version 4.5.0

* Thu Jul 29 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.4.95-1mdv2011.0
+ Revision: 562941
- kde 4.4.95

* Tue May 04 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.4.3-1mdv2010.1
+ Revision: 542109
- Update to version 4.4.3

* Sun Mar 28 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.4.2-1mdv2010.1
+ Revision: 528323
- Update to version 4.4.2

* Tue Mar 02 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.4.1-1mdv2010.1
+ Revision: 513417
- Update to version 4.4.1

* Tue Feb 09 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.4.0-1mdv2010.1
+ Revision: 502618
- Update to version 4.4.0

* Mon Feb 01 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.3.98-1mdv2010.1
+ Revision: 498949
- Update to version 4.3.98 aka "kde 4.4 RC3"
- Update to version 4.3.98 aka "kde 4.4 RC3"

* Mon Jan 25 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.3.95-1mdv2010.1
+ Revision: 495987
- Update to version 4.3.95 aka "kde 4.4 RC2"

* Sun Jan 10 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.3.90-1mdv2010.1
+ Revision: 488238
- Update to kde 4.4 rc1
- kpackage is not anymore

* Mon Dec 21 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.3.85-1mdv2010.1
+ Revision: 480754
- Update to kde 4.4 beta2

* Fri Dec 04 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.3.80-1mdv2010.1
+ Revision: 473346
- Update to KDE 4.4 Beta1
- Add branch switch

* Mon Nov 30 2009 Funda Wang <fwang@mandriva.org> 1:4.3.77-1mdv2010.1
+ Revision: 471754
- new version 4.3.77

* Tue Nov 17 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.3.75-1mdv2010.1
+ Revision: 466842
- Update to kde 4.3.75

* Thu Nov 12 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.3.73-2mdv2010.1
+ Revision: 465253
- Rebuild against new Qt

* Sun Nov 08 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.3.73-1mdv2010.1
+ Revision: 463255
- Update to kde 4.3.73

* Sat Oct 24 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.3.2-3mdv2010.0
+ Revision: 459136
- Add a provides for kdetoys

* Thu Oct 22 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.3.2-2mdv2010.0
+ Revision: 458984
- Add obsolete for 2009.0 -> 2010.0 upgrade

* Tue Oct 06 2009 Helio Chissini de Castro <helio@mandriva.com> 1:4.3.2-1mdv2010.0
+ Revision: 454662
- New upstream release 4.3.2.

* Sat Sep 19 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.3.1-4mdv2010.0
+ Revision: 444734
- Fix typo
- Fix stupid typo

* Fri Sep 18 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.3.1-2mdv2010.0
+ Revision: 444216
- Add obsolete for kde3 upgrade

* Tue Sep 01 2009 Helio Chissini de Castro <helio@mandriva.com> 1:4.3.1-1mdv2010.0
+ Revision: 423218
- New upstream release 4.3.1.

* Tue Aug 04 2009 Helio Chissini de Castro <helio@mandriva.com> 1:4.3.0-1mdv2010.0
+ Revision: 409418
- New upstream release 4.3.0.
- Update to KDE 4.3 RC3

* Sun Jul 12 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.2.96-1mdv2010.0
+ Revision: 394962
- Update to Rc2

* Fri Jun 26 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.2.95-1mdv2010.0
+ Revision: 389372
- Update to kde 4.3Rc1

* Fri Jun 05 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.2.90-1mdv2010.0
+ Revision: 383152
- Update to beta2

* Fri May 29 2009 Funda Wang <fwang@mandriva.org> 1:4.2.88-1mdv2010.0
+ Revision: 380760
- New version 4.2.88

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - Adapt kdesdk to new layout

* Sat May 23 2009 Funda Wang <fwang@mandriva.org> 1:4.2.87-1mdv2010.0
+ Revision: 378876
- New version 4.2.87

* Fri May 08 2009 Funda Wang <fwang@mandriva.org> 1:4.2.85-1mdv2010.0
+ Revision: 373449
- New version 4.2.85

* Mon May 04 2009 Funda Wang <fwang@mandriva.org> 1:4.2.71-0.svn961800.1mdv2010.0
+ Revision: 371530
- New version 4.2.71

* Sun May 03 2009 Funda Wang <fwang@mandriva.org> 1:4.2.70-0.svn954171.1mdv2010.0
+ Revision: 370948
- 4.2.70

* Fri Mar 27 2009 Helio Chissini de Castro <helio@mandriva.com> 1:4.2.2-1mdv2009.1
+ Revision: 361733
- Update with 4.2.2 try#1 packages

* Mon Mar 02 2009 Helio Chissini de Castro <helio@mandriva.com> 1:4.2.1-1mdv2009.1
+ Revision: 347010
- KDE 4.2.1 try#1 upstream release

* Mon Feb 16 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.2.0-2mdv2009.1
+ Revision: 340892
- Rebuild against qt4.5

* Tue Jan 27 2009 Helio Chissini de Castro <helio@mandriva.com> 1:4.2.0-1mdv2009.1
+ Revision: 334589
- Update with official 4.2.0 upstream tarball

* Sun Jan 11 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.1.96-2mdv2009.1
+ Revision: 328196
- Revive KTux

* Fri Jan 09 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.1.96-1mdv2009.1
+ Revision: 327440
- Package man pages
- Remove KTux

  + Helio Chissini de Castro <helio@mandriva.com>
    - Update with Release Candidate 1 - 4.1.96

* Sun Dec 14 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.1.85-1mdv2009.1
+ Revision: 314031
- New version KDE 4.2 Beta2

* Thu Dec 11 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.1.82-1mdv2009.1
+ Revision: 313431
- Update to kde 4.1.82

* Sun Nov 30 2008 Funda Wang <fwang@mandriva.org> 1:4.1.81-1mdv2009.1
+ Revision: 308435
- new version 4.1.81

* Thu Nov 20 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.1.80-1mdv2009.1
+ Revision: 304862
- Remove upstream merged patch

  + Helio Chissini de Castro <helio@mandriva.com>
    - Update with Beta 1 - 4.1.80

* Sat Nov 15 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.1.73-1mdv2009.1
+ Revision: 303425
- use -b option in %%patch

  + Funda Wang <fwang@mandriva.org>
    - New version 4.1.73
    - install kweather doc also

* Sat Oct 25 2008 Funda Wang <fwang@mandriva.org> 1:4.1.71-1mdv2009.1
+ Revision: 297032
- New version 4.1.71

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - Update to kde 4.1.70

* Sat Sep 27 2008 Helio Chissini de Castro <helio@mandriva.com> 1:4.1.2-1mdv2009.0
+ Revision: 288847
- KDE 4.1.2 arriving.

* Sun Sep 07 2008 Funda Wang <fwang@mandriva.org> 1:4.1.1-1mdv2009.0
+ Revision: 282151
- New version 4.1.1

* Fri Jul 25 2008 Helio Chissini de Castro <helio@mandriva.com> 1:4.1.0-1mdv2009.0
+ Revision: 247627
- Update with Release Candidate 1 - 4.1.0

* Thu Jul 10 2008 Helio Chissini de Castro <helio@mandriva.com> 1:4.0.98-1mdv2009.0
+ Revision: 233196
- Update with Release Candidate 1 - 4.0.98

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - New version kde 4.0.85

* Sun Jun 29 2008 Funda Wang <fwang@mandriva.org> 1:4.0.84-1mdv2009.0
+ Revision: 229950
- New version 4.0.84

* Thu Jun 19 2008 Helio Chissini de Castro <helio@mandriva.com> 1:4.0.83-1mdv2009.0
+ Revision: 226104
- Update with new snapshot tarballs 4.0.83

* Thu Jun 12 2008 Helio Chissini de Castro <helio@mandriva.com> 1:4.0.82-1mdv2009.0
+ Revision: 218303
- Update with new snapshot tarballs 4.0.82

* Tue Jun 03 2008 Helio Chissini de Castro <helio@mandriva.com> 1:4.0.81-1mdv2009.0
+ Revision: 214725
- Update with new snapshot tarballs 4.0.81

* Sun May 25 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.0.80-1mdv2009.0
+ Revision: 211068
- Remove patch0 (not needed anymore)
- Own %%_kde_appsdir/kteatime %%_kde_appsdir/ktux %%_kde_appsdir/amor %%_kde_appsdir/kweather and %%_kde_appsdir/kweather
- Do not package kworldclock doc (Patch0)
- Fix macros
- Fix File list
- Bye Bye kworldclock ( moved upstream to  unmaintained/4/

  + Helio Chissini de Castro <helio@mandriva.com>
    - New upstream kde4 4.1 beta1

  + Funda Wang <fwang@mandriva.org>
    - BR automoc
    - New version 4.0.74

* Thu May 08 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.0.73-1mdv2009.0
+ Revision: 204748
- Update to kde 4.0.73

* Tue May 06 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.0.72-1mdv2009.0
+ Revision: 202550
- Fix BuildRequires
- Update to kde 4.0.72
- New snapshot 4.0.70

  + Helio Chissini de Castro <helio@mandriva.com>
    - New upstream kde4 4.1 alpha 1

* Fri Mar 28 2008 Helio Chissini de Castro <helio@mandriva.com> 1:4.0.3-1mdv2008.1
+ Revision: 191017
- Update for last stable release 4.0.3

* Sat Mar 08 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.0.2-2mdv2008.1
+ Revision: 182266
- Rebuild against new qt4 changes

* Sat Mar 01 2008 Helio Chissini de Castro <helio@mandriva.com> 1:4.0.2-1mdv2008.1
+ Revision: 177464
- New upstream bugfix release 4.0.2

  + Thierry Vignaud <tv@mandriva.org>
    - fix no-buildroot-tag
    - fix description-line-too-long

* Mon Feb 11 2008 Helio Chissini de Castro <helio@mandriva.com> 1:4.0.1-1mdv2008.1
+ Revision: 165282
- Update to 4.0.1

* Wed Jan 09 2008 Helio Chissini de Castro <helio@mandriva.com> 1:4.0.0-1mdv2008.1
+ Revision: 147361
- Update for final stable 4.0.0

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - Fix File list
    - New snapshot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Dec 13 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:3.97.1-0.745233.1mdv2008.1
+ Revision: 119556
- Fix BuildRequires
- New snapshot
  Big Cleanup to follow kde4 policies
  	* Now we have new packages:
  		- kde4-kweather
  		- kde4-amor
  		- kde4-ktux
  		- kde4-kmoon
  		- kde4-kteatime
  		- kde4-kworldclock
  		- kde4-eyesapplet
  	* libkweather have been removed

  + Thierry Vignaud <tv@mandriva.org>
    - buildrequires X11-devel instead of XFree86-devel

* Wed May 09 2007 Laurent Montel <lmontel@mandriva.org> 1:3.90.1-0.20070502.1mdv2008.0
+ Revision: 25717
- new snapshot
- It compiles with enable final

* Thu May 03 2007 Laurent Montel <lmontel@mandriva.org> 1:3.80.3-0.20070502.1mdv2008.0
+ Revision: 21362
- SILEN
- new snapshot
- new snapshot


* Sun Mar 11 2007 Laurent Montel <lmontel@mandriva.com> 3.80.3-0.20070311.1mdv2007.1
+ Revision: 141309
- new snapshot
- Fix spec file
- new snapshot
- 3.80.3

* Fri Feb 16 2007 Laurent Montel <lmontel@mandriva.com> 1:3.80.2-0.20070215.1mdv2007.1
+ Revision: 121629
- new snapshot
- Fix spec file
- new snapshot
- new snapshot

* Wed Jan 17 2007 Laurent Montel <lmontel@mandriva.com> 1:3.80.2-0.20070117.1mdv2007.1
+ Revision: 109804
- Update

* Wed Jan 10 2007 Laurent Montel <lmontel@mandriva.com> 1:3.80.2-0.20070109.1mdv2007.1
+ Revision: 107038
- update

* Wed Jan 03 2007 Laurent Montel <lmontel@mandriva.com> 1:3.80.2-0.20070103.1mdv2007.1
+ Revision: 103663
- Fix file list
- Update
- (empty)
- new update
- Byebye menu macro

* Thu Dec 28 2006 Laurent Montel <lmontel@mandriva.com> 1:3.80-2mdv2007.1
+ Revision: 102289
- Import kdetoys4

* Wed Oct 18 2006 Laurent Montel <lmontel@mandriva.com> 3.5.5-1mdv2007.0
- First package

