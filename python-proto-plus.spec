Name:		python-proto-plus
Version:	1.29.0
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/p/proto-plus/proto_plus-%{version}.tar.gz
Summary:	Beautiful, Pythonic protocol buffers
URL:		https://pypi.org/project/proto-plus/
License:	Apache 2.0
Group:		Development/Python
BuildSystem:	python
BuildRequires:	python%{pyver}dist(setuptools)
BuildArch:	noarch

%description
Beautiful, Pythonic protocol buffers

%prep
%autosetup -p1
# Cooker python-protobuf provides python3.15dist(protobuf) = 6.32.1.
find . -name pyproject.toml -o -name PKG-INFO | xargs sed -i 's/6\.33\.5/6.32.1/g'

%files
%{py_sitedir}/proto
%{py_sitedir}/proto_plus-*.*-info
