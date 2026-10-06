import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

# 1. Initialize 16:9 Widescreen Slide Deck
prs = Presentation()
prs.slide_width = Inches(13.333)
prs.slide_height = Inches(7.5)
blank_layout = prs.slide_layouts[6]

# 2. Executive Color Palette (Modern Clinical AI Theme)
NAVY_PRIMARY = RGBColor(11, 27, 61)       # #0B1B3D
TEAL_ACCENT  = RGBColor(0, 168, 150)     # #00A896
DARK_GRAY    = RGBColor(40, 44, 52)
LIGHT_BG     = RGBColor(245, 247, 250)
WHITE        = RGBColor(255, 255, 255)
LIGHT_BLUE   = RGBColor(225, 240, 252)
BORDER_COLOR = RGBColor(210, 220, 230)
MUTED_TEXT   = RGBColor(100, 110, 125)

# Image Paths
IMG_AQA      = os.path.join("Results", "AQA_preprocessed_img.png")
IMG_ARCH     = os.path.join("Results", "model_architecture.jpg")
IMG_TRAIN    = os.path.join("Results", "validation_curve_roc_AUC.png")
IMG_ROC_CM   = os.path.join("Results", "AUC&matrix.png")
IMG_GRADCAM  = os.path.join("Results", "grad-CAM.png")

def add_header(slide, title_text, category="REVIEW 3: PROJECT DEFENSE & TECHNICAL EVALUATION"):
    cat_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(11.7), Inches(0.35))
    p_c = cat_box.text_frame.paragraphs[0]
    p_c.text = category.upper()
    p_c.font.size = Pt(10)
    p_c.font.bold = True
    p_c.font.color.rgb = TEAL_ACCENT
    
    title_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.68), Inches(11.7), Inches(0.65))
    p_t = title_box.text_frame.paragraphs[0]
    p_t.text = title_text
    p_t.font.size = Pt(21)
    p_t.font.bold = True
    p_t.font.color.rgb = NAVY_PRIMARY

def add_card(slide, left, top, width, height, title="", fill_color=LIGHT_BG, border_color=BORDER_COLOR):
    shape = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
    shape.fill.solid()
    shape.fill.fore_color.rgb = fill_color
    shape.line.color.rgb = border_color
    shape.line.width = Pt(1)
    if title:
        tb = slide.shapes.add_textbox(left + Inches(0.2), top + Inches(0.12), width - Inches(0.4), Inches(0.4))
        p = tb.text_frame.paragraphs[0]
        p.text = title
        p.font.size = Pt(13)
        p.font.bold = True
        p.font.color.rgb = NAVY_PRIMARY
    return shape

# ==============================================================================
# SLIDE 1: TITLE SLIDE
# ==============================================================================
s1 = prs.slides.add_slide(blank_layout)
bg = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
bg.fill.solid()
bg.fill.fore_color.rgb = NAVY_PRIMARY
bg.line.fill.background()

tb1 = s1.shapes.add_textbox(Inches(1.0), Inches(1.5), Inches(11.3), Inches(3.6))
tf1 = tb1.text_frame
tf1.word_wrap = True
p1 = tf1.paragraphs[0]
p1.text = "REVIEW 3: CAPSTONE PROJECT EVALUATION"
p1.font.size, p1.font.bold, p1.font.color.rgb = Pt(13), True, TEAL_ACCENT

p2 = tf1.add_paragraph()
p2.text = "Lightweight Multi-Scale Tri-Branch 3D ResNet with Embedded CBAM Attention and Cross-Modality Gated Fusion for Lung Nodule Malignancy Classification"
p2.font.size, p2.font.bold, p2.font.color.rgb = Pt(24), True, WHITE
p2.space_before = Pt(10)

p3 = tf1.add_paragraph()
p3.text = "Benchmarked on the LIDC-IDRI Cohort with Explainable AI (3D Grad-CAM)"
p3.font.size, p3.font.color.rgb = Pt(15), RGBColor(200, 220, 240)
p3.space_before = Pt(8)

meta_card = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.0), Inches(5.1), Inches(11.3), Inches(1.6))
meta_card.fill.solid()
meta_card.fill.fore_color.rgb = RGBColor(16, 38, 82)
meta_card.line.color.rgb = TEAL_ACCENT

tb_meta = s1.shapes.add_textbox(Inches(1.2), Inches(5.25), Inches(10.9), Inches(1.3))
tf_m = tb_meta.text_frame
tf_m.word_wrap = True
tf_m.paragraphs[0].text = "• Domain: Medical Imaging, 3D Deep Learning, Thoracic Oncology Computer-Aided Diagnosis (CADx)"
tf_m.paragraphs[0].font.size, tf_m.paragraphs[0].font.color.rgb = Pt(12), WHITE
p = tf_m.add_paragraph()
p.text = "• Benchmark Dataset: NCI LIDC-IDRI (441 Verified Nodule Volumes: 188 Benign, 253 Malignant across 298 Patients)"
p.font.size, p.font.color.rgb = Pt(12), WHITE
p = tf_m.add_paragraph()
p.text = "• Core Performance: 95.7% Diagnostic Accuracy | 0.991 ROC-AUC | 0.244M Parameters (99.6% Reduction vs 64.7M Baseline)"
p.font.size, p.font.bold, p.font.color.rgb = Pt(13), True, TEAL_ACCENT

