#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : certbot
Version  : 0.23.0
Release  : 23
URL      : https://github.com/certbot/certbot/archive/v0.23.0.tar.gz
Source0  : https://github.com/certbot/certbot/archive/v0.23.0.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: certbot-bin
Requires: certbot-python3
Requires: certbot-python
Requires: ConfigArgParse
Requires: acme
Requires: boto3
Requires: configobj
Requires: cryptography
Requires: dnspython
Requires: google-api-python-client
Requires: httplib2
Requires: josepy
Requires: oauth2client
Requires: parsedatetime
Requires: pyparsing
Requires: pyrfc3339
Requires: python-augeas
Requires: python-future-python3
Requires: python-mock
Requires: pytz
Requires: requests
Requires: setuptools
Requires: six
Requires: zope.component
Requires: zope.interface
BuildRequires : ConfigArgParse
BuildRequires : ConfigArgParse-python
BuildRequires : acme
BuildRequires : acme-python
BuildRequires : boto3
BuildRequires : cffi
BuildRequires : cffi-python
BuildRequires : configobj
BuildRequires : configobj-python
BuildRequires : cryptography
BuildRequires : dnspython
BuildRequires : enum34-python
BuildRequires : google-api-python-client
BuildRequires : httplib2
BuildRequires : josepy
BuildRequires : ndg_httpsclient-python
BuildRequires : oauth2client
BuildRequires : parsedatetime
BuildRequires : parsedatetime-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pyOpenSSL
BuildRequires : pyasn1-python
BuildRequires : pycparser
BuildRequires : pycparser-python
BuildRequires : pyparsing
BuildRequires : pyrfc3339
BuildRequires : pyrfc3339-python
BuildRequires : pytest
BuildRequires : python-augeas
BuildRequires : python-dev
BuildRequires : python-future-python3
BuildRequires : python-mock
BuildRequires : python-mock-python
BuildRequires : python3-dev
BuildRequires : pytz
BuildRequires : pytz-python
BuildRequires : requests
BuildRequires : setuptools
BuildRequires : six
BuildRequires : six-python
BuildRequires : tox
BuildRequires : virtualenv
BuildRequires : zope.component
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
Requires: certbot-python3

%description python
python components for the certbot package.


%package python3
Summary: python3 components for the certbot package.
Group: Default
Requires: python3-core

%description python3
python3 components for the certbot package.


%prep
%setup -q -n certbot-0.23.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1523649511
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python3.6/site-packages python3 setup.py test
%install
rm -rf %{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
## make_install_append content
for DIR in certbot-apache certbot-nginx certbot-nginx; do
(
cd ${DIR}
python3 setup.py build -b py3
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

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
