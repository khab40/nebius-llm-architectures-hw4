<p align="center">
  <img src="docs/repo-icon.png" alt="Nebius HW4 repository icon" width="120">
</p>

<h1 align="center">Nebius AI Performance Engineering HW4</h1>

<p align="center">
  <img src="docs/repo-banner.png" alt="Funny frog, cat, dog, ship, and dinosaur repository banner" width="720">
</p>

Standalone VS Code Python project for the HW4 notebooks. The project contains CIFAR-10 classification experiments, a character-level RNN language model, and custom forward/backward neural-network framework notebooks.

## Contents

- [`src/CIFAR10.ipynb`](src/CIFAR10.ipynb): original CIFAR-10 task notebook with data loading, binary classifiers, `CIFAR10Dataset`, and multi-class MLP training.
- [`src/p1_task_1_4_frog_ship_bin.ipynb`](src/p1_task_1_4_frog_ship_bin.ipynb): frog-vs-ship binary CIFAR-10 experiment.
- [`src/p1_task_1_5_cat_dog_bin.ipynb`](src/p1_task_1_5_cat_dog_bin.ipynb): cat-vs-dog binary CIFAR-10 experiment.
- [`src/p1_task_3_MCC.ipynb`](src/p1_task_3_MCC.ipynb): multi-class CIFAR-10 MLP experiment.
- [`src/p1_task_3_CNN.ipynb`](src/p1_task_3_CNN.ipynb): multi-class CIFAR-10 CNN experiment.
- [`src/p2_RNN_LM.ipynb`](src/p2_RNN_LM.ipynb): character-level dinosaur-name language model.
- [`src/bon_p2_forward.ipynb`](src/bon_p2_forward.ipynb): custom forward-pass framework using Torch tensors on `mps`/`cuda`/`cpu`.
- [`src/bon_p1_backward.ipynb`](src/bon_p1_backward.ipynb): custom backward-pass and mini-batch training framework using Torch tensors on `mps`/`cuda`/`cpu`.
- [`src/notebook_progress.py`](src/notebook_progress.py): shared notebook-friendly progress helper.
- [`docs/repo-icon.png`](docs/repo-icon.png): square repository icon.
- [`docs/repo-banner.png`](docs/repo-banner.png): README and social-preview banner artwork.
- [`docs/architecture/index.md`](docs/architecture/index.md): source-derived architecture notes for the notebooks.
- [`notebook-audit-report.md`](notebook-audit-report.md): HW4 notebook audit report.

## Data

Local data is kept under `data/` and ignored by git because the files are large or reproducible:

- `data/cifar-10-batches-py/` and `data/cifar-10-python.tar.gz` for CIFAR-10.
- `data/dinos.txt` for the RNN language model.
- `data/MNIST_csv/mnist_train.csv` and `data/MNIST_csv/mnist_test.csv` for the backward-pass image-classification smoke test.

The notebooks locate `data/` from the current working directory or its parents, so they work when VS Code starts kernels from either the project root or the `src/` folder.

## Environment

Install dependencies with uv:

```bash
uv sync --group dev
```

Open the folder in VS Code and select the workspace interpreter at `.venv/bin/python`. To start Jupyter from the managed environment:

```bash
uv run jupyter lab
```

Optional kernel registration:

```bash
uv run python -m ipykernel install --user --name nebius-hw4 --display-name "hw4 (.venv)"
```

## Accelerator Notes

The PyTorch notebooks prefer Apple Silicon `mps` when available, then CUDA, then CPU. The bonus forward and backward notebooks keep the custom layer/backpropagation style, but their model math now runs through Torch tensors on the selected device.

For long notebook cells, use `from notebook_progress import tqdm` through the existing import pattern in the notebooks. The helper provides widget progress bars when possible and bounded scrollable output when falling back to text progress.

## Validation

Check Python source syntax:

```bash
uv run python -m compileall src
```

Execute the shorter bonus notebooks:

```bash
uv run jupyter nbconvert --to notebook --execute src/bon_p2_forward.ipynb --output /tmp/bon_p2_forward.executed.ipynb
uv run jupyter nbconvert --to notebook --execute src/bon_p1_backward.ipynb --output /tmp/bon_p1_backward.executed.ipynb
```

The CIFAR-10 and RNN notebooks contain longer training cells; run them intentionally from VS Code or Jupyter Lab when GPU/CPU time is available.

## Repository Artwork

The repository artwork lives in [`docs/repo-icon.png`](docs/repo-icon.png) and [`docs/repo-banner.png`](docs/repo-banner.png). GitHub renders both from this README after the files are committed and pushed.

GitHub does not provide a separate per-repository icon setting. The closest standard web placement is the repository social preview image:

1. Open the repository on GitHub.
2. Go to **Settings**.
3. Scroll to **Social preview**.
4. Upload [`docs/repo-banner.png`](docs/repo-banner.png).
5. Save the repository description and topics in the **About** panel if needed.

For a square visual identity, keep [`docs/repo-icon.png`](docs/repo-icon.png) in the README or use it in any project page, release notes, or external course submission page.
