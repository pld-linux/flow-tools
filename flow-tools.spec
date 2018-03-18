Summary:	Collecting and processing NetFlow data
Summary(pl.UTF-8):	Gromadzenie i przetwarzanie informacji o przepływie w sieci
Name:		flow-tools
Version:	0.68.5
Release:	5
License:	BSD
Group:		Applications/Networking
Source0:	http://flow-tools.googlecode.com/files/%{name}-%{version}.tar.bz2
# Source0-md5:	3c5e75da2822ab6b4947c928c09ea365
Patch0:		%{name}-shebang.patch
Patch1:		format-security.patch
URL:		http://code.google.com/p/flow-tools/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	libtool
BuildRequires:	libwrap-devel >= 7.6-32
BuildRequires:	mysql-devel
BuildRequires:	openssl-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	zlib-devel
Requires:	%{name}-libs = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a software package for collecting and processing NetFlow data
from Cisco and Juniper routers.

%description -l pl.UTF-8
Jest to oprogramowanie służące do gromadzenia i przetwarzania
informacji o przepływie w sieci (NetFlow) z routerów Cisco i Juniper.

%package libs
Summary:	flow-tools library
Summary(pl.UTF-8):	Biblioteka flow-tools
Group:		Libraries
Conflicts:	flow-tools < 0.67-2

%description libs
flow-tools library.

%description libs -l pl.UTF-8
Biblioteka flow-tools.

%package devel
Summary:	Header files flow-tools library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki flow-tools
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	zlib-devel

%description devel
This package contains header files for flow-tools library.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe biblioteki flow-tools.

%package static
Summary:	Static flow-tools library
Summary(pl.UTF-8):	Statyczna biblioteka flow-tools
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static flow-tools library.

%description static -l pl.UTF-8
Statyczna biblioteka flow-tools.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--sysconfdir=%{_sysconfdir}/%{name} \
	--with-mysql \
	--with-openssl
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
%doc AUTHORS ChangeLog ChangeLog.old INSTALL README README.fork SECURITY TODO
%attr(755,root,root) %{_bindir}/flow-*
%attr(755,root,root) %{_datadir}/%{name}
%{_mandir}/man1/flow-*.1*

%files libs
%defattr(644,root,root,755)
%{_sysconfdir}/%{name}
%attr(755,root,root) %{_libdir}/libft.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libft.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libft.so
%{_libdir}/libft.la
%{_includedir}/*.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libft.a
