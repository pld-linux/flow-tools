Summary:	Collecting and processing NetFlow data
Summary(pl):	Gromadzenie i przetwarzanie informacji o przep³ywie w sieci
Name:		flow-tools
Version:	0.67
Release:	1
License:	BSD
Group:		Applications/Networking
Source0:	ftp://ftp.eng.oar.net/pub/flow-tools/%{name}-%{version}.tar.gz
# Source0-md5:	0ee0a2830effa554d1925236aad6b4fe
URL:		http://www.splintered.net/sw/flow-tools/
BuildRequires:	bison
BuildRequires:	flex
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_localstatedir	%{_sysconfdir}/%{name}

%description
This is a software package for collecting and processing NetFlow data
from Cisco and Juniper routers.

%description -l pl
Jest to oprogramowanie s³u¿±ce do gromadzenia i przetwarzania
informacji o przep³ywie w sieci (NetFlow) z routerów Cisco i Juniper.

%package devel
Summary:	Header files and develpment documentation for flow-tools
Summary(pl):	Pliki nag³ówkowe i dokumentacja programisty do flow-tools
Group:		Development/Libraries
#Requires:	%{name} = %{version}

%description devel
This package contains Header files and develpment documentation for
flow-tools.

%description devel -l pl
Ten pakiet zawiera pliki nag³ówkowe i dokumentacjê programisty do
flow-tools.

%prep
%setup -q

%build
%configure \
#	--with-mysql
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog INSTALL NEWS README SECURITY TODO
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man?/*
%{_sysconfdir}

%files devel
%defattr(644,root,root,755)
%{_includedir}/*.h
%{_libdir}/*.a
