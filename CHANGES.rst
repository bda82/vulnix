Changes
=======


1.4.1 (unreleased)
------------------

- Ignore case when guessing CVE identifiers from patch file names (thanks to
  adisbladis).


1.4.0 (2017-11-27)
------------------

- Guesses applied CVE patches out of the `patches` derivation envVar (see
  nixpkgs #15660).


1.3.4 (2017-10-29)
------------------

- Add '--no-requisites' flag which stops vulnix from determining the transitive
  closure of derivations passed on the command line.
- Provide structured JSON output with `--json`.
- Remove whitelist from README as it is quite buggy right now.


1.3.3 (2017-10-16)
------------------

- Fix return code bug (#28741).
- Fix partial whitelisting of products where several vulnerable versions are
  present on the system at the same time (#24).
- Improve error reporting for incorrectly formed whitelist rules.


1.3.2 (2017-10-06)
------------------

- Minor: fix packaging issues.


1.3.1 (2017-10-06)
------------------

- Security: Fix arbitrary code execution bug during derivation evaluation.


1.3.0 (2017-09-18)
------------------

- `.drv` files may be specified directly on the command line.
- Updated PyPI dependencies.
- Document system requirements (#12).
- Don't leave large files in /tmp around.
- Remove duplicate CVEs in output (#25).
- Fix bug with reporting less than 3 vulnerabilities (#28).


1.2.2 (2017-01-28)
------------------

- Packaging improvements: pin versions in setup.py, include NVDCVE test data in
  sdist.
- Reduce NVDCVE fixture size. This cuts tests run time by more than 50%.


1.2.1 (2017-01-27)
------------------

- Skip `/nix/var/nix/gcroots/booted-system` during system check.
- Make output a bit easier to read by removing visual clutter.


1.2 (2016-12-22)
----------------

- Improve CPU and memory usage: refactored the way we fetch, parse, store and
  process data. We now leverage ZODB as the storage for parsed data that is
  efficient to look up.

  On our test systems this caused memory usage to drop from > 1GiB to ~70MiB
  and a pure evaluation of existing data to around 7-10 seconds.

  This change requires a re-retrieval of all historic sources.

- Improve unit test coverage with at least a smoke test for our new fetching
  procedure.

1.1.5 (2016-10-13)
------------------

- Keep a reverse index: product name -> vulnerabilities to speed up scan process.
- Mark 'in progress' vulnerabilities with an asterisk
- The '-w' switch accepts URLs, too
- vulnix no longer scans /var/nix/var/gcroots/booted-system
- only cached files are saved (archives are to be deleted)
- added travis build: runs periodically against nixpkgs/master and updates
  requirements*.nix files in case of success


1.1.4 (2016-08-25)
------------------

- Add `src` to PYTHONPATH so that tests run also on older NixOS versions
  (tested on 15.09).
- Correct URL, add metadata.
- Add nix to propagatedBuildInputs, as vulnix calls `nix-store` at runtime.


1.1.3 (2016-08-16)
------------------

- Pin the Python version to 3.4 (Nix only)


1.1.2 (2016-08-15)
------------------

- Add Nix expressions (Nix/NixOS) to MANIFEST.in


1.1.1 (2016-08-12)
------------------

- Add VERSION to MANIFEST.in


1.1 (2016-08-11)
----------------

- Scans the whole system (NixOS only), the current user environment, or a
  project-specific path (e.g., ./result). #1

- Allow to specify site-specific whitelists in addition to the builtin default
  whitelist. #4

- Fully repeatable install using default.nix. Thanks to Rok Garbas. #4

- Cache pre-parsed NVD files for improved scanning speed. #2

- Support multiple whitelists (repeat -w option). #3

- Cache NVD files in `~/.cache/vulnix`. #7

- Document whitelist file format. #10

- Fix Nix build on macOS. #11
