.PHONY: default install

DESTDIR	:= 	/usr/local
SYSCONFDIR :=	/etc
default: ;

install:
	install -D -p -m 0644 guix.conf $(DESTDIR)/lib/sysusers.d/guix.conf
	install -D -p -m 0644 nix.conf $(DESTDIR)/lib/sysusers.d/nix.conf
