Summary:	Converts .fig files (such as those from xfig) to other formats
Summary(de):	Konvertiert .fig-Dateien (z.B. aus xfig) in andere Formate
Summary(fr):	Convertit les fichiers .fig (comme ceux d'xfig) en d'autres formats
Summary(pl):	konwerter formatu plików .fig (jakie generuje xfig) do innych formatów
Summary(tr):	fig dosyalarýný baþka biçimlere dönüþtürür
Name:		transfig
Version:	3.2.3d
Release:	1
Epoch:		1
License:	Distributable
Group:		X11/Applications/Graphics
Group(de):	X11/Applikationen/Grafik
Group(pl):	X11/Aplikacje/Grafika
Source0:	http://www.xfig.org/xfigdist/%{name}.%{version}.tar.gz
Patch0:		%{name}-config.patch
Patch1:		%{name}-anti_latin1.patch
BuildRequires:	XFree86-devel
BuildRequires:	libjpeg-devel
BuildRequires:	gdbm-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
TransFig is a set of tools for creating TeX documents with graphics
which are portable, in the sense that they can be printed in a wide
variety of environments.

%description -l de
TransFig ist ein Satz von Tools zum Erstellen von TeX-Dokumenten mit
Grafiken, die portabel sind, das heißt, sie können in einer großen
Auswahl von Umgebungen gedruckt werden.

%description -l fr
Transfig est un ensemble d'outils pour créer des documents textes avec
des graphiques portables, en ce sens qu'ils peuvent être imprimés dans
des nombreux environnements.

%description -l pl
Pakiet TransFig jest zbiorem narzêdzi do tworzenia dokumentów TeXowych
z grafik±, które bêd± przeno¶ne w sensie, ¿e bêdzie mo¿na je
wydrukowaæ na szerokiej palecie drukarek.

%description -l tr
TransFig, çizimler içeren TeX belgeleri üretebilmek için kullanýlan
bir araç kümesidir ve çeþitli ortamlarda çýktýsý alýnabilecek dosyalar
yaratýr.

%prep
%setup -q -n %{name}.%{version}
chmod u+w -R *
%patch0 -p1
%patch1 -p1

%build
xmkmf -a

%{__make} \
%ifarch alpha
	EXTRA_DEFINES="-Dcfree=free" \
%endif
	CDEBUGFLAGS="%{rpmcflags}" \
	CXXDEBUGFLAGS="%{rpmcflags}" \
	LOCAL_LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install install.man \
	DESTDIR=$RPM_BUILD_ROOT

gzip -9nf CHANGES NOTES README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_datadir}/xfig
%dir %{_datadir}/fig2dev
%lang(cz) %{_datadir}/fig2dev/cz*.ps
%lang(ja) %{_datadir}/fig2dev/ja*.ps
%lang(ko) %{_datadir}/fig2dev/ko*.ps
%{_mandir}/man1/*
