%define	debug_package	%{nil}

Summary:	FFmpeg based video cutter & joiner with a modern PyQt5 GUI
Name:		vidcutter
Version:	5.0.5
Release:	1
Group:		Video
License:	GPLv3+
Url:		http://vidcutter.ozmartians.com
Source0:	https://github.com/ozmartian/vidcutter/archive/%{name}-%{version}.tar.gz
BuildRequires:	python3-qt5-devel
BuildRequires:	pkgconfig(mpv)
BuildRequires:	pkgconfig(python3)
BuildRequires:	python3egg(setuptools)
Requires:	ffmpeg
Requires:	mediainfo
Requires:	mpv
Requires:	python3-qt5
Requires:	python3-qt5-opengl
Requires:	python3egg(setuptools)

%description
FFmpeg based video cutter & joiner with a modern PyQt5 GUI.
It focuses on getting the job done using tried and true tech in its arsenal
via mpv and FFmpeg.

%files
%doc README.md LICENSE
%{_bindir}/%{name}
%{py3_platsitedir}/%{name}
%{py3_platsitedir}/%{name}-%{version}-py?.?.egg-info
%{_datadir}/appdata/*.appdata.xml
%{_datadir}/applications/*.desktop
%{_datadir}/mime/packages/x-%{name}.xml
%{_datadir}/pixmaps/%{name}.svg
%{_iconsdir}/hicolor/*/apps/%{name}.png
%{_iconsdir}/hicolor/scalable/apps/%{name}.svg

#--------------------------------------------------------------

%prep
%setup -q

rm -rf %{name}.egg-info
sed -i "s/pypi/fedora/" "%{name}/__init__.py"


%build
%py3_build


%install
%py3_install

# Fix perms
chmod 0644 %{buildroot}%{_iconsdir}/hicolor/scalable/apps/vidcutter.svg

pushd %{buildroot}%{py3_platsitedir}/%{name}
find . -type f -name "*.py" -exec chmod 0755 {} \;
chmod 0644 resources.py
chmod 0644 libs/__init__.py
popd