# revision 33014
# category Collection
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-collection-pstricks
Epoch:		1
Version:	20140318
Release:	1
Summary:	PSTricks
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/collection-pstricks.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires:	texlive-collection-basic
Requires:	texlive-collection-genericrecommended
Requires:	texlive-auto-pst-pdf
Requires:	texlive-bclogo
Requires:	texlive-makeplot
Requires:	texlive-pdftricks
Requires:	texlive-pdftricks2
Requires:	texlive-pedigree-perl
Requires:	texlive-psbao
Requires:	texlive-pst-2dplot
Requires:	texlive-pst-3d
Requires:	texlive-pst-3dplot
Requires:	texlive-pst-abspos
Requires:	texlive-pst-am
Requires:	texlive-pst-asr
Requires:	texlive-pst-bar
Requires:	texlive-pst-barcode
Requires:	texlive-pst-bezier
Requires:	texlive-pst-blur
Requires:	texlive-pst-bspline
Requires:	texlive-pst-calendar
Requires:	texlive-pst-circ
Requires:	texlive-pst-coil
Requires:	texlive-pst-cox
Requires:	texlive-pst-dbicons
Requires:	texlive-pst-diffraction
Requires:	texlive-pst-electricfield
Requires:	texlive-pst-eps
Requires:	texlive-pst-eucl
Requires:	texlive-pst-exa
Requires:	texlive-pst-fill
Requires:	texlive-pst-fit
Requires:	texlive-pst-fr3d
Requires:	texlive-pst-fractal
Requires:	texlive-pst-fun
Requires:	texlive-pst-func
Requires:	texlive-pst-gantt
Requires:	texlive-pst-geo
Requires:	texlive-pst-ghsb
Requires:	texlive-pst-gr3d
Requires:	texlive-pst-grad
Requires:	texlive-pst-graphicx
Requires:	texlive-pst-infixplot
Requires:	texlive-pst-intersect
Requires:	texlive-pst-jtree
Requires:	texlive-pst-knot
Requires:	texlive-pst-labo
Requires:	texlive-pst-layout
Requires:	texlive-pst-lens
Requires:	texlive-pst-light3d
Requires:	texlive-pst-magneticfield
Requires:	texlive-pst-math
Requires:	texlive-pst-mirror
Requires:	texlive-pst-node
Requires:	texlive-pst-ob3d
Requires:	texlive-pst-ode
Requires:	texlive-pst-optexp
Requires:	texlive-pst-optic
Requires:	texlive-pst-osci
Requires:	texlive-pst-ovl
Requires:	texlive-pst-pad
Requires:	texlive-pst-pdgr
Requires:	texlive-pst-platon
Requires:	texlive-pst-plot
Requires:	texlive-pst-poly
Requires:	texlive-pst-pulley
Requires:	texlive-pst-qtree
Requires:	texlive-pst-rubans
Requires:	texlive-pst-sigsys
Requires:	texlive-pst-slpe
Requires:	texlive-pst-solarsystem
Requires:	texlive-pst-spectra
Requires:	texlive-pst-solides3d
Requires:	texlive-pst-soroban
Requires:	texlive-pst-stru
Requires:	texlive-pst-support
Requires:	texlive-pst-text
Requires:	texlive-pst-thick
Requires:	texlive-pst-tools
Requires:	texlive-pst-tree
Requires:	texlive-pst-tvz
Requires:	texlive-pst-uml
Requires:	texlive-pst-vectorian
Requires:	texlive-pst-vowel
Requires:	texlive-pst-vue3d
Requires:	texlive-pst2pdf
Requires:	texlive-pstricks
Requires:	texlive-pstricks-add
Requires:	texlive-pstricks_calcnotes
Requires:	texlive-uml
Requires:	texlive-vaucanson-g
Requires:	texlive-vocaltract

%description
PSTricks core and all add-on packages.

#-----------------------------------------------------------------------
%files

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
