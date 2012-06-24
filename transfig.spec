Summary:	Converts .fig files (such as those from xfig) to other formats
Summary(de):	Konvertiert .fig-Dateien (z.B. aus xfig) in andere Formate
Summary(es):	Convierte archivos .fig (como los del xfig) para otros formatos
Summary(fr):	Convertit les fichiers .fig (comme ceux d'xfig) en d'autres formats
Summary(pl):	Konwerter plik�w w formacie .fig (jakie generuje xfig) do innych format�w
Summary(pt_BR):	Converte arquivos .fig (como os do xfig) para outros formatos
Summary(ru):	��������� ������ .fig (������ ��������� xfig) � ������ �������
Summary(tr):	fig dosyalar�n� ba�ka bi�imlere d�n��t�r�r
Summary(uk):	��������� ���̦� .fig (������ �������� xfig) � ��ۦ �������
Name:		transfig
Version:	3.2.4
Release:	2
Epoch:		1
License:	distributable
Group:		X11/Applications/Graphics
Source0:	http://www.xfig.org/xfigdist/%{name}.%{version}.tar.gz
# Source0-md5:	742de0f7a3cae74d247bbd0c70dd9dd7
Patch0:		%{name}-config.patch
Patch1:		%{name}-broken.patch
Patch2:		%{name}-gcc33.patch
Patch3:		%{name}-strerror.patch
# seems outdated (some i18n support has been introduced)
#Patch1:		%{name}-anti_latin1.patch
BuildRequires:	XFree86-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
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

%description -l es
TransFig es un conjunto de herramientas para creaci�n de documentos
TeX con gr�ficos que son portables, en el sentido de que pueden ser
impresos en una gran variedad de ambientes.

%description -l fr
Transfig est un ensemble d'outils pour cr�er des documents textes avec
des graphiques portables, en ce sens qu'ils peuvent �tre imprim�s dans
des nombreux environnements.

%description -l pl
Pakiet TransFig jest zbiorem narz�dzi do tworzenia dokument�w TeXowych
z grafik�, kt�re b�d� przeno�ne w sensie, �e b�dzie mo�na je
wydrukowa� na szerokiej palecie drukarek.

%description -l pt_BR
TransFig � um conjunto de ferramentas para cria��o de documentos TeX
com gr�ficos que s�o port�veis, no sentido de que eles podem ser
impressos em uma grande variedade de ambientes.

%description -l ru
������� transfig ������� makefile, ������������� ������� FIG
(��������� ���������� xfig) ��� PIC � �������� ����������� ����
������� LaTeX (��������, PostScript(TM)). Transfig ������������ ���
�������� ���������� TeX, ���������� ������������� (�� ����, ��� �����
���� ���������� �� ��������� ����������).

%description -l tr
TransFig, �izimler i�eren TeX belgeleri �retebilmek i�in kullan�lan
bir ara� k�mesidir ve �e�itli ortamlarda ��kt�s� al�nabilecek dosyalar
yarat�r.

%description -l uk
���̦�� transfig ������� makefile, ���� �������� ������� FIG (������Φ
��������� xfig) �� PIC � ������ ���Ʀ��� ���� ������� LaTeX
(���������, PostScript(TM)). Transfig ����������դ���� ��� ���������
TeX �������Ԧ�, �˦ � ������������� (�����, ������ ���� ���������Φ ��
Ҧ�����Φ���� ����������).

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
	CDEBUGFLAGS="%{rpmcflags}" \
	CXXDEBUGFLAGS="%{rpmcflags}" \
	LOCAL_LDFLAGS="%{rpmldflags}" \
	BINDIR=%{_bindir} \
	MANPATH=%{_mandir}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install install.man \
	DESTDIR=$RPM_BUILD_ROOT \
	BINDIR=%{_bindir} \
	MANPATH=%{_mandir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES NOTES README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/xfig
%dir %{_datadir}/fig2dev
# other latin-2 files are symlinks to cs_CZ.ps
%lang(cs,hr,hu,pl,ro,sk,sl) %{_datadir}/fig2dev/cs*.ps
%lang(hr) %{_datadir}/fig2dev/hr*.ps
%lang(ja) %{_datadir}/fig2dev/ja*.ps
%lang(ko) %{_datadir}/fig2dev/ko*.ps
%lang(pl) %{_datadir}/fig2dev/pl*.ps
%lang(ro) %{_datadir}/fig2dev/ro*.ps
%lang(sk) %{_datadir}/fig2dev/sk*.ps
%lang(sl) %{_datadir}/fig2dev/sl*.ps
%{_mandir}/man1/*
