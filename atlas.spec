# Update from 3.6.0 to 3.8.3 is based on Fedora atlas package. See
# http://cvs.fedoraproject.org/viewvc/rpms/atlas/devel/atlas.spec?revision=1.21

%define name	atlas
%define major	3
%define libname	%mklibname %{name} %{major}

Name:		%{name}
Version:	3.8.3
Release:	%mkrel 1
Summary:        Automatically Tuned Linear Algebra Software
Group:          Sciences/Mathematics
License:        BSD
URL:            http://math-atlas.sourceforge.net/
Source0:	http://downloads.sourceforge.net/math-atlas/atlas%{version}.tar.bz2
Source1:	http://math-atlas.sourceforge.net/errata.html
Source2:	http://math-atlas.sourceforge.net/faq.html
Source3:	http://www.cs.utsa.edu/~whaley/papers.html

Patch0:		atlas-fedora_shared.patch

Requires:	gcc-gfortran liblapack-devel make
BuildRequires:	gcc-gfortran liblapack-devel

BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root

%description
The ATLAS (Automatically Tuned Linear Algebra Software) project is an
ongoing research effort focusing on applying empirical techniques in
order to provide portable performance. At present, it provides C and
Fortran77 interfaces to a portably efficient BLAS implementation, as
well as a few routines from LAPACK.

The performance improvements in ATLAS are obtained largely via
compile-time optimizations and tend to be specific to a given hardware
configuration.


########################################################################
%ifarch %{ix86}
%define types	sse sse2 sse3
%define mode	32

#--#####################################################################
%package	-n %{libname}-sse
Summary:	ATLAS libraries for SSE extensions (Pentium III)
Group:		System/Libraries
Obsoletes:	%{libname}-3dnow < 3.7
Provides:	%{libname}-sse = %{version}-%{release}
Obsoletes:	%mklibname %{name}3.0-sse
Obsoletes:	%mklibname %{name}3.0-3dnow
Obsoletes:	%mklibname %{name}%{major}-3dnow

%description	-n %{libname}-sse
This package contains the ATLAS (Automatically Tuned Linear Algebra
Software) libraries compiled with SSE optimizations (Pentium III).
This is a generic binary package. Install the "%{name}" package
to build a version tuned for your computer.

%if %mdkversion < 200900
%post -n %{libname}-sse -p /sbin/ldconfig

%postun -n %{libname}-sse -p /sbin/ldconfig
%endif

