#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v21
# autospec commit: fbbd4e3
#
Name     : R-estimability
Version  : 1.5.1
Release  : 54
URL      : https://cran.r-project.org/src/contrib/estimability_1.5.1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/estimability_1.5.1.tar.gz
Summary  : Tools for Assessing Estimability of Linear Predictions
Group    : Development/Tools
License  : GPL-3.0
BuildRequires : buildreq-R
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
of regression coefficients, and 'epredict' methods that handle 
  non-estimable cases correctly. Estimability theory is discussed in
  many linear-models textbooks including Chapter 3 of Monahan, JF (2008), 
  "A Primer on Linear Models", Chapman and Hall (ISBN 978-1-4200-6201-4).

%prep
%setup -q -n estimability
pushd ..
cp -a estimability buildavx2
popd
pushd ..
cp -a estimability buildavx512
popd
pushd ..
cp -a estimability buildapx
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1740092065

%install
export SOURCE_DATE_EPOCH=1740092065
rm -rf %{buildroot}
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
mkdir -p %{buildroot}-v3/usr/lib64/R/library
mkdir -p %{buildroot}-v4/usr/lib64/R/library
mkdir -p %{buildroot}-va/usr/lib64/R/library

mkdir -p ~/.R
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}-v3/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --preclean  --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}-v4/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -mapxf -mavx10.1-512 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -mapxf -mavx10.1-512 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}-va/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean  --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py avx512 %{buildroot}-v4 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py apx %{buildroot}-va %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib64/R/library/estimability/DESCRIPTION
/usr/lib64/R/library/estimability/INDEX
/usr/lib64/R/library/estimability/Meta/Rd.rds
/usr/lib64/R/library/estimability/Meta/features.rds
/usr/lib64/R/library/estimability/Meta/hsearch.rds
/usr/lib64/R/library/estimability/Meta/links.rds
/usr/lib64/R/library/estimability/Meta/nsInfo.rds
/usr/lib64/R/library/estimability/Meta/package.rds
/usr/lib64/R/library/estimability/Meta/vignette.rds
/usr/lib64/R/library/estimability/NAMESPACE
/usr/lib64/R/library/estimability/NEWS
/usr/lib64/R/library/estimability/R/estimability
/usr/lib64/R/library/estimability/R/estimability.rdb
/usr/lib64/R/library/estimability/R/estimability.rdx
/usr/lib64/R/library/estimability/doc/add-est-check.R
/usr/lib64/R/library/estimability/doc/add-est-check.Rmd
/usr/lib64/R/library/estimability/doc/add-est-check.html
/usr/lib64/R/library/estimability/doc/index.html
/usr/lib64/R/library/estimability/help/AnIndex
/usr/lib64/R/library/estimability/help/aliases.rds
/usr/lib64/R/library/estimability/help/estimability.rdb
/usr/lib64/R/library/estimability/help/estimability.rdx
/usr/lib64/R/library/estimability/help/paths.rds
/usr/lib64/R/library/estimability/html/00Index.html
/usr/lib64/R/library/estimability/html/R.css
