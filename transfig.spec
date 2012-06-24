Summary:	Converts .fig files (such as those from xfig) to other formats
Summary(de):	Konvertiert .fig-Dateien (z.B. aus xfig) in andere Formate
Summary(fr):	Convertit les fichiers .fig (comme ceux d'xfig) en d'autres formats."
Summary(pl):	konwerter formatu plik�w .fig (jakie generuje xfig) do innych format�w
Summary(tr):	fig dosyalar�n� ba�ka bi�imlere d�n��t�r�r
Name:		transfig
Version:	3.2.1
Release:	4
Copyright:	distributable
Group:		X11/Applications/Graphics
Group(pl):	X11/Aplikacje/Grafika
Source:		ftp://ftp.x.org/contrib/applications/drawing_tools/transfig/%{name}.%{version}.tar.gz
Patch0:		transfig-imake.patch
Buildroot:	/tmp/%{name}-%{version}-root

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
TransFig is a set of tools for creating TeX documents with graphics
which are portable, in the sense that they can be printed in a wide
variety of environments.

%description -l de
TransFig ist ein Satz von Tools zum Erstellen von TeX-Dokumenten mit
Grafiken, die portabel sind, das hei�t, sie k�nnen in einer gro�en Auswahl
von Umgebungen gedruckt werden.

%description -l fr
Transfig est un ensemble d'outils pour cr�er des documents textes avec
des graphiques portables, en ce sens qu'ils peuvent �tre imprim�s dans
des nombreux environnements.

%description -l pl
Pakiet TransFig jest zbiorem narz�dzi do tworzenia dokument�w TeXowych z
grafik�, kt�re b�d� przenoszalne w sensie, �e b�d� mozliwe do wydrukowania
na szrokiej palecie drukarek.

%description -l tr
TransFig, �izimler i�eren TeX belgeleri �retebilmek i�in kullan�lan bir ara�
k�mesidir ve �e�itli ortamlarda ��kt�s� al�nabilecek dosyalar yarat�r.

%prep
%setup -q -n %{name}.%{version}

%build
xmkmf
make Makefiles

%ifarch alpha
make EXTRA_DEFINES="-Dcfree=free" \
	CDEBUGFLAGS="$RPM_OPT_FLAGS" CXXDEBUGFLAGS="$RPM_OPT_FLAGS"
%else
make	CDEBUGFLAGS="$RPM_OPT_FLAGS" CXXDEBUGFLAGS="$RPM_OPT_FLAGS"
%endif

%install
rm -rf $RPM_BUILD_ROOT
make install install.man DESTDIR=$RPM_BUILD_ROOT

# Dunno why these are not installed
for i in fig2ps2tex fig2ps2tex.sh pic2tpic
do
	install -c fig2dev/$i.script $RPM_BUILD_ROOT%{_bindir}/$i
done

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/* \
	CHANGES NOTES README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
