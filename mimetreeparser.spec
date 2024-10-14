#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v20
# autospec commit: f35655a
#
Name     : mimetreeparser
Version  : 24.08.2
Release  : 9
URL      : https://invent.kde.org/pim/mimetreeparser/-/archive/v24.08.2/mimetreeparser-v24.08.2.tar.gz
Source0  : https://invent.kde.org/pim/mimetreeparser/-/archive/v24.08.2/mimetreeparser-v24.08.2.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-2-Clause BSD-3-Clause CC0-1.0 FSFULLR GPL-2.0 GPL-3.0 LGPL-2.0 LGPL-2.1 LGPL-3.0
Requires: mimetreeparser-data = %{version}-%{release}
Requires: mimetreeparser-lib = %{version}-%{release}
Requires: mimetreeparser-license = %{version}-%{release}
Requires: mimetreeparser-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : gpgme-dev
BuildRequires : kcalendarcore-dev
BuildRequires : kmbox-dev
BuildRequires : kmime-dev
BuildRequires : libkleo-dev
BuildRequires : qt6base-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# MimeTreeParser
This repository contains a parser for a MIME tree and is based on KMime. The
goal is given a MIME tree to extract a list of parts (e.g. text, html) and a
list of attachments, check the validity of the signatures and decrypt any
encrypted part.

%package data
Summary: data components for the mimetreeparser package.
Group: Data

%description data
data components for the mimetreeparser package.


%package dev
Summary: dev components for the mimetreeparser package.
Group: Development
Requires: mimetreeparser-lib = %{version}-%{release}
Requires: mimetreeparser-data = %{version}-%{release}
Provides: mimetreeparser-devel = %{version}-%{release}
Requires: mimetreeparser = %{version}-%{release}

%description dev
dev components for the mimetreeparser package.


%package lib
Summary: lib components for the mimetreeparser package.
Group: Libraries
Requires: mimetreeparser-data = %{version}-%{release}
Requires: mimetreeparser-license = %{version}-%{release}

%description lib
lib components for the mimetreeparser package.


%package license
Summary: license components for the mimetreeparser package.
Group: Default

%description license
license components for the mimetreeparser package.


%package locales
Summary: locales components for the mimetreeparser package.
Group: Default

%description locales
locales components for the mimetreeparser package.


%prep
%setup -q -n mimetreeparser-v24.08.2
cd %{_builddir}/mimetreeparser-v24.08.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1728927309
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1728927309
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/mimetreeparser
cp %{_builddir}/mimetreeparser-v%{version}/LICENSES/BSD-2-Clause.txt %{buildroot}/usr/share/package-licenses/mimetreeparser/07c1ab270255cf247438e2358ff0c18835b6a6ce || :
cp %{_builddir}/mimetreeparser-v%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/mimetreeparser/3630f1ffcec0e075bf446b88c7b507b1287b571d || :
cp %{_builddir}/mimetreeparser-v%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/mimetreeparser/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0 || :
cp %{_builddir}/mimetreeparser-v%{version}/LICENSES/FSFULLR.txt %{buildroot}/usr/share/package-licenses/mimetreeparser/6daff26780d253b9cfc59ac7b3a904a1a5aac8ab || :
cp %{_builddir}/mimetreeparser-v%{version}/LICENSES/GPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/mimetreeparser/3cb34cfc72e87654683f2894299adf912d14b284 || :
cp %{_builddir}/mimetreeparser-v%{version}/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/mimetreeparser/3cb34cfc72e87654683f2894299adf912d14b284 || :
cp %{_builddir}/mimetreeparser-v%{version}/LICENSES/LGPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/mimetreeparser/5c6c38fa1b6ac7c66252c83d1203e997ae3d1c98 || :
cp %{_builddir}/mimetreeparser-v%{version}/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/mimetreeparser/5c6c38fa1b6ac7c66252c83d1203e997ae3d1c98 || :
cp %{_builddir}/mimetreeparser-v%{version}/LICENSES/LGPL-2.1-only.txt %{buildroot}/usr/share/package-licenses/mimetreeparser/fa05e58320cb7c64786b26396f4b992579a628bc || :
cp %{_builddir}/mimetreeparser-v%{version}/LICENSES/LGPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/mimetreeparser/0b71159e19bef95069e18d17296291916e89b5cd || :
cp %{_builddir}/mimetreeparser-v%{version}/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/mimetreeparser/7d9831e05094ce723947d729c2a46a09d6e90275 || :
cp %{_builddir}/mimetreeparser-v%{version}/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/mimetreeparser/7d9831e05094ce723947d729c2a46a09d6e90275 || :
cp %{_builddir}/mimetreeparser-v%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/mimetreeparser/e458941548e0864907e654fa2e192844ae90fc32 || :
cp %{_builddir}/mimetreeparser-v%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/mimetreeparser/e458941548e0864907e654fa2e192844ae90fc32 || :
export GOAMD64=v2
GOAMD64=v2
pushd clr-build
%make_install
popd
%find_lang mimetreeparser6

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/qlogging-categories6/mimetreeparser.categories

