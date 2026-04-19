# Architecture Notes

These notes describe the current HW4 source files under [`../../src`](../../src). They do not depend on copied notes from another workspace.

## Source Map

- [`../../src/CIFAR10.ipynb`](../../src/CIFAR10.ipynb): original CIFAR-10 task notebook covering data loading, binary classifiers, `CIFAR10Dataset`, and multi-class MLP training.
- [`../../src/p1_task_1_4_frog_ship_bin.ipynb`](../../src/p1_task_1_4_frog_ship_bin.ipynb): frog-vs-ship binary experiment sweep.
- [`../../src/p1_task_1_5_cat_dog_bin.ipynb`](../../src/p1_task_1_5_cat_dog_bin.ipynb): cat-vs-dog binary experiment sweep.
- [`../../src/p1_task_3_MCC.ipynb`](../../src/p1_task_3_MCC.ipynb): multi-class CIFAR-10 MLP sweep.
- [`../../src/p1_task_3_CNN.ipynb`](../../src/p1_task_3_CNN.ipynb): multi-class CIFAR-10 CNN experiment.
- [`../../src/p2_RNN_LM.ipynb`](../../src/p2_RNN_LM.ipynb): character-level dinosaur-name language model.
- [`../../src/bon_p2_forward.ipynb`](../../src/bon_p2_forward.ipynb): custom forward-pass framework using Torch tensors on `mps`/`cuda`/`cpu`.
- [`../../src/bon_p1_backward.ipynb`](../../src/bon_p1_backward.ipynb): custom backward-pass framework using Torch tensors on `mps`/`cuda`/`cpu`.
- [`../../src/notebook_progress.py`](../../src/notebook_progress.py): notebook-friendly progress helper used by long-running training loops.

## Notes

- [CIFAR-10 Workflows](cifar10-workflows.md)
- [RNN Language Model](rnn-language-model.md)
- [Bonus Forward and Backward Frameworks](bonus-frameworks.md)
- [Notebook Progress Handling](notebook-progress.md)

