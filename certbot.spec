#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : certbot
Version  : 1.20.0
Release  : 96
URL      : https://github.com/certbot/certbot/archive/v1.20.0/certbot-1.20.0.tar.gz
Source0  : https://github.com/certbot/certbot/archive/v1.20.0/certbot-1.20.0.tar.gz
Summary  : ACME client
Group    : Development/Tools
License  : Apache-2.0
Requires: certbot-bin = %{version}-%{release}
Requires: certbot-license = %{version}-%{release}
Requires: certbot-python = %{version}-%{release}
Requires: certbot-python3 = %{version}-%{release}
Requires: ConfigArgParse
Requires: acme
Requires: augeas
Requires: boto3
Requires: cffi
Requires: charset-normalizer
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
Requires: ndg_httpsclient
Requires: oauth2client
Requires: parsedatetime
Requires: platformdirs
Requires: pyOpenSSL
Requires: pyRFC3339
Requires: pyasn1
Requires: pycparser
Requires: pyparsing
Requires: python-augeas
Requires: python-dateutil
Requires: python-digitalocean
Requires: python-future
Requires: python-mock
Requires: pytz
Requires: requests
Requires: requests-toolbelt
Requires: setuptools
Requires: zope.component
Requires: zope.interface
BuildRequires : ConfigArgParse
BuildRequires : PyYAML
BuildRequires : acme
BuildRequires : augeas
BuildRequires : boto3
BuildRequires : buildreq-distutils3
BuildRequires : cffi
BuildRequires : charset-normalizer
BuildRequires : cloudflare
BuildRequires : configobj
BuildRequires : coverage
BuildRequires : cryptography
BuildRequires : distro
BuildRequires : dns-lexicon
BuildRequires : dnspython
BuildRequires : docker-compose
BuildRequires : google-api-python-client
BuildRequires : httplib2
BuildRequires : josepy
BuildRequires : ndg_httpsclient
BuildRequires : oauth2client
BuildRequires : parsedatetime
BuildRequires : platformdirs
BuildRequires : py-python
BuildRequires : pyOpenSSL
BuildRequires : pyRFC3339
BuildRequires : pyasn1
BuildRequires : pycparser
BuildRequires : pyparsing
BuildRequires : pytest
BuildRequires : pytest-cov
BuildRequires : pytest-xdist
BuildRequires : python-augeas
BuildRequires : python-dateutil
BuildRequires : python-digitalocean
BuildRequires : python-future
BuildRequires : python-mock
BuildRequires : pytz
BuildRequires : requests
BuildRequires : requests-toolbelt
BuildRequires : setuptools
BuildRequires : zope.component
BuildRequires : zope.interface

%description
Eventually there will also be a compatibility test here like the Apache one.
Right now, this is data for the roundtrip test (checking that the parser
can parse each file and that the reserialized config file it generates is
identical to the original).

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
Requires: pypi(configargparse)
Requires: pypi(configobj)
Requires: pypi(cryptography)
Requires: pypi(distro)
Requires: pypi(josepy)
Requires: pypi(parsedatetime)
Requires: pypi(pyrfc3339)
Requires: pypi(pytz)
Requires: pypi(setuptools)
Requires: pypi(zope.component)
Requires: pypi(zope.interface)

%description python3
python3 components for the certbot package.


