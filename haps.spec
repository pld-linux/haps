Summary:	Hardware Auto Probing System
Summary(pl):	Hardware Auto Probing System - system wykrywania sprz�tu
Name:		haps
Version:	20030224
Release:	0.1
License:	GPL
Group:		Base
Source0:	%{name}-%{version}.tar.gz
# Source0-md5:	65a4042b66027cfe42d59e2bf9632dbc
URL:		http://ggodlewski.host.sk/haps/
Requires(post,preun):	/sbin/chkconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Hardware Auto Probing System.

%description -l pl
Hardware Auto Probing System - system wykrywania sprz�tu.

%prep
%setup -q -n %{name}

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}/haps/{config,current}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

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
%doc AUTHORS README TODO ChangeLog README
%attr(755,root,root) /sbin/*
%dir /lib/haps
%attr(755,root,root) /lib/haps/*.so
%attr(754,root,root) /etc/rc.d/init.d/*
#%config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/*
%dir %{_sysconfdir}/haps
#%dir /etc/haps/bus
#%config(noreplace) %verify(not md5 mtime size) /etc/haps/bus/*
%dir %{_sysconfdir}/haps/filters
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/haps/filters/*
%attr(755,root,root) %{_sysconfdir}/haps/adddevice
%attr(755,root,root) %{_sysconfdir}/haps/removedevice
%attr(755,root,root) %{_sysconfdir}/haps/cut_haps
%attr(755,root,root) %{_sysconfdir}/haps/makeconfig
%{_sysconfdir}/haps/config
%{_sysconfdir}/haps/current
%{_sysconfdir}/haps/templates
%{_sysconfdir}/haps/bioses
%{_sysconfdir}/haps/pcitable
