Summary: A utility for converting ELF binaries to a.out binaries.
Name: elftoaout
Version: 2.2
Release: 3
ExclusiveArch: sparc sparc64
Copyright: GPL
Group: System Environment/Kernel
Source: ftp://sunsite.mff.cuni.cz/OS/Linux/Sparc/local/elftoaout/elftoaout-2.2.tgz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The elftoaout utility converts a static ELF binary to a static a.out
binary.  If you're using an ELF system (i.e., Red Hat Linux) on a SPARC,
you'll need to run elftoaout on the kernel image so that the SPARC PROM
can netboot the image.

If you're installing Red Hat Linux on a SPARC, you'll need to install the
elftoaout package.

%description -l pl
Narzêdzie elftoaout konwertuje statyczne binaria ELF do statycznych binariów
a.out. Je¶li u¿ywacie systemu opartego na ELF-ie na SPARC-u, bêdziecie musieli
przekonwertowaæ obraz kernela za pomoc± elftoaout, aby SPARC PROM móg³
go uruchomiæ z sieci.
Je¶li instaluje siê Linuksa na SPARC-u, nale¿y zainstalowaæ pakiet elftoaout.

%prep
%setup -q

%build
make

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT/usr/bin
install -m 0755 -s elftoaout $RPM_BUILD_ROOT/usr/bin/elftoaout

mkdir -p $RPM_BUILD_ROOT/usr/man/man1
install -m 0644 elftoaout.1 $RPM_BUILD_ROOT/usr/man/man1/elftoaout.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/bin/elftoaout
/usr/man/man1/elftoaout.1
