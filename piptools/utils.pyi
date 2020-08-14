from typing import (
    Optional,
    Callable,
    Iterable,
    TypeVar,
    Union,
    Tuple,
    Collection,
    Mapping,
)

from click import Context
from pip._internal.req import InstallRequirement
from pip._vendor.pkg_resources import Distribution
from pip._vendor.packaging.requirements import Requirement
from pip._vendor.packaging.markers import Marker

_T = TypeVar("_T")
_K = TypeVar("_K")
_V = TypeVar("_V")
_R = TypeVar("_R")

def key_from_ireq(ireq: InstallRequirement) -> str: ...
def key_from_req(req: Union[Distribution, Requirement]) -> str: ...
def comment(text: str) -> str: ...
def make_install_requirement(
    name: str, version: str, extras: Collection[str], constraint: bool = False
) -> InstallRequirement: ...
def is_url_requirement(ireq: InstallRequirement) -> bool: ...
def format_requirement(
    ireq: InstallRequirement,
    marker: Optional[Marker] = None,
    hashes: Optional[Collection[str]] = None,
) -> str: ...
def format_specifier(ireq: InstallRequirement) -> str: ...
def is_pinned_requirement(ireq: InstallRequirement) -> bool: ...
def as_tuple(ireq: InstallRequirement) -> Tuple[str, str, Collection[str]]: ...
def flat_map(
    fn: Callable[[_T], Iterable[_R]], collection: Iterable[_T]
) -> Iterable[_R]: ...

# TODO: redefined via overrides due to keyval=... set: it affects the output of _T or _V in the end.
def lookup_table(
    values: _T,
    key: Optional[Callable[[_T], _K]] = None,
    keyval: Optional[Callable[[_T], Tuple[_K, _V]]] = None,
    unique: bool = False,
    use_lists: bool = False,
) -> Mapping[_K, Collection[Union[_T, _V]]]: ...
def dedup(iterable: Iterable[_T]) -> Iterable[_T]: ...
def name_from_req(req: Distribution) -> str: ...
def fs_str(string: str) -> bytes: ...
def get_hashes_from_ireq(ireq: InstallRequirement) -> Collection[str]: ...
def force_text(s: Optional[str]) -> str: ...
def get_compile_command(click_ctx: Context) -> str: ...