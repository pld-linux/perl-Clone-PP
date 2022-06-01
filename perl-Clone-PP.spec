#
# Conditional build:
%bcond_without	tests	# unit tests
#
%define	pdir	Clone
%define	pnam	PP
Summary:	Clone::PP - recursively copy Perl datatypes
Summary(pl.UTF-8):	Clone::PP - rekurencyjne kopiowanie perlowych typów danych
Name:		perl-Clone-PP
Version:	1.08
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Clone/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	62f9547aec61768af85b00bd2c3e5547
URL:		https://metacpan.org/dist/Clone-PP
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides a general-purpose clone function to make deep
copies of Perl data structures. It calls itself recursively to copy
nested hash, array, scalar and reference types, including tied
variables and objects.

%description -l pl.UTF-8
Ten moduł udostępnia funkcję ogólnego przeznaczenia clone, wykonującą
głęboką kopię perlowych struktur danych. Wywołuje sama siebie
rekurencyjnie, aby skopiować zagnieżdżone hasze, tablice, skalary i
referencje, w tym dowiązane zmienne i obiekty.

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
%doc Changes
%{perl_vendorlib}/Clone/PP.pm
%{_mandir}/man3/Clone::PP.3pm*
