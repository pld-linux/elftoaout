Summary:	A utility for converting ELF binaries to a.out binaries
Summary:	Narzêdzie do konwersji binariów ELF do a.out
Name:		elftoaout
Version:	2.3
Release:	1
License:	GPL
Group:		Applications/System
Group(de):	Applikationen/System
Group(pl):	Aplikacje/System
Source0:	ftp://sunsite.mff.cuni.cz/OS/Linux/Sparc/local/elftoaout/%{name}-%{version}.tgz
ExclusiveArch:	sparc sparc64
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The elftoaout utility converts a static ELF binary to a static a.out
binary. If you're using an ELF system (i.e., Red Hat Linux) on a
SPARC, you'll need to run elftoaout on the kernel image so that the
SPARC PROM can netboot the image.

If you're installing Red Hat Linux on a SPARC, you'll need to install
the elftoaout package.

%description -l pl
Narzêdzie elftoaout konwertuje statyczne binaria ELF do statycznych
binariów a.out. Je¶li u¿ywacie systemu opartego na ELF-ie na SPARC-u,
bêdziecie musieli przekonwertowaæ obraz kernela za pomoc± elftoaout,
aby SPARC PROM móg³ go uruchomiæ z sieci. Je¶li instaluje siê Linuksa
na SPARC-u, nale¿y zainstalowaæ pakiet elftoaout.

%prep
%setup -q

%build
%{__make} CFLAGS="%{rpmcflags}"

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
