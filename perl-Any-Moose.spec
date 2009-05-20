%define module   Any-Moose
%define version    0.07
%define release    %mkrel 3

Name:       perl-%{module}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Use Moose or Mouse modules
Url:        http://search.cpan.org/dist/%{module}
Source:     http://www.cpan.org/modules/by-module/Any/%{module}-%{version}.tar.gz
BuildRequires: perl(Mouse)
Requires:       perl-Moose-implementation
BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}

%description
Actual documentation is forthcoming, once we solidify all the bits of the
API. The examples above are very likely to continue working.

%prep
%setup -q -n %{module}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes LICENSE README
%{_mandir}/man3/*
%perl_vendorlib/*


