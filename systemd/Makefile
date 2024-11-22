.PHONY: default install

DESTDIR	:= 	/usr/local
SYSCONFDIR :=	/etc
default: ;

install:
	install -D -p -m 0644 mkrootlink@.service $(DESTDIR)/lib/systemd/system/mkrootlink@.service
	install -D -p -m 0644 mkrootdir@.service $(DESTDIR)/lib/systemd/system/mkrootdir@.service
	install -D -p -m 0644 gnu-store.mount $(DESTDIR)/lib/systemd/system/gnu-store.mount
	install -D -p -m 0644 nix-store.mount $(DESTDIR)/lib/systemd/system/nix-store.mount
	install -D -p -m 0644 var-guix.mount $(DESTDIR)/lib/systemd/system/var-guix.mount
	install -D -p -m 0644 guix-daemon.service.wants/gnu-store.mount $(DESTDIR)/lib/systemd/system/guix-daemon.service.wants/gnu-store.mount
	install -D -p -m 0644 guix-daemon.service.wants/var-guix.mount $(DESTDIR)/lib/systemd/system/guix-daemon.service.wants/var-guix.mount
	install -D -p -m 0644 nix-daemon.service.wants/nix-store.mount $(DESTDIR)/lib/systemd/system/nix-daemon.service.wants/nix-store.mount

	install -D -p -m 0644 Makefile.install $(DESTDIR)/share/nix-silverblue/systemd/Makefile
	install -D -p -m 0644 gnu.mount $(DESTDIR)/share/nix-silverblue/systemd/gnu.mount
	install -D -p -m 0644 nix.mount $(DESTDIR)/share/nix-silverblue/systemd/nix.mount
	install -D -p -m 0644 guix-daemon.service $(DESTDIR)/share/nix-silverblue/systemd/guix-daemon.service
	install -D -p -m 0644 nix-daemon.service $(DESTDIR)/share/nix-silverblue/systemd/nix-daemon.service
	install -D -p -m 0644 nix-daemon.socket $(DESTDIR)/share/nix-silverblue/systemd/nix-daemon.socket
