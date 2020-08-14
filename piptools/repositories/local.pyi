from contextlib import contextmanager
from typing import *

from pip._internal.index.package_finder import PackageFinder
from pip._internal.req import InstallRequirement
from pip._internal.network.session import PipSession

from .base import BaseRepository
from .pypi import __Options

def ireq_satisfied_by_existing_pin(
    ireq: InstallRequirement, existing_pin: InstallRequirement
) -> bool: ...

class LocalRequirementsRepository(BaseRepository):
    repository: BaseRepository
    existing_pins: Mapping[str, InstallRequirement]
    def __init__(
        self,
        existing_pins: Mapping[str, InstallRequirement],
        proxied_repository: BaseRepository,
    ) -> None: ...
    @property
    def options(self) -> __Options: ...
    @property
    def finder(self) -> PackageFinder: ...
    @property
    def session(self) -> PipSession: ...
    @property
    def DEFAULT_INDEX_URL(self) -> str: ...
    def clear_caches(self) -> None: ...
    def freshen_build_caches(self) -> None: ...
    def find_best_match(
        self, ireq: InstallRequirement, prereleases: Optional[bool] = None
    ) -> InstallRequirement: ...
    def get_dependencies(
        self, ireq: InstallRequirement
    ) -> Collection[InstallRequirement]: ...
    def get_hashes(self, ireq: InstallRequirement) -> Collection[str]: ...
    @contextmanager
    def allow_all_wheels(self) -> Iterator[None]: ...
