.PHONY: default install

default: ;

install:
	install -d $(DESTDIR)/sbin
	install -p -m 0755 src/restorecon-guix $(DESTDIR)/sbin/restorecon-guix
	install -p -m 0755 src/restorecon-nix $(DESTDIR)/sbin/restorecon-nix
	install -p -m 0755 src/mkrootdir $(DESTDIR)/sbin/mkrootdir
	install -p -m 0755 src/mkrootlink $(DESTDIR)/sbin/mkrootlink

	install -d $(DESTDIR)/lib/systemd/system/
	install -p -m 0644 systemd/mkrootlink@.service $(DESTDIR)/lib/systemd/system/mkrootlink@.service
	install -p -m 0644 systemd/mkrootdir@.service $(DESTDIR)/lib/systemd/system/mkrootdir@.service
	install -p -m 0644 systemd/gnu-store.mount $(DESTDIR)/lib/systemd/system/gnu-store.mount
	install -p -m 0644 systemd/nix-store.mount $(DESTDIR)/lib/systemd/system/nix-store.mount
	install -p -m 0644 systemd/var-guix.mount $(DESTDIR)/lib/systemd/system/var-guix.mount
	install -d $(DESTDIR)/lib/systemd/system/guix-daemon.service.wants/
	install -d $(DESTDIR)/lib/systemd/system/nix-daemon.service.wants/
	install -p -m 0644 systemd/guix-daemon.service.wants/gnu-store.mount $(DESTDIR)/lib/systemd/system/guix-daemon.service.wants/gnu-store.mount
	install -p -m 0644 systemd/guix-daemon.service.wants/var-guix.mount $(DESTDIR)/lib/systemd/system/guix-daemon.service.wants/var-guix.mount
	install -p -m 0644 systemd/nix-daemon.service.wants/nix-store.mount $(DESTDIR)/lib/systemd/system/nix-daemon.service.wants/nix-store.mount

	install -d $(DESTDIR)/share/nix-silverblue

	install -d $(DESTDIR)/share/nix-silverblue/selinux
	install -p -m 0755 selinux/fixseguix $(DESTDIR)/share/nix-silverblue/selinux/fixseguix
	install -p -m 0644 selinux/guix-daemon.cil $(DESTDIR)/share/nix-silverblue/selinux/guix-daemon.cil
	install -p -m 0755 selinux/fixsenix $(DESTDIR)/share/nix-silverblue/selinux/fixsenix

	install -d $(DESTDIR)/share/nix-silverblue/systemd
	install -p -m 0644 systemd/Makefile $(DESTDIR)/share/nix-silverblue/systemd/Makefile
	install -p -m 0644 systemd/gnu.mount $(DESTDIR)/share/nix-silverblue/systemd/gnu.mount
	install -p -m 0644 systemd/nix.mount $(DESTDIR)/share/nix-silverblue/systemd/nix.mount
	install -p -m 0644 systemd/guix-daemon.service $(DESTDIR)/share/nix-silverblue/systemd/guix-daemon.service
	install -p -m 0644 systemd/nix-daemon.service $(DESTDIR)/share/nix-silverblue/systemd/nix-daemon.service
	install -p -m 0644 systemd/nix-daemon.socket $(DESTDIR)/share/nix-silverblue/systemd/nix-daemon.socket