%files dev
%defattr(-,root,root,-)
/usr/include/KPim6/MimeTreeParserCore/MimeTreeParserCore/AttachmentModel
/usr/include/KPim6/MimeTreeParserCore/MimeTreeParserCore/CryptoHelper
/usr/include/KPim6/MimeTreeParserCore/MimeTreeParserCore/Enums
/usr/include/KPim6/MimeTreeParserCore/MimeTreeParserCore/Errors
/usr/include/KPim6/MimeTreeParserCore/MimeTreeParserCore/FileOpener
/usr/include/KPim6/MimeTreeParserCore/MimeTreeParserCore/MessageParser
/usr/include/KPim6/MimeTreeParserCore/MimeTreeParserCore/MessagePart
/usr/include/KPim6/MimeTreeParserCore/MimeTreeParserCore/ObjectTreeParser
/usr/include/KPim6/MimeTreeParserCore/MimeTreeParserCore/PartMetaData
/usr/include/KPim6/MimeTreeParserCore/MimeTreeParserCore/PartModel
/usr/include/KPim6/MimeTreeParserCore/mimetreeparsercore/attachmentmodel.h
/usr/include/KPim6/MimeTreeParserCore/mimetreeparsercore/cryptohelper.h
/usr/include/KPim6/MimeTreeParserCore/mimetreeparsercore/enums.h
/usr/include/KPim6/MimeTreeParserCore/mimetreeparsercore/errors.h
/usr/include/KPim6/MimeTreeParserCore/mimetreeparsercore/fileopener.h
/usr/include/KPim6/MimeTreeParserCore/mimetreeparsercore/messageparser.h
/usr/include/KPim6/MimeTreeParserCore/mimetreeparsercore/messagepart.h
/usr/include/KPim6/MimeTreeParserCore/mimetreeparsercore/mimetreeparser_core_export.h
/usr/include/KPim6/MimeTreeParserCore/mimetreeparsercore/objecttreeparser.h
/usr/include/KPim6/MimeTreeParserCore/mimetreeparsercore/partmetadata.h
/usr/include/KPim6/MimeTreeParserCore/mimetreeparsercore/partmodel.h
/usr/include/KPim6/MimeTreeParserCore/mimetreeparserng_version.h
/usr/include/KPim6/MimeTreeParserWidgets/MimeTreeParserWidgets/MessageViewer
/usr/include/KPim6/MimeTreeParserWidgets/MimeTreeParserWidgets/MessageViewerDialog
/usr/include/KPim6/MimeTreeParserWidgets/mimetreeparser_widgets_version.h
/usr/include/KPim6/MimeTreeParserWidgets/mimetreeparserwidgets/messageviewer.h
/usr/include/KPim6/MimeTreeParserWidgets/mimetreeparserwidgets/messageviewerdialog.h
/usr/include/KPim6/MimeTreeParserWidgets/mimetreeparserwidgets/mimetreeparser_widgets_export.h
/usr/lib64/cmake/KPim6MimeTreeParserCore/KPim6MimeTreeParserCoreConfig.cmake
/usr/lib64/cmake/KPim6MimeTreeParserCore/KPim6MimeTreeParserCoreConfigVersion.cmake
/usr/lib64/cmake/KPim6MimeTreeParserCore/KPim6MimeTreeParserCoreTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KPim6MimeTreeParserCore/KPim6MimeTreeParserCoreTargets.cmake
/usr/lib64/cmake/KPim6MimeTreeParserWidgets/KPim6MimeTreeParserWidgetsConfig.cmake
/usr/lib64/cmake/KPim6MimeTreeParserWidgets/KPim6MimeTreeParserWidgetsConfigVersion.cmake
/usr/lib64/cmake/KPim6MimeTreeParserWidgets/KPim6MimeTreeParserWidgetsTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KPim6MimeTreeParserWidgets/KPim6MimeTreeParserWidgetsTargets.cmake
/usr/lib64/libKPim6MimeTreeParserCore.so
/usr/lib64/libKPim6MimeTreeParserWidgets.so
/usr/lib64/qt6/mkspecs/modules/qt_MimeTreeParserCore.pri
/usr/lib64/qt6/mkspecs/modules/qt_MimeTreeParserWidgets.pri

