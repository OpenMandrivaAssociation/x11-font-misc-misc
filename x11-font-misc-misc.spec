Name: x11-font-misc-misc
Version: 1.1.2
Release: 17
Summary: Xorg X11 font misc-misc
Group: Development/X11
URL: http://xorg.freedesktop.org
Source0: http://xorg.freedesktop.org/releases/individual/font/font-misc-misc-%{version}.tar.bz2
License: Public Domain
BuildArch: noarch
BuildRequires: fontconfig

BuildRequires: x11-font-util >= 1.0.0
BuildRequires: x11-util-macros >= 1.0.2

Conflicts: xorg-x11 <= 6.9.0
Requires(post): /bin/sh
Requires(post,postun): mkfontdir mkfontscale

%description
Xorg X11 font misc-misc.

%prep
%autosetup -n font-misc-misc-%{version} -p1

%build
%configure --with-fontdir=%{_datadir}/fonts/misc

%make_build

%install
%make_install
rm -f %{buildroot}%{_datadir}/fonts/misc/fonts.dir
rm -f %{buildroot}%{_datadir}/fonts/misc/fonts.scale

%post
mkfontscale %{_datadir}/fonts/misc
mkfontdir %{_datadir}/fonts/misc

%postun
mkfontscale %{_datadir}/fonts/misc
mkfontdir %{_datadir}/fonts/misc

%files
%{_datadir}/fonts/misc/10x20*.pcf.gz
%{_datadir}/fonts/misc/12x13ja.pcf.gz
%{_datadir}/fonts/misc/18x18*.pcf.gz
%{_datadir}/fonts/misc/4x6*.pcf.gz
%{_datadir}/fonts/misc/5x7*.pcf.gz
%{_datadir}/fonts/misc/5x8*.pcf.gz
%{_datadir}/fonts/misc/6x10*.pcf.gz
%{_datadir}/fonts/misc/6x12*.pcf.gz
%{_datadir}/fonts/misc/6x13*.pcf.gz
%{_datadir}/fonts/misc/6x9*.pcf.gz
%{_datadir}/fonts/misc/7x13*.pcf.gz
%{_datadir}/fonts/misc/7x14*.pcf.gz
%{_datadir}/fonts/misc/8x13*.pcf.gz
%{_datadir}/fonts/misc/9x15*.pcf.gz
%{_datadir}/fonts/misc/9x18*.pcf.gz
%{_datadir}/fonts/misc/k14.pcf.gz
%{_datadir}/fonts/misc/nil2.pcf.gz
