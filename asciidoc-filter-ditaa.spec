# TODO: use system ditaa
Summary:	ditaa filter for AsciiDoc
Summary(pl.UTF-8):	Filtr ditaa do narzędzia AsciiDoc
Name:		asciidoc-filter-ditaa
Version:	1.1
Release:	1
License:	GPL v2
Group:		Applications/Graphics
#Source0Download: http://code.google.com/p/asciidoc-ditaa-filter/downloads/list
Source0:	http://asciidoc-ditaa-filter.googlecode.com/files/ditaa-filter-%{version}.zip
# Source0-md5:	782ed6a9832e60bf6be4ea2446ec63c7
URL:		http://code.google.com/p/asciidoc-ditaa-filter/
#BuildRequires:	sed >= 4.0
BuildRequires:	unzip
Requires:	asciidoc >= 8.6.3
Requires:	jre >= 1.5
#Requires:	ditaa >= 0.9
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ditaa is a small command-line utility written in Java, that can
convert diagrams drawn using ASCII art (drawings that contain
characters that resemble lines like | / - ), into proper bitmap
graphics.

Using the AsciiDoc ditaa filter, ASCII line art can be embedded into
AsciiDoc documents and processed as PNG bitmap graphics.

%description -l pl.UTF-8
ditaa to małe narzędzie działające z linii poleceń, napisane w Javie,
potrafiące konwertować diagramy rysowane przy użyciu ASCII art
("rysunków" zawierających znaki przypominające linie, takie jak | / -)
we właściwą grafikę bitmapową.

Przy użyciu filtra ditaa do narzędzia AsciiDoc można osadzać rysunki
ASCII art w dokumentach AsciiDoc, a następnie przetwarzać je w grafikę
bitmapową PNG.

%prep
%setup -q -c

sed -i -e '1s,#! /usr/bin/env python,#!/usr/bin/python,' ditaa2img.py

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/asciidoc/filters/ditaa

install ditaa2img.py $RPM_BUILD_ROOT/etc/asciidoc/filters/ditaa
cp -p ditaa-filter.conf ditaa0_9.jar $RPM_BUILD_ROOT/etc/asciidoc/filters/ditaa

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc asciidoc-ditaa-readme.{txt,html} images
%dir /etc/asciidoc/filters/ditaa
%attr(755,root,root) /etc/asciidoc/filters/ditaa/ditaa2img.py
/etc/asciidoc/filters/ditaa/ditaa-filter.conf
/etc/asciidoc/filters/ditaa/ditaa0_9.jar
