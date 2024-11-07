Name:		nix-silverblue
Version:	0.1.3
Release:	1%{?dist}
Summary:	Tools for nix/guix integration in Fedora Atomic distrols
License:	Apache2.0
URL:		https://github.com/iavel/nix-silverblue
# Source0:	https://github.com/iavael/#{name}/archive/v#{version}.tar.gz
Source0:	%{name}-%{version}.tar.gz

BuildArch:	noarch

BuildRequires:	make
Requires:	make cpp
Requires:	policycoreutils-python-utils policycoreutils

%description

%prep
%setup -q -n %{name}-%{version}

%build

%check

%install
make install DESTDIR=$RPM_BUILD_ROOT/usr SYSCONFDIR=$RPM_BUILD_ROOT/etc

%files
%doc COPYING
%{_sbindir}/restorecon-guix
%{_sbindir}/restorecon-nix
%{_sbindir}/mkrootdir
%{_sbindir}/mkrootlink

%{_sysconfdir}/profile.d/guix.sh
%{_sysconfdir}/profile.d/nix.sh

%{_sysusersdir}/guix.conf
%{_sysusersdir}/nix.conf

%{_unitdir}/mkrootlink@.service
%{_unitdir}/mkrootdir@.service
%{_unitdir}/gnu-store.mount
%{_unitdir}/nix-store.mount
%{_unitdir}/guix-daemon.service.wants/gnu-store.mount
%{_unitdir}/guix-daemon.service.wants/var-guix.mount
%{_unitdir}/nix-daemon.service.wants/nix-store.mount
%{_unitdir}/var-guix.mount

%{_datadir}/nix-silverblue/selinux/guix-daemon.cil
%{_datadir}/nix-silverblue/selinux/fixseguix
%{_datadir}/nix-silverblue/selinux/fixsenix

%{_datadir}/nix-silverblue/systemd/Makefile
%{_datadir}/nix-silverblue/systemd/gnu.mount
%{_datadir}/nix-silverblue/systemd/nix.mount
%{_datadir}/nix-silverblue/systemd/guix-daemon.service
%{_datadir}/nix-silverblue/systemd/nix-daemon.service
%{_datadir}/nix-silverblue/systemd/nix-daemon.socket

%changelog
* Fri Nov 08 2024 Iavael 0.1.3-1
- Added creation of system users and fixed typos
  (905853+iavael@users.noreply.github.com)

* Thu Nov 07 2024 Iavael 0.1.2-1
- Added shell profiles and made minor improvements
  (905853+iavael@users.noreply.github.com)

* Thu Nov 07 2024 Iavael 0.1.1-1
- Improve restorecon scripts (905853+iavael@users.noreply.github.com)

* Thu Nov 07 2024 Iavael 0.1.0-1
- Initial release
