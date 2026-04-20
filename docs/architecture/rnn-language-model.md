# RNN Language Model

Source notebook: [`../../src/RNN_LM_homework.ipynb`](../../src/RNN_LM_homework.ipynb)

## Data Flow

The notebook locates `data/dinos.txt`, wraps names with `<` and `>`, joins the text, and creates fixed-length character sequences through `DinosDataset`. Each dataset item returns:

- input character IDs for a fixed sequence;
- next-character target IDs shifted by one position.

The saved notebook records `21,396` fixed-length sequences, split into `19,256` training items and `2,140` validation items. The vocabulary size is `28`, covering `<`, `>`, and lowercase letters used in the dinosaur names.

## Model and Training

The model path is:

- `one_hot_encode` converts integer batches from `[batch, seq_len]` to `[batch, seq_len, vocab_size]`;
- `CharRNN` uses a 2-layer LSTM and a final linear layer;
- `train` runs Adam, cross-entropy loss, hidden-state detaching, and gradient clipping.

The saved inspection shows integer batches `[64, 50]` becoming one-hot batches `[64, 50, 28]`. The inspected LSTM output is `[64, 50, 128]`, hidden and cell states are `[2, 64, 128]`, flattened output is `[3200, 128]`, logits are `[3200, 28]`, and the checked softmax distribution sums to `1.0000`.

The trained model is documented in the notebook as a 2-layer LSTM with input size `28`, hidden size `256`, dropout `0.3`, and output logits of size `28`. The training cell executed `20` epochs with scrollable progress widgets; the saved output stores widget progress rather than plain-text loss checkpoint values, so the architecture note does not quote exact train/validation losses.

## Generation

The notebook includes several generation strategies:

- prefix-conditioned `predict` and `sample`;
- top-k sampling;
- temperature sampling;
- `beam_search` with helper functions `_forward_char` and `_clone_hidden`.

Saved prefix samples include `<rus>`, `<astrodontaurus>`, `<brohitosaurus>`, `<trimelodon>`, and `<rexaedosaurus>`. Top-k sampling with `k=5` produced examples such as `<sarcilosaurus>`, `<mecrocephalosaurus>`, `<sinopelta>`, `<amphicoelicaudia>`, and `<lepidon>`.

Temperature sampling behaved as expected in the saved run: `temperature=0.5` produced more conservative names, while `temperature=1.5` produced more creative and less reliably name-like strings. Beam search was deterministic but not identical across beam sizes: `beam_size=2` returned `<macrophalangia>` with log score `-6.19`, while `beam_size=3` and `beam_size=5` returned `<megadactylus>` with log score `-5.98`.