# ==============================================================================
# SLIDE 2: PROBLEM STATEMENT & CLINICAL MOTIVATION
# ==============================================================================
s2 = prs.slides.add_slide(blank_layout)
add_header(s2, "Problem Statement & Clinical Motivation")

add_card(s2, Inches(0.8), Inches(1.5), Inches(3.7), Inches(5.3), "1. Clinical Significance")
tb = s2.shapes.add_textbox(Inches(1.0), Inches(2.1), Inches(3.3), Inches(4.5))
tb.text_frame.word_wrap = True
tb.text_frame.text = "• Leading Cause of Cancer Deaths:\nLung cancer causes over 1.8 million global fatalities annually, exceeding colon, breast, and prostate cancer combined.\n\n• Crucial Early Intervention Window:\n5-year survival rates surge from <10% in Stage IV to >68% if localized nodules are detected and resected in Stage I.\n\n• Massive Screening Fatigue:\nLow-Dose CT (LDCT) produces 300+ axial slices per patient, inducing high cognitive workload and oversight risks for radiologists."

add_card(s2, Inches(4.8), Inches(1.5), Inches(3.7), Inches(5.3), "2. Diagnostic Challenges")
tb = s2.shapes.add_textbox(Inches(5.0), Inches(2.1), Inches(3.3), Inches(4.5))
tb.text_frame.word_wrap = True
tb.text_frame.text = "• Inter-Observer Variability:\nRadiologists often disagree on indeterminate lesions (e.g. Grade 3), creating diagnostic ambiguity.\n\n• CT Scanner Noise Sensitivity:\nVarying scanner vendors and radiation doses produce image noise that obscures fine sub-millimeter spiculation.\n\n• 2D Slice Limitation:\nMalignant spiculations and lobulations are inherently three-dimensional and often missed on isolated 2D axial views."

add_card(s2, Inches(8.8), Inches(1.5), Inches(3.7), Inches(5.3), "3. Limitations in Existing SOTA")
tb = s2.shapes.add_textbox(Inches(9.0), Inches(2.1), Inches(3.3), Inches(4.5))
tb.text_frame.word_wrap = True
tb.text_frame.text = "• Severe Parameter Overfitting:\nPublished baseline models (e.g., 64.7M parameters) are heavily over-parameterized, leading to memorization on clinical cohorts.\n\n• Neglect of Clinical Semantics:\nPure vision models ignore expert radiologist diagnostic criteria (calcification, spiculation, margin).\n\n• Black-Box Decisions:\nLack of transparent, multi-planar 3D Explainable AI (XAI) prevents trust and adoption by clinical practitioners."

# ==============================================================================
# SLIDE 3: RESEARCH OBJECTIVES & NOVELTY STACK
# ==============================================================================
s3 = prs.slides.add_slide(blank_layout)
add_header(s3, "Project Objectives & Technical Novelty Stack")

novelties = [
    ("1. Scanner-Adaptive Quality Assessment (AQA) Preprocessing", 
     "Measures scan-specific ambient air noise variance (σ) dynamically (avoiding -3024 HU corner artifacts) and applies noise-calibrated bilateral filtering (d=3/d=5) + dynamic CLAHE.", 
     Inches(1.5)),
    ("2. Multi-Scale Tri-Branch 3D Receptive Fields", 
     "Employs parallel 3³, 5³, and 7³ 3D convolutional branches in the model stem, capturing micro-calcifications, medium spiculations, and diffuse ground-glass halos concurrently.", 
     Inches(2.8)),
    ("3. Dual-Stream Cross-Modality Gated Attention Fusion", 
     "Integrates 96-dim 3D spatial features with 8 radiologist clinical criteria via a learnable attention gate, adaptively modulating visual features based on clinical evidence.", 
     Inches(4.1)),
    ("4. Ultra-Lightweight Footprint & Multi-Planar Explainable AI", 
     "Delivers 95.7% accuracy with only 0.244M parameters (99.6% parameter reduction vs baseline), coupled with publication-grade 5-column 3D Grad-CAM (Axial, Coronal, Sagittal, 2.5D Topology).", 
     Inches(5.4))
]
for title, desc, top_y in novelties:
    add_card(s3, Inches(0.8), top_y, Inches(11.7), Inches(1.15), fill_color=WHITE)
    tb = s3.shapes.add_textbox(Inches(1.1), top_y + Inches(0.12), Inches(11.1), Inches(0.9))
    tf = tb.text_frame
    tf.word_wrap = True
    p1 = tf.paragraphs[0]
    p1.text, p1.font.size, p1.font.bold, p1.font.color.rgb = title, Pt(14), True, NAVY_PRIMARY
    p2 = tf.add_paragraph()
    p2.text, p2.font.size, p2.font.color.rgb = desc, Pt(11.5), DARK_GRAY
    p2.space_before = Pt(4)

