# clode

CLI tool to open git repositories quickly.

## Installation

```console
pip install clode
```

## Usage

Clode with URL:

```console
$ clode https://github.com/olillin/clode
Cloning https://github.com/olillin/clode
```

Clode with owner and repository name only:

```console
$ clode olillin/clode
Cloning https://github.com/olillin/clode
```

> [!NOTE]
> The default service is GitHub. This can be changed in settings.
<!-- TODO: Add settings file name -->

Clode with repository name only:

```console
$ clode clode
Cloning https://github.com/olillin/clode
```

> [!NOTE]
> Requires a default user to be configured in settings
<!-- TODO: Add settings file name -->

Clode with GitHub search query:

```console
$ clode -q "org:cthit in:name hubbit"
[?] Select repository to clone:
 > cthit/hubbit
   cthit/hubbIT-old
```

Clode with lazy search:

```console
$ clode -l "cthit/chalmers it"
[?] Select repository to clone:
 > cthit/chalmers.it
   cthit/digit.chalmers.it
   cthit/chalmers.it-deprecated
   cthit/Avtal.chalmers.it

$ clode -l cals
Cloning https://github.com/olillin/cals-cals
```
