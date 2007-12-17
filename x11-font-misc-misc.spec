Name: x11-font-misc-misc
Version: 1.0.0
Release: %mkrel 6
Summary: Xorg X11 font misc-misc
Group: Development/X11
URL: http://xorg.freedesktop.org
Source: http://xorg.freedesktop.org/releases/individual/font/font-misc-misc-%{version}.tar.bz2
License: Public Domain
BuildArch: noarch

BuildRequires: x11-font-util >= 1.0.0
BuildRequires: x11-util-macros >= 1.0.1

Conflicts: xorg-x11 <= 6.9.0
PreReq: mkfontdir
PreReq: mkfontscale

%description
Xorg X11 font misc-misc

%prep
%setup -q -n font-misc-misc-%{version}

%build
%configure2_5x --with-fontdir=%_datadir/fonts/misc

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


