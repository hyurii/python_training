import contextlib
from typing import Generator, Tuple


class MyError(RuntimeError):
    pass


@contextlib.contextmanager
def ctx(s: str) -> Generator[Tuple[str, int], None, None]:
    print("Enter")
    file = f"{s}, Hello, 42"
    try:
        yield file, 42
    except MyError as e:
        print(f"MyError: {e}")
    except Exception as e:
        print(f"Error: {e}")
    print("Exit")


with ctx("KG") as (a, b):
    print(a, b)
    raise MyError("MyError raised")
