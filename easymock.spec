Name:           easymock
Version:        3.5
Release:        5
Summary:        Easy mock objects
License:        ASL 2.0
URL:            http://www.easymock.org
Source0:        %{name}-%{version}.tar.gz
Source1:        generate-tarball.sh

Patch0001:      0001-Disable-android-support.patch
Patch0002:      0002-Unshade-cglib-and-asm.patch
Patch0003:      0003-Fix-OSGi-manifest.patch

BuildArch:      noarch

BuildRequires:  maven-local mvn(cglib:cglib) mvn(junit:junit) mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-remote-resources-plugin) mvn(org.ow2.asm:asm)
BuildRequires:  mvn(org.apache.maven.surefire:surefire-junit47) mvn(org.testng:testng)
BuildRequires:  mvn(org.apache.maven.surefire:surefire-testng) mvn(org.objenesis:objenesis)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin) mvn(org.apache:apache-jar-resource-bundle)

Obsoletes:      %{name}3 < 3.4
Provides:       %{name}3 = %{version}-%{release}
Obsoletes:      %{name}2 < 2.5.2-10


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
%autosetup -n %{name}-%{name}-%{version} -p1

%pom_remove_plugin :maven-license-plugin

rm core/src/main/java/org/easymock/internal/Android*.java
rm core/src/test/java/org/easymock/tests2/ClassExtensionHelperTest.java
%pom_disable_module test-android
%pom_remove_dep :dexmaker core

%pom_disable_module test-nodeps
%pom_remove_plugin :maven-shade-plugin core

%pom_disable_module test-integration
%pom_disable_module test-osgi

%pom_remove_plugin org.codehaus.mojo:versions-maven-plugin

%pom_remove_plugin :maven-timestamp-plugin

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
* Thu Nov 14 2019 wangye<wangye54@huawei.com> - 3.5-5
- Package init
