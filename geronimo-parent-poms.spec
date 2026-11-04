Name:		geronimo-parent-poms
Version:	1.6
Release:	17
Summary:	Parent POM files for geronimo-specs

License:	ASL 2.0
URL:		https://geronimo.apache.org/
BuildArch:	noarch
BuildSystem:	maven
BuildOption(install):	--alias org.apache.geronimo.specs:specs

# Following the parent chain all the way up ...
Source0:	http://svn.apache.org/repos/asf/geronimo/specs/tags/specs-parent-%{version}/pom.xml
Source1:	http://www.apache.org/licenses/LICENSE-2.0.txt


# Dependencies and plugins from the POM files
Provides:       geronimo-specs = %{version}-%{release}

BuildRequires:	javapackages-tools
%description
The Project Object Model files for the geronimo-specs modules.

%prep
%setup -c -T
cp -p %{SOURCE0} .
cp -p %{SOURCE1} LICENSE
%pom_remove_parent
# IDEA plugin is not really useful in Fedora
%pom_remove_plugin :maven-idea-plugin

%files -f .mfiles
%doc LICENSE
