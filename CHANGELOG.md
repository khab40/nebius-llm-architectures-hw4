# Changelog

## 2026-04-19

- Added [`src/notebook_progress.py`](src/notebook_progress.py) and switched long-running notebooks to a shared progress helper with bounded scrollable output areas.
- Updated CIFAR-10, RNN, and bonus training loops to report live progress through tqdm postfix values instead of growing per-epoch print streams.
- Converted [`src/bon_p1_backward.ipynb`](src/bon_p1_backward.ipynb) from NumPy-backed model math to manual Torch tensor backpropagation on `mps`/`cuda`/`cpu`, while keeping NumPy for reference checks, plotting, and sklearn metrics.
- Converted [`src/bon_p2_forward.ipynb`](src/bon_p2_forward.ipynb) to run the custom forward-pass framework on Torch tensors with `mps`/`cuda`/`cpu` device selection.
- Replaced copied architecture notes with source-derived docs under [`docs/architecture/`](docs/architecture/index.md).
- Updated [`README.md`](README.md) to use the actual notebook filenames and current accelerator/progress behavior.
- Added generated repository artwork in [`docs/repo-icon.png`](docs/repo-icon.png) and [`docs/repo-banner.png`](docs/repo-banner.png), and embedded it in the README.

## 2026-04-18

- Created standalone `hw4` VS Code Python project beside the original notebook workspace.
- Moved HW4 source notebooks into `src/` at the new project root.
- Set up `uv` dependency management with the libraries required by the HW4 notebooks.
- Added VS Code Python and Jupyter workspace settings.
- Moved HW4-only local data into project-level `data/`, leaving `weatherAUS.csv` in the original workspace for HW2.
