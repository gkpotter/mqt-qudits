[![PyPI](https://img.shields.io/pypi/v/mqt.qudits?logo=pypi&style=flat-square)](https://pypi.org/project/mqt.qudits/)
![OS](https://img.shields.io/badge/os-linux%20%7C%20macos%20%7C%20windows-blue?style=flat-square)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square)](https://opensource.org/licenses/MIT)
[![CI](https://img.shields.io/github/actions/workflow/status/cda-tum/mqt-qudits/ci.yml?branch=main&style=flat-square&logo=github&label=ci)](https://github.com/cda-tum/mqt-qudits/actions/workflows/ci.yml)
[![CD](https://img.shields.io/github/actions/workflow/status/cda-tum/mqt-qudits/cd.yml?style=flat-square&logo=github&label=cd)](https://github.com/cda-tum/mqt-qudits/actions/workflows/cd.yml)
[![Documentation](https://img.shields.io/readthedocs/mqt-qudits?logo=readthedocs&style=flat-square)](https://mqt.readthedocs.io/projects/qudits)
[![codecov](https://img.shields.io/codecov/c/github/cda-tum/mqt-qudits?style=flat-square&logo=codecov)](https://codecov.io/gh/cda-tum/mqt-qudits)

<p align="center">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/cda-tum/mqt/main/docs/_static/mqt_light.png" width="60%">
   <img src="https://raw.githubusercontent.com/cda-tum/mqt/main/docs/_static/mqt_dark.png" width="60%">
 </picture>
</p>

# MQT Qudits - A framework for mixed-dimensional qudit quantum computing

A tool for research and education for mixed-dimensional qudit quantum computing developed as part of the _Munich Quantum Toolkit_ (_MQT_) by the [Chair for Design Automation](https://www.cda.cit.tum.de/) at the [Technical University of Munich](https://www.tum.de/).

<p align="center">
  <a href="https://mqt.readthedocs.io/projects/qudits">
  <img width=30% src="https://img.shields.io/badge/documentation-blue?style=for-the-badge&logo=read%20the%20docs" alt="Documentation" />
  </a>
</p>

If you have any questions, feel free to create a [discussion](https://github.com/cda-tum/mqt-qudits/discussions) or an [issue](https://github.com/cda-tum/mqt-qudits/issues) on [GitHub](https://github.com/cda-tum/mqt-qudits).

## Getting Started

`mqt.qudits` is available via [PyPI](https://pypi.org/project/mqt.qudits/) for all major operating systems and supports Python 3.8 to 3.12.

```console
(venv) $ pip install mqt.qudits
```

**Detailed documentation and examples are available at [ReadTheDocs](https://mqt.readthedocs.io/projects/qudits).**
The tool is presently in its Alpha release version. Within the repository and documentation, users can initiate their exploration of the library via a Jupyter notebook, showcasing its primary functionalities.
[Jupyter Notebook](https://github.com/cda-tum/mqt-qudits/blob/main/MQT%20Tutorial/MQT%20Qudits%20Tutorial.ipynb)

## System Requirements

The implementation is compatible with any C++17 compiler, a minimum CMake version of 3.19, and Python 3.8+.
Please refer to the [documentation](https://mqt.readthedocs.io/projects/qudits) on how to build the project.

Building (and running) is continuously tested under Linux, macOS, and Windows using the [latest available system versions for GitHub Actions](https://github.com/actions/virtual-environments).

## References

MQT Qudits has been developed based on methods proposed in the following papers:

- K. Mato, S. Hillmich and R. Wille, "[Mixed-Dimensional Qudit State Preparation Using Edge-Weighted Decision Diagrams]()," 2024 61st Design Automation Conference (DAC), San Francisco, USA, 2024.

- K. Mato, S. Hillmich and R. Wille, "[Mixed-Dimensional Quantum Circuit Simulation with Decision Diagrams](https://www.cda.cit.tum.de/files/eda/2023_mixed_dimensional_quantum_circuit_simulation_with_decision_diagrams.pdf)," 2023 IEEE International Conference on Quantum Computing and Engineering (QCE), Bellevue, Washington, USA, 2023.

- K. Mato, S. Hillmich, R. Wille, "Compression of Qubit Circuits: Mapping to Mixed-Dimensional Quantum Systems", IEEE QSW 2023 : IEEE International Conference on Quantum Software

- K. Mato, M. Ringbauer, S. Hillmich and R. Wille, "[Compilation of Entangling Gates for High-Dimensional Quantum Systems](https://www.cda.cit.tum.de/files/eda/2023_aspdac_qudit_entanglement_compilation.pdf)," 2023 28th Asia and South Pacific Design Automation Conference (ASP-DAC), Tokyo, Japan, 2023, pp. 202-208.

- K. Mato, M. Ringbauer, S. Hillmich and R. Wille, "[Adaptive Compilation of Multi-Level Quantum Operations](https://www.cda.cit.tum.de/files/eda/2022_qce_adaptive_compilation_of_multi_level_quantum_operations.pdf)," 2022 IEEE International Conference on Quantum Computing and Engineering (QCE), Broomfield, CO, USA, 2022, pp. 484-491, doi: 10.1109/QCE53715.2022.00070.

---

## Acknowledgements

Funded by the European Union under Horizon Europe Programme - Grant Agreement 101080086--NeQST.
Views and opinions expressed are however those of the author(s) only and do not necessarily reflect those of the European Union or European Climate, Infrastructure and Environment Executive Agency (CINEA). Neither the European Union nor the granting authority can be held responsible for them.

The Munich Quantum Toolkit has been supported by the European
Research Council (ERC) under the European Union's Horizon 2020 research and innovation program (grant agreement
No. 101001318), the Bavarian State Ministry for Science and Arts through the Distinguished Professorship Program, as well as the
Munich Quantum Valley, which is supported by the Bavarian state government with funds from the Hightech Agenda Bayern Plus.

<p align="center">
<picture>
<source media="(prefers-color-scheme: dark)" srcset="https://neqst-he.eu/icons/logo.svg" width="20%">
<img src="https://neqst-he.eu/icons/logo.svg" width="20%">
</picture>
<picture>
<source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/cda-tum/mqt/main/docs/_static/tum_dark.svg" width="20%">
<img src="https://raw.githubusercontent.com/cda-tum/mqt/main/docs/_static/tum_light.svg" width="20%">
</picture>
<picture>
<img src="https://raw.githubusercontent.com/cda-tum/mqt/main/docs/_static/logo-bavaria.svg" width="16%">
</picture>
<picture>
<source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/cda-tum/mqt/main/docs/_static/erc_dark.svg" width="20%">
<img src="https://raw.githubusercontent.com/cda-tum/mqt/main/docs/_static/erc_light.svg" width="20%">
</picture>
<picture>
<img src="https://raw.githubusercontent.com/cda-tum/mqt/main/docs/_static/logo-mqv.svg" width="20%">
</picture>
</p>
