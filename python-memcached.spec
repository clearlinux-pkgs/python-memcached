#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : python-memcached
Version  : 1.59
Release  : 25
URL      : http://pypi.debian.net/python-memcached/python-memcached-1.59.tar.gz
Source0  : http://pypi.debian.net/python-memcached/python-memcached-1.59.tar.gz
Summary  : Pure python memcached client
Group    : Development/Tools
License  : Python-2.0
Requires: python-memcached-legacypython
Requires: python-memcached-python3
Requires: python-memcached-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
[![Build
Status](https://travis-ci.org/linsomniac/python-memcached.svg)](https://travis-ci.org/linsomniac/python-memcached)

%package legacypython
Summary: legacypython components for the python-memcached package.
Group: Default
Requires: python-core

%description legacypython
legacypython components for the python-memcached package.


%package python
Summary: python components for the python-memcached package.
Group: Default
Requires: python-memcached-legacypython
Requires: python-memcached-python3

%description python
python components for the python-memcached package.


%package python3
Summary: python3 components for the python-memcached package.
Group: Default
Requires: python3-core

%description python3
python3 components for the python-memcached package.


%prep
%setup -q -n python-memcached-1.59

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1513370351
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
python setup.py test
%install
export SOURCE_DATE_EPOCH=1513370351
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
