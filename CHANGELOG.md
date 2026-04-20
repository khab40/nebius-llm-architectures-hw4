# Changelog

## 2026-04-20

- Renamed and consolidated the HW4 notebooks under the current source names:
  - [`src/homework_CIFAR10.ipynb`](src/homework_CIFAR10.ipynb)
  - [`src/homework_CIFAR10_bonus_3_CNN.ipynb`](src/homework_CIFAR10_bonus_3_CNN.ipynb)
  - [`src/RNN_LM_homework.ipynb`](src/RNN_LM_homework.ipynb)
  - [`src/Week 4 hometask bonus, forward.ipynb`](src/Week%204%20hometask%20bonus,%20forward.ipynb)
  - [`src/Week 4 hometask bonus, backward.ipynb`](src/Week%204%20hometask%20bonus,%20backward.ipynb)
- Merged the separate CIFAR-10 task notebooks back into the main CIFAR-10 notebook and kept the CNN experiment in a separate bonus notebook.
- Updated RNN language-model answers and conclusions to match the saved run, including dataset sizes, generation examples, temperature behavior, and beam-search scores.
- Updated the bonus forward and backward notebooks to document `mps` execution, verified expected arrays, and corrected saved-run conclusions.
- Refreshed [`docs/architecture/`](docs/architecture/index.md) so architecture links and metrics match the current files in `src/`.
- Updated [`README.md`](README.md) to use the current notebook filenames, validation commands, accelerator notes, and repository artwork links.

## 2026-04-19

- Added [`src/notebook_progress.py`](src/notebook_progress.py) and switched long-running notebooks to a shared progress helper with bounded scrollable output areas.
- Updated CIFAR-10, RNN, and bonus training loops to report live progress through tqdm postfix values instead of growing per-epoch print streams.
- Converted the bonus backward notebook from NumPy-backed model math to manual Torch tensor backpropagation on `mps`/`cuda`/`cpu`, while keeping NumPy for reference checks, plotting, and sklearn metrics.
- Converted the bonus forward notebook to run the custom forward-pass framework on Torch tensors with `mps`/`cuda`/`cpu` device selection.
- Replaced copied architecture notes with source-derived docs under [`docs/architecture/`](docs/architecture/index.md).
- Added generated repository artwork in [`docs/repo-icon.png`](docs/repo-icon.png) and [`docs/repo-banner.png`](docs/repo-banner.png), and embedded it in the README.

## 2026-04-18

- Created standalone `hw4` VS Code Python project beside the original notebook workspace.
- Moved HW4 source notebooks into `src/` at the new project root.
- Set up `uv` dependency management with the libraries required by the HW4 notebooks.
- Added VS Code Python and Jupyter workspace settings.
- Moved HW4-only local data into project-level `data/`, leaving `weatherAUS.csv` in the original workspace for HW2.
