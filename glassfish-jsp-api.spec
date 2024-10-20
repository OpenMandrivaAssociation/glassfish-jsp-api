%{?_javapackages_macros:%_javapackages_macros}
%global artifactId javax.servlet.jsp-api
%global jspspec 2.2


Name:       glassfish-jsp-api
Version:    2.3.1
Release:    4%{?dist}
Summary:    Glassfish J2EE JSP API specification

License:    (CDDL or GPLv2 with exceptions) and ASL 2.0
URL:        https://java.net/jira/browse/JSP
Source0:    %{artifactId}-%{version}.tar.xz
# no source releases, but this will generate tarball for you from an
# SVN tag
Source1:    generate_tarball.sh
Source2:    http://www.apache.org/licenses/LICENSE-2.0.txt
Source3:    http://hub.opensolaris.org/bin/download/Main/licensing/cddllicense.txt

BuildArch:  noarch

BuildRequires:  maven-local
BuildRequires:  maven-plugin-bundle
BuildRequires:  maven-source-plugin
BuildRequires:  jvnet-parent
BuildRequires:  mvn(javax.servlet:javax.servlet-api)
BuildRequires:  mvn(javax.el:javax.el-api)

%description
This project provides a container independent specification of JSP
2.2. Note that this package doesn't contain implementation of this
specification. See glassfish-jsp for one of implementations

%package javadoc
Summary:        API documentation for %{name}
BuildArch:      noarch

%description javadoc
%{summary}.

%prep
%setup -q -n %{artifactId}-%{version}
cp -p %{SOURCE2} LICENSE
cp -p %{SOURCE3} cddllicense.txt

# Submited upstream: http://java.net/jira/browse/JSP-31
sed -i "/<bundle.symbolicName>/s/-api//" pom.xml

%pom_xpath_remove "pom:dependency[pom:groupId='javax.el' or pom:groupId='javax.servlet']/pom:scope"

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE cddllicense.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE cddllicense.txt


%changelog
* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Mar 13 2014 Michael Simacek <msimacek@redhat.com> - 2.3.1-3
- Drop manual requires

* Tue Feb 25 2014 Alexander Kurtakov <akurtako@redhat.com> 2.3.1-2
- Do not require jvnet-parent.

* Thu Jan 02 2014 Michal Srb <msrb@redhat.com> - 2.3.1-1
- Update to upstream version 2.3.1

* Mon Aug 05 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.2.1-8
- Update to latest packaging guidelines

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 2.2.1-5
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Fri Oct 19 2012 Mikolaj Izdebski <mizdebsk@redhat.com> 2.2.1-4
- Change OSGi Bundle-SymbolicName to better match Eclipse needs
- Update URL
- Resolves: rhbz#868169

* Tue Sep  4 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.2.1-3
- Fix license tag
- Install license files

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Mar 21 2012 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.2.1-1
- Initial version of the package

