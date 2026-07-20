"""Research-use Raman Bacteria Prototype 0 foundation."""

from importlib.metadata import PackageNotFoundError, version


def get_version() -> str:
    """Return installed distribution metadata without duplicating a version literal."""
    try:
        return version("raman-bacteria-prototype")
    except PackageNotFoundError:
        return "0+uninstalled"


__all__ = ["get_version"]
