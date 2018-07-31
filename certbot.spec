#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : certbot
Version  : 0.26.1
Release  : 33
URL      : https://github.com/certbot/certbot/archive/v0.26.1.tar.gz
Source0  : https://github.com/certbot/certbot/archive/v0.26.1.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: certbot-bin
Requires: certbot-python3
Requires: certbot-license
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
Requires: pyOpenSSL
Requires: pyparsing
Requires: pyrfc3339
Requires: python-augeas
Requires: python-future-python3
Requires: pytz
Requires: requests
Requires: six
Requires: zope.component
Requires: zope.interface
BuildRequires : ConfigArgParse
BuildRequires : ConfigArgParse-python
BuildRequires : acme
BuildRequires : acme-python
BuildRequires : augeas
BuildRequires : boto3
BuildRequires : buildreq-distutils3
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
BuildRequires : python-future-python3
BuildRequires : python-mock
BuildRequires : python-mock-python
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
Requires: certbot-license

%description bin
bin components for the certbot package.


%package license
Summary: license components for the certbot package.
Group: Default

%description license
license components for the certbot package.


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
%setup -q -n certbot-0.26.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1533057257
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python3.7/site-packages python3 setup.py test || :
%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/certbot
cp LICENSE.txt %{buildroot}/usr/share/doc/certbot/LICENSE.txt
cp acme/LICENSE.txt %{buildroot}/usr/share/doc/certbot/acme_LICENSE.txt
cp certbot-apache/LICENSE.txt %{buildroot}/usr/share/doc/certbot/certbot-apache_LICENSE.txt
cp certbot-compatibility-test/LICENSE.txt %{buildroot}/usr/share/doc/certbot/certbot-compatibility-test_LICENSE.txt
cp certbot-dns-cloudflare/LICENSE.txt %{buildroot}/usr/share/doc/certbot/certbot-dns-cloudflare_LICENSE.txt
cp certbot-dns-cloudxns/LICENSE.txt %{buildroot}/usr/share/doc/certbot/certbot-dns-cloudxns_LICENSE.txt
cp certbot-dns-digitalocean/LICENSE.txt %{buildroot}/usr/share/doc/certbot/certbot-dns-digitalocean_LICENSE.txt
cp certbot-dns-dnsimple/LICENSE.txt %{buildroot}/usr/share/doc/certbot/certbot-dns-dnsimple_LICENSE.txt
cp certbot-dns-dnsmadeeasy/LICENSE.txt %{buildroot}/usr/share/doc/certbot/certbot-dns-dnsmadeeasy_LICENSE.txt
cp certbot-dns-gehirn/LICENSE.txt %{buildroot}/usr/share/doc/certbot/certbot-dns-gehirn_LICENSE.txt
cp certbot-dns-google/LICENSE.txt %{buildroot}/usr/share/doc/certbot/certbot-dns-google_LICENSE.txt
cp certbot-dns-linode/LICENSE.txt %{buildroot}/usr/share/doc/certbot/certbot-dns-linode_LICENSE.txt
cp certbot-dns-luadns/LICENSE.txt %{buildroot}/usr/share/doc/certbot/certbot-dns-luadns_LICENSE.txt
cp certbot-dns-nsone/LICENSE.txt %{buildroot}/usr/share/doc/certbot/certbot-dns-nsone_LICENSE.txt
cp certbot-dns-ovh/LICENSE.txt %{buildroot}/usr/share/doc/certbot/certbot-dns-ovh_LICENSE.txt
cp certbot-dns-rfc2136/LICENSE.txt %{buildroot}/usr/share/doc/certbot/certbot-dns-rfc2136_LICENSE.txt
cp certbot-dns-route53/LICENSE %{buildroot}/usr/share/doc/certbot/certbot-dns-route53_LICENSE
cp certbot-dns-sakuracloud/LICENSE.txt %{buildroot}/usr/share/doc/certbot/certbot-dns-sakuracloud_LICENSE.txt
cp certbot-nginx/LICENSE.txt %{buildroot}/usr/share/doc/certbot/certbot-nginx_LICENSE.txt
cp certbot-postfix/LICENSE.txt %{buildroot}/usr/share/doc/certbot/certbot-postfix_LICENSE.txt
cp letshelp-certbot/LICENSE.txt %{buildroot}/usr/share/doc/certbot/letshelp-certbot_LICENSE.txt
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
## install_append content
for DIR in certbot-apache certbot-nginx certbot-nginx; do
(
cd ${DIR}
python3 setup.py build -b py3
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
)
done
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/certbot

%files license
%defattr(-,root,root,-)
/usr/share/doc/certbot/LICENSE.txt
/usr/share/doc/certbot/acme_LICENSE.txt
/usr/share/doc/certbot/certbot-apache_LICENSE.txt
/usr/share/doc/certbot/certbot-compatibility-test_LICENSE.txt
/usr/share/doc/certbot/certbot-dns-cloudflare_LICENSE.txt
/usr/share/doc/certbot/certbot-dns-cloudxns_LICENSE.txt
/usr/share/doc/certbot/certbot-dns-digitalocean_LICENSE.txt
/usr/share/doc/certbot/certbot-dns-dnsimple_LICENSE.txt
/usr/share/doc/certbot/certbot-dns-dnsmadeeasy_LICENSE.txt
/usr/share/doc/certbot/certbot-dns-gehirn_LICENSE.txt
/usr/share/doc/certbot/certbot-dns-google_LICENSE.txt
/usr/share/doc/certbot/certbot-dns-linode_LICENSE.txt
/usr/share/doc/certbot/certbot-dns-luadns_LICENSE.txt
/usr/share/doc/certbot/certbot-dns-nsone_LICENSE.txt
/usr/share/doc/certbot/certbot-dns-ovh_LICENSE.txt
/usr/share/doc/certbot/certbot-dns-rfc2136_LICENSE.txt
/usr/share/doc/certbot/certbot-dns-route53_LICENSE
/usr/share/doc/certbot/certbot-dns-sakuracloud_LICENSE.txt
/usr/share/doc/certbot/certbot-nginx_LICENSE.txt
/usr/share/doc/certbot/certbot-postfix_LICENSE.txt
/usr/share/doc/certbot/letshelp-certbot_LICENSE.txt

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
