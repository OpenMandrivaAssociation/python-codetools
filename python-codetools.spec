%define module	codetools
%define name 	python-%{module}
%define version 4.0.0
%define release %mkrel 1

Summary:	Enthought Tool Suite - codetools project
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	%{module}-%{version}.tar.gz
License:	BSD
Group:		Development/Python
Url:		http://code.enthought.com/projects/code_tools/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:	noarch
Requires:	python-traits >= 4.0.0
BuildRequires:	python-setuptools >= 0.6c8
BuildRequires:	python-sphinx

%description
The codetools project includes packages that simplify meta-programming
and help the programmer separate data from code in Python. This
library contains classes that allow defining simple snippets, or
"blocks", of Python code, analyze variable dependencies in the code
block, and use these dependencies to construct or restrict an
execution graph. These (restricted) code blocks can then be executed
in any namespace. However, this project also provides a
Traits-event-enhanced namespace, called a "context", which can be used
in place of a vanilla namespace to allow actions to be performed
whenever variables are assigned or retrieved from the namespace. This
project is used as the foundation for the BlockCanvas project.

%prep
%setup -q -n %{module}-%{version}

%build
%__python setup.py build
pushd docs
make html
popd

%install
%__rm -rf %{buildroot}
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot} --record=FILE_LIST

%clean
%__rm -rf %{buildroot}

%files -f FILE_LIST
%defattr(-,root,root)
%doc *.txt *.rst examples/ docs/build/html/

