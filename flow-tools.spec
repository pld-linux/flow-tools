Summary:	collecting and processing NetFlow data
Name:		flow-tools
Version:	0.66
Release:	1
License:	BSD
Group:		Applications/Networking
Source0:	ftp://ftp.eng.oar.net/pub/flow-tools/%{name}-%{version}.tar.gz
# Source0-md5:	a32f02be71b29f0d4fe65c0d196d0093
URL:		http://www.splintered.net/sw/flow-tools/
BuildRequires:	flex
BuildRequires:	bison
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_localstatedir	%{_sysconfdir}/%{name}

%description
A software package for collecting and processing NetFlow data from Cisco and Juniper routers.

%package devel
Summary:        Header files and develpment documentation for flow-tools
Group:          Development/Libraries
#Requires:       %{name} = %{version}

%description devel
Header files and develpment documentation for flow-tools.

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
