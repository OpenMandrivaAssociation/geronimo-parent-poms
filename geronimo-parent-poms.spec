Name:		geronimo-parent-poms
Version:	1.6
Release:	18
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
# Children inherit build/plugins. The bundle manifest goal runs in their
# package phase, and the jar plugin then reads a manifest that was never
# written. Neither plugin is packaged.
python - <<'PY'
import re
from pathlib import Path
path = Path("pom.xml")
text = path.read_text()
text, n = re.subn(
	r"\s*<plugin>\s*<groupId>org\.apache\.felix</groupId>\s*<artifactId>maven-bundle-plugin</artifactId>.*?</plugin>",
	"",
	text,
	count=1,
	flags=re.S,
)
if n != 1:
	raise SystemExit(f"expected to remove maven-bundle-plugin, removed {n}")
text, n = re.subn(
	r"\s*<manifestFile>.*?</manifestFile>",
	"",
	text,
	count=1,
	flags=re.S,
)
if n != 1:
	raise SystemExit(f"expected to remove manifestFile, removed {n}")
path.write_text(text)
PY

%files -f .mfiles
%doc LICENSE
