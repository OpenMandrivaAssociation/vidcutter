%define	debug_package	%{nil}

Summary:	FFmpeg based video cutter & joiner with a modern PyQt5 GUI
Name:		vidcutter
Version:	6.0.5
Release:	1
Group:		Video
License:	GPLv3+
Url:		http://vidcutter.ozmartians.com
Source0:	https://github.com/ozmartian/vidcutter/archive/%{version}/vidcutter-%{version}.tar.gz
BuildRequires:	python-qt5-devel
BuildRequires:	pkgconfig(mpv)
BuildRequires:	pkgconfig(python)
BuildRequires:	python3egg(setuptools)
Requires:	ffmpeg
#Fixed but still in contrib, so make it recommends inteed rq
Recommends:	mediainfo
Requires:	mpv
Requires:	python-qt5
Requires:	python-qt5-opengl
Requires:	python3egg(setuptools)

%description
FFmpeg based video cutter & joiner with a modern PyQt5 GUI.
It focuses on getting the job done using tried and true tech in its arsenal
via mpv and FFmpeg.

%files
%doc README.md LICENSE CHANGELOG
%{_bindir}/%{name}
%{py3_platsitedir}/%{name}
%{py3_platsitedir}/%{name}-%{version}-py?.?.egg-info
#{_datadir}/appdata/*.appdata.xml
%{_datadir}/applications/*.desktop
#{_datadir}/mime/packages/x-%{name}.xml
#_datadir}/pixmaps/%{name}.svg
%{_iconsdir}/hicolor/*/apps/*
#{_iconsdir}/hicolor/scalable/apps/%{name}.svg
%{_datadir}/metainfo/com.ozmartians.VidCutter.appdata.xml
%{_datadir}/mime/packages/com.ozmartians.VidCutter.xml

#--------------------------------------------------------------

%prep
%setup -q

rm -rf %{name}.egg-info
sed -i "s/pypi/fedora/" "%{name}/__init__.py"


%build
%py_build


%install
%py_install

pushd %{buildroot}%{py3_platsitedir}/%{name}
find . -type f -name "*.py" -exec chmod 0755 {} \;
chmod 0644 resources.py
chmod 0644 libs/__init__.py
popd
