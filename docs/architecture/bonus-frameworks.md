# Bonus Forward and Backward Frameworks

Source notebooks:

- [`../../src/Week 4 hometask bonus, forward.ipynb`](../../src/Week%204%20hometask%20bonus,%20forward.ipynb)
- [`../../src/Week 4 hometask bonus, backward.ipynb`](../../src/Week%204%20hometask%20bonus,%20backward.ipynb)

Both notebooks select `torch_device` in this order:

1. Apple Silicon `mps`;
2. CUDA;
3. CPU.

They keep the custom framework style from the homework while using Torch tensors for model math on the selected device. NumPy remains useful for seeded reference data, assertions, plotting, and external metrics.

## Forward Pass

[`../../src/Week 4 hometask bonus, forward.ipynb`](../../src/Week%204%20hometask%20bonus,%20forward.ipynb) defines:

- `Module`;
- `Linear`;
- `Sigmoid`;
- `NN`;
- conversion helpers `to_tensor`, `to_numpy`, `to_scalar`, `tensor_allclose`, and `randn`.

`Linear` stores `W` and `b` as Torch tensors on `torch_device` and computes `X @ W + b`. `Sigmoid` uses `torch.sigmoid`. The assembled network is `Linear(300, 200) -> Sigmoid -> Linear(200, 1) -> Sigmoid`.

The saved run used `mps`. The deterministic checks verify output shapes `(5, 1)` and `(2, 5)` for `Linear`, compare `Sigmoid` to `torch.sigmoid`, and verify the composed network output for a `(5, 300)` input. The smoke output records a small linear shape of `[4, 2]`, sigmoid range `[0.0969, 0.9031]`, network shape `[4, 1]`, and network output range `[0.0019, 0.9869]`.

## Backward Pass

[`../../src/Week 4 hometask bonus, backward.ipynb`](../../src/Week%204%20hometask%20bonus,%20backward.ipynb) defines:

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

The saved run used `mps` and all backward-pass unit checks passed. Full-batch training on the 2D blob dataset reached train log loss `0.10254896689348596`, test log loss `0.1068072459236171`, train accuracy `0.989`, and test accuracy `0.99`. Mini-batch SGD reached train log loss `0.12587983210923065`, test log loss `0.13210193682746113`, train accuracy `0.984`, and test accuracy `0.97`.

The image-classification path used local MNIST CSV files in the saved run. The loaded training frame has shape `(60000, 785)` and the test frame has shape `(10000, 785)` before filtering to digits `0` and `1`. The 0-vs-1 experiment uses `784` inputs, a hidden width of `32`, one sigmoid output, and reached final test accuracy `0.9905437352245863`.
