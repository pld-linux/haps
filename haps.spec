Summary:	Hardware Auto Probing System
Summary(pl):	Hardware Auto Probing System - system wykrywania sprzêtu
Name:		haps
Version:	20030309
Release:	0.1
License:	GPL
Group:		Base
Source0:	http://ggodlewski.host.sk/haps/%{name}-%{version}.tar.gz
URL:		http://ggodlewski.host.sk/haps/
Requires(post,preun):	/sbin/chkconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Hardware Auto Probing System.

%description -l pl
Hardware Auto Probing System - system wykrywania sprzêtu.

%prep
%setup -q -n %{name}

%build
rm -f missing
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/haps/{config,current}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/chkconfig --add haps
if [ -f /var/lock/subsys/haps ]; then
	/etc/rc.d/init.d/haps restart >&2
else
	echo "Run \"/etc/rc.d/init.d/haps start\" to start haps." >&2
fi

%preun
if [ "$1" = "0" ]; then
	if [ -f /var/lock/subsys/haps ]; then
		/etc/rc.d/init.d/haps stop >&2
	fi
	/sbin/chkconfig --del haps
fi

%files
%defattr(644,root,root,755)
#%doc ChangeLog README
%attr(755,root,root) /sbin/*
%attr(644,root,root) /lib/*
%attr(754,root,root) /etc/rc.d/init.d/*
#%attr(644,root,root) %config(noreplace) %verify(not size mtime md5) /etc/sysconfig/*
%dir /etc/haps
#%dir /etc/haps/bus
#%attr(644,root,root) %config(noreplace) %verify(not size mtime md5) /etc/haps/bus/*
%dir /etc/haps/filters
%attr(644,root,root) %config(noreplace) %verify(not size mtime md5) /etc/haps/filters/*
%attr(755,root,root) /etc/haps/adddevice
%attr(755,root,root) /etc/haps/removedevice
%attr(755,root,root) /etc/haps/cut_haps
%attr(755,root,root) /etc/haps/makeconfig
/etc/haps/config
/etc/haps/current
/etc/haps/templates
%attr(644,root,root) /etc/haps/bioses
%attr(644,root,root) /etc/haps/pcitable
