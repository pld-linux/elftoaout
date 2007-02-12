Summary:	A utility for converting ELF binaries to a.out binaries
Summary(pl.UTF-8):   Narzędzie do konwersji binariów ELF do a.out
Name:		elftoaout
Version:	2.3
Release:	1.1
License:	GPL v2
Group:		Applications/System
Source0:	ftp://sunsite.icm.edu.pl/site/linux-sparc/elftoaout/%{name}-%{version}.tgz
# Source0-md5:	be3bd6f7ba8ae107cbdbaa820ba64f86
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The elftoaout utility converts a static ELF binary to a static a.out
binary. If you're using an ELF system (i.e., Red Hat Linux) on a
SPARC, you'll need to run elftoaout on the kernel image so that the
SPARC PROM can netboot the image.

If you're installing Red Hat Linux on a SPARC, you'll need to install
the elftoaout package.

%description -l pl.UTF-8
Narzędzie elftoaout konwertuje statyczne binaria ELF do statycznych
binariów a.out. Jeśli używacie systemu opartego na ELF-ie na SPARC-u,
będziecie musieli przekonwertować obraz kernela za pomocą elftoaout,
aby SPARC PROM mógł go uruchomić z sieci. Jeśli instaluje się Linuksa
na SPARC-u, należy zainstalować pakiet elftoaout.

%prep
%setup -q

%build
%{__make} \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install elftoaout $RPM_BUILD_ROOT%{_bindir}/elftoaout
install elftoaout.1 $RPM_BUILD_ROOT%{_mandir}/man1/elftoaout.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/elftoaout
%{_mandir}/man1/*
