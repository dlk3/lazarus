%define  debug_package %{nil}

Name:		lazarus
Version:	4.0.0
Release:	1
Summary:	Lazarus Component Library and IDE for Free Pascal
License:	GPLv2+ and LGPLv2+ with exceptions # https://sourceforge.net/p/lazarus/laz.git/ci/lazarus_4_0/tree/COPYING.txt
URL:		https://www.lazarus-ide.org/
Source0:	%{name}-%{version}.tar.gz
BuildArch:	x86_64

Requires:	fpc >= 3.2.2
BuildRequires:	fpc == 3.2.2
BuildRequires:	glibc-devel

%description
Lazarus is an IDE to create (graphical and console) applications with
Free Pascal, the (L)GPLed Pascal and Object Pascal compiler that runs on
Windows, Linux, Mac OS X, FreeBSD and more.

Lazarus is the missing part of the puzzle that will allow you to develop
programs for all of the above platforms in a Delphi-like environment.
The IDE is a RAD tool that includes a form designer.

Unlike Java's "write once, run anywhere" motto, Lazarus and Free Pascal
strive for "write once, compile anywhere". Since the exact same compiler
is available on all of the above platforms you don't need to do any recoding
to produce identical products for different platforms.

In short, Lazarus is a free RAD tool for Free Pascal using its
Lazarus Component Library (LCL).

%prep
%setup -q

%build
make bigide

%install
make PREFIX=%{buildroot}/usr install

%files
%{_bindir}
%{_datadir}

%changelog
* Fri Jun 06 2025 dlk3 <dave@daveking.com> 4.0.0-1
- Correct the version number

* Fri Jun 06 2025 dlk3 <dave@daveking.com> 3.2.4-1
- new package built with tito

* Thu Jun 05 2025 dlk3 <dave@daveking.com> 4.0.0-0
- Initial version of package
