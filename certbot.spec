#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : certbot
Version  : 1.3.0
Release  : 69
URL      : https://github.com/certbot/certbot/archive/v1.3.0/certbot-1.3.0.tar.gz
Source0  : https://github.com/certbot/certbot/archive/v1.3.0/certbot-1.3.0.tar.gz
Summary  : A tool to automatically receive and install X.509 certificates to enable TLS on servers. The client will interoperate with the Let’s Encrypt CA which will be issuing browser-trusted certificates for free.
Group    : Development/Tools
License  : Apache-2.0
Requires: certbot-bin = %{version}-%{release}
Requires: certbot-license = %{version}-%{release}
Requires: certbot-python = %{version}-%{release}
Requires: certbot-python3 = %{version}-%{release}
Requires: ConfigArgParse
Requires: acme
Requires: augeas-lib
Requires: boto3
Requires: cloudflare
Requires: configobj
Requires: cryptography
Requires: distro
Requires: dns-lexicon
Requires: dnspython
Requires: docker-compose
Requires: google-api-python-client
Requires: httplib2
Requires: josepy
Requires: oauth2client
Requires: parsedatetime
Requires: pyOpenSSL
Requires: pyparsing
Requires: python-augeas
Requires: python-dateutil
Requires: python-digitalocean
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
BuildRequires : PyYAML
BuildRequires : acme
BuildRequires : acme-python
BuildRequires : augeas
BuildRequires : boto3
BuildRequires : buildreq-distutils3
BuildRequires : cffi
BuildRequires : cffi-python
BuildRequires : cloudflare
BuildRequires : configobj
BuildRequires : configobj-python
BuildRequires : coverage
BuildRequires : cryptography
BuildRequires : distro
BuildRequires : dns-lexicon
BuildRequires : dnspython
BuildRequires : docker-compose
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
BuildRequires : pyRFC3339-python
BuildRequires : pyasn1-python
BuildRequires : pycparser
BuildRequires : pycparser-python
BuildRequires : pyparsing
BuildRequires : pytest
BuildRequires : pytest-cov
BuildRequires : pytest-xdist
BuildRequires : python-augeas
BuildRequires : python-dateutil
BuildRequires : python-digitalocean
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
Certbot is part of EFF’s effort to encrypt the entire Internet. Secure communication over the Web relies on HTTPS, which requires the use of a digital certificate that lets browsers verify the identity of web servers (e.g., is that really google.com?). Web servers obtain their certificates from trusted third parties called certificate authorities (CAs). Certbot is an easy-to-use client that fetches a certificate from Let’s Encrypt—an open certificate authority launched by the EFF, Mozilla, and others—and deploys it to a web server.

%package bin
Summary: bin components for the certbot package.
Group: Binaries
Requires: certbot-license = %{version}-%{release}

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
Requires: certbot-python3 = %{version}-%{release}

%description python
python components for the certbot package.


%package python3
Summary: python3 components for the certbot package.
Group: Default
Requires: python3-core
Provides: pypi(certbot)
Requires: pypi(acme)
Requires: pypi(parsedatetime)
Requires: pypi(josepy)
Requires: pypi(zope.component)
Requires: pypi(mock)
Requires: pypi(zope.interface)
Requires: pypi(pytz)
Requires: pypi(pytest-cov)
Requires: pypi(wheel)
Requires: pypi(cryptography)
Requires: pypi(repoze.sphinx.autointerface)
Requires: pypi(mypy)
Requires: pypi(tox)
Requires: pypi(Sphinx)
Requires: pypi(setuptools)
Requires: pypi(ipdb)
Requires: pypi(ConfigArgParse)
Requires: pypi(sphinx-rtd-theme)
Requires: pypi(pylint)
Requires: pypi(pytest-xdist)
Requires: pypi(coverage)
Requires: pypi(pytest)
Requires: pypi(astroid)
Requires: pypi(twine)
Requires: pypi(configobj)
Requires: pypi(distro)

%description python3
python3 components for the certbot package.