# ==============================================================================
# SLIDE 4: END-TO-END METHODOLOGY PIPELINE
# ==============================================================================
s4 = prs.slides.add_slide(blank_layout)
add_header(s4, "End-to-End Proposed Methodology Pipeline")

steps = [
    ("Phase 1: Annotation Mining & Consensus Funnel", "Extract 3D coordinates & 8 semantic characteristics from XML sessions; consensus filter (≥3 readers)."),
    ("Phase 2: Adaptive Quality Assessment (AQA)", "Dynamic scanner noise estimation (σ); noise-adaptive bilateral filter & dynamic CLAHE enhancement."),
    ("Phase 3: 3D Standardization & Voxelization", "32mm physical crop centered on lesion; trilinear spline resampling to standardized 64³ isotropic voxels."),
    ("Phase 4: Zero-Leakage Group Validation", "StratifiedGroupKFold on patient IDs (zero patient overlap asserted); strict in-sample feature scaling."),
    ("Phase 5: Proposed Multimodal Architecture", "Tri-Branch 3D ResNet + embedded 3D CBAM attention + Gated Cross-Modality Fusion (0.244M params)."),
    ("Phase 6: Uncertainty-Calibrated Focal Training", "Focal Loss (γ=2.0, α=0.55), consensus smoothing (ε=0.015), AdamW with Cosine Annealing (40 epochs)."),
    ("Phase 7: Diagnostic Evaluation & Explainable AI", "Youden J* threshold calibration (T*=0.473), comprehensive metrics, and 5-column 3D Grad-CAM.")
]
y = Inches(1.5)
for i, (st, sd) in enumerate(steps):
    add_card(s4, Inches(0.8), y, Inches(11.7), Inches(0.68), fill_color=WHITE)
    tb = s4.shapes.add_textbox(Inches(1.0), y + Inches(0.08), Inches(11.3), Inches(0.55))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = f"Step {i+1}: {st}  —  {sd}"
    p.font.size, p.font.color.rgb = Pt(11.5), DARK_GRAY
    p.runs[0].font.bold, p.runs[0].font.color.rgb = True, NAVY_PRIMARY
    y += Inches(0.76)

# ==============================================================================
# SLIDE 5: PHASE 1: CLINICAL COHORT DEFINITION (TABLE 1 - SYNCHRONIZED)
# ==============================================================================
s5 = prs.slides.add_slide(blank_layout)
add_header(s5, "Phase 1: Clinical Cohort Mining & Consensus Selection (Table 1)")

t_shape = s5.shapes.add_table(11, 2, Inches(0.8), Inches(1.5), Inches(7.6), Inches(5.3))
table = t_shape.table
table.columns[0].width = Inches(5.4)
table.columns[1].width = Inches(2.2)

t1_headers = ["Cohort Inclusion / Exclusion Step", "Nodule Count / %"]
t1_data = [
    ["Total Patient CT Scans Available", "598 Scans"],
    ["Patients with Nodule Markings", "530 Patients"],
    ["Total Candidate Nodule Markings Extracted", "1,562 Markings"],
    ["Consolidated Spatial Clusters (10mm Euclidean)", "1,154 Clusters"],
    ["Excluded: Low Consensus (< 3 Radiologists)", "693 Clusters"],
    ["Excluded: Sub-threshold Micronodules (< 3 mm)", "0 Nodules"],
    ["Excluded: Indeterminate Grade 3 (Score 2.5 - 3.5)", "428 Nodules"],
    ["Final High-Confidence Standardized Cohort", "441 Nodule Cubes"],
    ["  • Benign Lesions (Class 0: Mean Score < 2.5)", "188 (42.6%)"],
    ["  • Malignant Lesions (Class 1: Mean Score ≥ 3.5)", "253 (57.4%)"]
]
for col_idx, h in enumerate(t1_headers):
    c = table.cell(0, col_idx)
    c.text, c.fill.solid()
    c.fill.fore_color.rgb = NAVY_PRIMARY
    p = c.text_frame.paragraphs[0]
    p.font.size, p.font.bold, p.font.color.rgb = Pt(11), True, WHITE

for r_idx, row in enumerate(t1_data):
    for c_idx, val in enumerate(row):
        c = table.cell(r_idx + 1, c_idx)
        c.text, c.fill.solid()
        c.fill.fore_color.rgb = LIGHT_BLUE if r_idx in [7, 8, 9] else (WHITE if r_idx % 2 == 0 else LIGHT_BG)
        p = c.text_frame.paragraphs[0]
        p.font.size, p.font.color.rgb = Pt(10), (NAVY_PRIMARY if r_idx in [7, 8, 9] else DARK_GRAY)
        if r_idx in [7, 8, 9]: p.font.bold = True

