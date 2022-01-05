#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : certbot
Version  : 1.22.0
Release  : 99
URL      : https://github.com/certbot/certbot/archive/v1.22.0/certbot-1.22.0.tar.gz
Source0  : https://github.com/certbot/certbot/archive/v1.22.0/certbot-1.22.0.tar.gz
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
Requires: cloudflare
Requires: configobj
Requires: cryptography
Requires: distro
Requires: dns-lexicon
Requires: dnspython
Requires: google-api-python-client
Requires: httplib2
Requires: josepy
Requires: ndg_httpsclient
Requires: oauth2client
Requires: parsedatetime
Requires: pyOpenSSL
Requires: pyRFC3339
Requires: pyparsing
Requires: python-augeas
Requires: python-digitalocean
Requires: python-future
Requires: pytz
Requires: setuptools
Requires: zope.component
Requires: zope.interface
BuildRequires : ConfigArgParse
BuildRequires : augeas
BuildRequires : boto3
BuildRequires : buildreq-distutils3
BuildRequires : cloudflare
BuildRequires : configobj
BuildRequires : cryptography
BuildRequires : distro
BuildRequires : dns-lexicon
BuildRequires : dnspython
BuildRequires : google-api-python-client
BuildRequires : httplib2
BuildRequires : josepy
BuildRequires : ndg_httpsclient
BuildRequires : oauth2client
BuildRequires : parsedatetime
BuildRequires : py-python
BuildRequires : pyOpenSSL
BuildRequires : pyRFC3339
BuildRequires : pyparsing
BuildRequires : pypi(acme)
BuildRequires : pypi(alabaster)
BuildRequires : pypi(apacheconfig)
BuildRequires : pypi(appdirs)
BuildRequires : pypi(astroid)
BuildRequires : pypi(atomicwrites)
BuildRequires : pypi(attrs)
BuildRequires : pypi(awscli)
BuildRequires : pypi(azure_devops)
BuildRequires : pypi(babel)
BuildRequires : pypi(backcall)
BuildRequires : pypi(bcrypt)
BuildRequires : pypi(beautifulsoup4)
BuildRequires : pypi(bleach)
BuildRequires : pypi(boto3)
BuildRequires : pypi(botocore)
BuildRequires : pypi(cachecontrol)
BuildRequires : pypi(cached_property)
BuildRequires : pypi(cachetools)
BuildRequires : pypi(cachy)
BuildRequires : pypi(certbot)
BuildRequires : pypi(certifi)
BuildRequires : pypi(cffi)
BuildRequires : pypi(charset_normalizer)
BuildRequires : pypi(cleo)
BuildRequires : pypi(cloudflare)
BuildRequires : pypi(colorama)
BuildRequires : pypi(configargparse)
BuildRequires : pypi(configobj)
BuildRequires : pypi(coverage)
BuildRequires : pypi(crashtest)
BuildRequires : pypi(cryptography)
BuildRequires : pypi(cython)
BuildRequires : pypi(dataclasses)
BuildRequires : pypi(decorator)
BuildRequires : pypi(deprecated)
BuildRequires : pypi(distlib)
BuildRequires : pypi(distro)
BuildRequires : pypi(dns_lexicon)
BuildRequires : pypi(dnspython)
BuildRequires : pypi(docker)
BuildRequires : pypi(docker_compose)
BuildRequires : pypi(dockerpty)
BuildRequires : pypi(docopt)
BuildRequires : pypi(docutils)
BuildRequires : pypi(entrypoints)
BuildRequires : pypi(execnet)
BuildRequires : pypi(fabric)
BuildRequires : pypi(filelock)
BuildRequires : pypi(google_api_core)
BuildRequires : pypi(google_api_python_client)
BuildRequires : pypi(google_auth)
BuildRequires : pypi(google_auth_httplib2)
BuildRequires : pypi(googleapis_common_protos)
BuildRequires : pypi(html5lib)
BuildRequires : pypi(httplib2)
BuildRequires : pypi(idna)
BuildRequires : pypi(imagesize)
BuildRequires : pypi(importlib_metadata)
BuildRequires : pypi(importlib_resources)
BuildRequires : pypi(iniconfig)
BuildRequires : pypi(invoke)
BuildRequires : pypi(ipdb)
BuildRequires : pypi(ipython)
BuildRequires : pypi(ipython_genutils)
BuildRequires : pypi(isodate)
BuildRequires : pypi(isort)
BuildRequires : pypi(jedi)
BuildRequires : pypi(jeepney)
BuildRequires : pypi(jinja2)
BuildRequires : pypi(jmespath)
BuildRequires : pypi(josepy)
BuildRequires : pypi(jsonlines)
BuildRequires : pypi(jsonpickle)
BuildRequires : pypi(jsonschema)
BuildRequires : pypi(keyring)
BuildRequires : pypi(lazy_object_proxy)
BuildRequires : pypi(markupsafe)
BuildRequires : pypi(matplotlib_inline)
BuildRequires : pypi(mccabe)
BuildRequires : pypi(mock)
BuildRequires : pypi(msgpack)
BuildRequires : pypi(msrest)
BuildRequires : pypi(mypy)
BuildRequires : pypi(mypy_extensions)
BuildRequires : pypi(oauth2client)
BuildRequires : pypi(oauthlib)
BuildRequires : pypi(packaging)
BuildRequires : pypi(paramiko)
BuildRequires : pypi(parsedatetime)
BuildRequires : pypi(parso)
BuildRequires : pypi(pathlib2)
BuildRequires : pypi(pexpect)
BuildRequires : pypi(pickleshare)
BuildRequires : pypi(pip)
BuildRequires : pypi(pkginfo)
BuildRequires : pypi(platformdirs)
BuildRequires : pypi(pluggy)
BuildRequires : pypi(ply)
BuildRequires : pypi(poetry)
BuildRequires : pypi(poetry_core)
BuildRequires : pypi(prompt_toolkit)
BuildRequires : pypi(protobuf)
BuildRequires : pypi(ptyprocess)
BuildRequires : pypi(py)
BuildRequires : pypi(pyasn1)
BuildRequires : pypi(pyasn1_modules)
BuildRequires : pypi(pycparser)
BuildRequires : pypi(pygithub)
BuildRequires : pypi(pygments)
BuildRequires : pypi(pyjwt)
BuildRequires : pypi(pylev)
BuildRequires : pypi(pylint)
BuildRequires : pypi(pynacl)
BuildRequires : pypi(pynsist)
BuildRequires : pypi(pyopenssl)
BuildRequires : pypi(pyparsing)
BuildRequires : pypi(pyrfc3339)
BuildRequires : pypi(pyrsistent)
BuildRequires : pypi(pytest)
BuildRequires : pypi(pytest_cov)
BuildRequires : pypi(pytest_xdist)
BuildRequires : pypi(python_augeas)
BuildRequires : pypi(python_dateutil)
BuildRequires : pypi(python_digitalocean)
BuildRequires : pypi(python_dotenv)
BuildRequires : pypi(pytz)
BuildRequires : pypi(pywin32)
BuildRequires : pypi(pyyaml)
BuildRequires : pypi(readme_renderer)
BuildRequires : pypi(requests)
BuildRequires : pypi(requests_download)
BuildRequires : pypi(requests_file)
BuildRequires : pypi(requests_oauthlib)
BuildRequires : pypi(requests_toolbelt)
BuildRequires : pypi(rfc3986)
BuildRequires : pypi(rsa)
BuildRequires : pypi(s3transfer)
BuildRequires : pypi(secretstorage)
BuildRequires : pypi(semantic_version)
BuildRequires : pypi(setuptools)
BuildRequires : pypi(setuptools_rust)
BuildRequires : pypi(shellingham)
BuildRequires : pypi(six)
BuildRequires : pypi(snowballstemmer)
BuildRequires : pypi(soupsieve)
BuildRequires : pypi(sphinx)
BuildRequires : pypi(sphinx_rtd_theme)
BuildRequires : pypi(sphinxcontrib_applehelp)
BuildRequires : pypi(sphinxcontrib_devhelp)
BuildRequires : pypi(sphinxcontrib_htmlhelp)
BuildRequires : pypi(sphinxcontrib_jsmath)
BuildRequires : pypi(sphinxcontrib_qthelp)
BuildRequires : pypi(sphinxcontrib_serializinghtml)
BuildRequires : pypi(texttable)
BuildRequires : pypi(tldextract)
BuildRequires : pypi(toml)
BuildRequires : pypi(tomli)
BuildRequires : pypi(tomlkit)
BuildRequires : pypi(tox)
BuildRequires : pypi(tqdm)
BuildRequires : pypi(traitlets)
BuildRequires : pypi(twine)
BuildRequires : pypi(typed_ast)
BuildRequires : pypi(types_cryptography)
BuildRequires : pypi(types_enum34)
BuildRequires : pypi(types_ipaddress)
BuildRequires : pypi(types_mock)
BuildRequires : pypi(types_pyopenssl)
BuildRequires : pypi(types_pyrfc3339)
BuildRequires : pypi(types_python_dateutil)
BuildRequires : pypi(types_pytz)
BuildRequires : pypi(types_requests)
BuildRequires : pypi(types_setuptools)
BuildRequires : pypi(types_six)
BuildRequires : pypi(typing_extensions)
BuildRequires : pypi(uritemplate)
BuildRequires : pypi(urllib3)
BuildRequires : pypi(virtualenv)
BuildRequires : pypi(wcwidth)
BuildRequires : pypi(webencodings)
BuildRequires : pypi(websocket_client)
BuildRequires : pypi(wheel)
BuildRequires : pypi(wrapt)
BuildRequires : pypi(yarg)
BuildRequires : pypi(zipp)
BuildRequires : pypi(zope.component)
BuildRequires : pypi(zope.event)
BuildRequires : pypi(zope.hookable)
BuildRequires : pypi(zope.interface)
BuildRequires : pytest
BuildRequires : python-augeas
BuildRequires : python-digitalocean
BuildRequires : python-future
BuildRequires : pytz
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
Requires: pypi(certbot)
Requires: pypi(configargparse)
Requires: pypi(configobj)
Requires: pypi(cryptography)
Requires: pypi(distro)
Requires: pypi(josepy)
Requires: pypi(parsedatetime)
Requires: pypi(pynsist)
Requires: pypi(pyrfc3339)
Requires: pypi(pytest)
Requires: pypi(pytest_cov)
Requires: pypi(pytest_xdist)
Requires: pypi(pytz)
Requires: pypi(setuptools)
Requires: pypi(zope.component)
Requires: pypi(zope.interface)

