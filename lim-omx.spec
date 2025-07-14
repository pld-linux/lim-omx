#
# Conditional build:
%bcond_without	tests	# don't perform "make check"
#
Summary:	Less Is More OpenMAX software stack
Summary(pl.UTF-8):	Implementacja Less Is More stosu OpenMAX
Name:		lim-omx
Version:	1.0
Release:	1
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://downloads.sourceforge.net/limoa/%{name}-%{version}.tar.gz
# Source0-md5:	7e2d31ede28e7678f879c02911bbd7f0
Patch0:		%{name}-link.patch
URL:		http://limoa.sourceforge.net/
BuildRequires:	SDL-devel >= 1.2.11
BuildRequires:	alsa-lib-devel >= 0.9.1
BuildRequires:	autoconf >= 2.61
BuildRequires:	automake
BuildRequires:	ffmpeg-devel >= 0.8.4-2
BuildRequires:	libmad-devel
BuildRequires:	libtool
BuildRequires:	libvorbis-devel
BuildRequires:	pkgconfig
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LIM (Less Is More) open source implementation of OpenMAX Application
Layer and OpenMAX Integration Layer.

%description -l pl.UTF-8
LIM (Less Is More) to mająca otwarte źródła implementacja standardu
OpenMAX w warstwach aplikacji (OpenMAX AL) i integracji (OpenMAX IL).

%package -n limutil
Summary:	LIM utility library
Summary(pl.UTF-8):	Biblioteka narzędziowa LIM
Group:		Libraries

%description -n limutil
LIM (Less Is More) utility library.

%description -n limutil -l pl.UTF-8
Biblioteka narzędziowa LIM (Less Is More).

%package -n limutil-devel
Summary:	Header files for LIM utility library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki narzędziowej LIM
Group:		Development/Libraries
Requires:	limutil = %{version}-%{release}

%description -n limutil-devel
Header files for LIM (Less Is More) utility library.

%description -n limutil-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki narzędziowej LIM (Less Is More).

%package -n limutil-static
Summary:	Static LIM utility library
Summary(pl.UTF-8):	Statyczna biblioteka narzędziowa LIM
Group:		Development/Libraries
Requires:	limutil-devel = %{version}-%{release}

%description -n limutil-static
Static LIM (Less Is More) utility library.

%description -n limutil-static -l pl.UTF-8
Statyczna biblioteka narzędziowa LIM (Less Is More).

%package -n limoi-core
Summary:	Less Is More OpenMAX Integration Layer - core client library
Summary(pl.UTF-8):	Implementacja Less Is More standardu OpenMAX IL - główna biblioteka kliencka
Group:		Libraries
Requires:	limutil = %{version}-%{release}

%description -n limoi-core
LIM (Less Is More) implementation of OpenMAX Integration Layer.

limoi-core provides the component loader and all OpenMAX integration
layer APIs, it is designed to work with any integration layer
components, in addition to those developed under limoi framework.

%description -n limoi-core -l pl.UTF-8
Implementacja LIM (Less Is More) warstwy integracji standardu OpenMAX
(OpenMAX IL).

limoi-core dostarcza zarządcę komponentów oraz wszystkie API warstwy
integracji OpenMAX. Jest zaprojektowany do działania z dowolnymi
komponentami warstwy integracji, nie tylko stworzonymi w ramach
szkieletu limoi.

%package -n limoi-core-devel
Summary:	Header files for LIM OpenMAX IL core client library
Summary(pl.UTF-8):	Pliki nagłówkowe głównej biblioteki klienckiej implementacji LIM OpenMAX IL
Group:		Development/Libraries
Requires:	limoi-core = %{version}-%{release}
Requires:	limutil-devel = %{version}-%{release}

%description -n limoi-core-devel
Header files for LIM OpenMAX IL core client library.

%description -n limoi-core-devel -l pl.UTF-8
Pliki nagłówkowe głównej biblioteki klienckiej implementacji LIM
OpenMAX IL.

%package -n limoi-core-static
Summary:	Static LIM OpenMAX IL core client library
Summary(pl.UTF-8):	Statyczna główna biblioteka kliencka implementacji LIM OpenMAX IL
Group:		Development/Libraries
Requires:	limutil-devel = %{version}-%{release}

%description -n limoi-core-static
Static LIM OpenMAX IL core client library.

%description -n limoi-core-static -l pl.UTF-8
Statyczna główna biblioteka kliencka implementacji LIM OpenMAX IL.

