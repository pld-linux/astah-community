Summary:	A New Java/UML Object-Oriented Design Tool
Summary(pl):	¦rodowsko obiektowo zorientowanego projektowania narzêdzi UML
Name:		jude
Version:	1.3
Release:	1
License:	Freeware
Group:		Applications/Engineering
Source0:	%{name}_take%(echo %{version} |tr . _).zip
Source1:	%{name}.desktop
URL:		http://objectclub.esm.co.jp/Jude/
Requires:	jre
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Jude is a new tool which supports your object-oriented software
designing in JavaTM and UML1.4(Unified Modeling Language).

%description -l pl
Jude jest nowym narzêdziem obs³uguj±cym obiektowo-zorientowane
przygotowywanie oprogramowania w JavaTM i UML1.4(zunifikowany jêzyk
modelowania).

%prep
%setup -q -n jude_take -n jude_take -n jude_take -n jude_take

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name},%{_desktopdir}}

cat <<EOF > $RPM_BUILD_ROOT%{_bindir}/%{name}
#!/bin/sh
java -Xms16m -Xmx256m -Xss1m -jar %{_datadir}/%{name}/jude-take.jar \$*
EOF

install jude-take.jar JudeDefaultModel.jude $RPM_BUILD_ROOT%{_datadir}/%{name}
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README* Release_Note*
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_desktopdir}/%{name}.desktop
