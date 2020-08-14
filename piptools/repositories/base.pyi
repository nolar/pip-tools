from abc import ABCMeta, abstractmethod
from typing import *

from pip._internal.req import InstallRequirement

class BaseRepository(object, metaclass=ABCMeta):
    def clear_caches(self) -> None: ...
    def freshen_build_caches(self) -> None: ...
    @abstractmethod
    def find_best_match(
        self, ireq: InstallRequirement, prereleases: Optional[bool] = None
    ) -> InstallRequirement: ...
    @abstractmethod
    def get_dependencies(
        self, ireq: InstallRequirement
    ) -> Collection[InstallRequirement]: ...
    @abstractmethod
    def get_hashes(self, ireq: InstallRequirement) -> Collection[str]: ...
    def copy_ireq_dependencies(
        self, source: InstallRequirement, dest: InstallRequirement
    ) -> None: ...
