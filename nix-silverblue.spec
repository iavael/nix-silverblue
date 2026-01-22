Name:     nix-silverblue
Version:  0.1.7
Release:  1%{?dist}
Summary:  Tools for nix/guix integration in Fedora Atomic distros
License:  Apache2.0
URL:      https://github.com/iavel/nix-silverblue
# Source0:  https://github.com/iavael/#{name}/archive/v#{version}.tar.gz
Source0:  %{name}-%{version}.tar.gz
Source1:  sysusers/guix.conf
Source2:  sysusers/nix.conf

BuildArch: noarch

BuildRequires:    make
BuildRequires:    systemd-rpm-macros

Requires(post):   systemd
Requires(preun):  systemd
Requires(postun): systemd

# This ensures that the *-selinux package and all its dependencies are not pulled
# into containers and other systems that do not use SELinux
Requires:         (%{name}-selinux if selinux-policy-targeted)

%description

%package selinux
Summary: Tools for nix/guix integration in Fedora Atomic distros - selinux policies
BuildArch:        noarch

Requires:         selinux-policy-targeted
Requires(post):   selinux-policy-targeted
BuildRequires:    selinux-policy-devel

#selinux_requires
Requires:         selinux-policy
BuildRequires:    pkgconfig(systemd)
BuildRequires:    selinux-policy
BuildRequires:    selinux-policy-devel
Requires(post):   selinux-policy-base
Requires(post):   libselinux-utils
Requires(post):   policycoreutils
Requires(post):   policycoreutils-python-utils

%description selinux

%prep
%setup -q -n %{name}-%{version}

%build

%check

%install
make install DESTDIR=%{buildroot}/%{_prefix} SYSCONFDIR=%{buildroot}/%{_sysconfdir}

%pre
%sysusers_create_package guix %SOURCE1
%sysusers_create_package nix %SOURCE2

%preun
%systemd_preun var-guix.mount gnu-store.mount nix-store.mount

%pre selinux
%selinux_relabel_pre

%post selinux
%selinux_modules_install %{_datadir}/selinux/packages/targeted/guix-daemon.cil

%{_sbindir}/semanage fcontext -a -t etc_t '/gnu/store/[^/]+/etc(/.*)?'
%{_sbindir}/semanage fcontext -a -t lib_t '/gnu/store/[^/]+/lib(/.*)?'
%{_sbindir}/semanage fcontext -a -t systemd_unit_file_t '/gnu/store/[^/]+/lib/systemd/system(/.*)?'
%{_sbindir}/semanage fcontext -a -t man_t '/gnu/store/[^/]+/man(/.*)?'
%{_sbindir}/semanage fcontext -a -t bin_t '/gnu/store/[^/]+/s?bin(/.*)?'
%{_sbindir}/semanage fcontext -a -t usr_t '/gnu/store/[^/]+/share(/.*)?'
%{_sbindir}/semanage fcontext -a -t var_run_t '/var/guix/daemon-socket(/.*)?'
%{_sbindir}/semanage fcontext -a -t usr_t '/var/guix/profiles(/per-user/[^/]+)?/[^/]+'

%{_sbindir}/semanage fcontext -a -t etc_t '/nix/store/[^/]+/etc(/.*)?'
%{_sbindir}/semanage fcontext -a -t lib_t '/nix/store/[^/]+/lib(/.*)?'
%{_sbindir}/semanage fcontext -a -t systemd_unit_file_t '/nix/store/[^/]+/lib/systemd/system(/.*)?'
%{_sbindir}/semanage fcontext -a -t man_t '/nix/store/[^/]+/man(/.*)?'
%{_sbindir}/semanage fcontext -a -t bin_t '/nix/store/[^/]+/s?bin(/.*)?'
%{_sbindir}/semanage fcontext -a -t usr_t '/nix/store/[^/]+/share(/.*)?'
%{_sbindir}/semanage fcontext -a -t var_run_t '/nix/var/nix/daemon-socket(/.*)?'
%{_sbindir}/semanage fcontext -a -t usr_t '/nix/var/nix/profiles(/per-user/[^/]+)?/[^/]+'

