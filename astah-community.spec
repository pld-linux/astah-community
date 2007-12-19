%define		codename	community
%define		ver		%(echo %{version} | tr . _)
%include	/usr/lib/rpm/macros.java
Summary:	A New Java/UML Object-Oriented Design Tool
Summary(pl.UTF-8):	Narzędzie wspomagające projektowanie oprogramowania w UML
Name:		jude
Version:	5.1.1
Release:	2
# non-distributable, can be used for free upon restrictions and registration
License:	Proprietary (see http://jude.change-vision.com/jude-web/notes/ProductLicenseAgreement.html)
Group:		Applications/Engineering
Source0:	http://jude-users.com/edujjude/%{name}-community-%{ver}.zip
# NoSource0-md5:	ce46e0f9ca720ead60d52c052da228a3
Source1:	%{name}.desktop
Source2:	x-%{name}.desktop
Source3:	%{name}-icon.png
NoSource:	0
URL:		http://jude-users.com/en/
BuildRequires:	rpm-javaprov
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	jre
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Jude is a new tool which supports your object-oriented software
designing in JavaTM and UML1.4 (Unified Modeling Language).

This package contains Community version, which is freely usable upon
some restrictions after registration on vendor site.

%description -l pl.UTF-8
Jude jest nowym narzędziem wspomagającym zorientowane obiektowo
projektowanie oprogramowania w JavaTM i UML1.4 (Unified Modeling
Language).

Ten pakiet zawiera wersję społecznościową, której można używać bez
opłat pod pewnymi ograniczenami, po uprzedniej rejestracji na stronie
producenta.

%prep
%setup -q -n %{name}_%{codename}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name}}

cat <<'EOF' > $RPM_BUILD_ROOT%{_bindir}/%{name}
#!/bin/sh
exec java -Xms16m -Xmx256m -Xss1m -jar %{_datadir}/%{name}/jude-%{codename}.jar ${1:+"$@"}
EOF
install jude-%{codename}.jar JudeDefaultModel.jude $RPM_BUILD_ROOT%{_datadir}/%{name}

install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_datadir}/mimelnk/application,%{_pixmapsdir}}
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/mimelnk/application
install %{SOURCE3} $RPM_BUILD_ROOT%{_pixmapsdir}/%{name}.png

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README* ReleaseNote*
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_desktopdir}/%{name}.desktop
%{_datadir}/mimelnk/application/x-%{name}.desktop
%{_pixmapsdir}/%{name}.png
