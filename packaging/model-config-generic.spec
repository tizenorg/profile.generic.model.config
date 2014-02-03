Name:		model-config-generic
Summary:	A Model configuration
Version:	0.0.1
Release:	0
Group:		System/Configuration
License:	Apache-2.0
BuildArch:	noarch
Source0:	%{name}-%{version}.tar.gz

%description
Model configuration data package

%prep
%setup -q -n %{name}-%{version}

%build

%install
mkdir -p %{buildroot}%{_sysconfdir}/config
cp -f model-config.xml %{buildroot}%{_sysconfdir}/config/model-config.xml

%files
%manifest model-config.manifest
%license LICENSE.APLv2
%config %{_sysconfdir}/config/model-config.xml
