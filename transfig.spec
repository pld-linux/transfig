Summary:	Converts .fig files (such as those from xfig) to other formats
Summary(de):	Konvertiert .fig-Dateien (z.B. aus xfig) in andere Formate
Summary(fr):	Convertit les fichiers .fig (comme ceux d'xfig) en d'autres formats
Summary(pl):	konwerter formatu plik�w .fig (jakie generuje xfig) do innych format�w
Summary(tr):	fig dosyalar�n� ba�ka bi�imlere d�n��t�r�r
Name:		transfig
Version:	3.2.3c
Release:	2
License:	Distributable
Group:		X11/Applications/Graphics
Group(de):	X11/Applikationen/Grafik
Group(pl):	X11/Aplikacje/Grafika
Source0:	http://www.xfig.org/xfigdist/%{name}.%{version}.tar.gz
Patch0:		%{name}-i18n.patch
Patch1:		%{name}-config.patch
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
Grafiken, die portabel sind, das hei�t, sie k�nnen in einer gro�en
Auswahl von Umgebungen gedruckt werden.

%description -l fr
Transfig est un ensemble d'outils pour cr�er des documents textes avec
des graphiques portables, en ce sens qu'ils peuvent �tre imprim�s dans
des nombreux environnements.

%description -l pl
Pakiet TransFig jest zbiorem narz�dzi do tworzenia dokument�w TeXowych
z grafik�, kt�re b�d� przenoszalne w sensie, �e b�d� mozliwe do
wydrukowania na szrokiej palecie drukarek.

%description -l tr
TransFig, �izimler i�eren TeX belgeleri �retebilmek i�in kullan�lan
bir ara� k�mesidir ve �e�itli ortamlarda ��kt�s� al�nabilecek dosyalar
yarat�r.

%prep
%setup -q -n %{name}.%{version}
%patch0 -p1
%patch1 -p1

%build
xmkmf -a

%{__make} \
%ifarch alpha
	EXTRA_DEFINES="-Dcfree=free" \
%endif
	CDEBUGFLAGS="%{!?debug:$RPM_OPT_FLAGS}%{?debug:-O -g}" \
	CXXDEBUGFLAGS="%{!?debug:$RPM_OPT_FLAGS}%{?debug:-O -g}" \
	LOCAL_LDFLAGS=%{!?debug:-s}

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
%{_mandir}/man1/*