%package -n limoi-base
Summary:	Less Is More OpenMAX Integration Layer - base components
Summary(pl.UTF-8):	Implementacja Less Is More standardu OpenMAX IL - podstawowe komponenty
Group:		Libraries
Requires:	limoi-core = %{version}-%{release}

%description -n limoi-base
LIM (Less Is More) implementation of OpenMAX Integration Layer.

This package contains limoi base components library.

%description -n limoi-base -l pl.UTF-8
Implementacja LIM (Less Is More) warstwy integracji standardu OpenMAX
(OpenMAX IL).

Ten pakiet zawiera bibliotekę podstawowych komponentów limoi.

%package -n limoi-base-devel
Summary:	Header files for LIM OpenMAX IL base components library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki podstawowych komponentów implementacji LIM OpenMAX IL
Group:		Development/Libraries
Requires:	limoi-base = %{version}-%{release}
Requires:	limoi-core-devel = %{version}-%{release}

%description -n limoi-base-devel
Header files for LIM OpenMAX IL base components library.

%description -n limoi-base-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki podstaowych komponentów implementacji LIM
OpenMAX IL.

%package -n limoi-base-static
Summary:	Static LIM OpenMAX IL base components library
Summary(pl.UTF-8):	Statyczna biblioteka podstawowych komponentów implementacji LIM OpenMAX IL
Group:		Development/Libraries
Requires:	limutil-devel = %{version}-%{release}

%description -n limoi-base-static
Static LIM OpenMAX IL base components library.

%description -n limoi-base-static -l pl.UTF-8
Statyczna biblioteka podstawowych komponentów implementacji LIM
OpenMAX IL.

%package -n limomx-ffmpeg
Summary:	LIM OpenMAX ffmpeg wrapper library
Summary(pl.UTF-8):	Biblioteka LIM OpenMAX obudowująca ffmpeg
Group:		Libaries
Requires:	limoi-base = %{version}-%{release}
Requires:	ffmpeg-libs >= 0.8.4-2

%description -n limomx-ffmpeg
LIM OpenMAX ffmpeg wrapper library and LIMOI components.

%description -n limomx-ffmpeg -l pl.UTF-8
Biblioteka LIM OpenMAX obudowująca ffmpeg oraz komponenty ffmpeg dla
LIMOI.

%package -n limomx-ffmpeg-devel
Summary:	Header file for LIM OpenMAX ffmpeg wrapper library
Summary(pl.UTF-8):	Plik nagłówkowy biblioteki LIM OpenMAX obudowującej ffmpeg
Group:		Development/Libraries
Requires:	ffmpeg-devel >= 0.8.4-2
Requires:	limoi-base-devel = %{version}-%{release}
Requires:	limomx-ffmpeg = %{version}-%{release}

%description -n limomx-ffmpeg-devel
Header file for LIM OpenMAX ffmpeg wrapper library.

%description -n limomx-ffmpeg-devel -l pl.UTF-8
Plik nagłówkowy biblioteki LIM OpenMAX obudowującej ffmpeg.

%package -n limomx-ffmpeg-static
Summary:	Static LIM OpenMAX ffmpeg wrapper library
Summary(pl.UTF-8):	Statyczna biblioteka LIM OpenMAX obudowująca ffmpeg
Group:		Development/Libraries
Requires:	limomx-ffmpeg-static = %{version}-%{release}

%description -n limomx-ffmpeg-static
Static LIM OpenMAX ffmpeg wrapper library.

%description -n limomx-ffmpeg-static -l pl.UTF-8
Statyczna biblioteka LIM OpenMAX obudowująca ffmpeg.

%package -n limoi-component-alsa
Summary:	ALSA audio sink component for LIM OpenMAX IL
Summary(pl.UTF-8):	Komponent wyjścia dźwięku ALSA dla implementacji LIM OpenMAX IL
Group:		Libraries
Requires:	limoi-base = %{version}-%{release}

%description -n limoi-component-alsa
ALSA audio sink component for LIM OpenMAX IL.

%description -n limoi-component-alsa -l pl.UTF-8
Komponent wyjścia dźwięku ALSA dla implementacji LIM OpenMAX IL.

%package -n limoi-component-mad
Summary:	Mad MP3 decoder component for LIM OpenMAX IL
Summary(pl.UTF-8):	Komponent dekodera MP3 Mad dla implementacji LIM OpenMAX IL
Group:		Libraries
Requires:	limoi-base = %{version}-%{release}

