%global commit          ca8ab7d8e196a6081ba4ae571174b29d6ee516c2
%global commit_short    %(c=%{commit}; echo ${c:0:7})

Name:       featherpad
Version:    0.5.8
Release:    2.%{commit_short}%{?dist}
Summary:    Lightweight Qt5 Plain Text Editor for Linux
Group:      Applications/Editors
License:    GPLv3
URL:        https://github.com/tsujan/FeatherPad
Source0:    https://github.com/tsujan/FeatherPad/archive/%{commit}.tar.gz#/%{name}-%{commit_short}.tar.gz
BuildRequires:	qt5-linguist
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xext)
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5X11Extras)
BuildRequires:	pkgconfig(Qt5Svg)
Requires:       pkgconfig(Qt5Svg)

%description
FeatherPad is a lightweight Qt5 plain-text editor for Linux.
It is independent of any desktop environment

%prep
%setup -n FeatherPad-%{commit}

%build
%{qmake_qt5}
make %{?_smp_mflags}

%install
make install INSTALL_ROOT=%{buildroot}

%files
%doc COPYING README ChangeLog NEWS
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/%{name}/help
%dir %{_datadir}/%{name}/translations
%{_datadir}/%{name}/translations/*.qm


%changelog
* Tue Feb 14 2017 Vaughan <devel at agrez dot net> - 0.5.8-2.ca8ab7d
- Update to git commit: ca8ab7d8e196a6081ba4ae571174b29d6ee516c2
- Add BuildRequires: qt5-linguist

* Sun Oct 16 2016 Vaughan <devel at agrez dot net> - 0.5.8-1.17c8ca4
- New release (git commit 17c8ca4d6faa36ba84c63f033beb089ba3168bbc)
- Update BuildRequires/Requires

* Fri Aug 26 2016 Vaughan <devel at agrez dot net> - 0.5.7-1.c7f6246
- Initial package

