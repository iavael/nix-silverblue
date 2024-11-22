.PHONY: default daemons mounts

default: ;

daemons: /etc/systemd/system/guix-daemon.service /etc/systemd/system/nix-daemon.service /etc/systemd/system/nix-daemon.socket

/etc/systemd/system/guix-daemon.service: guix-daemon.service
	install -p -m 0644 $< $@

/etc/systemd/system/nix-daemon.service: nix-daemon.service
	install -p -m 0644 $< $@

/etc/systemd/system/nix-daemon.socket: nix-daemon.socket
	install -p -m 0644 $< $@

mounts: /etc/systemd/system/gnu.mount /etc/systemd/system/nix.mount

UUID := $(shell blkid -o value -s UUID $(shell findmnt -n -o SOURCE /sysroot))

/etc/systemd/system/gnu.mount: gnu.mount
	cpp -DUUID=$(UUID) -DEUUID=$(shell systemd-escape $(UUID)) -o $@ $<

/etc/systemd/system/nix.mount: nix.mount
	cpp -DUUID=$(UUID) -DEUUID=$(shell systemd-escape $(UUID)) -o $@ $<
