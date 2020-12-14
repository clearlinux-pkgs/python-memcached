#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : python-memcached
Version  : 1.59
Release  : 52
URL      : http://pypi.debian.net/python-memcached/python-memcached-1.59.tar.gz
Source0  : http://pypi.debian.net/python-memcached/python-memcached-1.59.tar.gz
Summary  : Pure python memcached client
Group    : Development/Tools
License  : Python-2.0
Requires: python-memcached-python = %{version}-%{release}
Requires: python-memcached-python3 = %{version}-%{release}
Requires: six
BuildRequires : buildreq-distutils3
BuildRequires : six
BuildRequires : six-python

%description
[![Build
Status](https://travis-ci.org/linsomniac/python-memcached.svg)](https://travis-ci.org/linsomniac/python-memcached)

%package python
Summary: python components for the python-memcached package.
Group: Default
Requires: python-memcached-python3 = %{version}-%{release}

%description python
python components for the python-memcached package.


%package python3
Summary: python3 components for the python-memcached package.
Group: Default
Requires: python3-core
Provides: pypi(python_memcached)
Requires: pypi(six)

%description python3
python3 components for the python-memcached package.


%prep
%setup -q -n python-memcached-1.59
cd %{_builddir}/python-memcached-1.59

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1583541457
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
python setup.py test
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
