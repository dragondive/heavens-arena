# CHANGELOG



## v0.4.0 (2023-08-01)

### Ci

* ci: setup semantic-release and contract publish

This workflow performs a semantic-release. It can be triggered only manually, but this may change in future.

On every semantic-release, the pact contract is also published to the pact broker.

pull-request: #2 ([`ec80183`](https://github.com/kukuroo-mountain/contract-consumer/commit/ec801836cdf458ac4a1d719e4c525092af154ca5))

* ci: setup semantic release for main branch ([`81a00a3`](https://github.com/kukuroo-mountain/contract-consumer/commit/81a00a304159f0ac12f373d10099eccb6bb45515))

* ci: setup pipeline build

Github Actions config file for CI build on main branch

pull-request: #1 ([`65a2594`](https://github.com/kukuroo-mountain/contract-consumer/commit/65a25940c23216b6528727df726c9bd409f12d40))

* ci: add github actions configuration file to setup main branch build

The CI build will be prepared on a feature branch. However, Github Actions requires a workflow file
with the same name on the main branch to run the action from a feature branch. This file will be
replaced with the configuration on the feature branch when it is ready. ([`35cdf7f`](https://github.com/kukuroo-mountain/contract-consumer/commit/35cdf7fdc27e8335eae18494b4d4353b112be20a))

### Feature

* feat: get project version from the project config ([`3dcf754`](https://github.com/kukuroo-mountain/contract-consumer/commit/3dcf754b5b8ad5a2bcef8208fa0bf2d6d916e9b9))

* feat: add the first contract test for consumer module

Sample of the consumer-driven contract test using `pact-python`.

The generated contract file is not included. It should be generated and published automatically
in the CI workflow which will be done in a subsequent feature implementation. ([`1445796`](https://github.com/kukuroo-mountain/contract-consumer/commit/144579600334d59085664d358f0522934f6d9239))

### Style

* style: minor file formatting fix ([`94049e4`](https://github.com/kukuroo-mountain/contract-consumer/commit/94049e4100e3f69160295b1afd417162fd333310))

### Test

* test: rework unit test to use consumer fixture ([`cb42e5c`](https://github.com/kukuroo-mountain/contract-consumer/commit/cb42e5cdbdd944ad6e814c7220df9ba2f4fdd923))


## v0.3.0 (2023-07-30)

### Documentation

* docs: fixed copy-paste mistake in docstring ([`50b8acc`](https://github.com/kukuroo-mountain/contract-consumer/commit/50b8acc11a9b3e3899c9f1638cde645910d6cac9))

### Feature

* feat: add consumer module ([`c952595`](https://github.com/kukuroo-mountain/contract-consumer/commit/c9525956086deb031765e573ffc1beb075c638e6))


## v0.2.0 (2023-07-30)

### Build

* build: add prospector.yaml config file ([`7ba7759`](https://github.com/kukuroo-mountain/contract-consumer/commit/7ba77592a645c139cc3866ccc3acab58101e968f))

* build: added vscode settings file for convenience ([`e114f2d`](https://github.com/kukuroo-mountain/contract-consumer/commit/e114f2db1bf44c56df98eb663263c767cdd4f545))

### Chore

* chore: fix EOL from CRLF to LF in pyproject.toml ([`6da6bcb`](https://github.com/kukuroo-mountain/contract-consumer/commit/6da6bcb2bf825455efb3cc367885abeadf4508d6))

### Feature

* feat: setup portray documentation generator ([`3f6ad27`](https://github.com/kukuroo-mountain/contract-consumer/commit/3f6ad2784f75285f19481492b838eeb86d71dd2a))

### Style

* style: reformatted helloworld.py with black ([`02dd4a7`](https://github.com/kukuroo-mountain/contract-consumer/commit/02dd4a7b352103059ef221e27445702989111fd1))


## v0.1.0 (2023-07-29)

### Build

* build: added a pyproject.toml for project build configuration ([`616a124`](https://github.com/kukuroo-mountain/contract-consumer/commit/616a124ac19d912c0fb14d7e3beb00c243a8c2a1))

### Feature

* feat: add helloworld.py ([`d2f3035`](https://github.com/kukuroo-mountain/contract-consumer/commit/d2f30352fa9ea37510b526b55be1bc8793b1a4d1))


## v0.0.0 (2023-07-29)

### Unknown

* Initial commit ([`b770af8`](https://github.com/kukuroo-mountain/contract-consumer/commit/b770af8b571eb4f8a666a22d8b2f07c0c04efad6))
