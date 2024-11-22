.PHONY: default install

DESTDIR	:= 	/usr/local
SYSCONFDIR :=	/etc

PROFILE_DIR = $(SYSCONFDIR)/profile.d
NIXCONF_DIR = $(SYSCONFDIR)/nix

default: ;

install: $(PROFILE_DIR)/guix.sh $(PROFILE_DIR)/nix.sh $(NIXCONF_DIR)/nix.conf

$(PROFILE_DIR)/guix.sh: guix.sh
	install -D -p -m 0644 $< $@

$(PROFILE_DIR)/nix.sh: nix.sh
	install -D -p -m 0644 $< $@

$(NIXCONF_DIR)/nix.conf: nix.conf
	install -D -p -m 0644 $< $@