%postun selinux
if [ $1 -eq 0 ]; then
    %selinux_modules_uninstall guix-daemon

    %{_sbindir}/semanage fcontext -d -t etc_t '/gnu/store/[^/]+/etc(/.*)?'
    %{_sbindir}/semanage fcontext -d -t lib_t '/gnu/store/[^/]+/lib(/.*)?'
    %{_sbindir}/semanage fcontext -d -t systemd_unit_file_t '/gnu/store/[^/]+/lib/systemd/system(/.*)?'
    %{_sbindir}/semanage fcontext -d -t man_t '/gnu/store/[^/]+/man(/.*)?'
    %{_sbindir}/semanage fcontext -d -t bin_t '/gnu/store/[^/]+/s?bin(/.*)?'
    %{_sbindir}/semanage fcontext -d -t usr_t '/gnu/store/[^/]+/share(/.*)?'
    %{_sbindir}/semanage fcontext -d -t var_run_t '/var/guix/daemon-socket(/.*)?'
    %{_sbindir}/semanage fcontext -d -t usr_t '/var/guix/profiles(/per-user/[^/]+)?/[^/]+'

    %{_sbindir}/semanage fcontext -d -t etc_t '/nix/store/[^/]+/etc(/.*)?'
    %{_sbindir}/semanage fcontext -d -t lib_t '/nix/store/[^/]+/lib(/.*)?'
    %{_sbindir}/semanage fcontext -d -t systemd_unit_file_t '/nix/store/[^/]+/lib/systemd/system(/.*)?'
    %{_sbindir}/semanage fcontext -d -t man_t '/nix/store/[^/]+/man(/.*)?'
    %{_sbindir}/semanage fcontext -d -t bin_t '/nix/store/[^/]+/s?bin(/.*)?'
    %{_sbindir}/semanage fcontext -d -t usr_t '/nix/store/[^/]+/share(/.*)?'
    %{_sbindir}/semanage fcontext -d -t var_run_t '/nix/var/nix/daemon-socket(/.*)?'
    %{_sbindir}/semanage fcontext -d -t usr_t '/nix/var/nix/profiles(/per-user/[^/]+)?/[^/]+'

fi

%posttrans selinux
%selinux_relabel_post

%files
%doc COPYING
%{_sbindir}/restorecon-guix
%{_sbindir}/restorecon-nix
%{_sbindir}/mkrootdir
%{_sbindir}/mkrootlink

%{_sysconfdir}/profile.d/guix.sh
%{_sysconfdir}/profile.d/nix.sh
%{_sysconfdir}/nix/nix.conf

%{_sysusersdir}/guix.conf
%{_sysusersdir}/nix.conf

%{_unitdir}/mkrootlink@.service
%{_unitdir}/mkrootdir@.service
%{_unitdir}/gnu-store.mount
%{_unitdir}/nix-store.mount
%{_unitdir}/var-guix.mount

%{_datadir}/nix-silverblue/systemd/Makefile
%{_datadir}/nix-silverblue/systemd/gnu.mount
%{_datadir}/nix-silverblue/systemd/nix.mount
%{_datadir}/nix-silverblue/systemd/guix-daemon.service
%{_datadir}/nix-silverblue/systemd/nix-daemon.service
%{_datadir}/nix-silverblue/systemd/nix-daemon.socket

%files selinux
%{_datadir}/selinux/packages/targeted/guix-daemon.cil
%ghost %verify(not md5 size mode mtime) %{_sharedstatedir}/selinux/targeted/active/modules/200/guix-daemon

%changelog
* Thu Jan 22 2026 Iavael 0.1.7-1
- Fix packaging

* Thu Jan 22 2026 Iavael 0.1.6-1
- Fix selinux packaging (905853+iavael@users.noreply.github.com)

* Thu Jan 22 2026 Iavael 0.1.5-1
- Improve selinux support (905853+iavael@users.noreply.github.com)
- Fix systemd .wants deps (905853+iavael@users.noreply.github.com)
- Add copilot-instructions.md for GitHub Copilot coding agent
  (198982749+Copilot@users.noreply.github.com)

* Thu Nov 28 2024 Iavael 0.1.4-1
- Split makefiles and add nix config (905853+iavael@users.noreply.github.com)
- Switch tito builder to mock (905853+iavael@users.noreply.github.com)
- Add buildusers to buildgroups fixes #2
  (905853+iavael@users.noreply.github.com)

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
