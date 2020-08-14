from typing import *

from click import Context
from click.utils import LazyFile

def _get_default_option(option_name: str) -> Any: ...
def cli(
    ctx: Context,
    verbose: int,
    quiet: int,
    dry_run: bool,
    pre: bool,
    rebuild: bool,
    find_links: Collection[str],
    index_url: Optional[str],
    extra_index_url: Collection[str],
    cert: Optional[str],
    client_cert: Optional[str],
    trusted_host: Collection[str],
    header: bool,
    index: bool,
    emit_trusted_host: bool,
    annotate: bool,
    upgrade: bool,
    upgrade_packages: Collection[str],
    output_file: Optional[LazyFile],
    allow_unsafe: bool,
    generate_hashes: bool,
    src_files: Collection[str],
    max_rounds: int,
    build_isolation: bool,
    emit_find_links: bool,
    cache_dir: Optional[str],
    pip_args: Optional[str],
) -> None: ...
