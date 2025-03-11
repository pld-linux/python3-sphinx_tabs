Summary:	Tabbed views for Sphinx
Summary(pl.UTF-8):	Przeglądanie w zakładkach dla Sphinksa
Name:		python3-sphinx_tabs
Version:	3.4.7
Release:	3
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/sphinx-tabs/
Source0:	https://files.pythonhosted.org/packages/source/s/sphinx-tabs/sphinx-tabs-%{version}.tar.gz
# Source0-md5:	114f4336f6ae286020761e77a8629981
URL:		https://pypi.org/project/sphinx-tabs/
BuildRequires:	python3-modules >= 1:3.7
BuildRequires:	python3-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
BuildRequires:	sed >= 4.0
Requires:	python3-modules >= 1:3.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Create tabbed content in Sphinx documentation when building HTML.

%description -l pl.UTF-8
Tworzenie treści w zakładkach w dokumentacji Sphinksa w formacie HTML.

%prep
%setup -q -n sphinx-tabs-%{version}

%build
%py3_build

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README.md
%{py3_sitescriptdir}/sphinx_tabs
%{py3_sitescriptdir}/sphinx_tabs-%{version}-py*.egg-info
