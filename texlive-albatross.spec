%global tl_name albatross
%global tl_revision 79618
%global tl_bin_links albatross:%{_texmfdistdir}/scripts/albatross/albatross.sh

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
BuildSystem:	texlive
Requires:	texlive(albatross.bin)
Provides:	texlive(%{tl_name}) = %{tl_revision}
Provides:	texlive(%{tl_name}.bin) = %{tl_revision}
Provides:	texlive-%{tl_name}.bin = %{EVRD}

%description
This is a command line tool for finding fonts that contain a given
(Unicode) glyph. It relies on Fontconfig.

