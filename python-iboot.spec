%global modname iboot

Name:               python-iboot
Version:            0.1.0
Release:            1
Summary:            Python class to interface with Dataprobe iBoot devices

Group:              Development/Libraries
License:            BSD
URL:                https://github.com/darkip/python-iboot
Source0:            http://pypi.python.org/packages/source/d/%{modname}/%{modname}-%{version}.tar.gz

BuildArch:          noarch

BuildRequires:      python2-devel
BuildRequires:      python-setuptools

%description
Python class to interface with Dataprobe iBoot devices over the DxP protocol

%prep
%setup -q -n %{modname}-%{upstream_version}

# Remove bundled egg-info in case it exists
rm -rf %{modname}.egg-info

%build
%{__python} setup.py build

%install
%{__python} setup.py install -O1 --skip-build --root=%{buildroot}

%files
%{python_sitelib}/iboot/
%{python_sitelib}/%{modname}-%{version}*

%changelog
* Thu Oct 09 2014 Dan Prince <dprince@redhat.com> - 0.1.0-1
- Initial build.