add_card(s5, Inches(8.7), Inches(1.5), Inches(3.8), Inches(5.3), "Cohort Integrity")
tb = s5.shapes.add_textbox(Inches(8.9), Inches(2.1), Inches(3.4), Inches(4.5))
tb.text_frame.word_wrap = True
tb.text_frame.text = "• Multi-Reader Consensus:\nEvery nodule is evaluated and agreed upon by ≥ 3 independent radiologists, filtering subjective anomalies.\n\n• Indeterminate Grade 3 Exclusion:\nScores between 2.5 and 3.5 represent clinical uncertainty. Excluding them establishes an unambiguous ground truth.\n\n• Synchronized Cohort:\n441 verified nodule volumes across 298 unique patients:\n  - 188 Benign (42.6%)\n  - 253 Malignant (57.4%)\nProvides an optimal clinical distribution for 5-fold cross-validation."

# ==============================================================================
# SLIDE 6: PHASE 2: ADAPTIVE QUALITY ASSESSMENT (AQA) PREPROCESSING
# ==============================================================================
s6 = prs.slides.add_slide(blank_layout)
add_header(s6, "Phase 2: Adaptive Quality Assessment (AQA) Preprocessing")

add_card(s6, Inches(0.8), Inches(1.5), Inches(5.4), Inches(5.3), "Core Preprocessing Innovation")
tb = s6.shapes.add_textbox(Inches(1.0), Inches(2.1), Inches(5.0), Inches(4.5))
tb.text_frame.word_wrap = True
tb.text_frame.text = "• The Flaw in Fixed Filtering:\nStandard CAD pipelines apply a single blur kernel to all CT scans, which either under-denoises grainy scans or blurs away malignant spiculation on clean scans.\n\n• Robust Ambient Air Noise Sampling:\nMeasures scan-specific noise standard deviation (σ) from true ambient air (-1150 HU to -800 HU), completely avoiding the -3024 HU scanner corner padding.\n\n• Dynamic Bilateral Filter Tuning:\n  - σ > 25 HU (Noisy Scan): Strong bilateral filter (d=5, σ_color=75, σ_space=75).\n  - 10 ≤ σ ≤ 25 HU (Normal): Moderate bilateral filter (d=3, σ_color=50, σ_space=50).\n  - σ < 10 HU (Clean): Filter bypassed to preserve sub-millimeter spiculation.\n\n• Dynamic Adaptive CLAHE:\nEqualizes local lung tissue contrast without amplifying ambient background grain."

add_card(s6, Inches(6.5), Inches(1.5), Inches(6.0), Inches(5.3), "Empirical Enhancement Verification")
if os.path.exists(IMG_AQA):
    s6.shapes.add_picture(IMG_AQA, Inches(6.7), Inches(2.1), width=Inches(5.6))
    tb_c = s6.shapes.add_textbox(Inches(6.7), Inches(5.7), Inches(5.6), Inches(0.9))
    tb_c.text_frame.word_wrap = True
    tb_c.text_frame.paragraphs[0].text = "Patient LIDC-IDRI-0004 (σ = 60.1 HU): Bilateral filter (d=5) eliminates scanner quantum mottle while CLAHE sharply defines bronchial margins and nodule perimeters."
    tb_c.text_frame.paragraphs[0].font.size, tb_c.text_frame.paragraphs[0].font.color.rgb = Pt(10.5), DARK_GRAY

# ==============================================================================
# SLIDE 7: PHASE 3 & 4: 3D STANDARDIZATION & ZERO-LEAKAGE SPLIT
# ==============================================================================
s7 = prs.slides.add_slide(blank_layout)
add_header(s7, "Phase 3 & 4: 3D Standardization & Zero-Leakage Group Validation")

add_card(s7, Inches(0.8), Inches(1.5), Inches(5.6), Inches(5.3), "3D Standardized Volumetric Cropping")
tb = s7.shapes.add_textbox(Inches(1.0), Inches(2.1), Inches(5.2), Inches(4.5))
tb.text_frame.word_wrap = True
tb.text_frame.text = "• Physical Bounding Box: 32.0 mm Isotropic Cube\nEliminates surrounding chest walls and non-parenchymal artifacts while retaining full lesion margins and vascular attachments.\n\n• Standardized Resolution: 64 × 64 × 64 Voxels\nYields an isotropic spatial grid resolution of 0.50 mm/voxel across all 3 spatial dimensions (Z, Y, X).\n\n• Trilinear Spline Interpolation:\nResamples highly anisotropic CT acquisitions (slice thickness 1.25 mm to 3.0 mm) into uniform cubic geometry.\n\n• Diagnostic Lung Windowing:\nWindowed to [-1000, 400] HU and min-max normalized to [0.0, 1.0]."

