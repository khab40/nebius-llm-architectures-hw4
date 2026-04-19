# RNN Language Model

Source notebook: [`../../src/p2_RNN_LM.ipynb`](../../src/p2_RNN_LM.ipynb)

## Data Flow

The notebook locates `data/dinos.txt`, wraps names with `<` and `>`, joins the text, and creates fixed-length character sequences through `DinosDataset`. Each dataset item returns:

- input character IDs for a fixed sequence;
- next-character target IDs shifted by one position.

The executed notebook records `21,396` fixed-length sequences, split into `19,256` training items and `2,140` validation items. The vocabulary size is `28`.

## Model and Training

The model path is:

- `one_hot_encode` converts integer batches from `[batch, seq_len]` to `[batch, seq_len, vocab_size]`;
- `CharRNN` uses a 2-layer LSTM and a final linear layer;
- `train` runs Adam, cross-entropy loss, hidden-state detaching, and gradient clipping.

The source notebook documents the trained model as a 2-layer LSTM with input size `28`, hidden size `256`, dropout `0.3`, and output logits of size `28`.

## Generation

The notebook includes several generation strategies:

- greedy or probability-based `predict` and `sample`;
- top-k sampling;
- temperature sampling;
- `beam_search` with helper functions `_forward_char` and `_clone_hidden`.

The recorded results show validation loss improving through training, with a best printed validation loss of `0.4224` at epoch `20`, step `5900`. Sampling produced name-like strings, while beam sizes `2`, `3`, and `5` all returned `<protognathus>` in the recorded deterministic beam-search run.

