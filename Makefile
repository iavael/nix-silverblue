.PHONY: default install

DESTDIR	:= 	/usr/local
SYSCONFDIR :=	/etc
default: ;

install:
	$(MAKE) -C src install
	$(MAKE) -C systemd install
	$(MAKE) -C selinux install
	$(MAKE) -C etc install
	$(MAKE) -C sysusers install
