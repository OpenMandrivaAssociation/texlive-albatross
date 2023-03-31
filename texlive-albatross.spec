Name:		texlive-albatross
Version:	61175
Release:	2
Summary:	Find fonts that contain a given glyph
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/albatross
License:	bsd3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/albatross.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/albatross.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/albatross.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This is a command line tool for finding fonts that contain a
given (Unicode) glyph. It relies on Fontconfig.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_datadir}
cp -a texmf-dist %{buildroot}%{_datadir}

%files
%doc %{_texmfdistdir}/source/support/albatross
%{_texmfdistdir}/scripts/albatross
%doc %{_texmfdistdir}/doc/support/albatross
%doc %{_texmfdistdir}/doc/man/man1/*

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
