Summary:	Linux USB utilities
Name:		usbutils
Version:	005
Release:	2
License:	GPL
Group:		Applications/System
#Source0:	http://www.kernel.org/pub/linux/utils/usb/usbutils/%{name}-%{version}.tar.bz2
Source0:	http://ftp.de.debian.org/debian/pool/main/u/usbutils/%{name}_%{version}.orig.tar.gz
# Source0-md5:	2e990265d472e2f6f0662356d654683b
Patch0:		%{name}-canons90.patch
URL:		http://www.linux-usb.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	libusbx-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_datadir	/etc

%description
usbutils contains a utility for inspecting devices connected to the
USB bus.

%prep
%setup -q
%patch0 -p1

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
	--disable-silent-rules
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
%attr(755,root,root) %{_bindir}/usb-devices
%attr(755,root,root) %{_bindir}/usbhid-dump
%attr(755,root,root) %{_sbindir}/*
%{_datadir}/usb.ids
%{_pkgconfigdir}/usbutils.pc
%{_mandir}/man1/*.1*
%{_mandir}/man8/*.8*

