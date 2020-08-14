from typing import Tuple, Set, Iterator, Iterable, Mapping

from pip._internal.req import InstallRequirement

from .repositories.base import BaseRepository
from .cache import DependencyCache

class RequirementSummary(object):
    def __init__(self, ireq: InstallRequirement) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...
    def __str__(self) -> str: ...

def combine_install_requirements(
    repository: BaseRepository, ireqs: Iterable[InstallRequirement]
) -> InstallRequirement: ...

class Resolver(object):
    our_constraints: Set[InstallRequirement]
    their_constraints: Set[InstallRequirement]
    unsafe_constraints: Set[InstallRequirement]
    repository: BaseRepository
    dependency_cache: DependencyCache
    prereleases: bool
    clear_caches: bool
    allow_unsafe: bool
    def __init__(
        self,
        constraints: Iterable[InstallRequirement],
        repository: BaseRepository,
        cache: DependencyCache,
        prereleases: bool = False,
        clear_caches: bool = False,
        allow_unsafe: bool = False,
    ) -> None: ...
    @property
    def constraints(self) -> Set[InstallRequirement]: ...
    def resolve_hashes(
        self, ireqs: Iterable[InstallRequirement]
    ) -> Mapping[InstallRequirement, Set[str]]: ...
    def resolve(self, max_rounds: int = 10) -> Set[InstallRequirement]: ...
    def _group_constraints(
        self, constraints: Iterable[InstallRequirement]
    ) -> Iterator[InstallRequirement]: ...
    def _resolve_one_round(self) -> Tuple[bool, Set[InstallRequirement]]: ...
    def get_best_match(self, ireq: InstallRequirement) -> InstallRequirement: ...
    def _iter_dependencies(
        self, ireq: InstallRequirement
    ) -> Iterator[InstallRequirement]: ...
    def reverse_dependencies(
        self, ireqs: Iterable[InstallRequirement]
    ) -> Mapping[str, Set[str]]: ...
