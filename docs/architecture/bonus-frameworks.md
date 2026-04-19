# Bonus Forward and Backward Frameworks

Source notebooks:

- [`../../src/bon_p2_forward.ipynb`](../../src/bon_p2_forward.ipynb)
- [`../../src/bon_p1_backward.ipynb`](../../src/bon_p1_backward.ipynb)

Both notebooks now select `torch_device` in this order:

1. Apple Silicon `mps`;
2. CUDA;
3. CPU.

They keep the custom framework style from the homework while using Torch tensors for model math on the selected device. NumPy remains useful for seeded reference data, assertions, plotting, and external metrics.

## Forward Pass

[`../../src/bon_p2_forward.ipynb`](../../src/bon_p2_forward.ipynb) defines:

- `Module`;
- `Linear`;
- `Sigmoid`;
- `NN`;
- conversion helpers `to_tensor`, `to_numpy`, `to_scalar`, `tensor_allclose`, and `randn`.

`Linear` stores `W` and `b` as Torch tensors on `torch_device` and computes `X @ W + b`. `Sigmoid` uses `torch.sigmoid`. The assembled network is `Linear(300, 200) -> Sigmoid -> Linear(200, 1) -> Sigmoid`.

The deterministic checks verify output shapes `(5, 1)` and `(2, 5)` for `Linear`, compare `Sigmoid` to `torch.sigmoid`, and verify the composed network output for a `(5, 300)` input.

## Backward Pass

[`../../src/bon_p1_backward.ipynb`](../../src/bon_p1_backward.ipynb) defines:

- `Module`;
- `Linear`;
- `Sigmoid`;
- `NN`;
- `LogLoss`;
- `DataLoader`;
- `train`;
- `train_stochastic`;
- conversion helpers `to_tensor`, `to_numpy`, `to_scalar`, `tensor_allclose`, `randn`, and `binary_predictions`.

`Linear.backward` manually computes:

- `dL/dW = X.T @ grad_output`;
- `dL/db = sum(grad_output)`;
- `dL/dX = grad_output @ W.T`.

It then applies the gradient-descent update directly to `W` and `b`. `Sigmoid.backward` applies `sigmoid(x) * (1 - sigmoid(x))`, and `LogLoss.backward` computes the binary cross-entropy gradient after clipping predictions.

The notebook includes full-batch and mini-batch training on a 2D blob dataset, plus an image-classification smoke path for digits `0` and `1`. The current code path keeps training tensors on the selected Torch device and converts back to CPU arrays only for plotting and sklearn metrics.

