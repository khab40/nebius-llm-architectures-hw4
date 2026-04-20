# Notebook Progress Handling

Source module: [`../../src/notebook_progress.py`](../../src/notebook_progress.py)

The training notebooks use `tqdm` through this helper instead of importing notebook or terminal tqdm directly.

## Purpose

The helper solves two practical notebook problems:

- `tqdm.notebook` can import successfully even when the frontend widget renderer is unavailable or stale;
- long training cells can flood notebook output if progress updates fall back to text mode.

## Behavior

`tqdm` from [`../../src/notebook_progress.py`](../../src/notebook_progress.py):

- prefers widget-backed notebook progress bars when available;
- falls back to standard tqdm on stdout when widgets cannot be constructed;
- displays progress output inside a bounded scrollable area;
- uses CSS markers for notebook frontends and an `ipywidgets.Output` container for widget progress;
- supports `HW4_TQDM_BACKEND=std` to force the text backend.

The CIFAR-10, RNN, and bonus training notebooks import this helper by locating the project `src/` directory from the current working directory or its parents, then running `from notebook_progress import tqdm`.
