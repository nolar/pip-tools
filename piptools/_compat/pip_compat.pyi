from typing import *

from pip._internal.req import InstallRequirement
from pip._internal.network.session import PipSession
from pip._internal.index.package_finder import PackageFinder

PIP_VERSION: Collection[int]

BAR_TYPES: Any  # it is actually unused, so the type is irrelevant

# Ignore the specific signature -- it is an external function anyway.
install_req_from_parsed_requirement: Callable[..., InstallRequirement]

def parse_requirements(
    filename: str,
    session: PipSession,
    finder: Optional[PackageFinder] = None,
    options: Optional[bool] = None,
    constraint: Optional[bool] = False,
    isolated: Optional[bool] = False,
) -> Iterator[InstallRequirement]: ...