%files lib
%defattr(-,root,root,-)
/usr/lib64/libKPim6MimeTreeParserCore.so.6
/usr/lib64/libKPim6MimeTreeParserCore.so.6.2.2
/usr/lib64/libKPim6MimeTreeParserWidgets.so.6
/usr/lib64/libKPim6MimeTreeParserWidgets.so.6.2.2
/usr/lib64/qt6/qml/org/kde/pim/mimetreeparser/MailViewer.qml
/usr/lib64/qt6/qml/org/kde/pim/mimetreeparser/kde-qmlmodule.version
/usr/lib64/qt6/qml/org/kde/pim/mimetreeparser/libmimetreeparser_plugin.so
/usr/lib64/qt6/qml/org/kde/pim/mimetreeparser/mimetreeparser_plugin.qmltypes
/usr/lib64/qt6/qml/org/kde/pim/mimetreeparser/private/AttachmentDelegate.qml
/usr/lib64/qt6/qml/org/kde/pim/mimetreeparser/private/Banner.qml
/usr/lib64/qt6/qml/org/kde/pim/mimetreeparser/private/ErrorPart.qml
/usr/lib64/qt6/qml/org/kde/pim/mimetreeparser/private/HtmlPart.qml
/usr/lib64/qt6/qml/org/kde/pim/mimetreeparser/private/ICalPart.qml
/usr/lib64/qt6/qml/org/kde/pim/mimetreeparser/private/MailPart.qml
/usr/lib64/qt6/qml/org/kde/pim/mimetreeparser/private/MailPartModel.qml
/usr/lib64/qt6/qml/org/kde/pim/mimetreeparser/private/MailPartView.qml
/usr/lib64/qt6/qml/org/kde/pim/mimetreeparser/private/TextPart.qml
/usr/lib64/qt6/qml/org/kde/pim/mimetreeparser/qmldir

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/mimetreeparser/07c1ab270255cf247438e2358ff0c18835b6a6ce
/usr/share/package-licenses/mimetreeparser/0b71159e19bef95069e18d17296291916e89b5cd
/usr/share/package-licenses/mimetreeparser/3630f1ffcec0e075bf446b88c7b507b1287b571d
/usr/share/package-licenses/mimetreeparser/3cb34cfc72e87654683f2894299adf912d14b284
/usr/share/package-licenses/mimetreeparser/5c6c38fa1b6ac7c66252c83d1203e997ae3d1c98
/usr/share/package-licenses/mimetreeparser/6daff26780d253b9cfc59ac7b3a904a1a5aac8ab
/usr/share/package-licenses/mimetreeparser/7d9831e05094ce723947d729c2a46a09d6e90275
/usr/share/package-licenses/mimetreeparser/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0
/usr/share/package-licenses/mimetreeparser/e458941548e0864907e654fa2e192844ae90fc32
/usr/share/package-licenses/mimetreeparser/fa05e58320cb7c64786b26396f4b992579a628bc

%files locales -f mimetreeparser6.lang
%defattr(-,root,root,-)

