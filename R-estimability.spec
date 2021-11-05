#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-estimability
Version  : 1.3
Release  : 35
URL      : https://cran.r-project.org/src/contrib/estimability_1.3.tar.gz
Source0  : https://cran.r-project.org/src/contrib/estimability_1.3.tar.gz
Summary  : Tools for Assessing Estimability of Linear Predictions
Group    : Development/Tools
License  : GPL-3.0
BuildRequires : buildreq-R

%description
of regression coefficients, and 'epredict' methods that handle 
  non-estimable cases correctly. Estimability theory is discussed in
  many linear-models textbooks including Chapter 3 of Monahan, JF (2008), 
  "A Primer on Linear Models", Chapman and Hall (ISBN 978-1-4200-6201-4).

%prep
%setup -q -c -n estimability
cd %{_builddir}/estimability

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1589531421

%install
export SOURCE_DATE_EPOCH=1589531421
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
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library estimability
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library estimability
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library estimability
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc estimability || :


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
/usr/lib64/R/library/estimability/NAMESPACE
/usr/lib64/R/library/estimability/NEWS
/usr/lib64/R/library/estimability/R/estimability
/usr/lib64/R/library/estimability/R/estimability.rdb
/usr/lib64/R/library/estimability/R/estimability.rdx
/usr/lib64/R/library/estimability/help/AnIndex
/usr/lib64/R/library/estimability/help/aliases.rds
/usr/lib64/R/library/estimability/help/estimability.rdb
/usr/lib64/R/library/estimability/help/estimability.rdx
/usr/lib64/R/library/estimability/help/paths.rds
/usr/lib64/R/library/estimability/html/00Index.html
/usr/lib64/R/library/estimability/html/R.css
