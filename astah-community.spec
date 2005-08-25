%define		codename	community
Summary:	A New Java/UML Object-Oriented Design Tool
Summary(pl):	�rodowisko obiektowo zorientowanego projektowania narz�dzi UML
Name:		jude
Version:	1.6.2
Release:	1
License:	Freeware
Group:		Applications/Engineering
Source0:	http://www.esm.co.jp/jude/jude-%{codename}-%(echo %{version} | tr . _).zip
Source1:	%{name}.desktop
Source2:	%{name}-icon.png
URL:		http://objectclub.esm.co.jp/Jude/
Requires:	jre
BuildArch:	noarch
NoSource:	0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Jude is a new tool which supports your object-oriented software
designing in JavaTM and UML1.4 (Unified Modeling Language).

%description -l pl
Jude jest nowym narz�dziem obs�uguj�cym obiektowo-zorientowane
przygotowywanie oprogramowania w JavaTM i UML1.4 (zunifikowany 
j�zyk modelowania).

%prep
%setup -q -n jude_%{codename}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name},%{_desktopdir},%{_pixmapsdir}}

cat <<EOF > $RPM_BUILD_ROOT%{_bindir}/%{name}
#!/bin/sh
java -Xms16m -Xmx256m -Xss1m -jar %{_datadir}/%{name}/jude-%{codename}.jar \$*
EOF

install jude-%{codename}.jar JudeDefaultModel.jude $RPM_BUILD_ROOT%{_datadir}/%{name}
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}/%{name}.png

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README* ReleaseNote*
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.png
