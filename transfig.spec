# NOTE: since 3.2.6 official package name is "fig2dev" and transfig considered obsolete.
# TODO: Fork fig2dev.spec from transfig.spec when they stop shipping transfig with fig2dev
#       (and keep the last version of transfig here).
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
Version:	3.2.6a
Release:	1
Epoch:		1
License:	distributable
Group:		X11/Applications/Graphics
Source0:	http://downloads.sourceforge.net/mcj/fig2dev-%{version}.tar.xz
# Source0-md5:	f795a492cd9fa6d9abe0e11e581946f9
Patch0:		%{name}-broken.patch
URL:		http://mcj.sourceforge.net/
BuildRequires:	libpng-devel
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-lib-libXpm-devel
BuildRequires:	xz
Requires:	fig2dev = %{version}-%{release}
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

%package -n fig2dev
Summary:	Tools for creating portable TeX documents with graphics
Summary(pl.UTF-8):	Narzędzia do tworzenia przenośnych dokumentów TeXa z grafiką
Epoch:		0
Group:		Applications/Graphics
Requires:	fonts-Type1-urw
Requires:	ghostscript

%description -n fig2dev
Fig2dev is a set of tools for creating TeX documents with graphics
which are portable, in the sense that they can be printed in a wide
variety of environments.

%description -n fig2dev -l pl.UTF-8
Fig2dev to zbiór narzędzi do tworzenia dokumentów TeXa z grafiką,
które są przenośne - w takim sensie, że mogą być drukowane w wielu
różnych środowiskach.

%prep
%setup -q -n fig2dev-%{version}
%patch0 -p1

%build
%configure \
	--enable-transfig

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/transfig
%{_mandir}/man1/transfig.1*

%files -n fig2dev
%defattr(644,root,root,755)
%doc CHANGES NOTES README
%attr(755,root,root) %{_bindir}/fig2dev
%attr(755,root,root) %{_bindir}/fig2ps2tex
%attr(755,root,root) %{_bindir}/pic2tpic
%dir %{_datadir}/fig2dev
%{_datadir}/fig2dev/rgb.txt
%{_datadir}/fig2dev/bitmaps
%dir %{_datadir}/fig2dev/i18n
# other latin-2 files are symlinks to cs_CZ.ps
%lang(cs,hr,hu,pl,ro,sk,sl) %{_datadir}/fig2dev/i18n/cs_CZ.ps
%lang(hr) %{_datadir}/fig2dev/i18n/hr_HR.ps
%lang(hu) %{_datadir}/fig2dev/i18n/hu_HU.ps
%lang(ja) %{_datadir}/fig2dev/i18n/japanese.ps
%lang(ja) %{_datadir}/fig2dev/i18n/ja.ps
%lang(ja) %{_datadir}/fig2dev/i18n/ja_JP*.ps
%lang(ko) %{_datadir}/fig2dev/i18n/korean.ps
%lang(ko) %{_datadir}/fig2dev/i18n/ko.ps
%lang(ko) %{_datadir}/fig2dev/i18n/ko_KR*.ps
%lang(pl) %{_datadir}/fig2dev/i18n/pl_PL.ps
%lang(ro) %{_datadir}/fig2dev/i18n/ro_RO.ps
%lang(ru) %{_datadir}/fig2dev/i18n/ru_RU*.ps
%lang(sk) %{_datadir}/fig2dev/i18n/sk_SK.ps
%lang(sl) %{_datadir}/fig2dev/i18n/sl_SI.ps
%{_mandir}/man1/fig2dev.1*
%{_mandir}/man1/fig2ps2tex.1*
%{_mandir}/man1/pic2tpic.1*
