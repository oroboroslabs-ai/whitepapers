# Quantum-Floor Models: Edge-Optimized Inference

## Core Function

High-density intelligence models optimized for local execution on consumer hardware (CPU/NPU).

## Technical Architecture

### Quantization-Aware Training (QAT)
Models are not simply compressed after training; they are trained specifically to operate at 4-bit (INT4) precision. This reduces VRAM requirements by ~4x with <1% loss in perplexity.

### Speculative Decoding
The "Quantum-Floor" runtime uses a smaller "draft" model (e.g., 1B params) to predict tokens, which are then verified in parallel by the larger model (REGIS-7B). This effectively doubles inference speed without hardware changes.

### Format Standardization
All models are distributed in GGUF format, enabling "mmap" (memory mapping) loading. This allows models to load instantly without eating up full system RAM, sharing memory between processes.

## Tech Spec 1001

- **Inference Engine**: Custom llama.cpp bindings with Metal (Apple Silicon) and Vulkan (Windows/Linux) backend support
- **Context Compression**: Sliding Window Attention with cache eviction policies to handle large documents on limited RAM

## Implementation Details

### Model Architecture
```python
class QuantumFloorModel:
    def __init__(self, model_path):
        self.model = GGUFModel.load(model_path)
        self.draft_model = GGUFModel.load(draft_path)
    
    def generate(self, prompt):
        # Speculative decoding pipeline
        draft_tokens = self.draft_model.predict(prompt)
        verified_tokens = self.model.verify(draft_tokens)
        return verified_tokens
```

### Performance Optimization
- **Memory Mapping**: Models load instantly via mmap
- **Cache Management**: Sliding window attention reduces memory usage
- **Parallel Processing**: Draft and verification models run concurrently