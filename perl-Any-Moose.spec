%define upstream_name    Any-Moose
%define upstream_version 0.21

Name:		perl-%{upstream_name}
Version:	%perl_convert_version 0.21
Release:	3

Summary:	Use Moose or Mouse modules
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/authors/id/S/SA/SARTAK/Any-Moose-0.21.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Mouse)
BuildArch:	noarch
Requires:	perl(Mouse)

%description
Actual documentation is forthcoming, once we solidify all the bits of the
API. The examples above are very likely to continue working.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes LICENSE README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Mon Jun 13 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.150.0-1mdv2011.0
+ Revision: 684735
- update to new version 0.15

* Mon Apr 25 2011 Funda Wang <fwang@mandriva.org> 0.130.0-2
+ Revision: 658514
- rebuild for updated spec-helper

* Wed Jul 14 2010 Jérôme Quelin <jquelin@mandriva.org> 0.130.0-1mdv2011.0
+ Revision: 553061
- update to 0.13

* Tue Apr 06 2010 Jérôme Quelin <jquelin@mandriva.org> 0.120.0-1mdv2010.1
+ Revision: 532137
- update to 0.12

* Mon Dec 14 2009 Jérôme Quelin <jquelin@mandriva.org> 0.110.0-1mdv2010.1
+ Revision: 478547
- update to 0.11

* Thu Oct 01 2009 Jérôme Quelin <jquelin@mandriva.org> 0.100.0-2mdv2010.0
+ Revision: 452038
- bump mkrel
- adding missing runtime requires:

* Mon Jul 06 2009 Jérôme Quelin <jquelin@mandriva.org> 0.100.0-1mdv2010.0
+ Revision: 392717
- update to 0.10

* Mon Jun 08 2009 Jérôme Quelin <jquelin@mandriva.org> 0.90.0-1mdv2010.0
+ Revision: 384052
- update to 0.09
- using %%perl_convert_version
- cleaned license tag

* Thu May 21 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.07-4mdv2010.0
+ Revision: 378280
- hardcode Mouse dependency, virtual package is useless

* Thu May 21 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.07-3mdv2010.0
+ Revision: 378182
- requires perl-Moose-implementation virtual package

* Fri May 15 2009 Jérôme Quelin <jquelin@mandriva.org> 0.07-2mdv2010.0
+ Revision: 375966
- rebuild

* Mon May 04 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.07-1mdv2010.0
+ Revision: 371866
- import perl-Any-Moose


* Mon May 04 2009 cpan2dist 0.07-1mdv
- initial mdv release, generated with cpan2dist


