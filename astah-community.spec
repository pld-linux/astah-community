# TODO
# - package API to java-astah
# - repackage to have default opener xdg-open instead of firefox?
#
# Conditional build:
%bcond_without	javadoc		# don't build javadoc

%define		codename	community
%define		ver		%(echo %{version} | tr . _)
%include	/usr/lib/rpm/macros.java
Summary:	A New Java/UML Object-Oriented Design Tool
Summary(pl.UTF-8):	Narzędzie wspomagające projektowanie oprogramowania w UML
Name:		astah
Version:	6.2.1
Release:	0.6
# non-distributable, can be used for free upon restrictions and registration
# http://astah.change-vision.com/en/product/astah-eula.html
License:	Astah* EULA
Group:		Applications/Engineering
# Source0Download:	https://members.change-vision.com/members/files/astah_community/%{ver}/astah-community-%{ver}.zip
Source0:	http://jude-users.com/edujjude/%{name}-%{codename}-%{ver}.zip
# NoSource0-md5:	7323ea7b751a6bd39f0dd906cdf58ca4
Source1:	%{name}.desktop
Source2:	%{name}.xml
Source3:	%{name}-icon.png
NoSource:	0
URL:		http://astah.change-vision.com/en/product/astah-community.html
BuildRequires:	rpm-javaprov
BuildRequires:	rpmbuild(macros) >= 1.311
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	shared-mime-info
BuildRequires:	unzip
Requires:	jre-X11
Obsoletes:	jude
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Astah is a new tool which supports your object-oriented software
designing in JavaTM and UML1.4 (Unified Modeling Language).

This package contains Community version, which is freely usable upon
some restrictions after registration on vendor site.

%description -l pl.UTF-8
Astah jest nowym narzędziem wspomagającym zorientowane obiektowo
projektowanie oprogramowania w JavaTM i UML1.4 (Unified Modeling
Language).

Ten pakiet zawiera wersję społecznościową, której można używać bez
opłat pod pewnymi ograniczenami, po uprzedniej rejestracji na stronie
producenta.

%package javadoc
Summary:	Online manual for astah
Summary(pl.UTF-8):	Dokumentacja online do astah
Group:		Documentation
Requires:	jpackage-utils

%description javadoc
Documentation for astah.

%description javadoc -l pl.UTF-8
Dokumentacja do astah.

%description javadoc -l fr.UTF-8
Javadoc pour astah.

%prep
%setup -q -n %{name}_%{codename}

cat <<'EOF' > %{name}.sh
#!/bin/sh
exec java -Xms16m -Xmx512m -Xss2m -jar %{_datadir}/%{name}/astah-%{codename}.jar ${1:+"$@"}
EOF

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name}}

install -p %{name}.sh $RPM_BUILD_ROOT%{_bindir}/%{name}
cp -a astah-%{codename}.jar $RPM_BUILD_ROOT%{_datadir}/%{name}

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a *.asta $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_datadir}/mime/packages,%{_pixmapsdir}}
cp -a %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
cp -a %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/mime/packages/astah.xml
cp -a %{SOURCE3} $RPM_BUILD_ROOT%{_pixmapsdir}/%{name}.png

# javadoc
%if %{with javadoc}
install -d $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -a api/en/doc/javadoc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_mime_database
%update_desktop_database_post

%postun
%update_mime_database
%update_desktop_database_postun

%post javadoc
ln -nfs %{name}-%{version} %{_javadocdir}/%{name}

%files
%defattr(644,root,root,755)
%doc README-e.txt ReleaseNote-e.html
%doc %lang(ja) README.txt ReleaseNote.html ProductInformation.txt
%attr(755,root,root) %{_bindir}/%{name}
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/%{name}-%{codename}.jar
%{_desktopdir}/%{name}.desktop
%{_datadir}/mime/packages/astah.xml
%{_pixmapsdir}/%{name}.png

%dir %{_examplesdir}/%{name}-%{version}
%{_examplesdir}/%{name}-%{version}/Welcome.asta
%{_examplesdir}/%{name}-%{version}/Sample.asta
%lang(ja) %{_examplesdir}/%{name}-%{version}/Welcome_ja.asta

%if %{with javadoc}
%files javadoc
%defattr(644,root,root,755)
%{_javadocdir}/%{name}-%{version}
%ghost %{_javadocdir}/%{name}
%endif
