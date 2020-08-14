from typing import Collection

from pip._internal.req import InstallRequirement
from pip._internal.index.package_finder import PackageFinder

class PipToolsError(Exception): ...

class NoCandidateFound(PipToolsError):
    ireq: InstallRequirement
    candidates_tried: Collection[IncompatibleRequirements]
    finder: PackageFinder
    def __init__(
        self,
        ireq: InstallRequirement,
        candidates_tried: Collection[InstallRequirement],
        finder: PackageFinder,
    ) -> None: ...
    def __str__(self) -> str: ...

class IncompatibleRequirements(PipToolsError):
    ireq_a: InstallRequirement
    ireq_b: InstallRequirement
    def __init__(
        self, ireq_a: InstallRequirement, ireq_b: InstallRequirement
    ) -> None: ...
    def __str__(self) -> str: ...