%description -n limoi-component-mad
Mad MP3 decoder component for LIM OpenMAX IL.

%description -n limoi-component-mad -l pl.UTF-8
Komponent dekodera MP3 Mad dla implementacji LIM OpenMAX IL.

%package -n limoi-component-ogg
Summary:	Ogg Vorbis decoder component for LIM OpenMAX IL
Summary(pl.UTF-8):	Komponent dekodera Ogg Vorbis dla implementacji LIM OpenMAX IL
Group:		Libraries
Requires:	limoi-base = %{version}-%{release}

%description -n limoi-component-ogg
Ogg Vorbis decoder component for LIM OpenMAX IL.

%description -n limoi-component-ogg -l pl.UTF-8
Komponent dekodera Ogg Vorbis dla implementacji LIM OpenMAX IL.

%package -n limoi-component-sdl
Summary:	SDL video sink component for LIM OpenMAX IL
Summary(pl.UTF-8):	Komponent wyjścia obrazu SDL dla implementacji LIM OpenMAX IL
Group:		Libraries
Requires:	limoi-base = %{version}-%{release}

%description -n limoi-component-sdl
SDL video sink component for LIM OpenMAX IL.

%description -n limoi-component-sdl -l pl.UTF-8
Komponent wyjścia obrazu SDL dla implementacji LIM OpenMAX IL.

%package -n limoa
Summary:	Less Is More OpenMAX Application Layer library
Summary(pl.UTF-8):	Biblioteka implementacji Less Is More standardu OpenMAX AL
Group:		Libraries
Requires:	limoi-core = %{version}-%{release}

%description -n limoa
LIM (Less Is More) implementation of OpenMAX Application Layer
library.

%description -n limoa -l pl.UTF-8
Biblioteka implementacji LIM (Less Is More) warstwy aplikacji
standardu OpenMAX (OpenMAX AL).

%package -n limoa-devel
Summary:	Header files for LIM OpenMAX AL library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki implementacji LIM OpenMAX AL
Group:		Development/Libraries
Requires:	limoa = %{version}-%{release}
Requires:	limoi-core-devel = %{version}-%{release}

%description -n limoa-devel
Header files for LIM OpenMAX Application Layer library.

%description -n limoa-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki implementacji LIM OpenMAX AL.

%package -n limoa-static
Summary:	Static LIM OpenMAX AL library
Summary(pl.UTF-8):	Statyczna biblioteka implementacji LIM OpenMAX AL
Group:		Development/Libraries
Requires:	limoa = %{version}-%{release}
Requires:	limoi-core-devel = %{version}-%{release}

%description -n limoa-static
Static LIM OpenMAX Application Layer library.

%description -n limoa-static -l pl.UTF-8
Statyczna bibliotek implementacji LIM OpenMAX AL.

%prep
%setup -q
%patch -P0 -p1

%{__sed} -i -e 's/ -Werror//' \
	limoi-core/src/Makefile.am \
	limoi-base/src/Makefile.am \
	limoi-components/alsa_sink/src/Makefile.am \
	limoi-components/ffmpeg/decode/src/Makefile.am \
	limoi-components/ffmpeg/demux/src/Makefile.am \
	limoi-components/ffmpeg/encode/src/Makefile.am \
	limoi-components/ffmpeg/mux/src/Makefile.am \
	limoi-components/mad_dec/src/Makefile.am \
	limoi-components/ogg_dec/src/Makefile.am \
	limoi-components/video_scheduler/src/Makefile.am \
	limoa/src/frontend/Makefile.am

%build
BASEDIR=$(pwd)

cd limutil
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}
%if %{with tests}
%{__make} check
%endif

cd ../limoi-core
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	PKG_CONFIG_PATH="$BASEDIR/limutil" \
	LIMUTIL_CFLAGS="-I$BASEDIR/limutil/include" \
	LIMUTIL_LIBS="-L$BASEDIR/limutil/src/.libs -llimutil"
%{__make}
%if %{with tests}
%{__make} check
%endif

cd ../limoi-base
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	PKG_CONFIG_PATH="$BASEDIR/limutil:$BASEDIR/limoi-core" \
	LIMUTIL_CFLAGS="-I$BASEDIR/limutil/include" \
	LIMUTIL_LIBS="-L$BASEDIR/limutil/src/.libs -llimutil" \
	LIMOI_CFLAGS="-I$BASEDIR/limoi-core/include" \
	LIMOI_LIBS="-L$BASEDIR/limoi-core/src/.libs -llimoi-core"
