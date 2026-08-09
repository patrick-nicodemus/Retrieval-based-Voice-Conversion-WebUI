import os


def require_asset(path, readme_hint):
    """Raise a clear error pointing at the README if a downloaded model/asset is missing.

    Assets under assets/ and logs/mute/ are fetched separately (README.md, "Model
    downloads") rather than checked into git, so a plain FileNotFoundError from
    torch.load/open leaves no clue that a download step was skipped.
    """
    if not os.path.exists(path):
        raise FileNotFoundError(
            f"Required asset not found: {path}\n"
            f"This file is downloaded separately (see README.md, \"Model downloads\"). {readme_hint}"
        )


def read_text(path, errors="strict", newline=None):
    last_error = None
    for encoding in (None, "utf8", "gbk"):
        try:
            kwargs = {"errors": "strict", "newline": newline}
            if encoding is not None:
                kwargs["encoding"] = encoding
            with open(path, "r", **kwargs) as file:
                return file.read()
        except UnicodeDecodeError as error:
            last_error = error
    if errors != "strict":
        with open(path, "r", encoding="gbk", errors=errors, newline=newline) as file:
            return file.read()
    raise last_error