%prep
%setup -q -n certbot-1.3.0
cd %{_builddir}/certbot-1.3.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1583333500
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
pushd certbot
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/certbot
cp %{_builddir}/certbot-1.3.0/LICENSE.txt %{buildroot}/usr/share/package-licenses/certbot/4bdc361ecc9ed00f502ec709aabdf54cc856b5cb
cp %{_builddir}/certbot-1.3.0/acme/LICENSE.txt %{buildroot}/usr/share/package-licenses/certbot/d095fa0d394cc9417a65aecd0d28e7d10e762f98
cp %{_builddir}/certbot-1.3.0/certbot-apache/LICENSE.txt %{buildroot}/usr/share/package-licenses/certbot/d095fa0d394cc9417a65aecd0d28e7d10e762f98
cp %{_builddir}/certbot-1.3.0/certbot-compatibility-test/LICENSE.txt %{buildroot}/usr/share/package-licenses/certbot/d095fa0d394cc9417a65aecd0d28e7d10e762f98
cp %{_builddir}/certbot-1.3.0/certbot-dns-cloudflare/LICENSE.txt %{buildroot}/usr/share/package-licenses/certbot/d095fa0d394cc9417a65aecd0d28e7d10e762f98
cp %{_builddir}/certbot-1.3.0/certbot-dns-cloudxns/LICENSE.txt %{buildroot}/usr/share/package-licenses/certbot/d095fa0d394cc9417a65aecd0d28e7d10e762f98
cp %{_builddir}/certbot-1.3.0/certbot-dns-digitalocean/LICENSE.txt %{buildroot}/usr/share/package-licenses/certbot/d095fa0d394cc9417a65aecd0d28e7d10e762f98
cp %{_builddir}/certbot-1.3.0/certbot-dns-dnsimple/LICENSE.txt %{buildroot}/usr/share/package-licenses/certbot/d095fa0d394cc9417a65aecd0d28e7d10e762f98
cp %{_builddir}/certbot-1.3.0/certbot-dns-dnsmadeeasy/LICENSE.txt %{buildroot}/usr/share/package-licenses/certbot/d095fa0d394cc9417a65aecd0d28e7d10e762f98
cp %{_builddir}/certbot-1.3.0/certbot-dns-gehirn/LICENSE.txt %{buildroot}/usr/share/package-licenses/certbot/d706715c5c263c4fcfd50231edb7889ae9711747
cp %{_builddir}/certbot-1.3.0/certbot-dns-google/LICENSE.txt %{buildroot}/usr/share/package-licenses/certbot/d095fa0d394cc9417a65aecd0d28e7d10e762f98
cp %{_builddir}/certbot-1.3.0/certbot-dns-linode/LICENSE.txt %{buildroot}/usr/share/package-licenses/certbot/d095fa0d394cc9417a65aecd0d28e7d10e762f98
cp %{_builddir}/certbot-1.3.0/certbot-dns-luadns/LICENSE.txt %{buildroot}/usr/share/package-licenses/certbot/d095fa0d394cc9417a65aecd0d28e7d10e762f98
cp %{_builddir}/certbot-1.3.0/certbot-dns-nsone/LICENSE.txt %{buildroot}/usr/share/package-licenses/certbot/d095fa0d394cc9417a65aecd0d28e7d10e762f98
cp %{_builddir}/certbot-1.3.0/certbot-dns-ovh/LICENSE.txt %{buildroot}/usr/share/package-licenses/certbot/d095fa0d394cc9417a65aecd0d28e7d10e762f98
cp %{_builddir}/certbot-1.3.0/certbot-dns-rfc2136/LICENSE.txt %{buildroot}/usr/share/package-licenses/certbot/d095fa0d394cc9417a65aecd0d28e7d10e762f98
cp %{_builddir}/certbot-1.3.0/certbot-dns-route53/LICENSE.txt %{buildroot}/usr/share/package-licenses/certbot/92170cdc034b2ff819323ff670d3b7266c8bffcd
cp %{_builddir}/certbot-1.3.0/certbot-dns-sakuracloud/LICENSE.txt %{buildroot}/usr/share/package-licenses/certbot/d706715c5c263c4fcfd50231edb7889ae9711747
cp %{_builddir}/certbot-1.3.0/certbot-nginx/LICENSE.txt %{buildroot}/usr/share/package-licenses/certbot/affa5dedd6ca7042fe64265d0c0433bc15b96f89
cp %{_builddir}/certbot-1.3.0/certbot/LICENSE.txt %{buildroot}/usr/share/package-licenses/certbot/4bdc361ecc9ed00f502ec709aabdf54cc856b5cb
pushd certbot
python3 -tt setup.py build  install --root=%{buildroot}
popd
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
## install_append content
for DIR in certbot-apache \
certbot-apache \
certbot-dns-cloudflare \
certbot-dns-cloudxns \
certbot-dns-digitalocean \
certbot-dns-dnsimple \
certbot-dns-dnsmadeeasy \
certbot-dns-gehirn \
certbot-dns-google \
certbot-dns-linode \
certbot-dns-luadns \
certbot-dns-nsone \
certbot-dns-ovh \
certbot-dns-rfc2136 \
certbot-dns-route53 \
certbot-dns-sakuracloud \
certbot-nginx \
; do
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
%defattr(0644,root,root,0755)
/usr/share/package-licenses/certbot/4bdc361ecc9ed00f502ec709aabdf54cc856b5cb
/usr/share/package-licenses/certbot/92170cdc034b2ff819323ff670d3b7266c8bffcd
/usr/share/package-licenses/certbot/affa5dedd6ca7042fe64265d0c0433bc15b96f89
/usr/share/package-licenses/certbot/d095fa0d394cc9417a65aecd0d28e7d10e762f98
/usr/share/package-licenses/certbot/d706715c5c263c4fcfd50231edb7889ae9711747

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
