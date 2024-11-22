.PHONY: default install

DESTDIR	:= 	/usr/local
SYSCONFDIR :=	/etc
default: ;

install:
	install -D -p -m 0755 fixseguix $(DESTDIR)/share/nix-silverblue/selinux/fixseguix
	install -D -p -m 0644 guix-daemon.cil $(DESTDIR)/share/nix-silverblue/selinux/guix-daemon.cil
	install -D -p -m 0755 fixsenix $(DESTDIR)/share/nix-silverblue/selinux/fixsenix
