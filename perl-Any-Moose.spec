%define upstream_name    Any-Moose
%define upstream_version 0.09

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

License:    GPL+ or Artistic
Group:      Development/Perl
Summary:    Use Moose or Mouse modules
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://search.cpan.org/CPAN/authors/id/F/FL/FLORA/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Mouse)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
Actual documentation is forthcoming, once we solidify all the bits of the
API. The examples above are very likely to continue working.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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

