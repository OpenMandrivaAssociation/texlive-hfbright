# revision 29349
# category Package
# catalog-ctan /fonts/ps-type1/hfbright
# catalog-date 2012-07-13 13:47:30 +0200
# catalog-license lppl
# catalog-version undef
Name:		texlive-hfbright
Version:	20120713
Release:	5
Summary:	The hfbright fonts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/ps-type1/hfbright
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hfbright.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hfbright.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
These are Adobe Type 1 versions of the OT1-encoded and maths
parts of the Computer Modern Bright fonts.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/afm/public/hfbright/hfbr10.afm
%{_texmfdistdir}/fonts/afm/public/hfbright/hfbr17.afm
%{_texmfdistdir}/fonts/afm/public/hfbright/hfbr8.afm
%{_texmfdistdir}/fonts/afm/public/hfbright/hfbr9.afm
%{_texmfdistdir}/fonts/afm/public/hfbright/hfbras10.afm
%{_texmfdistdir}/fonts/afm/public/hfbright/hfbras8.afm
%{_texmfdistdir}/fonts/afm/public/hfbright/hfbras9.afm
%{_texmfdistdir}/fonts/afm/public/hfbright/hfbrbs10.afm
%{_texmfdistdir}/fonts/afm/public/hfbright/hfbrbs8.afm
%{_texmfdistdir}/fonts/afm/public/hfbright/hfbrbs9.afm
%{_texmfdistdir}/fonts/afm/public/hfbright/hfbrbx10.afm
%{_texmfdistdir}/fonts/afm/public/hfbright/hfbrmb10.afm
%{_texmfdistdir}/fonts/afm/public/hfbright/hfbrmi10.afm
%{_texmfdistdir}/fonts/afm/public/hfbright/hfbrmi8.afm
%{_texmfdistdir}/fonts/afm/public/hfbright/hfbrmi9.afm
%{_texmfdistdir}/fonts/afm/public/hfbright/hfbrsl10.afm
%{_texmfdistdir}/fonts/afm/public/hfbright/hfbrsl17.afm
%{_texmfdistdir}/fonts/afm/public/hfbright/hfbrsl8.afm
%{_texmfdistdir}/fonts/afm/public/hfbright/hfbrsl9.afm
%{_texmfdistdir}/fonts/afm/public/hfbright/hfbrsy10.afm
%{_texmfdistdir}/fonts/afm/public/hfbright/hfbrsy8.afm
%{_texmfdistdir}/fonts/afm/public/hfbright/hfbrsy9.afm
%{_texmfdistdir}/fonts/afm/public/hfbright/hfsltl10.afm
%{_texmfdistdir}/fonts/afm/public/hfbright/hftl10.afm
%{_texmfdistdir}/fonts/enc/dvips/hfbright/hfmital.enc
%{_texmfdistdir}/fonts/enc/dvips/hfbright/hfmsa.enc
%{_texmfdistdir}/fonts/enc/dvips/hfbright/hfmsb.enc
%{_texmfdistdir}/fonts/enc/dvips/hfbright/hfmsym.enc
%{_texmfdistdir}/fonts/enc/dvips/hfbright/hfot1.enc
%{_texmfdistdir}/fonts/map/dvips/hfbright/hfbright.map
%{_texmfdistdir}/fonts/type1/public/hfbright/hfbr10.pfb
%{_texmfdistdir}/fonts/type1/public/hfbright/hfbr17.pfb
%{_texmfdistdir}/fonts/type1/public/hfbright/hfbr8.pfb
%{_texmfdistdir}/fonts/type1/public/hfbright/hfbr9.pfb
%{_texmfdistdir}/fonts/type1/public/hfbright/hfbras10.pfb
%{_texmfdistdir}/fonts/type1/public/hfbright/hfbras8.pfb
%{_texmfdistdir}/fonts/type1/public/hfbright/hfbras9.pfb
%{_texmfdistdir}/fonts/type1/public/hfbright/hfbrbs10.pfb
%{_texmfdistdir}/fonts/type1/public/hfbright/hfbrbs8.pfb
%{_texmfdistdir}/fonts/type1/public/hfbright/hfbrbs9.pfb
%{_texmfdistdir}/fonts/type1/public/hfbright/hfbrbx10.pfb
%{_texmfdistdir}/fonts/type1/public/hfbright/hfbrmb10.pfb
%{_texmfdistdir}/fonts/type1/public/hfbright/hfbrmi10.pfb
%{_texmfdistdir}/fonts/type1/public/hfbright/hfbrmi8.pfb
%{_texmfdistdir}/fonts/type1/public/hfbright/hfbrmi9.pfb
%{_texmfdistdir}/fonts/type1/public/hfbright/hfbrsl10.pfb
%{_texmfdistdir}/fonts/type1/public/hfbright/hfbrsl17.pfb
%{_texmfdistdir}/fonts/type1/public/hfbright/hfbrsl8.pfb
%{_texmfdistdir}/fonts/type1/public/hfbright/hfbrsl9.pfb
%{_texmfdistdir}/fonts/type1/public/hfbright/hfbrsy10.pfb
%{_texmfdistdir}/fonts/type1/public/hfbright/hfbrsy8.pfb
%{_texmfdistdir}/fonts/type1/public/hfbright/hfbrsy9.pfb
%{_texmfdistdir}/fonts/type1/public/hfbright/hfsltl10.pfb
%{_texmfdistdir}/fonts/type1/public/hfbright/hftl10.pfb
%doc %{_texmfdistdir}/doc/fonts/hfbright/README
%doc %{_texmfdistdir}/doc/fonts/hfbright/config.hfbright
%doc %{_texmfdistdir}/doc/fonts/hfbright/generate.sh
%doc %{_texmfdistdir}/doc/fonts/hfbright/install.sh
%doc %{_texmfdistdir}/doc/fonts/hfbright/simplify-rename.pe

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts doc %{buildroot}%{_texmfdistdir}
