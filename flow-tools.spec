Summary:	Collecting and processing NetFlow data
Summary(pl):	Gromadzenie i przetwarzanie informacji o przepływie w sieci
Name:		flow-tools
Version:	0.67
Release:	2
License:	BSD
Group:		Applications/Networking
Source0:	ftp://ftp.eng.oar.net/pub/flow-tools/%{name}-%{version}.tar.gz
# Source0-md5:	0ee0a2830effa554d1925236aad6b4fe
Patch0:		%{name}-shared.patch
URL:		http://www.splintered.net/sw/flow-tools/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	libtool
BuildRequires:	libwrap-devel >= 7.6-32
BuildRequires:	zlib-devel
Requires:	%{name}-libs = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_localstatedir	%{_sysconfdir}/%{name}

%description
This is a software package for collecting and processing NetFlow data
from Cisco and Juniper routers.

%description -l pl
Jest to oprogramowanie służące do gromadzenia i przetwarzania
informacji o przepływie w sieci (NetFlow) z routerów Cisco i Juniper.

%package libs
Summary:	flow-tools library
Summary(pl):	Biblioteka flow-tools
Group:		Libraries
Conflicts:	flow-tools < 0.67-2

%description libs
flow-tools library.

%description libs -l pl
Biblioteka flow-tools.

%package devel
Summary:	Header files flow-tools library
Summary(pl):	Pliki nagłówkowe biblioteki flow-tools
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	zlib-devel

%description devel
This package contains header files for flow-tools library.

%description devel -l pl
Ten pakiet zawiera pliki nagłówkowe biblioteki flow-tools.

%package static
Summary:	Static flow-tools library
Summary(pl):	Statyczna biblioteka flow-tools
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static flow-tools library.

%description static -l pl
Statyczna biblioteka flow-tools.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
#	--with-mysql
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog INSTALL NEWS README SECURITY TODO
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libft.so.*.*.*
%{_sysconfdir}

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libft.so
%{_libdir}/libft.la
%{_includedir}/*.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libft.a
