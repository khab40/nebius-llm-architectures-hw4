# Notebook Audit Report

## Summary
Audited notebooks: [`src/CIFAR10.ipynb`](src/CIFAR10.ipynb), [`src/p1_task_1_4_frog_ship_bin.ipynb`](src/p1_task_1_4_frog_ship_bin.ipynb), [`src/p1_task_1_5_cat_dog_bin.ipynb`](src/p1_task_1_5_cat_dog_bin.ipynb), [`src/p1_task_3_MCC.ipynb`](src/p1_task_3_MCC.ipynb)

Total notebooks: 4
Findings: 1 incorrectness identified
Overall assessment: Mostly correct implementations with strong experimental results and well-supported conclusions.

## Findings by Notebook

### `src/CIFAR10.ipynb`
- **Task Fulfillment**:
  - Task 1.1: Code implements a correct binary classification NN (Net class with 3072->512->128->1, ReLU hidden, Sigmoid output).
  - Task 1.2: Train function implemented correctly for binary classification with BCE loss.
  - Task 1.3: **Incorrectness** - Evaluate function is called but not defined for binary classification. The notebook has an evaluate function for multi-class but not for binary.
  - Task 1.4: No training code; refers to experiment notebook.
  - Task 1.5: No training code; refers to experiment notebook.
  - Task 3.1: NetMCC class implemented for multi-class (3072->512->256->128->10 with BatchNorm and ReLU).
  - Task 3.2: Train function adapted for multi-class.
  - Task 3.3: Evaluate function implemented for multi-class with CrossEntropy loss.
  - Task 3.4: No training code; refers to experiment notebook.

- **Result Correctness**: Code structures are correct; dynamic execution would need to verify outputs, but static analysis shows proper implementations.

- **Conclusion Support**: N/A (main notebook has no conclusions, only refers to exp notebooks).

### `src/p1_task_1_4_frog_ship_bin.ipynb`
- **Task Fulfillment**: Experiment code implements training sweeps for frog/ship binary classification, achieving >0.94 accuracy target.

- **Result Correctness**: Best accuracy 0.9525 at epoch 18, exceeding 0.94 target. Results show proper convergence and hyperparameter tuning.

- **Conclusion Support**: Conclusions logically supported by results - ReLU performs best, Adam converges quickly, overfitting observed after peak epoch. All claims backed by experimental data.

### `src/p1_task_1_5_cat_dog_bin.ipynb`
- **Task Fulfillment**: Experiment code implements training for cat/dog binary classification, achieving >0.64 accuracy target.

- **Result Correctness**: Best accuracy 0.6665 at epoch 7, exceeding 0.64 target. Shows BatchNorm helps, Dropout not beneficial.

- **Conclusion Support**: Conclusions supported - cat/dog harder than frog/ship, BatchNorm improves results, overfitting occurs. Data matches claims.

### `src/p1_task_3_MCC.ipynb`
- **Task Fulfillment**: Experiment code implements multi-class CIFAR-10 classification, achieving >0.53 accuracy target.

- **Result Correctness**: Best MLP accuracy 0.5671, exceeding the target. The CNN result is maintained separately in [`src/p1_task_3_CNN.ipynb`](src/p1_task_3_CNN.ipynb), where it reaches 0.8492. Proper loss/accuracy tracking is present.

- **Conclusion Support**: Well-supported conclusions - CNN much better than MLP for image tasks, BatchNorm/standardization beneficial, overfitting patterns observed. All quantitative claims verified by results.

## Overall Assessment
The notebooks demonstrate correct task implementation with strong experimental results. The main issue is the missing binary evaluate function in the main notebook. All accuracy targets are met, and conclusions are evidence-based. The experiments show good understanding of NN training, hyperparameter tuning, and architectural choices.