%description python3
python3 components for the certbot package.


%prep
%setup -q -n certbot-1.22.0
cd %{_builddir}/certbot-1.22.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641400951
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
cp %{_builddir}/certbot-1.22.0/LICENSE.txt %{buildroot}/usr/share/package-licenses/certbot/4bdc361ecc9ed00f502ec709aabdf54cc856b5cb
cp %{_builddir}/certbot-1.22.0/acme/LICENSE.txt %{buildroot}/usr/share/package-licenses/certbot/d095fa0d394cc9417a65aecd0d28e7d10e762f98
cp %{_builddir}/certbot-1.22.0/certbot-apache/LICENSE.txt %{buildroot}/usr/share/package-licenses/certbot/d095fa0d394cc9417a65aecd0d28e7d10e762f98
cp %{_builddir}/certbot-1.22.0/certbot-compatibility-test/LICENSE.txt %{buildroot}/usr/share/package-licenses/certbot/d095fa0d394cc9417a65aecd0d28e7d10e762f98
cp %{_builddir}/certbot-1.22.0/certbot-dns-cloudflare/LICENSE.txt %{buildroot}/usr/share/package-licenses/certbot/d095fa0d394cc9417a65aecd0d28e7d10e762f98
cp %{_builddir}/certbot-1.22.0/certbot-dns-cloudxns/LICENSE.txt %{buildroot}/usr/share/package-licenses/certbot/d095fa0d394cc9417a65aecd0d28e7d10e762f98
cp %{_builddir}/certbot-1.22.0/certbot-dns-digitalocean/LICENSE.txt %{buildroot}/usr/share/package-licenses/certbot/d095fa0d394cc9417a65aecd0d28e7d10e762f98
cp %{_builddir}/certbot-1.22.0/certbot-dns-dnsimple/LICENSE.txt %{buildroot}/usr/share/package-licenses/certbot/d095fa0d394cc9417a65aecd0d28e7d10e762f98
cp %{_builddir}/certbot-1.22.0/certbot-dns-dnsmadeeasy/LICENSE.txt %{buildroot}/usr/share/package-licenses/certbot/d095fa0d394cc9417a65aecd0d28e7d10e762f98
cp %{_builddir}/certbot-1.22.0/certbot-dns-gehirn/LICENSE.txt %{buildroot}/usr/share/package-licenses/certbot/d706715c5c263c4fcfd50231edb7889ae9711747
cp %{_builddir}/certbot-1.22.0/certbot-dns-google/LICENSE.txt %{buildroot}/usr/share/package-licenses/certbot/d095fa0d394cc9417a65aecd0d28e7d10e762f98
cp %{_builddir}/certbot-1.22.0/certbot-dns-linode/LICENSE.txt %{buildroot}/usr/share/package-licenses/certbot/d095fa0d394cc9417a65aecd0d28e7d10e762f98
cp %{_builddir}/certbot-1.22.0/certbot-dns-luadns/LICENSE.txt %{buildroot}/usr/share/package-licenses/certbot/d095fa0d394cc9417a65aecd0d28e7d10e762f98
cp %{_builddir}/certbot-1.22.0/certbot-dns-nsone/LICENSE.txt %{buildroot}/usr/share/package-licenses/certbot/d095fa0d394cc9417a65aecd0d28e7d10e762f98
cp %{_builddir}/certbot-1.22.0/certbot-dns-ovh/LICENSE.txt %{buildroot}/usr/share/package-licenses/certbot/d095fa0d394cc9417a65aecd0d28e7d10e762f98
cp %{_builddir}/certbot-1.22.0/certbot-dns-rfc2136/LICENSE.txt %{buildroot}/usr/share/package-licenses/certbot/d095fa0d394cc9417a65aecd0d28e7d10e762f98
cp %{_builddir}/certbot-1.22.0/certbot-dns-route53/LICENSE.txt %{buildroot}/usr/share/package-licenses/certbot/92170cdc034b2ff819323ff670d3b7266c8bffcd
cp %{_builddir}/certbot-1.22.0/certbot-dns-sakuracloud/LICENSE.txt %{buildroot}/usr/share/package-licenses/certbot/d706715c5c263c4fcfd50231edb7889ae9711747
cp %{_builddir}/certbot-1.22.0/certbot-nginx/LICENSE.txt %{buildroot}/usr/share/package-licenses/certbot/affa5dedd6ca7042fe64265d0c0433bc15b96f89
cp %{_builddir}/certbot-1.22.0/certbot/LICENSE.txt %{buildroot}/usr/share/package-licenses/certbot/4bdc361ecc9ed00f502ec709aabdf54cc856b5cb
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
