Summary:     Converts .fig files (such as those from xfig) to other formats
Summary(de): Konvertiert .fig-Dateien (z.B. aus xfig) in andere Formate
Summary(fr): Convertit les fichiers .fig (comme ceux d'xfig) en d'autres formats."
Summary(pl): konwerter formatu plików .fig (jakie generuje xfig) do innych formatów
Summary(tr): fig dosyalarýný baþka biçimlere dönüþtürür
Name:        transfig
Version:     3.2.1
Release:     2
Copyright:   distributable
Group:       X11/Applications/Graphics
Group(pl):   X11/Aplikacje/Grafika
Source:      ftp://ftp.x.org/contrib/applications/drawing_tools/transfig/%{name}.%{version}.tar.gz
Patch0:      transfig-3.2.1-imake.patch
Buildroot:   /tmp/%{name}-%{version}-root

%description
TransFig is a set of tools for creating TeX documents with graphics
which are portable, in the sense that they can be printed in a wide
variety of environments.

%description -l de
TransFig ist ein Satz von Tools zum Erstellen von TeX-Dokumenten mit
Grafiken, die portabel sind, das heißt, sie können in einer großen Auswahl
von Umgebungen gedruckt werden.

%description -l fr
Transfig est un ensemble d'outils pour créer des documents textes avec
des graphiques portables, en ce sens qu'ils peuvent être imprimés dans
des nombreux environnements.

%description
Pakiet TransFig  jest zbiorem narzêdzi do tworzenia dokumentóe TeXowych z
grafik±, które bêd± przenoszalne w sensie, ¿e bêd± mozliwe do wydrukowania
na szrokiej palecie drukarek.

%description -l tr
TransFig, çizimler içeren TeX belgeleri üretebilmek için kullanýlan bir araç
kümesidir ve çeþitli ortamlarda çýktýsý alýnabilecek dosyalar yaratýr.

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
make DESTDIR=$RPM_BUILD_ROOT install install.man

# Dunno why these are not installed
for i in fig2ps2tex fig2ps2tex.sh pic2tpic
do
	install -c fig2dev/$i.script $RPM_BUILD_ROOT/usr/X11R6/bin/$i
done

gzip -9nf $RPM_BUILD_ROOT/usr/X11R6/man/man1/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644, root, root, 755)
%doc CHANGES NOTES README
/usr/X11R6/bin/*
/usr/X11R6/man/man1/*

%changelog
* Tue Dec  1 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [3.2.1-2]
- added gziping man pages,
- changed Buildroot to /tmp/%%{name}-%%{version}-root,
- added using %%{name} and %%{version} in Source,
- added using $RPM_OPT_FLAGS during compile,
- added full %attr description in %files,
- simplification in %install,
- added pl translation,
- added %attr and %defattr macros in %files (allow build package from
  non-root account).

* Tue Jul  7 1998 Jeff Johnson <jbj@redhat.com>
- update to 3.2.1.

* Sat Jun 27 1998 Jeff Johnson <jbj@redhat.com>
- add %clean.

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Thu Nov 13 1997 Otto Hammersmith <otto@redhat.com>
- fixed problem with Imakefile for fig2dev not including $(XLIB)
- build rooted.

* Fri Oct 24 1997 Otto Hammersmith <otto@redhat.com>
- recreated the glibc patch that is needed for an alpha build, missed it
  building on the intel.

* Tue Oct 21 1997 Otto Hammersmith <otto@redhat.com>
- updated version
- fixed source url

* Fri Jul 18 1997 Erik Troan <ewt@redhat.com>
- built against glibc
