%define	upstream_name	 CGI-Minimal
%define upstream_version 1.29

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Extremely lightweight CGI processing package
License:	GPL
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/CGI/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildArch:	noarch

%description
CGI-Minimal is an extremely lightweight Perl module that provides CGI
processing abilities designed to provide form decoding and related services
with low overhead.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std
rm -f %{buildroot}%{perl_archlib}/perllocal.pod

%files
%doc Changes README
%{perl_vendorlib}/CGI
%{_mandir}/man3/*


%changelog
* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 1.290.0-2mdv2011.0
+ Revision: 680691
- mass rebuild

* Wed Jul 29 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.290.0-1mdv2011.0
+ Revision: 402999
- rebuild using %%perl_convert_version

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 1.29-3mdv2009.0
+ Revision: 255776
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 1.29-1mdv2008.1
+ Revision: 136678
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Aug 22 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.29-1mdv2008.0
+ Revision: 69214
- update to new version 1.29

* Sun Jul 01 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.27-1mdv2008.0
+ Revision: 46338
- update to new version 1.27

* Tue May 01 2007 Olivier Thauvin <nanardon@mandriva.org> 1.26-1mdv2008.0
+ Revision: 19750
- 1.26


* Sat Oct 28 2006 Nicolas LÃ©cureuil <neoclust@mandriva.org> 1.25-1mdv2007.0
+ Revision: 73391
- import perl-CGI-Minimal-1.25-1mdv2007.0

* Wed May 31 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.25-1mdv2007.0
- New release 1.25

* Fri Apr 28 2006 Nicolas Lécureuil <neoclust@mandriva.org> 1.24-2mdk
- Fix SPEC Using perl Policies
	- Source URL
- use mkrel

* Tue Sep 27 2005 Nicolas Lécureuil <neoclust@mandriva.org> 1.24-1mdk
- New release 1.24

* Thu Sep 22 2005 Guillaume Rousse <guillomovitch@mandriva.org> 1.23-1mdk
- New release 1.23
- spec cleanup
- don't ship manifest
- fix directory ownership
- better url

* Tue Nov 16 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.16-1mdk
- 1.16

* Wed May 12 2004 Michael Scherer <misc@mandrake.org> 1.11-1mdk
- New release 1.11
- rpmbuildupdate aware

