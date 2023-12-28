from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mqt.qudits.qudit_circuits.components.instructions.gate_set.csum import CSum
from mqt.qudits.qudit_circuits.components.instructions.gate_set.custom_multi import CustomMulti, CustomOne
from mqt.qudits.qudit_circuits.components.instructions.gate_set.custom_two import CustomTwo
from mqt.qudits.qudit_circuits.components.instructions.gate_set.cx import CEx
from mqt.qudits.qudit_circuits.components.instructions.gate_set.gellman import GellMann
from mqt.qudits.qudit_circuits.components.instructions.gate_set.h import H
from mqt.qudits.qudit_circuits.components.instructions.gate_set.ls import LS
from mqt.qudits.qudit_circuits.components.instructions.gate_set.ms import MS
from mqt.qudits.qudit_circuits.components.instructions.gate_set.perm import Perm
from mqt.qudits.qudit_circuits.components.instructions.gate_set.r import R
from mqt.qudits.qudit_circuits.components.instructions.gate_set.randu import RandU
from mqt.qudits.qudit_circuits.components.instructions.gate_set.rz import Rz
from mqt.qudits.qudit_circuits.components.instructions.gate_set.s import S
from mqt.qudits.qudit_circuits.components.instructions.gate_set.x import X
from mqt.qudits.qudit_circuits.components.instructions.gate_set.z import Z
from mqt.qudits.qudit_circuits.components.registers.quantum_register import QuantumRegister
from mqt.qudits.qudit_circuits.qasm_interface.qasm import QASM

if TYPE_CHECKING:
    import numpy as np

    from mqt.qudits.qudit_circuits.components.instructions.gate_extensions.controls import ControlData


def add_gate_decorator(func):
    def gate_constructor(circ, *args):
        gate = func(circ, *args)
        circ.number_gates += 1
        circ.instructions.append(gate)
        return gate

    return gate_constructor


