from typing import Iterable, List, Union

import numpy as np
import tensornetwork as tn

from mqt.qudits.qudit_circuits.circuit import QuantumCircuit
from mqt.qudits.qudit_circuits.components.instructions.gate import Gate
from mqt.qudits.qudit_circuits.components.instructions.gate_extensions.gate_types import GateTypes
from mqt.qudits.simulation.provider.backend_properties.quditproperties import QuditProperties
from mqt.qudits.simulation.provider.backends.backendv2 import Backend


class TNSim(Backend):
    @property
    def target(self):
        raise NotImplementedError

    @property
    def max_circuits(self):
        raise NotImplementedError

    def qudit_properties(self, qudit: Union[int, List[int]]) -> Union[QuditProperties, List[QuditProperties]]:
        raise NotImplementedError

    def drive_channel(self, qudit: int):
        raise NotImplementedError

    def measure_channel(self, qudit: int):
        raise NotImplementedError

    def acquire_channel(self, qudit: int):
        raise NotImplementedError

    def control_channel(self, qudits: Iterable[int]):
        raise NotImplementedError

    def run(self, circuit: QuantumCircuit, **options):
        self.system_sizes = circuit.dimensions
        self.circ_operations = circuit.instructions
        return self.__execute(self.system_sizes, self.circ_operations)

    @classmethod
    def _default_options(cls):
        pass

    def __init__(self, **fields):
        self.system_sizes = None
        self.circ_operations = None
        super().__init__(**fields)

    def __apply_gate(self, qudit_edges, gate, operating_qudits):
        op = tn.Node(gate)
        for i, bit in enumerate(operating_qudits):
            tn.connect(qudit_edges[bit], op[i])
            qudit_edges[bit] = op[i + len(operating_qudits)]

    def __execute(self, system_sizes, operations: List[Gate]):
        all_nodes = []

        with tn.NodeCollection(all_nodes):
            state_nodes = []
            for s in system_sizes:
                z = [0] * s
                z[0] = 1
                state_nodes.append(tn.Node(np.array(z, dtype="complex")))

            qudits_legs = [node[0] for node in state_nodes]

            for op in operations:
                op_matrix = op.to_matrix(identities=1)
                lines = op.reference_lines

                if op.gate_type == GateTypes.SINGLE:
                    op_matrix = op_matrix.reshape((system_sizes[lines[0]], system_sizes[lines[0]]))

                elif op.gate_type == GateTypes.TWO and not op.is_long_range:
                    op_matrix = op_matrix.reshape(
                        (system_sizes[lines[0]], system_sizes[lines[1]], system_sizes[lines[0]], system_sizes[lines[1]])
                    )

                elif op.is_long_range or op.gate_type == GateTypes.MULTI:
                    minimum_line, maximum_line = min(lines), max(lines)
                    interested_lines = list(range(minimum_line, maximum_line + 1))
                    inputs_outputs_legs = []
                    for i in interested_lines:
                        inputs_outputs_legs.append(system_sizes[i])
                    inputs_outputs_legs += inputs_outputs_legs

                    op_matrix = op_matrix.reshape(tuple(inputs_outputs_legs))
                    lines = interested_lines

                self.__apply_gate(qudits_legs, op_matrix, lines)

        return tn.contractors.optimal(all_nodes, output_edge_order=qudits_legs)