%{__make}
%if %{with tests}
%{__make} check
%endif

for d in limoi-components/{alsa_sink,clock,ffmpeg/libomx-ffmpeg,mad_dec,ogg_dec,sdl/video_sink,video_scheduler} limoi-plugins/resource_managers/demo ; do
	cd $BASEDIR/$d
	%{__libtoolize}
	%{__aclocal}
	%{__autoconf}
	%{__autoheader}
	%{__automake}
	%configure \
		PKG_CONFIG_PATH="$BASEDIR/limutil:$BASEDIR/limoi-core:$BASEDIR/limoi-base" \
		LIMOI_CFLAGS="-I$BASEDIR/limoi-core/include -I$BASEDIR/limutil/include" \
		LIMOI_LIBS="-L$BASEDIR/limoi-core/src/.libs -llimoi-core" \
		LIMOIBASE_CFLAGS="-I$BASEDIR/limoi-base/include" \
		LIMOIBASE_LIBS="-L$BASEDIR/limoi-base/src/.libs -llimoi-base"
	%{__make}
%if %{with tests}
	%{__make} check
%endif
done

for d in limoi-components/ffmpeg/{decode,demux,encode,mux} ; do
	cd $BASEDIR/$d
	%{__libtoolize}
	%{__aclocal}
	%{__autoconf}
	%{__autoheader}
	%{__automake}
	%configure \
		PKG_CONFIG_PATH="$BASEDIR/limutil:$BASEDIR/limoi-core:$BASEDIR/limoi-base:$BASEDIR/limoi-components/ffmpeg/libomx-ffmpeg" \
		LIMOI_CFLAGS="-I$BASEDIR/limoi-core/include -I$BASEDIR/limutil/include" \
		LIMOI_LIBS="-L$BASEDIR/limoi-core/src/.libs -llimoi-core" \
		LIMOIBASE_CFLAGS="-I$BASEDIR/limoi-base/include" \
		LIMOIBASE_LIBS="-L$BASEDIR/limoi-base/src/.libs -llimoi-base" \
		OMX_FFMPEG_CFLAGS="-I$BASEDIR/limoi-components/ffmpeg/libomx-ffmpeg/include" \
		OMX_FFMPEG_LIBS="-L$BASEDIR/limoi-components/ffmpeg/libomx-ffmpeg/src/.libs -lomx-ffmpeg"
	%{__make}
%if %{with tests}
	%{__make} check
%endif
done

cd $BASEDIR/limoa
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	PKG_CONFIG_PATH="$BASEDIR/limutil:$BASEDIR/limoi-core" \
	LIMUTIL_CFLAGS="-I$BASEDIR/limutil/include" \
	LIMUTIL_LIBS="-L$BASEDIR/limutil/src/.libs -llimutil" \
	OMXIL_CFLAGS="-I$BASEDIR/limoi-core/include" \
	OMXIL_LIBS="-L$BASEDIR/limoi-core/src/.libs -llimoi-core"
%{__make}
%if %{with tests}
%{__make} check
%endif

%install
rm -rf $RPM_BUILD_ROOT

for d in limutil limoi-core limoi-base limoi-components/{alsa_sink,clock,ffmpeg/{libomx-ffmpeg,decode,demux,encode,mux},mad_dec,ogg_dec,sdl/video_sink,video_scheduler} limoi-plugins/resource_managers/demo limoa ; do
	%{__make} -C $d install \
		DESTDIR=$RPM_BUILD_ROOT
done

