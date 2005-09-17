# ToDo:
# - fix pl description (arbitrary data ?)

%include	/usr/lib/rpm/macros.php
%define		_class		HTTP
%define		_subclass	Download
%define		_status		beta
%define		_pearname	%{_class}_%{_subclass}
%define		_rc			RC3

Summary:	%{_pearname} - send HTTP Downloads
Summary(pl):	%{_pearname} - obs³uga transferu plików przez HTTP
Name:		php-pear-%{_pearname}
Version:	1.1.0
Release:	0.%{_rc}.1
License:	PHP 3.0
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}%{_rc}.tgz
# Source0-md5:	99407a5748ae3c87f4d0e087a6c127e5
URL:		http://pear.php.net/package/HTTP_Download/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# Archive_Zip was never released
%define		_noautoreq	'pear(Archive/Zip.php)'

%description
Provides an easy interface to send hidden files or any arbitrary data to
the client over HTTP. It features HTTP Caching, Compression and Ranges
(partial downloads and resuming).

NOTE: Don't use with PHP's on-the-fly output compression, because files
may be sent coruppted.

In PEAR status of this package is: %{_status}.

%description -l pl
Dostarcza prostego w u¿yciu interfejsu do wysy³ania ukrytych plików do
klienta poprzez HTTP. Mo¿liwo¶ci to cache'owanie HTTP, kompresja oraz
zakresy (czê¶ciowe ¶ci±ganie oraz wznawianie po³±czenia).

UWAGA: Nie u¿ywaj tej klasy wraz z opcj± PHP kompresji "w locie", gdy¿
przes³ane pliki mog± byæ uszkodzone.

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c -n %{name}-%{version}%{_rc}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

install %{_pearname}-%{version}%{_rc}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{php_pear_dir}/%{_class}/*.php
