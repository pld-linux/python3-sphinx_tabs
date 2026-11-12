Summary:	Tabbed views for Sphinx
Summary(pl.UTF-8):	Przeglądanie w zakładkach dla Sphinksa
Name:		python3-sphinx_tabs
Version:	3.5.0
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/sphinx-tabs/
Source0:	https://files.pythonhosted.org/packages/source/s/sphinx-tabs/sphinx_tabs-%{version}.tar.gz
# Source0-md5:	ec6b4ecae290c00a6ad9a762907017c0
URL:		https://pypi.org/project/sphinx-tabs/
BuildRequires:	python3-build
BuildRequires:	python3-installer
BuildRequires:	python3-modules >= 1:3.10
BuildRequires:	python3-setuptools
BuildRequires:	python3-wheel
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 2.044
Requires:	python3-modules >= 1:3.10
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Create tabbed content in Sphinx documentation when building HTML.

%description -l pl.UTF-8
Tworzenie treści w zakładkach w dokumentacji Sphinksa w formacie HTML.

%prep
%setup -q -n sphinx_tabs-%{version}

%build
%py3_build_pyproject

%install
rm -rf $RPM_BUILD_ROOT

%py3_install_pyproject

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README.md
%{py3_sitescriptdir}/sphinx_tabs
%{py3_sitescriptdir}/sphinx_tabs-%{version}.dist-info
