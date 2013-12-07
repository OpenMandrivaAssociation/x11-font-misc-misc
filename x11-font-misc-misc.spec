Name: x11-font-misc-misc
Version: 1.1.2
Release: 7
Summary: Xorg X11 font misc-misc
Group: Development/X11
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
URL: http://xorg.freedesktop.org
Source: http://xorg.freedesktop.org/releases/individual/font/font-misc-misc-%{version}.tar.bz2
License: Public Domain
BuildArch: noarch
BuildRequires: fontconfig

BuildRequires: x11-font-util >= 1.0.0
BuildRequires: x11-util-macros >= 1.0.2

Conflicts: xorg-x11 <= 6.9.0
Requires(post,postun): mkfontdir mkfontscale

%description
Xorg X11 font misc-misc

%prep
%setup -q -n font-misc-misc-%{version}

%build
./configure --prefix=/usr --with-fontdir=%_datadir/fonts/misc

%make

%install
rm -rf %{buildroot}
%makeinstall_std
rm -f %{buildroot}%_datadir/fonts/misc/fonts.dir
rm -f %{buildroot}%_datadir/fonts/misc/fonts.scale

%post
mkfontscale %_datadir/fonts/misc
mkfontdir %_datadir/fonts/misc

%postun
mkfontscale %_datadir/fonts/misc
mkfontdir %_datadir/fonts/misc

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%_datadir/fonts/misc/10x20*.pcf.gz
%_datadir/fonts/misc/12x13ja.pcf.gz
%_datadir/fonts/misc/18x18*.pcf.gz
%_datadir/fonts/misc/4x6*.pcf.gz
%_datadir/fonts/misc/5x7*.pcf.gz
%_datadir/fonts/misc/5x8*.pcf.gz
%_datadir/fonts/misc/6x10*.pcf.gz
%_datadir/fonts/misc/6x12*.pcf.gz
%_datadir/fonts/misc/6x13*.pcf.gz
%_datadir/fonts/misc/6x9*.pcf.gz
%_datadir/fonts/misc/7x13*.pcf.gz
%_datadir/fonts/misc/7x14*.pcf.gz
%_datadir/fonts/misc/8x13*.pcf.gz
%_datadir/fonts/misc/9x15*.pcf.gz
%_datadir/fonts/misc/9x18*.pcf.gz
%_datadir/fonts/misc/k14.pcf.gz
%_datadir/fonts/misc/nil2.pcf.gz




%changelog
* Tue May 17 2011 Funda Wang <fwang@mandriva.org> 1.1.2-4mdv2011.0
+ Revision: 675490
- br fontconfig for fc-query used in new rpm-setup-build

* Tue May 17 2011 Funda Wang <fwang@mandriva.org> 1.1.2-3
+ Revision: 675255
- rebuild for new rpm-setup

* Sat May 07 2011 Oden Eriksson <oeriksson@mandriva.com> 1.1.2-2
+ Revision: 671213
- mass rebuild

* Thu Dec 09 2010 Thierry Vignaud <tv@mandriva.org> 1.1.2-1mdv2011.0
+ Revision: 618743
- new release

* Wed Oct 06 2010 Thierry Vignaud <tv@mandriva.org> 1.1.1-1mdv2011.0
+ Revision: 583220
- new release

* Wed Oct 06 2010 Thierry Vignaud <tv@mandriva.org> 1.1.0-1mdv2011.0
+ Revision: 583212
- new release

* Wed Jan 13 2010 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 1.1.0-1mdv2010.1
+ Revision: 490609
- New version: 1.1.0

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 1.0.0-9mdv2009.1
+ Revision: 351282
- rebuild

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 1.0.0-8mdv2009.0
+ Revision: 225999
- rebuild
- fix no-buildroot-tag

* Mon Feb 04 2008 Thierry Vignaud <tv@mandriva.org> 1.0.0-7mdv2008.1
+ Revision: 162433
- fix uninstalling
- stop using prereq
- kill re-definition of %%buildroot on Pixel's request

* Thu Jul 05 2007 Ademar de Souza Reis Jr <ademar@mandriva.com.br> 1.0.0-6mdv2008.0
+ Revision: 48673
- remove unecessary configure flags
- remove /usr/share/fonts/misc/ from %%files, will put it in
  x11-font-alias where other directories belong.

* Tue Jul 03 2007 Ademar de Souza Reis Jr <ademar@mandriva.com.br> 1.0.0-5mdv2008.0
+ Revision: 47633
- own %%_datadir/fonts/misc
- fix license field


* Thu Aug 03 2006 Helio Chissini de Castro <helio@mandriva.com>
+ 2006-08-03 18:55:09 (51491)
- Fonts packages now are noarch. Moved for new place /usr/share/fonts. Approved by Boiko

* Wed May 31 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-31 18:32:34 (31796)
- rebuild to fix cooker uploading

* Mon May 29 2006 Andreas Hasenack <andreas@mandriva.com>
+ 2006-05-29 14:36:37 (31646)
- renamed mdv to packages because mdv is too generic and it's hosting only packages anyway

* Thu May 04 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-04 21:25:17 (26918)
- increment release

* Thu Apr 27 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-04-27 04:02:05 (26704)
- Adding X.org 7.0 to the repository

