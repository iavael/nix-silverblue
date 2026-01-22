#!/bin/sh

# _GUIX_PROFILE: `guix pull` profile
_GUIX_PROFILE="$HOME/.config/guix/current"
export PATH="$_GUIX_PROFILE/bin${PATH:+:}$PATH"
# Export INFOPATH so that the updated info pages can be found
# and read by both /usr/bin/info and/or $GUIX_PROFILE/bin/info
# When INFOPATH is unset, add a trailing colon so that Emacs
# searches 'Info-default-directory-list'.
export INFOPATH="$_GUIX_PROFILE/share/info:$INFOPATH"

# GUIX_PROFILE: User's default profile
GUIX_PROFILE="$HOME/.guix-profile"
[ -L "$GUIX_PROFILE" ] || return
GUIX_LOCPATH="$GUIX_PROFILE/lib/locale"
export GUIX_LOCPATH

[ -e "$GUIX_PROFILE/etc/profile" ] && . "$GUIX_PROFILE/etc/profile"

# set XDG_DATA_DIRS to include Guix installations
export XDG_DATA_DIRS="$GUIX_PROFILE/share:${XDG_DATA_DIRS:-/usr/local/share/:/usr/share/}"
