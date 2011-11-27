%global genesis_version 1.5

Name:		geronimo-parent-poms
Version:	1.6
Release:	6
Summary:	Parent POM files for geronimo-specs

Group:		Development/Java
License:	ASL 2.0
URL:		http://geronimo.apache.org/

# Following the parent chain all the way up ...
# http://svn.apache.org/repos/asf/geronimo/specs/tags/specs-parent-%{version}/pom.xml
Source0:	specs-parent.pom
# http://svn.apache.org/repos/asf/geronimo/genesis/tags/genesis-%{genesis_version}/config/project-config/pom.xml
Source1:	genesis-project-config.pom
# http://svn.apache.org/repos/asf/geronimo/genesis/tags/genesis-%{genesis_version}/config/pom.xml
Source2:	genesis-config.pom
# http://svn.apache.org/repos/asf/geronimo/genesis/tags/genesis-%{genesis_version}/pom.xml
Source3:	genesis-parent.pom

# Remove dependencies from POMs that aren't yet in Fedora
Patch0:		geronimo-parent-poms-remove-dependencies.patch
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildRequires:	jpackage-utils >= 1.7.3
Requires(post):	jpackage-utils >= 1.7.3
Requires(postun):	jpackage-utils >= 1.7.3

Provides:	genesis-project-config = %{genesis_version}
Provides:	genesis-config = %{genesis_version}
Provides:	genesis-parent = %{genesis_version}

BuildArch:	noarch

# Dependencies and plugins from the POM files
Requires:	apache-resource-bundles
Requires:	junit
Requires:	maven2-common-poms
Requires:	maven2-plugin-antrun
Requires:	maven2-plugin-assembly
Requires:	maven2-plugin-clean
Requires:	maven2-plugin-compiler
Requires:	maven2-plugin-dependency
Requires:	maven2-plugin-deploy
Requires:	maven2-plugin-eclipse
Requires:	maven2-plugin-enforcer
Requires:	maven2-plugin-gpg
Requires:	maven2-plugin-idea
Requires:	maven2-plugin-install
Requires:	maven2-plugin-jar
Requires:	maven2-plugin-javadoc
Requires:	maven2-plugin-one
Requires:	maven2-plugin-plugin
Requires:	maven2-plugin-pmd
Requires:	maven2-plugin-project-info-reports
Requires:	maven2-plugin-rar
Requires:	maven2-plugin-remote-resources
Requires:	maven2-plugin-site
Requires:	maven2-plugin-source
Requires:	maven2-plugin-stage
Requires:	maven2-plugin-war
Requires:	maven-archiver
Requires:	maven-plugin-build-helper
Requires:	maven-plugin-bundle
Requires:	maven-plugin-jxr
Requires:	maven-surefire-maven-plugin
Requires:	maven-surefire-report-maven-plugin
Requires:	maven-wagon

%description
The Project Object Model files for the geronimo-specs modules.

%prep
%setup -c -T
cp %SOURCE0 %SOURCE1 %SOURCE2 %SOURCE3 .
%patch0 -p1

%build
# Nothing to do ...

%install
rm -rf $RPM_BUILD_ROOT
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}

install -pm 644 specs-parent.pom \
	$RPM_BUILD_ROOT%{_mavenpomdir}/JPP-geronimo-specs.pom
%add_to_maven_depmap org.apache.geronimo.specs specs %{version} JPP geronimo-specs

install -pm 644 genesis-project-config.pom \
	$RPM_BUILD_ROOT%{_mavenpomdir}/JPP-geronimo-genesis-project-config.pom
%add_to_maven_depmap org.apache.geronimo.genesis.config project-config %{genesis_version} JPP geronimo-genesis-project-config

install -pm 644 genesis-config.pom \
	$RPM_BUILD_ROOT%{_mavenpomdir}/JPP-geronimo-genesis-config.pom
%add_to_maven_depmap org.apache.geronimo.genesis.config config %{genesis_version} JPP geronimo-genesis-config

install -pm 644 genesis-parent.pom \
	$RPM_BUILD_ROOT%{_mavenpomdir}/JPP-geronimo-genesis.pom
%add_to_maven_depmap org.apache.geronimo.genesis genesis %{genesis_version} JPP geronimo-genesis

%post
%update_maven_depmap

%postun
%update_maven_depmap

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%{_mavendepmapfragdir}/*
%{_mavenpomdir}/*.pom



