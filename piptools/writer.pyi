from typing import *

from click import Context, File
from click.utils import LazyFile
from pip._internal.req import InstallRequirement
from pip._internal.models.format_control import FormatControl
from pip._vendor.packaging.markers import Marker

MESSAGE_UNHASHED_PACKAGE: str = ...
MESSAGE_UNSAFE_PACKAGES_UNPINNED: str = ...
MESSAGE_UNSAFE_PACKAGES: str = ...
MESSAGE_UNINSTALLABLE: str = ...

strip_comes_from_line_re: Pattern[str] = ...

def _comes_from_as_string(ireq: InstallRequirement) -> str: ...

class OutputWriter(object):
    def __init__(
        self,
        src_files: List[str],
        dst_file: Union[File, LazyFile],
        click_ctx: Context,
        dry_run: bool,
        emit_header: bool,
        emit_index: bool,
        emit_trusted_host: bool,
        annotate: bool,
        generate_hashes: bool,
        default_index_url: str,
        index_urls: List[str],
        trusted_hosts: Iterable[str],
        format_control: FormatControl,
        allow_unsafe: bool,
        find_links: List[str],
        emit_find_links: bool,
    ) -> None: ...
    def _sort_key(self, ireq: InstallRequirement) -> Tuple[bool, str]: ...
    def write_header(self) -> Iterator[str]: ...
    def write_index_options(self) -> Iterator[str]: ...
    def write_trusted_hosts(self) -> Iterator[str]: ...
    def write_format_controls(self) -> Iterator[str]: ...
    def write_find_links(self) -> Iterator[str]: ...
    def write_flags(self) -> Iterator[str]: ...
    def _iter_lines(
        self,
        results: Set[InstallRequirement],
        unsafe_requirements: Optional[List[InstallRequirement]] = None,
        markers: Optional[Mapping[str, Marker]] = None,
        hashes: Optional[Mapping[InstallRequirement, Set[str]]] = None,
    ) -> Iterator[str]: ...
