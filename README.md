# Adaptive Quality-Aware Multi-Scale Lightweight 3D CNN for Explainable Lung Nodule Malignancy Prediction

[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.0%2B-red.svg)](https://pytorch.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

An end-to-end, clinically explainable deep learning CADx system for lung nodule malignancy classification on thoracic computed tomography (CT) scans from the **National Cancer Institute (NCI) LIDC-IDRI** benchmark dataset.

---

## 💾 Dataset & Source Links

The benchmark evaluation is conducted on the public **LIDC-IDRI** (Lung Image Database Consortium and Image Database Resource Initiative) cohort:

- **Kaggle Dataset Source:** [LIDC-IDRI on Kaggle (washingtongold/lidcidri30)](https://www.kaggle.com/datasets/washingtongold/lidcidri30)
- **Official TCIA Archive:** [The Cancer Imaging Archive (TCIA) LIDC-IDRI Collection](https://wiki.cancerimagingarchive.net/display/Public/LIDC-IDRI)

---

## 📌 Key Highlights & Contributions

- **Adaptive Quality Assessment (AQA):** Dynamically measures scan-specific noise standard deviation ($\sigma$) from ambient air ($-1150$ to $-800$ HU) and calibrates edge-preserving bilateral filtering ($d=3/5$) and CLAHE, preserving delicate malignant spiculation while eliminating quantum mottle.
- **Isotropic 3D Standardization:** Extracts $32\text{ mm}$ physical bounding cubes resampled via trilinear spline interpolation into standardized $64 \times 64 \times 64$ voxel grids ($0.50\text{ mm/voxel}$).
- **Multi-Scale Tri-Branch 3D Stem:** Parallel $3^3$, $5^3$, and $7^3$ 3D convolutions simultaneously resolve micro-textures, spicular margins, and diffuse ground-glass halos.
- **Embedded 3D CBAM Attention:** Successive 3D channel and spatial attention modules inside all 4 residual blocks spotlight lesion boundaries and suppress non-parenchymal background noise.
- **Cross-Modality Gated Fusion:** A learnable sigmoid gate dynamically integrates 3D CT visual features ($96\text{D}$) with 8 radiologist clinical semantic criteria ($32\text{D}$), yielding a **+6.14% accuracy gain** with only 9k gating parameters.
- **Strict Zero-Leakage Guarantee:** Patient-stratified Group 5-Fold Cross-Validation (`StratifiedGroupKFold`) ensures all nodules from the same patient remain strictly isolated within the same fold ($\text{Patients}_{\text{train}} \cap \text{Patients}_{\text{val}} = \emptyset$).
- **Extreme Parameter Efficiency:** **0.244M parameters (244,205)** — **99.62% model size reduction** compared to heavy baseline models (~64.7M parameters).
- **Explainable AI (3D Grad-CAM):** Multi-planar 5-column visualization (Axial CT, Saliency Map, Overlay, 2.5D Topology Surface, Orthogonal MPR) verifying true 3D spatial focus.

---

## 📊 Benchmark Results (LIDC-IDRI Cohort)

Evaluated across **441 consensus-verified nodule volumes** (188 Benign, 253 Malignant) from **298 unique patients**:

| Metric | Baseline Architecture (~64.7M) | Proposed Multimodal 3D ResNet (**0.244M**) |
| :--- | :---: | :---: |
| **Diagnostic Accuracy** | 93.00 % | **95.69 %** |
| **Sensitivity (Recall)** | 91.00 % | **96.44 %** ($244/253$ detected) |
| **Specificity** | 92.50 % | **94.68 %** ($178/188$ correct) |
| **ROC-AUC** | 0.950 | **0.9907 ± 0.0078** |
| **Trainable Parameters** | ~64.7 M | **0.244 M (-99.62%)** |
| **Inference Latency** | ~48.2 ms | **4.21 ms / volume** |
| **Model Size on Disk** | ~258 MB | **0.93 MB** |

---

## 🏛️ Model Architecture

```
                 ┌────────────────────────────────────────────────────────┐
                 │ 3D CT Volume ROI (64 × 64 × 64, 0.50 mm/voxel)         │
                 └──────────────────────────┬─────────────────────────────┘
                                            │
                                            ▼
               ┌──────────────────────────────────────────────────────────┐
               │ Multi-Scale Tri-Branch Stem (3³ || 5³ || 7³ Convolutions)│
               └──────────────────────────┬─────────────────────────────┘
                                            │
                                            ▼
               ┌──────────────────────────────────────────────────────────┐
               │ 4 Residual Stages with Embedded 3D CBAM Attention        │
               │ (32 → 48 → 64 → 96 channels, Channel + Spatial Attention)│
               └──────────────────────────┬─────────────────────────────┘
                                            │
                                            ▼
               ┌──────────────────────────────────────────┐
               │ Global Average Pooling (GAP) → 96-dim    │
               └────────────────────┬─────────────────────┘
                                    │
                                    │ ◄─── Cross-Modality Gated Attention ───► ┌──────────────────────────────────────┐
                                    │      Gate = σ(W_g · [v_img || v_clin])   │ 8 Semantic Clinical Descriptors      │
                                    │                                          └──────────────────┬───────────────────┘
                                    ▼                                                             │
               ┌──────────────────────────────────────────┐                                       ▼
               │ Gated Multimodal Representation (128-dim)│ ◄─────────────────────────── 2-Layer MLP → 32-dim
               └────────────────────┬─────────────────────┘
                                    │
                                    ▼
               ┌──────────────────────────────────────────┐
               │ Classification MLP Head (128 → 48 → 1)   │
               └────────────────────┬─────────────────────┘
                                    │
                                    ▼
               ┌──────────────────────────────────────────┐
               │ Output: P(Malignancy) [0.0, 1.0]         │
               └──────────────────────────────────────────┘
```

---

## 📁 Repository Structure

```
├── Results/
│   ├── AQA_preprocessed_img.png        # Adaptive Quality Assessment comparison
│   ├── validation_curve_roc_AUC.png    # 5-Fold validation AUC & Focal Loss trajectories
│   ├── AUC&matrix.png                  # 5-Fold ROC curves & calibrated confusion matrix
│   ├── grad-CAM.png                    # 5-Column multi-planar 3D Grad-CAM interpretability
│   └── model_architecture.jpg          # Model architecture blueprint diagram
├── requirements.txt                    # Project dependencies
├── .gitignore                          # Git ignore configuration
└── README.md                           # Project documentation
```

*(Note: The full end-to-end execution notebook will be updated in an upcoming commit).*

---

## 🚀 Installation & Setup

```bash
# Clone the repository
git clone https://github.com/Yashyashwanth07/lung-nodule-malignancy.git
cd lung-nodule-malignancy

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```
