#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
#
Name     : R-interp
Version  : 1.1.4
Release  : 7
URL      : https://cran.r-project.org/src/contrib/interp_1.1-4.tar.gz
Source0  : https://cran.r-project.org/src/contrib/interp_1.1-4.tar.gz
Summary  : Interpolation Methods
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-interp-lib = %{version}-%{release}
Requires: R-Rcpp
Requires: R-RcppEigen
Requires: R-deldir
BuildRequires : R-Deriv
BuildRequires : R-Rcpp
BuildRequires : R-RcppEigen
BuildRequires : R-Ryacas
BuildRequires : R-deldir
BuildRequires : R-ggplot2
BuildRequires : R-gridExtra
BuildRequires : R-scatterplot3d
BuildRequires : buildreq-R

%description
grids, either linear or using splines are the main part of this
  package.  It is intended to provide FOSS replacement functions for

%package lib
Summary: lib components for the R-interp package.
Group: Libraries

%description lib
lib components for the R-interp package.


%prep
%setup -q -n interp

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1680538097

%install
export SOURCE_DATE_EPOCH=1680538097
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper -mprefer-vector-width=512  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/interp/DESCRIPTION
/usr/lib64/R/library/interp/INDEX
/usr/lib64/R/library/interp/Meta/Rd.rds
/usr/lib64/R/library/interp/Meta/data.rds
/usr/lib64/R/library/interp/Meta/features.rds
/usr/lib64/R/library/interp/Meta/hsearch.rds
/usr/lib64/R/library/interp/Meta/links.rds
/usr/lib64/R/library/interp/Meta/nsInfo.rds
/usr/lib64/R/library/interp/Meta/package.rds
/usr/lib64/R/library/interp/Meta/vignette.rds
/usr/lib64/R/library/interp/NAMESPACE
/usr/lib64/R/library/interp/R/interp
/usr/lib64/R/library/interp/R/interp.rdb
/usr/lib64/R/library/interp/R/interp.rdx
/usr/lib64/R/library/interp/data/akima.rda
/usr/lib64/R/library/interp/data/akima474.rda
/usr/lib64/R/library/interp/data/circtest.rda
/usr/lib64/R/library/interp/data/circtest2.rda
/usr/lib64/R/library/interp/data/franke.rda
/usr/lib64/R/library/interp/data/tritest.rda
/usr/lib64/R/library/interp/doc/index.html
/usr/lib64/R/library/interp/doc/interp.R
/usr/lib64/R/library/interp/doc/interp.Rnw
/usr/lib64/R/library/interp/doc/interp.pdf
/usr/lib64/R/library/interp/doc/partDeriv.R
/usr/lib64/R/library/interp/doc/partDeriv.Rnw
/usr/lib64/R/library/interp/doc/partDeriv.pdf
/usr/lib64/R/library/interp/doc/tri.R
/usr/lib64/R/library/interp/doc/tri.Rnw
/usr/lib64/R/library/interp/doc/tri.pdf
/usr/lib64/R/library/interp/help/AnIndex
/usr/lib64/R/library/interp/help/aliases.rds
/usr/lib64/R/library/interp/help/interp.rdb
/usr/lib64/R/library/interp/help/interp.rdx
/usr/lib64/R/library/interp/help/paths.rds
/usr/lib64/R/library/interp/html/00Index.html
/usr/lib64/R/library/interp/html/R.css

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/interp/libs/interp.so
/usr/lib64/R/library/interp/libs/interp.so.avx2
/usr/lib64/R/library/interp/libs/interp.so.avx512
