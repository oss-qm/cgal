# Min dependencies
%global boost_version 1.39

Name:		cgal
Version:	4.7
Release:	mtx.1
Summary:	Computational Geometry Algorithms Library

License:	LGPLv3+ and GPLv3+ and Boost
URL:		http://www.cgal.org/
Source0:	%{name}-%{version}.tar.gz


# Required devel packages.
BuildRequires:	cmake >= 2.6.2 gmp-devel boost-devel >= %{boost_version}
BuildRequires:	zlib-devel
BuildRequires:	blas-devel lapack-devel mpfr-devel gcc-c++

%description
Libraries for CGAL applications.
CGAL is a collaborative effort of several sites in Europe and
Israel. The goal is to make the most important of the solutions and
methods developed in computational geometry available to users in
industry and academia in a C++ library. The goal is to provide easy
access to useful, reliable geometric algorithms.


%package devel
Summary:	Development files and tools for CGAL applications
Requires:	cmake
Requires:	%{name} = %{version}-%{release}
Requires:	boost-devel%{?_isa} >= %{boost_version}
Requires:	blas-devel%{?_isa} lapack-devel%{?_isa} zlib-devel%{?_isa} gmp-devel%{?_isa}
Requires:	mpfr-devel%{?_isa}

%description devel
The %{name}-devel package provides the headers files and tools you may need to
develop applications using CGAL.


%prep
%setup -q -n %{name}-%{version}


%build
%cmake \
    -DCGAL_INSTALL_LIB_DIR=%{_lib} \
    -DCGAL_INSTALL_DOC_DIR= \
    ${CHANGE_SOVERSION} \
    -DCMAKE_BUILD_TYPE=Release \
    ..

make VERBOSE=1 %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}

pushd build

make install DESTDIR=$RPM_BUILD_ROOT

popd

%clean
%{__rm} -rf %{buildroot}


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%defattr(-,root,root,-)
%doc Installation/AUTHORS Installation/LICENSE* Installation/CHANGES
%{_libdir}/libCGAL*.so.*


%files devel
%defattr(-,root,root,-)
%{_includedir}/CGAL
%{_libdir}/libCGAL*.so
%{_libdir}/CGAL
%{_mandir}


%changelog
* Fri Feb 07 2020 Enrico Weigelt, metux IT consult <info@metux.net> - 4.7-1.2
- Fresh packaging (pg 12)
