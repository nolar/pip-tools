from contextlib import contextmanager
from typing import (
    Optional,
    NamedTuple,
    BinaryIO,
    Mapping,
    MutableMapping,
    Collection,
    Iterator,
    Any,
)

from typing_extensions import Protocol

from pip._internal.index.package_finder import PackageFinder
from pip._internal.req import InstallRequirement
from pip._internal.cache import WheelCache
from pip._internal.models.link import Link
from pip._internal.cli.base_command import Command
from pip._internal.models.format_control import FormatControl
from pip._internal.network.session import PipSession

from .base import BaseRepository
from .._compat.tempfile import TemporaryDirectory

# De facto, a generic namespace accessed via attributes.
# We annotate only those options that are acvtually used.
class __Options(Protocol):
    format_control: FormatControl
    no_color: bool
    cache_dir: str
    log: Optional[str]
    require_hashes: bool
    ignore_dependencies: bool

class FileStream(NamedTuple):
    stream: BinaryIO
    size: int

class PyPIRepository(BaseRepository):

    command: Command
    options: __Options
    session: PipSession
    finder: PackageFinder

    _available_candidates_cache: MutableMapping[str, Collection[InstallRequirement]]
    _dependencies_cache: MutableMapping[
        InstallRequirement, Collection[InstallRequirement]
    ]

    _cache_dir: str
    _download_dir: bytes
    _wheel_download_dir: bytes

    _build_dir: TemporaryDirectory
    _source_dir: TemporaryDirectory
    def __init__(self, pip_args: Collection[str], cache_dir: str) -> None: ...
    def freshen_build_caches(self) -> None: ...
    @property
    def build_dir(self) -> TemporaryDirectory: ...
    @property
    def source_dir(self) -> TemporaryDirectory: ...
    def clear_caches(self) -> None: ...
    def find_all_candidates(self, req_name: str) -> Collection[InstallRequirement]: ...
    def find_best_match(
        self, ireq: InstallRequirement, prereleases: Optional[bool] = None
    ) -> InstallRequirement: ...
    def resolve_reqs(
        self, download_dir: str, ireq: InstallRequirement, wheel_cache: WheelCache
    ) -> Collection[InstallRequirement]: ...
    def get_dependencies(
        self, ireq: InstallRequirement
    ) -> Collection[InstallRequirement]: ...
    def copy_ireq_dependencies(
        self, source: InstallRequirement, dest: InstallRequirement
    ) -> None: ...
    def _get_project(self, ireq: InstallRequirement) -> Optional[Mapping[str, Any]]: ...
    def get_hashes(self, ireq: InstallRequirement) -> Collection[str]: ...
    def _get_hashes_from_pypi(self, ireq: InstallRequirement) -> Collection[str]: ...
    def _get_hashes_from_files(self, ireq: InstallRequirement) -> Collection[str]: ...
    def _get_file_hash(self, link: Link) -> str: ...
    @contextmanager
    def allow_all_wheels(self) -> Iterator[None]: ...
    def _setup_logging(self) -> None: ...

@contextmanager
def open_local_or_remote_file(
    link: Link, session: PipSession
) -> Iterator[FileStream]: ...
