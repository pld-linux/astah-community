%define		codename	community
Summary:	A New Java/UML Object-Oriented Design Tool
Summary(pl):	¦rodowisko obiektowo zorientowanego projektowania narzêdzi UML
Name:		jude
Version:	1.4
Release:	2
License:	Freeware
Group:		Applications/Engineering
Source0:	http://objectclub.esm.co.jp/Jude/com%(echo %{version} |tr -d .)/%{name}-%{codename}-%(echo %{version} |tr . _).zip
Source1:	%{name}.desktop
URL:		http://objectclub.esm.co.jp/Jude/
Requires:	jre
BuildArch:	noarch
NoSource:	0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Jude is a new tool which supports your object-oriented software
designing in JavaTM and UML1.4 (Unified Modeling Language).

%description -l pl
Jude jest nowym narzêdziem obs³uguj±cym obiektowo-zorientowane
przygotowywanie oprogramowania w JavaTM i UML1.4 (zunifikowany 
jêzyk modelowania).

%prep
%setup -q -n jude_%{codename}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name},%{_desktopdir}}

cat <<EOF > $RPM_BUILD_ROOT%{_bindir}/%{name}
#!/bin/sh
java -Xms16m -Xmx256m -Xss1m -jar %{_datadir}/%{name}/jude-%{codename}.jar \$*
EOF

install jude-%{codename}.jar JudeDefaultModel.jude $RPM_BUILD_ROOT%{_datadir}/%{name}
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README* ReleaseNote*
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_desktopdir}/%{name}.desktop
