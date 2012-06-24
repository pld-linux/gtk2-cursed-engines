Summary:	Theme engine for cursed GTK+
Summary(pl):	Silnik motyw�w GTK+ opartego na curses
Name:		gtk2-cursed-engines
Version:	2.2.0
Release:	1
Copyright:	GPL
Group:		Libraries
Source0:	http://zemljanka.sourceforge.net/cursed/current/gtk-cursed-engines-%{version}.tar.gz
# Source0-md5:	03ba589a40d3c8651a71c79fbdf54cdd
Requires:	gtk2-cursed >= 2.2.0
BuildRequires:	gtk2-cursed-devel >= 2.2.0
URL:		http://zemljanka.sf.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The gtk2-cursed-engines package contains Cursed Theme (no graphics,
only text symbols) for cursed Gtk.

%description -l pl
Pakiet gtk2-cursed-engines zawiera motyw "Cursed" (bez grafiki, tylko
symbole tekstowe) dla GTK+ opartego na curses.

%prep
%setup -q -n gtk-cursed-engines-%{version}

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%makeinstall

# remove backup files that shouldn't be here.  Fix me.
find $RPM_BUILD_ROOT%{_datadir}/themes -name \*~ | xargs rm -rvf

# No, we don't need to package these either
find $RPM_BUILD_ROOT%{_datadir}/themes -type d -name ".xvpics" | xargs rm -rvf

# sanitize permissions
find $RPM_BUILD_ROOT%{_datadir}/themes -type d -exec chmod 755 {} \;
find $RPM_BUILD_ROOT%{_datadir}/themes -type f -name "*.png" -exec chmod 644 {} \;
find $RPM_BUILD_ROOT%{_datadir}/themes -name "gtkrc*" -perm +111 -exec chmod 644 {} \;

find $RPM_BUILD_ROOT%{_libdir} -name "*.la" | xargs rm 

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING README ChangeLog

%attr (755,root,root) %{_libdir}/gtk-cursed-2.0/*/engines/*.so
%dir %{_libdir}/gtk-cursed-2.0
%dir %{_libdir}/gtk-cursed-2.0/*
%dir %{_libdir}/gtk-cursed-2.0/*/engines
%{_libdir}/pkgconfig
%{_datadir}/themes
