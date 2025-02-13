Name:		python-proto-plus
Version:	1.26.0
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/p/proto-plus/proto_plus-%{version}.tar.gz
Summary:	Beautiful, Pythonic protocol buffers
URL:		https://pypi.org/project/proto-plus/
License:	Apache 2.0
Group:		Development/Python
BuildRequires:	python
BuildSystem:	python
BuildArch:	noarch

%description
Beautiful, Pythonic protocol buffers

%files
%{py_sitedir}/proto
%{py_sitedir}/proto_plus-*.*-info
