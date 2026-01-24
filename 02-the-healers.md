# The Healers: Interpretable Inference Pipelines

## Core Function
To provide medical-grade decision support where the inference logic is transparent and deterministic.

## Technical Architecture

### Attention Mechanism Extraction
We do not rely on "confidence scores." The Healers utilize modified Transformer architectures that export Attention Head weights alongside the output. This allows the system to highlight exactly which tokens in the input (symptoms, history) influenced the generated recommendation.

### Deterministic JSON Output
To prevent hallucinations in dosage or diagnosis, models are constrained via Grammar-Based Sampling (e.g., GBNF). The model is forced to output valid JSON that strictly conforms to a schema generated from medical ontologies (SNOMED CT, ICD-10).

### Dual-Accountability Loop
The system creates an immutable Audit Log (hash-chained) of every interaction. The UI renders the "AI Confidence" vs. "Evidence Score" distinctly, requiring a cryptographic signature from a verified practitioner to authorize any high-risk recommendation.

## Tech Spec 1001

- **XAI Method**: Layer-wise Relevance Propagation (LRP) or Integrated Gradients
- **Data Formatting**: FHIR (Fast Healthcare Interoperability Resources) compliant JSON structures