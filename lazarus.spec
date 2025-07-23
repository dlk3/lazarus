%define  debug_package %{nil}

Name:		{{{ git_dir_name }}}
Version:	4.0.0
Release:	3
Summary:	Lazarus Component Library and IDE for Free Pascal
License:	GPLv2+ and LGPLv2+ with exceptions # https://sourceforge.net/p/lazarus/laz.git/ci/lazarus_4_0/tree/COPYING.txt
URL:		https://www.lazarus-ide.org/
Source0:	{{{ git_dir_pack}}}
BuildArch:	x86_64

Requires:	fpc >= 3.2.4
BuildRequires:	fpc == 3.2.4
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
{{{ git_dir_setup_macro }}}

%build
make bigide

%install
make PREFIX=%{buildroot}/usr install

%files
%{_bindir}
%{_datadir}

%changelog
{{{ git_dir_changelog }}}

* Wed Jul 23 2025 dlk3 <dave@daveking.com> 4.0.0-2
- Modify spec file to support rpkg build on COPR

* Fri Jun 06 2025 dlk3 <dave@daveking.com> 4.0.0-2
- Add glibc-devel build dependency to get cmake package included
  (dave@daveking.com)

* Fri Jun 06 2025 dlk3 <dave@daveking.com> 4.0.0-1
- Correct the version number

* Fri Jun 06 2025 dlk3 <dave@daveking.com> 3.2.4-1
- new package built with tito

* Thu Jun 05 2025 dlk3 <dave@daveking.com> 4.0.0-0
- Initial version of package
