Summary:	File compressor using LZO library
Name:		lzop
Version:	1.03
Release:	1
License:	GPL v2+
Group:		Applications/Archiving
Source0:	http://www.lzop.org/download/%{name}-%{version}.tar.gz
# Source0-md5:	006c5e27fb78cdd14a628fdfa5aa1905
URL:		http://www.lzop.org/
BuildRequires:	automake
BuildRequires:	lzo-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
lzop is a file compressor which is very similar to gzip. lzop uses the
LZO data compression library for compression services, and its main
advantages over gzip are much higher compression and decompression
speed (at the cost of some compression ratio).

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README THANKS
%attr(755,root,root) %{_bindir}/lzop
%{_mandir}/man1/lzop.1*

