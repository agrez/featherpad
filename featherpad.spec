%global commit          c7f62469af0222a3cedefbb39278e4f80077dcfb
%global commit_short    %(c=%{commit}; echo ${c:0:7})

Name:       featherpad
Version:    0.5.7
Release:    1.%{commit_short}%{?dist}
Summary:    Lightweight Qt5 Plain Text Editor for Linux
Group:      Applications/Editors
License:    GPLv3
URL:        https://github.com/tsujan/FeatherPad
Source0:    https://github.com/tsujan/FeatherPad/archive/%{commit}.tar.gz#/%{name}-%{commit_short}.tar.gz
BuildRequires:	libX11-devel
BuildRequires:	libXext-devel
BuildRequires:	qt5-qtbase-devel
BuildRequires:	qt5-qtx11extras-devel
Requires:       qt5-qtsvg

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


%changelog
* Fri Aug 26 2016 Vaughan <devel at agrez dot net> - 0.5.7-1.c7f6246
- Initial package

