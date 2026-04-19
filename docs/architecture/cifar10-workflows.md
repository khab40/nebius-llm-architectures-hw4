# CIFAR-10 Workflows

Source notebooks:

- [`../../src/CIFAR10.ipynb`](../../src/CIFAR10.ipynb)
- [`../../src/p1_task_1_4_frog_ship_bin.ipynb`](../../src/p1_task_1_4_frog_ship_bin.ipynb)
- [`../../src/p1_task_1_5_cat_dog_bin.ipynb`](../../src/p1_task_1_5_cat_dog_bin.ipynb)
- [`../../src/p1_task_3_MCC.ipynb`](../../src/p1_task_3_MCC.ipynb)
- [`../../src/p1_task_3_CNN.ipynb`](../../src/p1_task_3_CNN.ipynb)

## Shared Flow

The CIFAR-10 notebooks load data with `torchvision.datasets.CIFAR10`, locate the project `data/` directory from the current working directory or its parents, and train PyTorch models with `DataLoader`. Device selection prefers an available accelerator and otherwise uses CPU. Long-running loops use [`../../src/notebook_progress.py`](../../src/notebook_progress.py).

The original [`../../src/CIFAR10.ipynb`](../../src/CIFAR10.ipynb) contains the broad task sequence:

- load CIFAR-10 and flatten images into `32 * 32 * 3 = 3072` pixel-channel features;
- train binary classifiers through `NetBin`, `train`, and `evaluate`;
- implement `CIFAR10Dataset`;
- train multi-class classifiers through `NetMCC`, `train`, and `evaluate`.

## Binary Experiments

[`../../src/p1_task_1_4_frog_ship_bin.ipynb`](../../src/p1_task_1_4_frog_ship_bin.ipynb) trains `BinaryMLP` models for frog-vs-ship classification. Its executed findings identify `3072 -> 512 -> 128 -> 1` with ReLU hidden activations, Sigmoid output, standardized flattened pixels, Adam, `lr=0.0005`, and batch size `64` as the best run. It reached `0.9525` test accuracy at epoch `18`, clearing the `>0.94` target.

[`../../src/p1_task_1_5_cat_dog_bin.ipynb`](../../src/p1_task_1_5_cat_dog_bin.ipynb) reuses the binary MLP pattern for the harder cat-vs-dog task. Its best executed run was `3072 -> 512 -> 256 -> 1` with BatchNorm, ReLU hidden activations, Sigmoid output, standardized pixels, Adam, `lr=0.0003`, batch size `64`, and `weight_decay=1e-5`. It reached `0.6665` test accuracy at epoch `7`, clearing the `>0.64` target.

## Multi-Class MLP

[`../../src/p1_task_3_MCC.ipynb`](../../src/p1_task_3_MCC.ipynb) builds multi-class MLP experiments with:

- `CIFAR10ExperimentDataset`;
- `compute_rgb_stats`;
- `make_loaders`;
- `MLPClassifier`;
- `make_optimizer`;
- `evaluate`;
- `train_one_experiment`.

The MLP uses `10` output logits for the ten CIFAR-10 classes and trains with `nn.CrossEntropyLoss`, so the final layer intentionally returns raw logits with no `Softmax`. The strongest executed MLP was `wide_bn_relu_512_256_128_standardized_adam`, equivalent to `3072 -> 512 -> 256 -> 128 -> 10` with BatchNorm and ReLU. It reached `0.5671` test accuracy at epoch `8`, clearing the `>0.53` target.

## Multi-Class CNN

[`../../src/p1_task_3_CNN.ipynb`](../../src/p1_task_3_CNN.ipynb) keeps CIFAR-10 images in channel-first shape `3 x 32 x 32` and defines:

- `CIFAR10ImageDataset`;
- `SmallCIFAR10CNN`;
- `make_cnn_loaders`;
- `clone_state_dict_to_cpu`;
- `train_one_cnn_experiment`.

The CNN also returns raw logits for `nn.CrossEntropyLoss`. Its executed configuration, `small_cnn_rgb_standardized_adam_60ep_plateau`, uses RGB standardization, horizontal-flip augmentation, Adam, `ReduceLROnPlateau`, best-checkpoint tracking, and early stopping configuration. The run completed all `60` epochs and reached best test accuracy `0.8492` at epoch `59`.

