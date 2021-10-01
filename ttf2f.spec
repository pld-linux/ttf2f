Summary:	Truetype font to RISC OS font converter
Summary(pl.UTF-8):	Konwerter fontów TrueType na fonty RISC OS
Name:		ttf2f
Version:	0.0.6
Release:	1
License:	BSD
Group:		Applications/File
#Source0Download: http://source.netsurf-browser.org/ttf2f.git/
Source0:	http://source.netsurf-browser.org/ttf2f.git/snapshot/ttf2f-releases/%{version}.tar.bz2?/%{name}-%{version}.tar.bz2
# Source0-md5:	4fa5e48467c4614d3c325d12b9ee8e6d
URL:		http://www.netsurf-browser.org/projects/ttf2f/
BuildRequires:	freetype-devel >= 2.0
BuildRequires:	netsurf-buildsystem
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Truetype font to RISC OS font converter.

%description -l pl.UTF-8
Konwerter fontów TrueType na fonty RISC OS.

%prep
%setup -q -c

%{__mv} ttf2f-releases/%{version}/* .

%build
CFLAGS="%{rpmcflags}" \
%{__make} \
	CC="%{__cc}" \
	PREFIX=%{_prefix}

%install
rm -rf $RPM_BUILD_ROOT

install -D build-*-release-binary/ttf2f $RPM_BUILD_ROOT%{_bindir}/ttf2f

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc riscos/Help
%attr(755,root,root) %{_bindir}/ttf2f
