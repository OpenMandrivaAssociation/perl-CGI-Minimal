%define	module	CGI-Minimal
%define name	perl-%{module}
%define version 1.29
%define release %mkrel 3

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Extremely lightweight CGI processing package
License:	GPL
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}
Source:		http://www.cpan.org/modules/by-module/CGI/%{module}-%{version}.tar.bz2
%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildArch:	noarch
Buildroot:	%{_tmppath}/%{name}-%{version}

%description
CGI-Minimal is an extremely lightweight Perl module that provides CGI
processing abilities designed to provide form decoding and related services
with low overhead.


%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std
rm -f %{buildroot}%{perl_archlib}/perllocal.pod

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/CGI
%{_mandir}/man3/*



