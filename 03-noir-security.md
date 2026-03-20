# NOIR: Zero-Trust, Post-Quantum Security Layer

## Core Function

To ensure data sovereignty via client-side encryption and post-quantum safe key exchange.

## Technical Architecture

### The "See Nothing" Architecture
The NOIR Browser and API are architected to perform Client-Side Encryption (CSE) before data ever leaves the libnet layer. The server receives only ciphertext blobs (AES-256-GCM). Decryption keys are derived from user hardware TPM (Trusted Platform Module) keys, never stored in a database.

### Post-Quantum Key Exchange
We implement CRYSTALS-Kyber (NIST PQC Standard) for the initial handshake. This ensures that even if a transcript is recorded today, a future quantum computer cannot decrypt the session keys.

### Traffic Obfuscation
NOIR-NET wraps all packets in a custom protocol that mimics standard video streaming (UDP/QUIC) with randomized padding to prevent Traffic Analysis (fingerprinting).

## Tech Spec 1001

- **Encryption**: AES-256-GCM for data at rest/transit + XChaCha20-Poly1305 for stream encryption
- **Forward Secrecy**: Ephemeral key rotation for every session request

## Implementation Details

### Key Management
```python
class NoirKeyManager:
    def __init__(self):
        self.tpm_key = self._derive_from_tpm()
        self.session_keys = {}
    
    def create_session_key(self):
        # Generate ephemeral key using Kyber-1024
        return kyber.keygen()
```

### Encryption Pipeline
1. Client-side data encryption using AES-256-GCM
2. Session key exchange via Kyber-1024
3. Traffic obfuscation using custom UDP/QUIC protocol
4. Server receives only encrypted payloads