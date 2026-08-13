%global tl_name hfbright
%global tl_revision 29349

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	The hfbright fonts
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/ps-type1/hfbright
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hfbright.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hfbright.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{version}

%description
These are Adobe Type 1 versions of the OT1-encoded and maths parts of
the Computer Modern Bright fonts.


%install -a
mkdir -p %{buildroot}%{_texmf_updmap_d}
cat > %{buildroot}%{_texmf_updmap_d}/%{tl_name} <<'TL_DROPIN_EOF'
# from hfbright:
MixedMap hfbright.map
TL_DROPIN_EOF
