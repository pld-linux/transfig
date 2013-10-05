Summary:	Converts .fig files (such as those from xfig) to other formats
Summary(de.UTF-8):	Konvertiert .fig-Dateien (z.B. aus xfig) in andere Formate
Summary(es.UTF-8):	Convierte archivos .fig (como los del xfig) para otros formatos
Summary(fr.UTF-8):	Convertit les fichiers .fig (comme ceux d'xfig) en d'autres formats
Summary(pl.UTF-8):	Konwerter plików w formacie .fig (jakie generuje xfig) do innych formatów
Summary(pt_BR.UTF-8):	Converte arquivos .fig (como os do xfig) para outros formatos
Summary(ru.UTF-8):	Конвертор файлов .fig (формат программы xfig) в другие форматы
Summary(tr.UTF-8):	fig dosyalarını başka biçimlere dönüştürür
Summary(uk.UTF-8):	Конвертор файлів .fig (формат програми xfig) в інші формати
Name:		transfig
Version:	3.2.5e
Release:	1
Epoch:		1
License:	distributable
Group:		X11/Applications/Graphics
#Source0Download: http://xfig.org/art15.html
# Source0:	http://xfig.org/software/xfig/%{version}/%{name}.%{version}.tar.gz
Source0:	http://downloads.sourceforge.net/mcj/%{name}.%{version}.tar.gz
# Source0-md5:	f547c67a93422c72039204f159f53ea9
Patch0:		%{name}-config.patch
Patch1:		%{name}-broken.patch
Patch2:		%{name}-3.2.5c-maxfontsize.patch
Patch3:		%{name}-format_string.patch
URL:		http://xfig.org/
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	rman
BuildRequires:	xorg-cf-files
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXpm-devel
BuildRequires:	xorg-util-gccmakedep
BuildRequires:	xorg-util-imake
Requires:	fonts-Type1-urw
Requires:	ghostscript
Conflicts:	netpbm-progs < 9.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
TransFig is a set of tools for creating TeX documents with graphics
which are portable, in the sense that they can be printed in a wide
variety of environments.

%description -l de.UTF-8
TransFig ist ein Satz von Tools zum Erstellen von TeX-Dokumenten mit
Grafiken, die portabel sind, das heißt, sie können in einer großen
Auswahl von Umgebungen gedruckt werden.

%description -l es.UTF-8
TransFig es un conjunto de herramientas para creación de documentos
TeX con gráficos que son portables, en el sentido de que pueden ser
impresos en una gran variedad de ambientes.

%description -l fr.UTF-8
Transfig est un ensemble d'outils pour créer des documents textes avec
des graphiques portables, en ce sens qu'ils peuvent être imprimés dans
des nombreux environnements.

%description -l pl.UTF-8
Pakiet TransFig jest zbiorem narzędzi do tworzenia dokumentów TeXowych
z grafiką, które będą przenośne w tym sensie, że będzie można je
wydrukować na szerokiej palecie drukarek.

%description -l pt_BR.UTF-8
TransFig é um conjunto de ferramentas para criação de documentos TeX
com gráficos que são portáveis, no sentido de que eles podem ser
impressos em uma grande variedade de ambientes.

%description -l ru.UTF-8
Утилита transfig создает makefile, транслирующий рисунки FIG
(созданные программой xfig) или PIC в заданный графический язык
системы LaTeX (например, PostScript(TM)). Transfig используется для
создания документов TeX, являющихся портабельными (то есть, они могут
быть напечатаны на различных платформах).

%description -l tr.UTF-8
TransFig, çizimler içeren TeX belgeleri üretebilmek için kullanılan
bir araç kümesidir ve çeşitli ortamlarda çıktısı alınabilecek dosyalar
yaratır.

%description -l uk.UTF-8
Утиліта transfig створює makefile, який транслює малюнки FIG (створені
програмою xfig) чи PIC у задану графічну мову системи LaTeX
(наприклад, PostScript(TM)). Transfig використовується для створення
TeX документів, які є портабельними (тобто, можуть бути надруковані на
різноманітних платформах).

%prep
%setup -q -n %{name}.%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
xmkmf -a

%{__make} \
%ifarch alpha
	EXTRA_DEFINES="-Dcfree=free" \
%endif
	CC="%{__cc}" \
	CDEBUGFLAGS="%{rpmcflags}" \
	DOCDIR=%{_docdir} \
	LOCAL_LDFLAGS="%{rpmldflags}" \
	BINDIR=%{_bindir} \
	MANPATH=%{_mandir} \
	XFIGLIBDIR=%{_datadir}/xfig \
	FIG2DEV_LIBDIR=%{_datadir}/fig2dev

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install install.man \
	DESTDIR=$RPM_BUILD_ROOT \
	BINDIR=%{_bindir} \
	DOCDIR=%{_docdir} \
	MANPATH=%{_mandir} \
	XFIGLIBDIR=%{_datadir}/xfig \
	FIG2DEV_LIBDIR=%{_datadir}/fig2dev

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES NOTES README
%attr(755,root,root) %{_bindir}/fig2dev
%attr(755,root,root) %{_bindir}/fig2ps2tex
%attr(755,root,root) %{_bindir}/fig2ps2tex.sh
%attr(755,root,root) %{_bindir}/pic2tpic
%attr(755,root,root) %{_bindir}/transfig
%dir %{_datadir}/fig2dev
# other latin-2 files are symlinks to cs_CZ.ps
%lang(cs,hr,hu,pl,ro,sk,sl) %{_datadir}/fig2dev/cs*.ps
%lang(hr) %{_datadir}/fig2dev/hr*.ps
%lang(hu) %{_datadir}/fig2dev/hu*.ps
%lang(ja) %{_datadir}/fig2dev/ja*.ps
%lang(ko) %{_datadir}/fig2dev/ko*.ps
%lang(pl) %{_datadir}/fig2dev/pl*.ps
%lang(ro) %{_datadir}/fig2dev/ro*.ps
%lang(sk) %{_datadir}/fig2dev/sk*.ps
%lang(sl) %{_datadir}/fig2dev/sl*.ps
%dir %{_datadir}/xfig
%{_datadir}/xfig/*.bmp
%{_mandir}/man1/fig2dev.1x*
%{_mandir}/man1/fig2ps2tex.1x*
%{_mandir}/man1/pic2tpic.1x*
%{_mandir}/man1/transfig.1x*