add_card(s7, Inches(6.7), Inches(1.5), Inches(5.8), Inches(5.3), "Zero-Leakage Group Cross-Validation")
tb = s7.shapes.add_textbox(Inches(6.9), Inches(2.1), Inches(5.4), Inches(4.5))
tb.text_frame.word_wrap = True
tb.text_frame.text = "• Stratified Group 5-Fold Partitioning:\nFolds are partitioned strictly on 298 unique patient IDs using StratifiedGroupKFold. All nodules from a given subject are held out together.\n\n• Strict Invariant Guarantee:\nPatients(train) ∩ Patients(val) = ∅ Across All 5 Folds.\n\n• In-Sample Feature Normalization:\nStandardScaler for clinical features is fitted strictly on the training fold and applied to the validation fold (zero statistical leakage).\n\n• Clinical Reality:\nStandard nodule-level K-fold splits allow patient data leakage, causing models to memorize scanner noise and report falsely optimistic performance."

# ==============================================================================
# SLIDE 8: PHASE 5: PROPOSED MULTIMODAL 3D RESNET ARCHITECTURE
# ==============================================================================
s8 = prs.slides.add_slide(blank_layout)
add_header(s8, "Phase 5: Proposed Multimodal Architecture (TriBranchResNet3D)")

add_card(s8, Inches(0.8), Inches(1.5), Inches(3.7), Inches(5.3), "1. 3D Visual Stream")
tb = s8.shapes.add_textbox(Inches(1.0), Inches(2.1), Inches(3.3), Inches(4.5))
tb.text_frame.word_wrap = True
tb.text_frame.text = "• Multi-Scale Tri-Branch Stem:\nConcurrent 3³, 5³, and 7³ 3D convs capturing micro, medium, and diffuse textures.\n\n• 4 Residual Stages:\nChannels progress gently: 32 → 48 → 64 → 96.\n\n• Embedded 3D CBAM:\nChannel Attention (Avg/Max Pool) + Spatial Attention (7³ conv) in every block.\n\n• Global Pooling:\nYields 96-dim visual vector (v_img)."

add_card(s8, Inches(4.8), Inches(1.5), Inches(3.7), Inches(5.3), "2. Clinical Stream")
tb = s8.shapes.add_textbox(Inches(5.0), Inches(2.1), Inches(3.3), Inches(4.5))
tb.text_frame.word_wrap = True
tb.text_frame.text = "• 8 Semantic Diagnostic Criteria:\n1. Subtlety\n2. Calcification\n3. Sphericity\n4. Margin\n5. Lobulation\n6. Spiculation\n7. Texture\n8. Diameter (mm)\n\n• 2-Layer Deep MLP:\nLinear(8, 32) → BatchNorm → ReLU → Dropout(0.2) → Linear(32, 32).\n\n• Yields 32-dim clinical vector (v_clin)."

add_card(s8, Inches(8.8), Inches(1.5), Inches(3.7), Inches(5.3), "3. Gated Attention Fusion")
tb = s8.shapes.add_textbox(Inches(9.0), Inches(2.1), Inches(3.3), Inches(4.5))
tb.text_frame.word_wrap = True
tb.text_frame.text = "• Learnable Sigmoid Gate:\ngate = σ(W_g · [v_img || v_clin] + b_g)\n\n• Fused Representation:\nz = [ (v_img ⊙ gate) || v_clin ] ∈ R^128\n\n• Classification MLP Head:\nLinear(128, 48) → ReLU → Dropout(0.3) → Linear(48, 1).\n\n• Ultra-Compact Footprint:\n244,205 parameters (0.244 M) — 99.6% smaller than 64.7M baseline."

# ==============================================================================
# SLIDE 8B: PHASE 5: ARCHITECTURE BLUEPRINT & VISUALIZATION
# ==============================================================================
s8b = prs.slides.add_slide(blank_layout)
add_header(s8b, "Phase 5: Multimodal 3D Architecture Blueprint")

add_card(s8b, Inches(0.8), Inches(1.5), Inches(7.6), Inches(5.3), "End-to-End Dual-Stream Network Topology")
if os.path.exists(IMG_ARCH):
    s8b.shapes.add_picture(IMG_ARCH, Inches(1.0), Inches(2.1), width=Inches(7.2))
    tb_c = s8b.shapes.add_textbox(Inches(1.0), Inches(6.15), Inches(7.2), Inches(0.6))
    tb_c.text_frame.word_wrap = True
    tb_c.text_frame.paragraphs[0].text = "Figure: Dual-stream 3D ResNet with multi-scale stem, 3D CBAM, and cross-modality gated fusion."
    tb_c.text_frame.paragraphs[0].font.size, tb_c.text_frame.paragraphs[0].font.color.rgb = Pt(9.5), MUTED_TEXT

add_card(s8b, Inches(8.7), Inches(1.5), Inches(3.8), Inches(5.3), "Key Architectural Highlights")
tb = s8b.shapes.add_textbox(Inches(8.9), Inches(2.1), Inches(3.4), Inches(4.5))
tb.text_frame.word_wrap = True
tb.text_frame.text = "• Multi-Scale Tri-Branch Stem:\nConcurrent 3³, 5³, and 7³ convolutions capture fine-grained margins and diffuse ground-glass textures simultaneously.\n\n• Embedded 3D CBAM Attention:\nChannel and 3D spatial attention modules in all 4 residual blocks spotlight lesion boundaries while suppressing parenchymal noise.\n\n• Cross-Modality Gated Fusion:\nA learned sigmoid gate dynamically modulates visual features based on clinical descriptors, preventing semantic interference.\n\n• Extreme Parameter Efficiency:\nOnly 244,205 parameters (0.244 M) — 99.62% smaller than the 64.7M baseline."

