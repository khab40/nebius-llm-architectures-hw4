# Architecture Notes

These notes describe the current HW4 source files under [`../../src`](../../src). They are derived from the notebooks and helper module in this repository.

## Source Map

- [`../../src/homework_CIFAR10.ipynb`](../../src/homework_CIFAR10.ipynb): merged CIFAR-10 notebook covering data loading, binary frog/ship and cat/dog classifiers, `CIFAR10Dataset`, and multi-class MLP sweeps.
- [`../../src/homework_CIFAR10_bonus_3_CNN.ipynb`](../../src/homework_CIFAR10_bonus_3_CNN.ipynb): separate CIFAR-10 CNN experiment for all 10 classes.
- [`../../src/RNN_LM_homework.ipynb`](../../src/RNN_LM_homework.ipynb): character-level dinosaur-name language model with top-k, temperature, and beam-search generation.
- [`../../src/Week 4 hometask bonus, forward.ipynb`](../../src/Week%204%20hometask%20bonus,%20forward.ipynb): custom forward-pass framework using Torch tensors on `mps`/`cuda`/`cpu`.
- [`../../src/Week 4 hometask bonus, backward.ipynb`](../../src/Week%204%20hometask%20bonus,%20backward.ipynb): custom backward-pass framework using Torch tensors on `mps`/`cuda`/`cpu`.
- [`../../src/notebook_progress.py`](../../src/notebook_progress.py): notebook-friendly progress helper used by long-running cells.

## Notes

- [CIFAR-10 Workflows](cifar10-workflows.md)
- [RNN Language Model](rnn-language-model.md)
- [Bonus Forward and Backward Frameworks](bonus-frameworks.md)
- [Notebook Progress Handling](notebook-progress.md)