%files		-n %{libname}-sse
%defattr(-,root,root,-)
%dir %{_libdir}/atlas-sse
%{_libdir}/atlas-sse/*.so.*
%{_sysconfdir}/ld.so.conf.d/atlas-sse.conf

#----###################################################################
%package	-n lib%{name}-sse-devel
Summary:	Development files for ATLAS SSE (Pentium III)
Group:		Development/Other
Requires:	%{libname}-sse = %{version}-%{release}
Obsoletes:	%mklibname -d %{name}3.0-sse
Obsoletes:	%mklibname -d %{name}3.0-3dnow
Obsoletes:	%mklibname -d %{name}%{major}-3dnow

%description	-n lib%{name}-sse-devel
This package contains headers and development libraries of ATLAS
(Automatically Tuned Linear Algebra Software) compiled with SSE
optimizations (Pentium III).

%files		-n lib%{name}-sse-devel
%defattr(-,root,root,-)
%doc doc/*
%{_libdir}/atlas-sse/*.so
%{_libdir}/atlas-sse/*.a
%dir %{_includedir}/atlas
%{_includedir}/atlas/*.h
%{_includedir}/cblas.h
%{_includedir}/clapack.h

#--#####################################################################
%package	-n %{libname}-sse2
Summary:	ATLAS libraries for SSE2 extensions (Pentium IV)
Group:		System/Libraries
Obsoletes:	%mklibname %{name}3.0-sse2
Provides:	%{libname}-sse2 = %{version}-%{release}
Provides:	%{libname} = %{version}-%{release}

%description	-n %{libname}-sse2
This package contains the ATLAS (Automatically Tuned Linear Algebra
Software) libraries compiled with SSE2 optimizations (Pentium IV).
This is a generic binary package. Install the "%{name}" package
to build a version tuned for your computer.

%if %mdkversion < 200900
%post -n %{libname}-sse2 -p /sbin/ldconfig

%postun -n %{libname}-sse2 -p /sbin/ldconfig
%endif

%files		-n %{libname}-sse2
%defattr(-,root,root,-)
%dir %{_libdir}/atlas
%{_libdir}/atlas/*.so.*
%{_sysconfdir}/ld.so.conf.d/atlas.conf

#----###################################################################
%package	-n lib%{name}-sse2-devel
Summary:	Development files for ATLAS with SSE2 extensions
Group:		Development/Other
Requires:	%{libname}-sse2 = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}

%description	-n lib%{name}-sse2-devel
This package contains headers and development libraries of ATLAS
(Automatically Tuned Linear Algebra Software) compiled with SSE2
optimizations (Pentium IV).

%files		-n lib%{name}-sse2-devel
%defattr(-,root,root,-)
%doc doc/*
%{_libdir}/atlas/*.so
%{_libdir}/atlas/*.a
%dir %{_includedir}/atlas
%{_includedir}/atlas/*.h
%{_includedir}/cblas.h
%{_includedir}/clapack.h

#--#####################################################################
%package	-n %{libname}-sse3
Summary:	ATLAS libraries for SSE3 extensions (Pentium IV)
Group:		System/Libraries

%description	-n %{libname}-sse3
This package contains the ATLAS (Automatically Tuned Linear Algebra
Software) libraries compiled with SS3 optimizations (Pentium IV).
This is a generic binary package. Install the "%{name}" package
to build a version tuned for your computer.

%if %mdkversion < 200900
%post -n %{libname}-sse3 -p /sbin/ldconfig

%postun -n %{libname}-sse3 -p /sbin/ldconfig
%endif

%files		-n %{libname}-sse3
%defattr(-,root,root,-)
%dir %{_libdir}/atlas-sse3
%{_libdir}/atlas-sse3/*.so.*
%{_sysconfdir}/ld.so.conf.d/atlas-sse3.conf

#----###################################################################
%package	-n lib%{name}-sse3-devel
Summary:	Development files for ATLAS SSE3 (Pentium IV)
Group:		Development/Other
Requires:	%{libname}-sse3 = %{version}-%{release}

%description	-n lib%{name}-sse3-devel
This package contains headers and development libraries of ATLAS
(Automatically Tuned Linear Algebra Software) compiled with SSE3
optimizations (Pentium IV).

%files		-n lib%{name}-sse3-devel
%defattr(-,root,root,-)
%doc doc/*
%{_libdir}/atlas-sse3/*.so
%{_libdir}/atlas-sse3/*.a
%dir %{_includedir}/atlas
%{_includedir}/atlas/*.h
%{_includedir}/cblas.h
%{_includedir}/clapack.h

########################################################################
%else
%ifarch x86_64
%define mode	64
%define types	x86_64

#--#####################################################################
%package	-n %{libname}-x86_64
Summary:	ATLAS libraries for x86_64
Group:		System/Libraries
Provides:	%{libname} = %{version}-%{release}

%description	-n %{libname}-x86_64
This package contains the ATLAS (Automatically Tuned Linear Algebra
Software) libraries compiled with x86_64 optimizations.
This is a generic binary package. Install the "%{name}" package
to build a version tuned for your computer.

%if %mdkversion < 200900
%post -n %{libname}-x86_64 -p /sbin/ldconfig

%postun -n %{libname}-x86_64 -p /sbin/ldconfig
%endif

%files		-n %{libname}-x86_64
%defattr(-,root,root,-)
%dir %{_libdir}/atlas
%{_libdir}/atlas/*.so.*
%{_sysconfdir}/ld.so.conf.d/atlas.conf

#----###################################################################
%package	-n lib%{name}-x86_64-devel
Summary:	Development files for ATLAS for x86_64
Group:		Development/Other
Requires:	%{libname}-x86_64 = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}

%description	lib%{name}-x86_64-devel
This package contains headers and development libraries of ATLAS
(Automatically Tuned Linear Algebra Software) compiled with x86_64
optimizations.

%files		-n lib%{name}-x86_64-devel
%defattr(-,root,root,-)
%doc doc/*
%{_libdir}/atlas/*.so
%{_libdir}/atlas/*.a
%dir %{_includedir}/atlas
%{_includedir}/atlas/*.h
%{_includedir}/cblas.h
%{_includedir}/clapack.h

%endif	# x86_64
%endif	# ix86


########################################################################
%prep
%setup -q -n ATLAS

%patch0 -p0 -b .shared

cp %{SOURCE1} %{SOURCE2} %{SOURCE3} doc

%build
for type in %{types}; do
    case $type in
	sse2|x86_64)	libname=%{name}		;;
	*)		libname=%{name}-$type	;;
    esac
    mkdir -p %{_arch}_${type}
    pushd %{_arch}_${type}
	../configure -b %{mode} -D c -DWALL -Fa alg			\
	    '-Wa,--noexecstack -fPIC'					\
	    -Ss f77lib `gfortran --print-file-name=libgfortran.so`	\
	    -t 2							\
	    --prefix=%{buildroot}%{_prefix}				\
	    --incdir=%{buildroot}%{_includedir}				\
	    --libdir=%{buildroot}%{_libdir}/${libname}			\
	    --with-netlib-lapack=%{_libdir}/liblapack_pic.a
	if [ "$type" = "sse" ]; then
		sed -i 's#ARCH =.*#ARCH = PIII32SSE1#' Make.inc
		sed -i 's#-DATL_SSE3 -DATL_SSE2##' Make.inc 
	elif [ "$type" = "sse2" ]; then
		sed -i 's#ARCH =.*#ARCH = P432SSE2#' Make.inc
		sed -i 's#-DATL_SSE3##' Make.inc 
	elif [ "$type" = "sse3" ]; then
		sed -i 's#ARCH =.*#ARCH = P4E32SSE3#' Make.inc
	fi
	make build
	cd lib
	make shared
	make ptshared
    popd
done

%install
for type in %{types}; do
    case $type in
	sse2|x86_64)	dirname=%{name}		;;
	*)		dirname=%{name}-$type	;;
    esac
    pushd %{_arch}_${type}
	make DESTDIR=%{buildroot} install || :
	mkdir -p %{buildroot}%{_libdir}/${dirname}
	cp -pr lib/*.so* %{buildroot}%{_libdir}/${dirname}/
    popd
    mkdir -p %{buildroot}%{_sysconfdir}/ld.so.conf.d
    echo "%{_libdir}/${dirname}"				\
	> %{buildroot}%{_sysconfdir}/ld.so.conf.d/${dirname}.conf
done

mkdir -p %{buildroot}%{_libdir}/%{name}
mkdir -p %{buildroot}%{_usrsrc}
tar jxf %{SOURCE0} -C %{buildroot}%{_usrsrc}
pushd %{buildroot}%{_usrsrc}/ATLAS
    patch -p0 < %{PATCH0}
popd

cat > %{buildroot}%{_usrsrc}/ATLAS/Makefile << EOF

all:	config libs

libs:
	mkdir -p %{_libdir}/%{name} &&					\
	(cd %{_arch} && make build && cd lib && make shared && make ptshared || :)

config:
	[ -d %{_arch} ] || (mkdir -p %{_arch} && cd %{_arch} &&		\
	../configure -b %{mode} -D c -DWALL -Fa alg			\
	'-Wa,--noexecstack -fPIC'					\
	-Ss f77lib `gfortran --print-file-name=libgfortran.so`		\
	--prefix=%{_prefix}						\
	--incdir=%{_includedir}/%{name}					\
	--libdir=%{_libdir}/%{name}					\
	--with-netlib-lapack=%{_libdir}/liblapack_pic.a)

clean:
	rm -fr %{_arch}

install:
	(cd %{_arch} && (make install || :) &&				\
	cp -pr lib/*.so* %{_libdir}/%{name} &&				\
	echo "%{_libdir}/%{name}" > %{_sysconfdir}/ld.so.conf.d/%{name}.conf)

uninstall:
	rm -fr %{_libdir}/%{name}/*
	rm -fr %{_includedir}/%{name}/*
	rm -f %{_sysconfdir}/ld.so.conf.d/%{name}.conf
	rm -f %{_includedir}/cblas.h
	rm -f %{_includedir}/clapack.h

EOF

cat >  %{buildroot}%{_usrsrc}/ATLAS/README.mandriva << EOF

  To build a tuned version of atlas for you computer, as root, run:

% cd %{_usrsrc}/ATLAS

% make all install

  The Makefile in this directory uses the same options as the
precompiled atlas packages, and uses the same directory layout.


  NOTES

o It is advisable to ensure cpu throttling is off. To do this:

  % urpmi cpufrequtils
  % cpufreq-set -g performance

o The tests during compilation are heavily dependent on cpu
  load. It is advisable to have as few background processes as
  possible during compilation, otherwise if timing samples are
  too much different, the build will fail, in which case, you
  can run:

  % cd %{_arch}
  % make

  to retry.

o Please also consult the files README and INSTALL.txt.
  Extra documentation is in %{_docdir}/atlas
  Example:
  % cd %{_arch}		# change to architecture build
  % make check		# check if library produces expected results
  % make ptcheck	# check threaded/smp library (if detected/built)
  % make time		# check if library has the expected performance

EOF

%clean
rm -rf %{buildroot}

########################################################################
%post
echo "

  Please check %{_usrsrc}/ATLAS/README.mandriva for build instructions.

"

%files
%defattr(-,root,root,-)
%dir %{_usrsrc}/ATLAS
%{_usrsrc}/ATLAS/*
%dir %{_includedir}/%{name}
%dir %{_libdir}/%{name}
%doc doc/*