%prep
%setup -q -n certbot-1.20.0
cd %{_builddir}/certbot-1.20.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1633444390
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
pushd certbot
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/certbot
cp %{_builddir}/certbot-1.20.0/LICENSE.txt %{buildroot}/usr/share/package-licenses/certbot/4bdc361ecc9ed00f502ec709aabdf54cc856b5cb
cp %{_builddir}/certbot-1.20.0/acme/LICENSE.txt %{buildroot}/usr/share/package-licenses/certbot/d095fa0d394cc9417a65aecd0d28e7d10e762f98
cp %{_builddir}/certbot-1.20.0/certbot-apache/LICENSE.txt %{buildroot}/usr/share/package-licenses/certbot/d095fa0d394cc9417a65aecd0d28e7d10e762f98
cp %{_builddir}/certbot-1.20.0/certbot-compatibility-test/LICENSE.txt %{buildroot}/usr/share/package-licenses/certbot/d095fa0d394cc9417a65aecd0d28e7d10e762f98
cp %{_builddir}/certbot-1.20.0/certbot-dns-cloudflare/LICENSE.txt %{buildroot}/usr/share/package-licenses/certbot/d095fa0d394cc9417a65aecd0d28e7d10e762f98
cp %{_builddir}/certbot-1.20.0/certbot-dns-cloudxns/LICENSE.txt %{buildroot}/usr/share/package-licenses/certbot/d095fa0d394cc9417a65aecd0d28e7d10e762f98
cp %{_builddir}/certbot-1.20.0/certbot-dns-digitalocean/LICENSE.txt %{buildroot}/usr/share/package-licenses/certbot/d095fa0d394cc9417a65aecd0d28e7d10e762f98
cp %{_builddir}/certbot-1.20.0/certbot-dns-dnsimple/LICENSE.txt %{buildroot}/usr/share/package-licenses/certbot/d095fa0d394cc9417a65aecd0d28e7d10e762f98
cp %{_builddir}/certbot-1.20.0/certbot-dns-dnsmadeeasy/LICENSE.txt %{buildroot}/usr/share/package-licenses/certbot/d095fa0d394cc9417a65aecd0d28e7d10e762f98
cp %{_builddir}/certbot-1.20.0/certbot-dns-gehirn/LICENSE.txt %{buildroot}/usr/share/package-licenses/certbot/d706715c5c263c4fcfd50231edb7889ae9711747
cp %{_builddir}/certbot-1.20.0/certbot-dns-google/LICENSE.txt %{buildroot}/usr/share/package-licenses/certbot/d095fa0d394cc9417a65aecd0d28e7d10e762f98
cp %{_builddir}/certbot-1.20.0/certbot-dns-linode/LICENSE.txt %{buildroot}/usr/share/package-licenses/certbot/d095fa0d394cc9417a65aecd0d28e7d10e762f98
cp %{_builddir}/certbot-1.20.0/certbot-dns-luadns/LICENSE.txt %{buildroot}/usr/share/package-licenses/certbot/d095fa0d394cc9417a65aecd0d28e7d10e762f98
cp %{_builddir}/certbot-1.20.0/certbot-dns-nsone/LICENSE.txt %{buildroot}/usr/share/package-licenses/certbot/d095fa0d394cc9417a65aecd0d28e7d10e762f98
cp %{_builddir}/certbot-1.20.0/certbot-dns-ovh/LICENSE.txt %{buildroot}/usr/share/package-licenses/certbot/d095fa0d394cc9417a65aecd0d28e7d10e762f98
cp %{_builddir}/certbot-1.20.0/certbot-dns-rfc2136/LICENSE.txt %{buildroot}/usr/share/package-licenses/certbot/d095fa0d394cc9417a65aecd0d28e7d10e762f98
cp %{_builddir}/certbot-1.20.0/certbot-dns-route53/LICENSE.txt %{buildroot}/usr/share/package-licenses/certbot/92170cdc034b2ff819323ff670d3b7266c8bffcd
cp %{_builddir}/certbot-1.20.0/certbot-dns-sakuracloud/LICENSE.txt %{buildroot}/usr/share/package-licenses/certbot/d706715c5c263c4fcfd50231edb7889ae9711747
cp %{_builddir}/certbot-1.20.0/certbot-nginx/LICENSE.txt %{buildroot}/usr/share/package-licenses/certbot/affa5dedd6ca7042fe64265d0c0433bc15b96f89
cp %{_builddir}/certbot-1.20.0/certbot/LICENSE.txt %{buildroot}/usr/share/package-licenses/certbot/4bdc361ecc9ed00f502ec709aabdf54cc856b5cb
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
