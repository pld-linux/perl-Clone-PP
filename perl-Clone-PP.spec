#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Clone
%define	pnam	PP
Summary:	Clone::PP - Recursively copy Perl datatypes
#Summary(pl.UTF-8):	
Name:		perl-Clone-PP
Version:	1.02
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Clone/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	8dd40e1072232006ff0242a823897e09
URL:		http://search.cpan.org/dist/Clone-PP/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides a general-purpose clone function to make deep
copies of Perl data structures. It calls itself recursively to copy
nested hash, array, scalar and reference types, including tied
variables and objects.

# %description -l pl.UTF-8
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorlib}/Clone/*.pm
%{_mandir}/man3/*