class QuantumCircuit:
    __qasm_to_gate_set_dict: ClassVar[dict] = {
        "csum": "csum",
        "cuone": "cu_one",
        "cutwo": "cu_two",
        "cumulti": "cu_multi",
        "cx": "cx",
        "gell": "gellmann",
        "h": "h",
        "ls": "ls",
        "ms": "ms",
        "pm": "pm",
        "rxy": "r",
        "rdu": "randu",
        "rz": "rz",
        "s": "s",
        "x": "x",
        "z": "z",
    }

    def __init__(self, *args):
        self.number_gates = 0
        self.instructions = []
        self.quantum_registers = []
        self._sitemap = {}
        self._num_cl = 0
        self._num_qudits = 0
        self._dimensions = []

        if len(args) == 0:
            return
        if len(args) > 1:
            # case 1
            # num_qudits: int, dimensions_slice: List[int]|None, numcl: int
            self._num_qudits = args[0]
            self._dimensions = self._num_qudits * [2] if args[1] is None else args[1]
            self._num_cl = args[2]
        elif isinstance(args[0], QuantumRegister):
            # case 2
            # quantum register based construction
            register = args[0]
            self.append(register)

    @classmethod
    def get_qasm_set(cls):
        return cls.__qasm_to_gate_set_dict

    @property
    def num_qudits(self):
        return self._num_qudits

    @property
    def dimensions(self):
        return self._dimensions

    def reset(self):
        self.number_gates = 0
        self.instructions = []
        self.quantum_registers = []
        self._sitemap = {}
        self._num_cl = 0
        self._num_qudits = 0
        self._dimensions = []

    def append(self, qreg: QuantumRegister):
        self.quantum_registers.append(qreg)
        self._num_qudits += qreg.size
        self._dimensions += qreg.dimensions

        num_lines_stored = len(self._sitemap)
        for i in range(qreg.size):
            qreg.local_sitemap[i] = num_lines_stored + i
            self._sitemap[(str(qreg.label), i)] = (num_lines_stored + i, qreg.dimensions[i])

    @add_gate_decorator
    def csum(self, qudits: list[int]):
        return CSum(
            self, "CSum" + str([self.dimensions[i] for i in qudits]), qudits, [self.dimensions[i] for i in qudits], None
        )

    @add_gate_decorator
    def cu_one(self, qudits: int, parameters: np.ndarray, controls: ControlData | None = None):
        return CustomOne(
            self, "CUo" + str(self.dimensions[qudits]), qudits, parameters, self.dimensions[qudits], controls
        )

    @add_gate_decorator
    def cu_two(self, qudits: int, parameters: np.ndarray, controls: ControlData | None = None):
        return CustomTwo(
            self,
            "CUt" + str([self.dimensions[i] for i in qudits]),
            qudits,
            parameters,
            [self.dimensions[i] for i in qudits],
            controls,
        )

    @add_gate_decorator
    def cu_multi(self, qudits: int, parameters: np.ndarray, controls: ControlData | None = None):
        return CustomMulti(
            self,
            "CUm" + str([self.dimensions[i] for i in qudits]),
            qudits,
            parameters,
            [self.dimensions[i] for i in qudits],
            controls,
        )

    @add_gate_decorator
    def cx(self, qudits: list[int], parameters: list | None = None):
        return CEx(
            self,
            "CEx" + str([self.dimensions[i] for i in qudits]),
            qudits,
            parameters,
            [self.dimensions[i] for i in qudits],
            None,
        )

    @add_gate_decorator
    def gellmann(self, qudit: int, parameters: list | None = None, controls: ControlData | None = None):
        return GellMann(self, "Gell" + str(self.dimensions[qudit]), qudit, parameters, self.dimensions[qudit], controls)

    @add_gate_decorator
    def h(self, qudit: int, controls: ControlData | None = None):
        return H(self, "H" + str(self.dimensions[qudit]), qudit, self.dimensions[qudit], controls)

    @add_gate_decorator
    def ls(self, qudits: list[int], parameters: list | None = None):
        return LS(
            self,
            "LS" + str([self.dimensions[i] for i in qudits]),
            qudits,
            parameters,
            [self.dimensions[i] for i in qudits],
            None,
        )

    @add_gate_decorator
    def ms(self, qudits: list[int], parameters: list | None = None):
        return MS(
            self,
            "MS" + str([self.dimensions[i] for i in qudits]),
            qudits,
            parameters,
            [self.dimensions[i] for i in qudits],
            None,
        )

    @add_gate_decorator
    def pm(self, qudits: list[int], parameters: list):
        return Perm(
            self,
            "Pm" + str([self.dimensions[i] for i in qudits]),
            qudits,
            parameters,
            [self.dimensions[i] for i in qudits],
            None,
        )

    @add_gate_decorator
    def r(self, qudit: int, parameters: list, controls: ControlData | None = None):
        return R(self, "R" + str(self.dimensions[qudit]), qudit, parameters, self.dimensions[qudit], controls)

    @add_gate_decorator
    def randu(self, qudits: list[int] | int):
        return RandU(
            self, "RandU" + str([self.dimensions[i] for i in qudits]), qudits, [self.dimensions[i] for i in qudits]
        )

    @add_gate_decorator
    def rz(self, qudit: int, parameters: list, controls: ControlData | None = None):
        return Rz(self, "Rz" + str(self.dimensions[qudit]), qudit, parameters, self.dimensions[qudit], controls)

    @add_gate_decorator
    def s(self, qudit: int, controls: ControlData | None = None):
        return S(self, "S" + str(self.dimensions[qudit]), qudit, self.dimensions[qudit], controls)

    @add_gate_decorator
    def x(self, qudit: int, controls: ControlData | None = None):
        return X(self, "X" + str(self.dimensions[qudit]), qudit, self.dimensions[qudit], controls)

    @add_gate_decorator
    def z(self, qudit: int, controls: ControlData | None = None):
        return Z(self, "Z" + str(self.dimensions[qudit]), qudit, self.dimensions[qudit], controls)

    def from_qasm(self, qasm_prog):
        self.reset()
        qasm_parser = QASM().parse_ditqasm2_str(qasm_prog)
        instructions = qasm_parser["instructions"]
        temp_sitemap = qasm_parser["sitemap"]

        for qreg in QuantumRegister.from_map(temp_sitemap):
            self.append(qreg)

        qasm_set = self.get_qasm_set()

        for op in instructions:
            if op["name"] in qasm_set:
                gate_constructor_name = qasm_set[op["name"]]
                if hasattr(self, gate_constructor_name):
                    function = getattr(self, gate_constructor_name)

                    tuples_qudits = op["qudits"]
                    if not tuples_qudits:
                        msg = "Qudit parameter not applied"
                        raise IndexError(msg)
                    # Check if the list contains only one tuple
                    if len(tuples_qudits) == 1:
                        qudits_call = tuples_qudits[0][0]
                    # Extract the first element from each tuple and return as a list
                    else:
                        qudits_call = [t[0] for t in list(tuples_qudits)]
                    if op["params"]:
                        function(op["params"], qudits_call)
                    else:
                        function(qudits_call)
                else:
                    msg = "the required gate is not available anymore."
                    raise NotImplementedError(msg)

    def to_qasm(self):
        text = ""
        text += "DITQASM 2.0;\n"
        for qreg in self.quantum_registers:
            text += qreg.__qasm__
        for op in self.instructions:
            text += op.__qasm__

    def draw(self):
        # TODO
        pass