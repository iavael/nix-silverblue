#!/bin/sh

export NIX_PATH="$HOME/.nix-defexpr/channels:/nix/var/nix/profiles/per-user/root/channels${NIX_PATH+:$NIX_PATH}"

# Nix
if [ -e '/nix/var/nix/profiles/nix/etc/profile.d/nix-daemon.sh' ]; then
  # shellcheck disable=SC1091
  . '/nix/var/nix/profiles/nix/etc/profile.d/nix-daemon.sh'
fi
# End Nix
