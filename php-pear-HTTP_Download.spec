# ToDo:
# - fix pl description (arbitrary data ?)

%include	/usr/lib/rpm/macros.php
%define		_class		HTTP
%define		_subclass	Download
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}
Summary:	%{_pearname} - send HTTP Downloads
Summary(pl.UTF-8):	%{_pearname} - obsługa transferu plików przez HTTP
Name:		php-pear-%{_pearname}
Version:	1.1.3
Release:	2
Epoch:		0
License:	PHP 3.0
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	d8113c7e6fca25724680b499e3c0644a
URL:		http://pear.php.net/package/HTTP_Download/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php(pcre)
Requires:	php-common >= 3:4.2.0
Requires:	php-pear
Requires:	php-pear-HTTP_Header
Requires:	php-pear-PEAR-core
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# Archive_Zip was never released
%define		_noautoreq	'pear(Archive/Tar.php)' 'pear(Archive/Zip.php)' 'pear(MIME/Type.*)'

%description
Provides an easy interface to send hidden files or any arbitrary data
to the client over HTTP. It features HTTP Caching, Compression and
Ranges (partial downloads and resuming).

NOTE: Don't use with PHP's on-the-fly output compression, because
files may be sent coruppted.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Dostarcza prostego w użyciu interfejsu do wysyłania ukrytych plików do
klienta poprzez HTTP. Możliwości to cache'owanie HTTP, kompresja oraz
zakresy (częściowe ściąganie oraz wznawianie połączenia).

UWAGA: Nie używaj tej klasy wraz z opcją PHP kompresji "w locie", gdyż
przesłane pliki mogą być uszkodzone.

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl.UTF-8):	Testy dla PEAR::%{_pearname}
Group:		Development/Languages/PHP
Requires:	%{name} = %{epoch}:%{version}-%{release}
AutoReq:	no
AutoProv:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl.UTF-8
Testy dla PEAR::%{_pearname}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -f %{_docdir}/%{name}-%{version}/optional-packages.txt ]; then
	cat %{_docdir}/%{name}-%{version}/optional-packages.txt
fi

%files
%defattr(644,root,root,755)
%doc install.log optional-packages.txt
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/*