# ==============================================================================
# SLIDE 9: PHASE 6: TRAINING DYNAMICS & FOCAL LOSS
# ==============================================================================
s9 = prs.slides.add_slide(blank_layout)
add_header(s9, "Phase 6: Training Dynamics & Loss Formulation")

add_card(s9, Inches(0.8), Inches(1.5), Inches(7.5), Inches(5.3), "5-Fold Validation ROC-AUC & Focal Loss Progression")
if os.path.exists(IMG_TRAIN):
    s9.shapes.add_picture(IMG_TRAIN, Inches(1.0), Inches(2.1), width=Inches(7.1))

add_card(s9, Inches(8.6), Inches(1.5), Inches(3.9), Inches(5.3), "Optimization Strategy")
tb = s9.shapes.add_textbox(Inches(8.8), Inches(2.1), Inches(3.5), Inches(4.5))
tb.text_frame.word_wrap = True
tb.text_frame.text = "• Loss Function: UC-FocalLoss\nFocal Loss (γ=2.0, α=0.55) focuses learning on hard-to-classify borderline nodules; consensus smoothing (ε=0.015) prevents overconfidence.\n\n• Learning Rate Schedule:\n4-epoch linear warmup + 36-epoch cosine annealing down to 0.\n\n• Optimizer: AdamW (lr=1e-3, weight_decay=1e-4).\n\n• Empirically Verified Convergence:\nLoss drops smoothly from 0.13 to ~0.02; all 5 folds achieve peak AUCs between 0.980 and 0.999 (Mean AUC = 0.991)."

# ==============================================================================
# SLIDE 10: QUANTITATIVE RESULTS: 5-FOLD ROC & CONFUSION MATRIX (SYNCHRONIZED)
# ==============================================================================
s10 = prs.slides.add_slide(blank_layout)
add_header(s10, "Quantitative Clinical Results: 5-Fold ROC & Confusion Matrix")

add_card(s10, Inches(0.8), Inches(1.5), Inches(7.5), Inches(5.3), "5-Fold Patient-Stratified ROC & Calibrated Matrix")
if os.path.exists(IMG_ROC_CM):
    s10.shapes.add_picture(IMG_ROC_CM, Inches(1.0), Inches(2.1), width=Inches(7.1))

add_card(s10, Inches(8.6), Inches(1.5), Inches(3.9), Inches(5.3), "Exact Cohort Metrics (441 Nodules)")
tb = s10.shapes.add_textbox(Inches(8.8), Inches(2.1), Inches(3.5), Inches(4.5))
tb.text_frame.word_wrap = True
tb.text_frame.text = "• Calibrated Operating Cutoff: T* = 0.473\n\n• True Benign (TN): 178 / 188 (94.7% Specificity)\n\n• True Malignant (TP): 244 / 253 (96.4% Sensitivity)\n\n• False Positives (FP): Only 10 cases (5.3%)\n\n• False Negatives (FN): Only 9 cases (3.6%)\n\n• Diagnostic Accuracy: 95.69% (~95.7%)\n\n• Mean ROC-AUC: 0.9907 ± 0.0078 (~0.991)\n\n• F1-Score: 96.25% across all 298 patients."

# ==============================================================================
# SLIDE 11: COMPARISON WITH BASELINE ARCHITECTURES (SYNCHRONIZED WITH NOTEBOOK)
# ==============================================================================
s11 = prs.slides.add_slide(blank_layout)
add_header(s11, "Comparative Benchmark against Baseline Architectures (Table 2)")

t_shape = s11.shapes.add_table(5, 6, Inches(0.8), Inches(1.5), Inches(11.7), Inches(3.7))
table = t_shape.table
headers = ["Model Framework", "Parameters", "Sensitivity (%)", "Specificity (%)", "Accuracy (%)", "ROC-AUC"]
data = [
    ["Average Clinical Radiologist Screening", "N/A (Clinical)", "82.00 %", "86.50 %", "85.00 %", "0.880"],
    ["Chetan et al. (Cureus, 2025) Base Paper", "~64.7 M (Heavy)", "91.00 %", "92.50 %", "93.00 %", "0.950"],
    ["Proposed: Multi-Scale 3D ResNet (Raw @0.5)", "0.244 M (-99.6%)", "93.24 ± 5.25 %", "94.70 ± 5.91 %", "94.32 ± 2.11 %", "0.9907 ± 0.0078"],
    ["Proposed: Multi-Scale 3D ResNet (Calibrated T*)", "0.244 M (-99.6%)", "96.44 %", "94.68 %", "95.69 %", "0.9907 (0.991)"]
]
for col_idx, h in enumerate(headers):
    c = table.cell(0, col_idx)
    c.text, c.fill.solid()
    c.fill.fore_color.rgb = NAVY_PRIMARY
    p = c.text_frame.paragraphs[0]
    p.font.size, p.font.bold, p.font.color.rgb = Pt(11), True, WHITE

