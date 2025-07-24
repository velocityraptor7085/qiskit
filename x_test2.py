import io
from qiskit import qpy, QuantumCircuit

class CustomWriter(io.RawIOBase):
    """A custom IO object that supports writes, but not seeking (nor reading but
    that's not relevant right now)."""

    def write(self, payload):
        pass

# Raises "io.UnsupportedOperation: seek"
qpy.dump(QuantumCircuit(), CustomWriter())