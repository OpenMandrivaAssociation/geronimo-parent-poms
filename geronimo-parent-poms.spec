Name:		geronimo-parent-poms
Version:	1.6
Release:	17
Summary:	Parent POM files for geronimo-specs
Group:		Development/Java
License:	ASL 2.0
URL:		https://geronimo.apache.org/
BuildArch:	noarch
# Literal, so the first rpmbuild -bs records them before sysjar is installed.
BuildRequires:	maven
BuildRequires:	java-current-devel
BuildSystem:	maven
BuildOption:	validate
BuildOption(install):	--alias org.apache.geronimo.specs:specs

# Following the parent chain all the way up ...
Source0:	http://svn.apache.org/repos/asf/geronimo/specs/tags/specs-parent-%{version}/pom.xml
Source1:	http://www.apache.org/licenses/LICENSE-2.0.txt


# Dependencies and plugins from the POM files
Provides:       geronimo-specs = %{version}-%{release}

%description
The Project Object Model files for the geronimo-specs modules.

%prep
%setup -c -T
cp -p %{SOURCE0} .
cp -p %{SOURCE1} LICENSE
# genesis project-config is not packaged. This POM already has its own
# group, artifact and version.
sed -i '/<parent>/,/<\/parent>/d' pom.xml
# maven-bundle-plugin is a build extension, so Maven resolves it while
# reading the POM. Version 1.2.0 is not packaged. The manifest goal is
# not part of validate.
sed -i '/<extensions>true<\/extensions>/d' pom.xml

%files -f .mfiles
%doc LICENSE
