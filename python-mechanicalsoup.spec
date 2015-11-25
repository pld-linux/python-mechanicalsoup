#
# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define 	module	mechanicalsoup
Summary:	A Python library for automating interaction with websites
Name:		python-%{module}
Version:	0.4.0
Release:	1
License:	MIT
Group:		Libraries/Python
Source0:	https://pypi.python.org/packages/source/M/MechanicalSoup/MechanicalSoup-%{version}.zip
# Source0-md5:	f6eb7d7fc69fb6ce434b64a3a92c7e48
URL:		https://github.com/hickford/MechanicalSoup
BuildRequires:	rpm-pythonprov
%if %{with python2}
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-setuptools
%endif
Requires:	python-bs4
Requires:	python-requests
Requires:	python-six
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A Python library for automating interaction with websites.
MechanicalSoup automatically stores and sends cookies, follows
redirects, and can follow links and submit forms. It doesn't do
Javascript.

%package -n python3-%{module}
Summary:	A Python library for automating interaction with websites
Group:		Libraries/Python
Requires:	python3-bs4
Requires:	python3-requests
Requires:	python3-six

%description -n python3-%{module}
A Python library for automating interaction with websites.
MechanicalSoup automatically stores and sends cookies, follows
redirects, and can follow links and submit forms. It doesn't do
Javascript.

%prep
%setup -q -n MechanicalSoup-%{version}

%build
%if %{with python2}
%{__python} setup.py build --build-base build-2 %{?with_tests:test}
%endif

%if %{with python3}
%{__python3} setup.py build --build-base build-3 %{?with_tests:test}
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%{__python} setup.py \
	build --build-base build-2 \
	install --skip-build \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT
%endif

%if %{with python3}
%{__python3} setup.py \
	build --build-base build-3 \
	install --skip-build \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%{py_sitescriptdir}/mechanicalsoup
%{py_sitescriptdir}/MechanicalSoup-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%{py3_sitescriptdir}/mechanicalsoup
%{py3_sitescriptdir}/MechanicalSoup-%{version}-py*.egg-info
%endif
