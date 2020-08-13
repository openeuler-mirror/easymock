Name:                easymock
Version:             3.6
Release:             1
Summary:             Easy mock objects
License:             ASL 2.0
URL:                 http://www.easymock.org
Source0:             https://github.com/easymock/easymock/archive/easymock-%{version}.tar.gz
Patch1:              0001-Disable-android-support.patch
Patch2:              0002-Unshade-cglib-and-asm.patch
Patch3:              0003-Fix-OSGi-manifest.patch
BuildArch:           noarch
BuildRequires:       maven-local mvn(cglib:cglib) mvn(junit:junit)
BuildRequires:       mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:       mvn(org.apache.maven.plugins:maven-remote-resources-plugin)
BuildRequires:       mvn(org.apache.maven.surefire:surefire-junit47)
BuildRequires:       mvn(org.apache.maven.surefire:surefire-testng)
BuildRequires:       mvn(org.codehaus.mojo:build-helper-maven-plugin) mvn(org.objenesis:objenesis)
BuildRequires:       mvn(org.ow2.asm:asm) mvn(org.testng:testng)
BuildRequires:       mvn(org.apache:apache-jar-resource-bundle)
Obsoletes:           %{name}3 < 3.4
Provides:            %{name}3 = %{version}-%{release}
Obsoletes:           %{name}2 < 2.5.2-10
%description
EasyMock provides Mock Objects for interfaces in JUnit tests by generating
them on the fly using Java's proxy mechanism. Due to EasyMock's unique style
of recording expectations, most refactorings will not affect the Mock Objects.
So EasyMock is a perfect fit for Test-Driven Development.

%package        help
Summary:        API documentation for easymock
Provides:       %{name}-javadoc = %{version}-%{release}
Obsoletes:      %{name}-javadoc < %{version}-%{release}

%description    help
The help for easymock to use.

%prep
%autosetup  -n %{name}-%{name}-%{version} -p1
find -name '*.jar' -delete
find -name '*.class' -delete
rm -rf website/*
%pom_remove_plugin :maven-license-plugin
%pom_remove_plugin :maven-timestamp-plugin
%pom_remove_plugin :maven-enforcer-plugin
%pom_remove_plugin :animal-sniffer-maven-plugin
%pom_remove_plugin :animal-sniffer-maven-plugin core
rm core/src/main/java/org/easymock/internal/Android*.java
rm core/src/test/java/org/easymock/tests2/ClassExtensionHelperTest.java
%pom_disable_module test-android
%pom_remove_dep :dexmaker core
%pom_disable_module test-nodeps
%pom_remove_plugin :maven-shade-plugin core
%pom_disable_module test-integration
%pom_disable_module test-osgi
%pom_remove_plugin org.codehaus.mojo:versions-maven-plugin
%mvn_file ":easymock{*}" easymock@1 easymock3@1
%pom_xpath_remove pom:extensions

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%license core/LICENSE.txt

%files help -f .mfiles-javadoc
%license core/LICENSE.txt

%changelog
* Thu Aug 13 2020 yanan li <liyanan032@huawei.com> - 3.6-1
- Update to 3.6-1

* Tue Jan 21 2020 wutao <wutao61@huawei.com> - 3.5-6
- Type:bugfix
- ID:NA
- SUG:NA
- DESC: modify spec

* Thu Nov 14 2019 wangye<wangye54@huawei.com> - 3.5-5
- Package init
