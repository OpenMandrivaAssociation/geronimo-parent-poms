%global genesis_version 1.5

Summary:	Parent POM files for geronimo-specs
Name:		geronimo-parent-poms
Version:	1.6
Release:	6
Group:		Development/Java
License:	ASL 2.0
Url:		http://geronimo.apache.org/
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
BuildArch:	noarch

BuildRequires:	jpackage-utils >= 1.7.3
Requires(post,postun):	jpackage-utils >= 1.7.3
# Dependencies and plugins from the POM files
Suggests:	apache-resource-bundles
Suggests:	junit
Suggests:	maven2-common-poms
Suggests:	maven2-plugin-antrun
Suggests:	maven2-plugin-assembly
Suggests:	maven2-plugin-clean
Suggests:	maven2-plugin-compiler
Suggests:	maven2-plugin-dependency
Suggests:	maven2-plugin-deploy
Suggests:	maven2-plugin-eclipse
Suggests:	maven2-plugin-enforcer
Suggests:	maven2-plugin-gpg
Suggests:	maven2-plugin-idea
Suggests:	maven2-plugin-install
Suggests:	maven2-plugin-jar
Suggests:	maven2-plugin-javadoc
Suggests:	maven2-plugin-one
Suggests:	maven2-plugin-plugin
Suggests:	maven2-plugin-pmd
Suggests:	maven2-plugin-project-info-reports
Suggests:	maven2-plugin-rar
Suggests:	maven2-plugin-remote-resources
Suggests:	maven2-plugin-site
Suggests:	maven2-plugin-source
Suggests:	maven2-plugin-stage
Suggests:	maven2-plugin-war
Suggests:	maven-archiver
Suggests:	maven-plugin-build-helper
Suggests:	maven-plugin-bundle
Suggests:	maven-plugin-jxr
Suggests:	maven-surefire-maven-plugin
Suggests:	maven-surefire-report-maven-plugin
Suggests:	maven-wagon

%description
The Project Object Model files for the geronimo-specs modules.

%prep
%setup -c -T
cp %SOURCE0 %SOURCE1 %SOURCE2 %SOURCE3 .
%patch0 -p1

%build
# Nothing to do ...

%install
install -d -m 755 %{buildroot}%{_mavenpomdir}

install -pm 644 specs-parent.pom \
	%{buildroot}%{_mavenpomdir}/JPP-geronimo-specs.pom
%add_to_maven_depmap org.apache.geronimo.specs specs %{version} JPP geronimo-specs

install -pm 644 genesis-project-config.pom \
	%{buildroot}%{_mavenpomdir}/JPP-geronimo-genesis-project-config.pom
%add_to_maven_depmap org.apache.geronimo.genesis.config project-config %{genesis_version} JPP geronimo-genesis-project-config

install -pm 644 genesis-config.pom \
	%{buildroot}%{_mavenpomdir}/JPP-geronimo-genesis-config.pom
%add_to_maven_depmap org.apache.geronimo.genesis.config config %{genesis_version} JPP geronimo-genesis-config

install -pm 644 genesis-parent.pom \
	%{buildroot}%{_mavenpomdir}/JPP-geronimo-genesis.pom
%add_to_maven_depmap org.apache.geronimo.genesis genesis %{genesis_version} JPP geronimo-genesis

%post
%update_maven_depmap

%postun
%update_maven_depmap

%files
%{_mavendepmapfragdir}/*
%{_mavenpomdir}/*.pom

