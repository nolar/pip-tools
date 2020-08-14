from typing import *

from pip._internal.req import InstallRequirement
from pip._vendor.pkg_resources import Distribution

PACKAGES_TO_IGNORE: List[str] = ...

def dependency_tree(
    installed_keys: Mapping[str, Distribution], root_key: str
) -> Set[str]: ...
def get_dists_to_ignore(installed: List[Distribution]) -> List[str]: ...
def merge(
    requirements: Iterable[InstallRequirement], ignore_conflicts: bool
) -> Iterable[InstallRequirement]: ...
def diff_key_from_ireq(ireq: InstallRequirement) -> str: ...
def diff(
    compiled_requirements: Iterable[InstallRequirement],
    installed_dists: List[Distribution],
) -> Tuple[Set[InstallRequirement], Set[str]]: ...
def sync(
    to_install: Set[InstallRequirement],
    to_uninstall: Set[str],
    verbose: bool = False,
    dry_run: bool = False,
    install_flags: Optional[Collection[str]] = None,
    ask: bool = False,
) -> int: ...
