from contextlib import AbstractContextManager
from typing import TypeVar, Any

_T = TypeVar("_T")

class nullcontext(AbstractContextManager[_T]):
    enter_result: _T
    def __init__(self, enter_result: _T) -> None: ...
    def __enter__(self) -> _T: ...
    def __exit__(self, *excinfo: Any) -> None: ...