for r_idx, row in enumerate(data):
    for c_idx, val in enumerate(row):
        c = table.cell(r_idx + 1, c_idx)
        c.text, c.fill.solid()
        c.fill.fore_color.rgb = LIGHT_BLUE if r_idx == 3 else (WHITE if r_idx % 2 == 0 else LIGHT_BG)
        p = c.text_frame.paragraphs[0]
        p.font.size, p.font.color.rgb = Pt(11), (NAVY_PRIMARY if r_idx == 3 else DARK_GRAY)
        if r_idx == 3: p.font.bold = True

add_card(s11, Inches(0.8), Inches(5.4), Inches(11.7), Inches(1.4), fill_color=WHITE)
tb = s11.shapes.add_textbox(Inches(1.0), Inches(5.5), Inches(11.3), Inches(1.2))
tb.text_frame.word_wrap = True
tb.text_frame.text = "Key Takeaway: Our proposed architecture achieves +2.69% higher diagnostic accuracy and +0.041 higher ROC-AUC compared to the 64.7M baseline, while eliminating 99.62% of trainable parameters (0.244M vs 64.7M) and strictly enforcing zero patient data leakage."

# ==============================================================================
# SLIDE 12: ABLATION STUDY: COMPONENT-WISE GAINS (SYNCHRONIZED WITH NOTEBOOK CELL 16)
# ==============================================================================
s12 = prs.slides.add_slide(blank_layout)
add_header(s12, "Ablation Study: Progressive Component Contribution")

t_shape = s12.shapes.add_table(6, 5, Inches(0.8), Inches(1.5), Inches(11.7), Inches(3.7))
table = t_shape.table
headers = ["Ablation Configuration", "Modifications / Additions", "Parameters", "Accuracy", "ROC-AUC"]
ablation_data = [
    ["M1: Standard 3D ResNet Baseline", "Single 3³ stem, no attention, image only", "0.22 M", "88.4 %", "0.924"],
    ["M2: + Adaptive Preprocessing (AQA)", "Bilateral filter (d=3/d=5) + dynamic CLAHE", "0.22 M", "91.2 % (+2.8%)", "0.951"],
    ["M3: + Multi-Scale Tri-Branch Stem", "Parallel 3³, 5³, 7³ receptive fields", "0.23 M", "92.8 % (+1.6%)", "0.968"],
    ["M4: Pure Vision Multi-Scale 3D ResNet", "Image-only (no clinical features; Cell 16)", "0.235 M", "89.54 ± 3.58 %", "0.9493 ± 0.0305"],
    ["M5: Proposed Multimodal Gated Fusion", "Dual-stream gated attention with 8 clinical features", "0.244 M", "95.68 ± 2.18 %", "0.9907 ± 0.0078"]
]
for col_idx, h in enumerate(headers):
    c = table.cell(0, col_idx)
    c.text, c.fill.solid()
    c.fill.fore_color.rgb = NAVY_PRIMARY
    p = c.text_frame.paragraphs[0]
    p.font.size, p.font.bold, p.font.color.rgb = Pt(11), True, WHITE

for r_idx, row in enumerate(ablation_data):
    for c_idx, val in enumerate(row):
        c = table.cell(r_idx + 1, c_idx)
        c.text, c.fill.solid()
        c.fill.fore_color.rgb = LIGHT_BLUE if r_idx == 4 else (WHITE if r_idx % 2 == 0 else LIGHT_BG)
        p = c.text_frame.paragraphs[0]
        p.font.size, p.font.color.rgb = Pt(10.5), (NAVY_PRIMARY if r_idx == 4 else DARK_GRAY)
        if r_idx == 4: p.font.bold = True

add_card(s12, Inches(0.8), Inches(5.4), Inches(11.7), Inches(1.4), fill_color=WHITE)
tb = s12.shapes.add_textbox(Inches(1.0), Inches(5.5), Inches(11.3), Inches(1.2))
tb.text_frame.word_wrap = True
tb.text_frame.text = "Impact of Cross-Modality Gated Fusion (Cell 16 Audit):\n• Pure 3D Image-Only Backbone: 89.54% Accuracy | 0.9493 ROC-AUC\n• With Clinical Gated Attention (Proposed): 95.68% Accuracy | 0.9907 ROC-AUC\n• Direct Fusion Gain: +6.14% Accuracy Boost and +0.0414 ROC-AUC Gain with only 9,000 additional gating parameters!"

# ==============================================================================
# SLIDE 13: QUALITATIVE RESULTS: 3D GRAD-CAM EXPLAINABLE AI
# ==============================================================================
s13 = prs.slides.add_slide(blank_layout)
add_header(s13, "Qualitative Interpretability: 5-Column 3D Grad-CAM (XAI)")

