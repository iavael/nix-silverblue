# Copilot Instructions for nix-silverblue

## Project Overview

This repository provides **nix-silverblue** - a collection of tools and configurations for integrating Nix and Guix package managers with Fedora Atomic distributions (Silverblue, Kinoite, etc.). The project enables these functional package managers to work seamlessly on immutable Fedora systems.

## Repository Structure

```
nix-silverblue/
├── src/              # Shell scripts for system setup
│   ├── mkrootdir     # Creates root directories
│   ├── mkrootlink    # Creates root symlinks
│   ├── restorecon-guix  # SELinux context restoration for Guix
│   └── restorecon-nix   # SELinux context restoration for Nix
├── systemd/          # systemd unit files
│   ├── *.mount       # Mount units for Nix/Guix stores
│   ├── *.service     # Service units for daemons
│   └── *.socket      # Socket activation units
├── selinux/          # SELinux policy modules
│   ├── guix-daemon.cil  # SELinux policy for Guix
│   ├── fixseguix     # SELinux policy installer for Guix
│   └── fixsenix      # SELinux policy installer for Nix
├── etc/              # System configuration files
│   ├── guix.sh       # Shell profile for Guix
│   ├── nix.sh        # Shell profile for Nix
│   └── nix.conf      # Nix configuration
├── sysusers/         # systemd-sysusers configuration
├── Makefile          # Top-level build file
├── nix-silverblue.spec  # RPM package specification
└── .tito/            # Tito release management configuration
```

## Building and Testing

### Build System

The project uses **GNU Make** for building and **Tito** for release management.

**Build commands:**
```bash
# Default target (no-op)
make

# Install to a custom destination (for packaging)
make install DESTDIR=/path/to/dest SYSCONFDIR=/path/to/etc
```

**Installation locations:**
- Executables: `${DESTDIR}/sbin/`
- Configuration: `${SYSCONFDIR}/profile.d/`, `${SYSCONFDIR}/nix/`
- Systemd units: `${DESTDIR}/lib/systemd/system/`
- Data files: `${DESTDIR}/share/nix-silverblue/`

### RPM Packaging

Build RPM packages using Tito:
```bash
tito build --test --rpm
```

The spec file (`nix-silverblue.spec`) defines all package dependencies and installation procedures.

### Testing

**Note:** There is no automated test infrastructure in this repository. Changes should be validated manually by:

1. **Syntax checking shell scripts:**
   ```bash
   bash -n src/mkrootdir
   shellcheck src/* 2>/dev/null || echo "shellcheck not available"
   ```

2. **Validating systemd units:**
   ```bash
   systemd-analyze verify systemd/*.service systemd/*.mount
   ```

3. **Checking SELinux policy syntax:**
   ```bash
   # CIL policies can be checked with:
   checkmodule -M -m -o /dev/null selinux/guix-daemon.cil 2>/dev/null || echo "SELinux tools not available"
   ```

## Coding Standards

### Shell Scripts

- **Shebang:** Use `#!/bin/sh` for POSIX compatibility unless bash-specific features are needed
- **Error handling:** Use `set -e` to exit on errors
- **Cleanup:** Implement proper trap handlers for signal handling
- **Style:**
  - Use lowercase for local variables
  - Use UPPERCASE for environment variables
  - Indent with 2 spaces (no tabs)
  - Quote all variable expansions: `"$variable"`

### Systemd Units

- Follow systemd unit file best practices
- Include appropriate dependencies (After=, Requires=, Wants=)
- Use descriptive `Description=` fields
- For mount units, ensure proper ordering with `Before=` directives

### SELinux Policies

- Use CIL (Common Intermediate Language) format for policies
- Follow least-privilege principle
- Document policy rules with comments
- Test policies in permissive mode before enforcement

## Important Notes

### System Integration

- This project modifies system root directories, which requires careful handling
- Scripts use `chattr +i /` to protect the root filesystem from accidental modifications
- All changes should preserve the immutability principles of Fedora Atomic

### Dependencies

The project requires:
- `make` and `cpp` (C preprocessor)
- `systemd` and `systemd-rpm-macros`
- `policycoreutils` and `policycoreutils-python-utils`
- SELinux must be enabled on the target system

### Release Process

- Version management: Use Tito for tagging and building releases
- Changelog: Automatically maintained in the spec file
- Tag format: `v{version}` (e.g., v0.1.4)

## Making Changes

When making changes to this repository:

1. **For shell scripts:**
   - Maintain POSIX compatibility where possible
   - Preserve existing error handling patterns
   - Test scripts with `bash -n` for syntax errors

2. **For systemd units:**
   - Validate with `systemd-analyze verify`
   - Ensure proper dependencies are maintained
   - Test on actual Fedora Atomic systems when possible

3. **For SELinux policies:**
   - Understand the security implications
   - Follow the existing CIL policy structure
   - Document any new policy rules

4. **For the spec file:**
   - Update `%changelog` using Tito
   - Maintain proper RPM macro usage
   - Keep `BuildRequires` and `Requires` accurate

5. **Documentation:**
   - Update inline comments for complex logic
   - Keep this file updated if project structure changes
   - Document any new configuration options

## Common Tasks

### Adding a new script

1. Create the script in `src/`
2. Add installation rule to `src/Makefile`
3. Add file reference to `nix-silverblue.spec` in `%files` section
4. Test syntax with `bash -n`

### Adding a new systemd unit

1. Create the unit file in `systemd/`
2. Add installation rule to `systemd/Makefile`
3. Update spec file with `%systemd_preun` if needed
4. Add to `%files` section in spec file
5. Validate with `systemd-analyze verify`

### Modifying SELinux policy

1. Edit the `.cil` file in `selinux/`
2. Update the corresponding `fixse*` installer script if needed
3. Test the policy changes carefully
4. Document the changes in commit messages

## Contact and Contribution

- Repository: https://github.com/iavael/nix-silverblue
- License: Apache 2.0
- Primary maintainer: iavael

When contributing, ensure changes align with Fedora Atomic's immutability principles and maintain compatibility with both Nix and Guix package managers.
