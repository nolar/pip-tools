from typing import *

from pip._internal.index.package_finder import PackageFinder

def cli(
    ask: bool,
    dry_run: bool,
    force: bool,
    find_links: Optional[str],
    index_url: Optional[str],
    extra_index_url: Collection[str],
    trusted_host: Collection[str],
    no_index: bool,
    quiet: bool,
    user_only: bool,
    cert: Optional[str],
    client_cert: Optional[str],
    src_files: Collection[str],
    pip_args: Optional[str],
) -> None: ...
def _compose_install_flags(
    finder: PackageFinder,
    no_index: bool = False,
    index_url: Optional[str] = None,
    extra_index_url: Optional[Collection[str]] = None,
    trusted_host: Optional[Collection[str]] = None,
    find_links: Optional[Collection[str]] = None,
    user_only: bool = False,
    cert: Optional[str] = None,
    client_cert: Optional[str] = None,
) -> Collection[str]: ...