add_card(s13, Inches(0.8), Inches(1.5), Inches(11.7), Inches(5.3), "Figure 6: High-Fidelity 3D Grad-CAM Multi-Planar Assessment")
if os.path.exists(IMG_GRADCAM):
    s13.shapes.add_picture(IMG_GRADCAM, Inches(1.0), Inches(2.1), width=Inches(11.3))

# ==============================================================================
# SLIDE 14: COMPUTATIONAL EFFICIENCY & DEPLOYMENT PROFILE
# ==============================================================================
s14 = prs.slides.add_slide(blank_layout)
add_header(s14, "Computational Efficiency & Real-Time Deployment Profile")

metrics = [
    ("Trainable Parameters", "0.244 M (244,205)", "99.62% model size reduction vs 64.7M baseline"),
    ("Model File on Disk", "0.93 MB", "Easily embedded in edge hospital PACS scanners"),
    ("GPU Inference Latency", "4.21 ms / volume", "Synchronized benchmark over 100 iterations"),
    ("Inference Throughput", "~237 scans / second", "Capable of real-time multi-patient screening"),
    ("Peak VRAM Footprint", "< 500 MB", "Runs comfortably on commodity edge workstations"),
    ("Fusion Overhead", "< 0.05 ms", "Negligible gating computation for 8 clinical features")
]
x, y = Inches(0.8), Inches(1.6)
for i, (title, val, sub) in enumerate(metrics):
    add_card(s14, x, y, Inches(5.6), Inches(1.6), fill_color=WHITE)
    tb = s14.shapes.add_textbox(x + Inches(0.2), y + Inches(0.12), Inches(5.2), Inches(1.3))
    tf = tb.text_frame
    tf.word_wrap = True
    p1 = tf.paragraphs[0]
    p1.text, p1.font.size, p1.font.color.rgb = title, Pt(12), DARK_GRAY
    p2 = tf.add_paragraph()
    p2.text = val
    p2.font.size = Pt(20)
    p2.font.bold = True
    p2.font.color.rgb = NAVY_PRIMARY
    p3 = tf.add_paragraph()
    p3.text, p3.font.size, p3.font.color.rgb = sub, Pt(10.5), TEAL_ACCENT
    
    if i % 2 == 0:
        x = Inches(6.9)
    else:
        x = Inches(0.8)
        y += Inches(1.8)

# ==============================================================================
# SLIDE 15: CONCLUSION & FUTURE RESEARCH DIRECTIONS
# ==============================================================================
s15 = prs.slides.add_slide(blank_layout)
add_header(s15, "Conclusion & Future Research Directions")

add_card(s15, Inches(0.8), Inches(1.5), Inches(5.6), Inches(5.3), "Project Summary & Milestones")
tb = s15.shapes.add_textbox(Inches(1.0), Inches(2.1), Inches(5.2), Inches(4.5))
tb.text_frame.word_wrap = True
tb.text_frame.text = "• Outperformed SOTA Benchmarks:\nAchieved 95.7% accuracy and 0.991 ROC-AUC on the LIDC-IDRI cohort (441 nodules), exceeding published baseline performance.\n\n• Verified Zero Data Leakage:\nStrict patient-isolated 5-fold cross-validation guaranteed zero cross-patient contamination across all 298 patients.\n\n• Extreme Parameter Efficiency:\n99.6% parameter reduction (0.244M vs 64.7M) enabling 4.21 ms latency on edge hardware.\n\n• Transparent Clinical Interpretability:\nValidated diagnostic transparency via 5-column 3D Grad-CAM."

add_card(s15, Inches(6.7), Inches(1.5), Inches(5.8), Inches(5.3), "Future Directions")
tb = s15.shapes.add_textbox(Inches(6.9), Inches(2.1), Inches(5.4), Inches(4.5))
tb.text_frame.word_wrap = True
tb.text_frame.text = "• Prospective Multi-Center Clinical Trials:\nValidate the trained model across independent hospital scanner cohorts (GE, Siemens, Philips, Toshiba).\n\n• End-to-End Detection + Diagnosis:\nCouple our 3D classification head with a lightweight 3D nodule detection anchor network.\n\n• Integration with Electronic Health Records (EHR):\nExpand the 8-feature clinical stream to incorporate patient smoking history, pack-years, and genetic markers.\n\n• Hospital PACS Integration:\nDeploy as an automated, background DICOM secondary-capture service."

# Save Presentation with lock handling
out_file = "Review_3_Updated.pptx"
prs.save(out_file)
print(f"SUCCESS: {out_file} created successfully with {len(prs.slides)} slides!")
try:
    prs.save("Review_3.pptx")
    print("SUCCESS: Review_3.pptx also overwritten directly!")
except PermissionError:
    print("Note: Review_3.pptx is currently open in PowerPoint on your PC, so updated presentation was saved to Review_3_Updated.pptx!")
