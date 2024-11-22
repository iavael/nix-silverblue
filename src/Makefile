.PHONY: default install

DESTDIR	:= 	/usr/local
SYSCONFDIR :=	/etc
default: ;

install:
	install -D -p -m 0755 restorecon-guix $(DESTDIR)/sbin/restorecon-guix
	install -D -p -m 0755 restorecon-nix $(DESTDIR)/sbin/restorecon-nix
	install -D -p -m 0755 mkrootdir $(DESTDIR)/sbin/mkrootdir
	install -D -p -m 0755 mkrootlink $(DESTDIR)/sbin/mkrootlink
