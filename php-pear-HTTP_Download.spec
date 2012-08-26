%define		_class		HTTP
%define		_subclass	Download
%define		_status		stable
%define		_pearname	HTTP_Download
%include	/usr/lib/rpm/macros.php
Summary:	%{_pearname} - send HTTP Downloads
Summary(pl.UTF-8):	%{_pearname} - obsługa transferu plików przez HTTP
Name:		php-pear-%{_pearname}
Version:	1.1.4
Release:	4
License:	PHP 3.0
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	5b206aee22b0865a5991c74054154bf3
URL:		http://pear.php.net/package/HTTP_Download/
BuildRequires:	php-pear-PEAR >= 1:1.6.0
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php(core) >= 4.2.0
Requires:	php(pcre)
Requires:	php-pear
Requires:	php-pear-HTTP_Header
Requires:	php-pear-PEAR-core
Suggests:	php-mime_magic
Suggests:	php-pear-Archive_Tar
Suggests:	php-pear-Archive_Zip
Suggests:	php-pear-MIME_Type
Suggests:	php-pgsql
Obsoletes:	php-pear-HTTP_Download-tests
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
Ta klasa dostarcza prosty w użyciu interfejs do wysyłania ukrytych
plików lub dowolnych danych do klienta poprzez HTTP. Możliwości to
cache'owanie HTTP, kompresja oraz zakresy (częściowe ściąganie oraz
wznawianie połączenia).

UWAGA: Nie należy używać tej klasy wraz z opcją PHP kompresji "w
locie", gdyż przesłane pliki mogą być uszkodzone.

Ta klasa ma w PEAR status: %{_status}.

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
%{php_pear_dir}/HTTP/*.php
%{php_pear_dir}/HTTP/Download