# obsoleted by pkg-config (and files are poisoned by builddir paths)
%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%{__rm} $RPM_BUILD_ROOT%{_libdir}/limoi/{component,resource-manager}/*.{la,a}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-n limutil -p /sbin/ldconfig
%postun	-n limutil -p /sbin/ldconfig

%post	-n limoi-core -p /sbin/ldconfig
%postun	-n limoi-core -p /sbin/ldconfig

%post	-n limoi-base -p /sbin/ldconfig
%postun	-n limoi-base -p /sbin/ldconfig

%post	-n limomx-ffmpeg -p /sbin/ldconfig
%postun	-n limomx-ffmpeg -p /sbin/ldconfig

%post	-n limoa -p /sbin/ldconfig
%postun	-n limoa -p /sbin/ldconfig

%files -n limutil
%defattr(644,root,root,755)
%doc limutil/README
%attr(755,root,root) %{_libdir}/liblimutil.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/liblimutil.so.0

%files -n limutil-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/liblimutil.so
%{_includedir}/limutil
%{_pkgconfigdir}/liblimutil.pc

%files -n limutil-static
%defattr(644,root,root,755)
%{_libdir}/liblimutil.a

%files -n limoi-core
%defattr(644,root,root,755)
%doc limoi-core/README
%attr(755,root,root) %{_libdir}/liblimoi-core.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/liblimoi-core.so.0
%dir %{_libdir}/limoi
%dir %{_libdir}/limoi/component
%attr(755,root,root) %{_libdir}/limoi/component/liblimoi-clock.so
%attr(755,root,root) %{_libdir}/limoi/component/liblimoi-video-scheduler.so
%dir %{_libdir}/limoi/resource-manager
%attr(755,root,root) %{_libdir}/limoi/resource-manager/liblim-demo-resource-manager.so

%files -n limoi-core-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/liblimoi-core.so
%{_includedir}/OMX_Audio.h
%{_includedir}/OMX_Component.h
%{_includedir}/OMX_ContentPipe.h
%{_includedir}/OMX_Core.h
%{_includedir}/OMX_IVCommon.h
%{_includedir}/OMX_Image.h
%{_includedir}/OMX_Index.h
%{_includedir}/OMX_Lim.h
%{_includedir}/OMX_Other.h
%{_includedir}/OMX_Types.h
%{_includedir}/OMX_Video.h
%{_pkgconfigdir}/liblimoi-core.pc

%files -n limoi-core-static
%defattr(644,root,root,755)
%{_libdir}/liblimoi-core.a

%files -n limoi-base
%defattr(644,root,root,755)
%doc limoi-base/README
%attr(755,root,root) %{_libdir}/liblimoi-base.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/liblimoi-base.so.0

%files -n limoi-base-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/liblimoi-base.so
%{_includedir}/limoi
%{_pkgconfigdir}/liblimoi-base.pc

%files -n limoi-base-static
%defattr(644,root,root,755)
%{_libdir}/liblimoi-base.a

%files -n limomx-ffmpeg
%defattr(644,root,root,755)
%doc limoi-components/ffmpeg/libomx-ffmpeg/README
%attr(755,root,root) %{_libdir}/libomx-ffmpeg.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libomx-ffmpeg.so.0
# the library requires limoi-base/core anyway, so we can package components here
%attr(755,root,root) %{_libdir}/limoi/component/liblimoi-ffmpeg-decode-audio.so
%attr(755,root,root) %{_libdir}/limoi/component/liblimoi-ffmpeg-decode-video.so
%attr(755,root,root) %{_libdir}/limoi/component/liblimoi-ffmpeg-demux.so
%attr(755,root,root) %{_libdir}/limoi/component/liblimoi-ffmpeg-encode-audio.so
%attr(755,root,root) %{_libdir}/limoi/component/liblimoi-ffmpeg-encode-video.so
%attr(755,root,root) %{_libdir}/limoi/component/liblimoi-ffmpeg-mux.so

%files -n limomx-ffmpeg-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libomx-ffmpeg.so
%{_includedir}/omx-ffmpeg
%{_pkgconfigdir}/libomx-ffmpeg.pc

%files -n limomx-ffmpeg-static
%defattr(644,root,root,755)
%{_libdir}/libomx-ffmpeg.a

%files -n limoi-component-alsa
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/limoi/component/liblimoi-alsa-sink.so

%files -n limoi-component-mad
%defattr(644,root,root,755)
%doc limoi-components/mad_dec/README
%attr(755,root,root) %{_libdir}/limoi/component/liblimoi-mad-dec.so

%files -n limoi-component-ogg
%defattr(644,root,root,755)
%doc limoi-components/ogg_dec/README
%attr(755,root,root) %{_libdir}/limoi/component/liblimoi-ogg-dec.so

%files -n limoi-component-sdl
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/limoi/component/liblimoi-sdl-video-sink.so

%files -n limoa
%defattr(644,root,root,755)
%doc limoa/{ChangeLog,NEWS,README}
%attr(755,root,root) %{_libdir}/liblimoa.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/liblimoa.so.0

%files -n limoa-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/liblimoa.so
%{_includedir}/OpenMAXAL.h
%{_includedir}/OpenMAXAL_Platform.h
%{_pkgconfigdir}/liblimoa.pc

%files -n limoa-static
%defattr(644,root,root,755)
%{_libdir}/liblimoa.a
