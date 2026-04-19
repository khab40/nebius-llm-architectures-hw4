"""Notebook-friendly progress bars for long HW4 training cells."""

from __future__ import annotations

import os
import sys
from typing import Any

from tqdm.std import tqdm as _std_tqdm

try:
    from IPython import get_ipython
    from IPython.display import HTML, display
except Exception:  # pragma: no cover - only used outside IPython.
    HTML = None
    display = None

    def get_ipython():  # type: ignore[no-redef]
        return None

try:
    from tqdm.notebook import tqdm as _notebook_tqdm
except Exception:  # pragma: no cover - depends on optional widget stack.
    _notebook_tqdm = None

try:
    import ipywidgets as widgets
except Exception:  # pragma: no cover - depends on optional widget stack.
    widgets = None


_STYLE_DISPLAYED = False
_ACTIVE_WIDGET_OUTPUT = None
_ACTIVE_WIDGET_DEPTH = 0

_SCROLL_STYLE = """
.hw4-progress-anchor {
    display: none;
}

/* JupyterLab and Notebook 7 */
.jp-OutputArea-child:has(.hw4-progress-anchor),
.jp-OutputArea-output:has(.hw4-progress-anchor),
.jp-Cell-outputWrapper:has(.hw4-progress-anchor) .jp-OutputArea {
    max-height: 420px !important;
    overflow-y: auto !important;
}

/* Classic Notebook */
.output_wrapper:has(.hw4-progress-anchor) .output,
.output_subarea:has(.hw4-progress-anchor) {
    max-height: 420px !important;
    overflow-y: auto !important;
}

/* VS Code notebooks */
.cell-output:has(.hw4-progress-anchor),
.cell-output-container:has(.hw4-progress-anchor) {
    max-height: 420px !important;
    overflow-y: auto !important;
}
"""


def _running_in_ipython() -> bool:
    try:
        return get_ipython() is not None
    except Exception:
        return False


def _mark_scrollable_output() -> None:
    """Attach CSS and an invisible marker to the current notebook output cell."""
    global _STYLE_DISPLAYED

    if not _running_in_ipython() or HTML is None or display is None:
        return

    if not _STYLE_DISPLAYED:
        display(HTML(f"<style>{_SCROLL_STYLE}</style>"))
        _STYLE_DISPLAYED = True

    display(HTML('<span class="hw4-progress-anchor" aria-hidden="true"></span>'))


def _use_notebook_backend() -> bool:
    """Prefer widget bars in notebooks unless explicitly disabled."""
    if os.environ.get("HW4_TQDM_BACKEND", "").lower() in {"std", "text", "terminal"}:
        return False
    return _running_in_ipython() and _notebook_tqdm is not None


def _acquire_widget_output():
    """Create or reuse a bounded widget output area for nested progress bars."""
    global _ACTIVE_WIDGET_DEPTH, _ACTIVE_WIDGET_OUTPUT

    if widgets is None or display is None or not _running_in_ipython():
        return None

    if _ACTIVE_WIDGET_OUTPUT is None:
        _ACTIVE_WIDGET_OUTPUT = widgets.Output(
            layout=widgets.Layout(
                max_height="420px",
                overflow_y="auto",
                width="100%",
            )
        )
        display(_ACTIVE_WIDGET_OUTPUT)

    _ACTIVE_WIDGET_DEPTH += 1
    return _ACTIVE_WIDGET_OUTPUT


def _release_widget_output() -> None:
    global _ACTIVE_WIDGET_DEPTH, _ACTIVE_WIDGET_OUTPUT

    if _ACTIVE_WIDGET_DEPTH > 0:
        _ACTIVE_WIDGET_DEPTH -= 1

    if _ACTIVE_WIDGET_DEPTH == 0:
        _ACTIVE_WIDGET_OUTPUT = None


def _release_output_when_closed(bar):
    original_close = bar.close
    released = False

    def close(*args: Any, **kwargs: Any):
        nonlocal released
        try:
            return original_close(*args, **kwargs)
        finally:
            if not released:
                released = True
                _release_widget_output()

    bar.close = close
    return bar


def tqdm(*args: Any, **kwargs: Any):
    """Return a tqdm progress bar that behaves well in notebooks.

    The previous notebooks used ``tqdm.notebook`` directly when it imported.
    That import can succeed even when the frontend cannot render widgets, and
    the text fallback can then flood the output cell. This wrapper makes every
    progress-bar cell scrollable and falls back to the standard tqdm backend if
    the widget backend cannot be constructed.
    """

    kwargs.setdefault("dynamic_ncols", True)
    kwargs.setdefault("mininterval", 0.2)
    kwargs.setdefault("smoothing", 0.05)
    _mark_scrollable_output()

    if _use_notebook_backend():
        output = _acquire_widget_output()
        try:
            if output is None:
                return _notebook_tqdm(*args, **kwargs)
            with output:
                return _release_output_when_closed(_notebook_tqdm(*args, **kwargs))
        except Exception:
            if output is not None:
                _release_widget_output()
            pass

    kwargs.setdefault("file", sys.stdout)
    return _std_tqdm(*args, **kwargs)
