%global tl_name albatross
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.5.1
Release:	%{tl_revision}.1
Summary:	Find fonts that contain a given glyph
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/support/albatross
License:	bsd3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/albatross.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/albatross.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/albatross.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Requires:	texlive(albatross.bin)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This is a command line tool for finding fonts that contain a given
(Unicode) glyph. It relies on Fontconfig.

%prep
%setup -q -c -a1 -a2
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/texmf-dist
%dir %{_datadir}/texmf-dist/texmf-dist/doc
%dir %{_datadir}/texmf-dist/texmf-dist/scripts
%dir %{_datadir}/texmf-dist/texmf-dist/source
%dir %{_datadir}/texmf-dist/texmf-dist/doc/man
%dir %{_datadir}/texmf-dist/texmf-dist/doc/support
%dir %{_datadir}/texmf-dist/texmf-dist/scripts/albatross
%dir %{_datadir}/texmf-dist/texmf-dist/source/support
%dir %{_datadir}/texmf-dist/texmf-dist/doc/man/man1
%dir %{_datadir}/texmf-dist/texmf-dist/doc/support/albatross
%dir %{_datadir}/texmf-dist/texmf-dist/source/support/albatross
%doc %{_datadir}/texmf-dist/texmf-dist/doc/man/man1/albatross.1
%doc %{_datadir}/texmf-dist/texmf-dist/doc/man/man1/albatross.man1.pdf
%doc %{_datadir}/texmf-dist/texmf-dist/doc/support/albatross/README.md
%doc %{_datadir}/texmf-dist/texmf-dist/doc/support/albatross/albatross-manual.pdf
%doc %{_datadir}/texmf-dist/texmf-dist/doc/support/albatross/albatross-manual.tex
%doc %{_datadir}/texmf-dist/texmf-dist/doc/support/albatross/version.tex
%{_datadir}/texmf-dist/texmf-dist/scripts/albatross/albatross.jar
%{_datadir}/texmf-dist/texmf-dist/scripts/albatross/albatross.sh
%doc %{_datadir}/texmf-dist/texmf-dist/source/support/albatross/albatross-0.5.1-src.zip
