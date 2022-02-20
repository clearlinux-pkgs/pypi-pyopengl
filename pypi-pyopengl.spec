#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-pyopengl
Version  : 3.1.6
Release  : 26
URL      : https://files.pythonhosted.org/packages/5b/01/f8fd986bc7f456f1a925ee0239f0391838ade92cdb6e5b674ffb8b86cfd6/PyOpenGL-3.1.6.tar.gz
Source0  : https://files.pythonhosted.org/packages/5b/01/f8fd986bc7f456f1a925ee0239f0391838ade92cdb6e5b674ffb8b86cfd6/PyOpenGL-3.1.6.tar.gz
Summary  : Standard OpenGL bindings for Python
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pypi-pyopengl-license = %{version}-%{release}
Requires: pypi-pyopengl-python = %{version}-%{release}
Requires: pypi-pyopengl-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
PyOpenGL and PyOpenGL_Accelerate
=================================
PyOpenGL is normally distributed via PyPI using standard pip::

%package license
Summary: license components for the pypi-pyopengl package.
Group: Default

%description license
license components for the pypi-pyopengl package.


%package python
Summary: python components for the pypi-pyopengl package.
Group: Default
Requires: pypi-pyopengl-python3 = %{version}-%{release}

%description python
python components for the pypi-pyopengl package.


%package python3
Summary: python3 components for the pypi-pyopengl package.
Group: Default
Requires: python3-core
Provides: pypi(pyopengl)

%description python3
python3 components for the pypi-pyopengl package.


%prep
%setup -q -n PyOpenGL-3.1.6
cd %{_builddir}/PyOpenGL-3.1.6

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1645386997
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-pyopengl
cp %{_builddir}/PyOpenGL-3.1.6/license.txt %{buildroot}/usr/share/package-licenses/pypi-pyopengl/f6479ca0a457064e71273860ec9eb1fd2423298e
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-pyopengl/f6479ca0a457064e71273860ec9eb1fd2423298e

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*