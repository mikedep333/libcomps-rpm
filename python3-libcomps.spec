%define orig_name libcomps
Name:           python3-libcomps
Version:        0.1.8
Release:        12%{?dist}
Summary:        Python 3 bindings for libcomps library

License:        GPLv2+
URL:            https://github.com/rpm-software-management/libcomps
Source0:        %{url}/archive/%{orig_name}-%{version}/%{orig_name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  libxml2-devel
BuildRequires:  check-devel
BuildRequires:  expat-devel

%description
Python3 bindings for libcomps library.

%package -n python%{python3_pkgversion}-%{orig_name}
Summary:        %{summary}
BuildRequires:  python3-devel
%{?python_provide:%python_provide python3-%{orig_name}}
Requires:       %{orig_name}% = %{version}
Requires:       %{orig_name}% >= %{version}-%{release}

%description -n python%{python3_pkgversion}-%{orig_name}
%{description}

%prep
%autosetup -n %{orig_name}-%{orig_name}-%{version}

mkdir build-py3

%build
pushd build-py3
# Workaround the limitations of EL7's RPM macros and/or old version of cmake
  %cmake ../libcomps/ -DPYTHON_DESIRED:STRING=3 -DPYTHON_INCLUDE_DIR=/usr/include/python3.6m -DPYTHON_LIBRARY=/usr/lib64/libpython3.6m.so
  %make_build
popd

%install
pushd build-py3
  %make_install
popd

%check
pushd build-py3
  make pytest
popd

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -n python%{python3_pkgversion}-%{orig_name}
%license COPYING
%doc README.md
%exclude %{_libdir}/%%{orig_name}.so.*

#%%files devel
%exclude %{_libdir}/%%{orig_name}.so
%exclude %{_includedir}/%%{orig_name}/
#
#%%files doc
#%%doc build/docs/libcomps-doc/html
#
#%%files -n python-%%{name}-doc
#%%doc build/src/python/docs/html
#
#%%files -n python2-%%{name}
#%%{python2_sitearch}/%%{name}/
#
#%%files -n python3-%%{name}
%{python3_sitearch}/%{orig_name}/

%changelog
* Tue Nov 12 2019 Mike DePaulo <mikedep333@gmail.com> - 0.1.8-12
- Convert to python3 bindings-only package for EPEL7
- Move libcomps.spec to root dir to fix copr / rpkg SRPM builds
- Adapt to the example of python3-rpm (the pythonXY RPM name in particular)

* Mon Jun 11 2018 Marek Blaha <mblaha@redhat.com> - 0.1.8-12
- Build for RHEL 7
- Do not use %%ldconfig_scriptlets

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.8-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 31 2018 Igor Gnatenko <ignatenko@redhat.com> - 0.1.8-10
- Switch to %%ldconfig_scriptlets

* Tue Nov 07 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.8-9
- Use better Obsoletes for platform-python

* Fri Nov 03 2017 Igor Gnatenko <ignatenko@redhat.com> - 0.1.8-8
- Remove platform-python subpackage

* Fri Sep 01 2017 Igor Gnatenko <ignatenko@redhat.com> - 0.1.8-7
- Disable platform python on old releases

* Thu Aug 10 2017 Lumír Balhar <lbalhar@redhat.com> - 0.1.8-6
- Add Platform Python subpackage (https://fedoraproject.org/wiki/Changes/Platform_Python_Stack)

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Dec 13 2016 Stratakis Charalampos <cstratak@redhat.com> - 0.1.8-2
- Rebuild for Python 3.6

* Thu Sep 22 2016 Igor Gnatenko <ignatenko@redhat.com> - 0.1.8-1
- Update to 0.1.8

* Tue Aug 09 2016 Igor Gnatenko <ignatenko@redhat.com> - 0.1.7-6
- Add %%{?system_python_abi}

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.7-5
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Tue Apr 12 2016 Igor Gnatenko <ignatenko@redhat.com> - 0.1.7-4
- Adopt to new packaging guidelines
- Use %%license macro
- Fix file ownerships

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Oct 14 2015 Robert Kuska <rkuska@redhat.com> - 0.1.7-2
- Rebuilt for Python3.5 rebuild

* Thu Jul 02 2015 Jindrich Luza <jluza@redhat.com> 0.1.7
- added langpacks to union process
- comps DOCTYPE read-write-read fix
- support biarchonly attribute
- fixed rhbz#1073885 rhbz#1073890 rhbz#1073907 rhbz#1073979
- fix rhbz#1073079
- comps_*_match() now support fnmatching
- added libpycomps.MATCH_IGNORECASE as matching flag
- added group.packages_match
- added comps.groups_match, comps.categories_match, comps.entironments_match
- PyCOMPS_Package hash
- cmake-2.6, python-2.6, RHEL-6 compatible
- '_arch' attribute change to 'arch'
- empty 'arch' attribute will be ommited from output from now

* Wed Jan 29 2014 Jindrich Luza <jluza@redhat.com> 0.1.6
- version bumped
- added libcomps.MDict.keys()
-         libcomps.MDict.values()
-         libcomps.MDict.items()
-         libcomps.MDict.clear()
-         libcomps.MDict.update()
-         libcomps.MDict.copy()
- COMPS_List replaced with COMPS_HSList
- added missing basearchonly to DocGroupPackage
- python3/CMakeLists.txt fixed
- added explicit attributes support for xml options
- added arch_filter test for python
- insert method in libcomps.Sequence
- Unioning is now accomplished with replace x append policy
- Weaker package equality check (comparing only name now)
- Fixed leeks in unioning
- modified test_merge_comps test_libcomps
- dictionaries are now storing keys in alphabetical order
- comps parser redesigned
- change python/tests directory composition
- added elem attributes check in parser
- xml output '_arch' attribute support
- parser and xml output defaults options for specify defaults values
- comps object validation in python
- added validity checker before append/set object to list (python only)
- .validate() method
- added libcomps.Dict.keys
-         libcomps.Dict.values
-         libcomps.Dict.items
-         libcomps.Dict.clear
-         libcomps.Dict.update
-         libcomps.Dict.copy
- added xml output options (comps.xml_str([options = {}]), comps.xml_f(options = {}))

* Wed Oct 23 2013 Jindrich Luza <jluza@redhat.com> 0.1.4-4
- group.uservisible is true by default now.
- fixed comps_mobjradix parent node problem
- implemented bindings for blacklist, whiteout and langpacks
- COMPS_Logger redesigned

* Tue Oct 08 2013 Jindrich Luza <jluza@redhat.com> 0.1.5
- version bump
- PyCOMPS_Sequence.__getitem__["objectid"] implemented for libcomps.GroupList, libcomps.CategoryList, libcomps.EnvList
- added missing files
- missing display_order fix for libcomps.Environment

* Tue Oct 01 2013 Jindrich Luza <jluza@redhat.com> 0.1.4
- added missing files
- architectural redesign finished
- fixed #1003986 by Gustavo Luiz Duarte guidelines (but not tested on ppc)
- fixed bug #1000449
- fixed bug #1000442
- added GroupId.default test
- some minor unreported bugs discovered during testing fixed
- finished default attribute support in groupid object
- Comps.get_last_parse_errors and Comps.get_last_parse_log has been renamed
-   as Comps.get_last_errors and Comps.get_last_log
- version bumped. Python bindings is now easier.
- added missing files

* Tue Aug 20 2013 Jindrich Luza <jluza@redhat.com> 0.1.3
- finished default attribute support in groupid object
- Comps.get_last_parse_errors and Comps.get_last_parse_log has been renamed
-   as Comps.get_last_errors and Comps.get_last_log
- finished default attribute support in groupid object
- Comps.get_last_parse_errors and Comps.get_last_parse_log has been renamed
-   as Comps.get_last_errors and Comps.get_last_log

* Thu Jul 18 2013 Jindrich Luza <jluza@redhat.com> 0.1.2
- automatic changelog system
- fixed issue #14
- libcomps.Dict is now behave more like python dict. Implemented iter(libcomps.Dict)
- libcomps.iteritems() and libcomps.itervalues()
- remaked error reporting system.
-     libcomps.Comps.fromxml_f and libcomps.Comps.fromxml_str now return
-     -1, 0 or 1. 0 means parse procedure completed without any problem,
-     1 means there's some errors or warnings but not fatal. -1 indicates
-     fatal error problem (some results maybe given, but probably incomplete
-     and invalid)
- errors catched during parsing can be obtained by calling
-     libcomps.Comps.get_last_parse_errors
- all log is given by
-     libcomps.Comps.get_last_parse_log
- prop system complete
- fixed issue 1
- fixed issue 3
- added <packagereq requires=...> support
- new prop system in progress....
- separated doc package
- some minor fixes in CMakeFiles
- improved integrated tests

* Tue Jun 25 2013 Jindrich Luza <jluza@redhat.com> 0.1.1-1
- Automatic commit of package [libcomps] release [0.1.1-1].

