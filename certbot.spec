#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : certbot
Version  : 0.14.2
Release  : 8
URL      : https://github.com/certbot/certbot/archive/v0.14.2.tar.gz
Source0  : https://github.com/certbot/certbot/archive/v0.14.2.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: certbot-bin
Requires: certbot-python
Requires: python-mock
Requires: requests
Requires: six
Requires: zope.interface
BuildRequires : ConfigArgParse-python
BuildRequires : acme
BuildRequires : acme-python
BuildRequires : cffi
BuildRequires : cffi-python
BuildRequires : configobj-python
BuildRequires : enum34-python
BuildRequires : ndg_httpsclient-python
BuildRequires : parsedatetime-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pyOpenSSL
BuildRequires : pyasn1-python
BuildRequires : pycparser
BuildRequires : pycparser-python
BuildRequires : pyparsing
BuildRequires : pyrfc3339-python
BuildRequires : python-augeas
BuildRequires : python-dev
BuildRequires : python-future
BuildRequires : python-mock
BuildRequires : python-mock-python
BuildRequires : python3-dev
BuildRequires : pytz-python
BuildRequires : requests
BuildRequires : setuptools
BuildRequires : six
BuildRequires : six-python
BuildRequires : zope.component-python
BuildRequires : zope.event-python
BuildRequires : zope.interface

%description
This directory contains your keys and certificates.
`privkey.pem`  : the private key for your certificate.
`fullchain.pem`: the certificate file used in most server software.
`chain.pem`    : used for OCSP stapling in Nginx >=1.3.7.
`cert.pem`     : will break many server configurations, and should not be used
without reading further documentation (see link below).

%package bin
Summary: bin components for the certbot package.
Group: Binaries

%description bin
bin components for the certbot package.


%package python
Summary: python components for the certbot package.
Group: Default

%description python
python components for the certbot package.


%prep
%setup -q -n certbot-0.14.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1496951875
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python2.7/site-packages python2 setup.py test || :
%install
export SOURCE_DATE_EPOCH=1496951875
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
## make_install_append content
for DIR in certbot-apache certbot-nginx certbot-nginx; do
(
cd ${DIR}
python2 setup.py build -b py2
python3 setup.py build -b py3
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
)
done
## make_install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/certbot

%files python
%defattr(-,root,root,-)
/usr/lib/python2*/*
/usr/lib/python3*/*
