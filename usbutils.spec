Summary:	Linux USB utilities
Name:		usbutils
Version:	008
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://www.kernel.org/pub/linux/utils/usb/usbutils/%{name}-%{version}.tar.xz
# Source0-md5:	2780b6ae21264c888f8f30fb2aab1259
URL:		http://www.linux-usb.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	libusbx-devel
BuildRequires:	rpm-pythonprov
Requires:	coreutils
Requires:	hwids
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_datadir	/usr/share/hwdata

%description
usbutils contains a utility for inspecting devices connected to the
USB bus.

%prep
%setup -q

%{__sed} -i 's/env python/python/' lsusb.py

%build
cd usbhid-dump
%{__aclocal} -I m4
%{__libtoolize}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
cd ..
%{__aclocal}
%{__libtoolize}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules	\
	--disable-zlib
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT	\
	pkgconfigdir=%{_pkgconfigdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/lsusb
%attr(755,root,root) %{_bindir}/lsusb.py
%attr(755,root,root) %{_bindir}/usb-devices
%attr(755,root,root) %{_bindir}/usbhid-dump
%{_pkgconfigdir}/usbutils.pc
%{_mandir}/man1/*.1*
%{_mandir}/man8/*.8*

