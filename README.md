[![ZnTrack](https://img.shields.io/badge/Powered%20by-ZnTrack-%23007CB0)](https://zntrack.readthedocs.io/en/latest/)
[![PyPI version](https://badge.fury.io/py/mace-models.svg)](https://badge.fury.io/py/mace-models)


# MACE models
Effortlessly integrate pre-trained MACE models into your projects with the user-friendly ``mace-models`` package.

```sh
pip install mace-models
```

Loading models is simple with a few lines of code:

```python
import mace_models

# Load a default MACE model
model = mace_models.load()
torch_model = model.get_model()
ase_calculator = model.get_calculator()
# get the model file 
model.get_file()
```

Customize your model selection by loading models from various repositories or specific revisions:

```python
model = mace_models.load(
    "<model-name>",
    rev="<branch-or-sha>",
    remote="https://github.com/<user>/<repo>"
)
```


Ensure a seamless integration by first installing the MACE library and upgrading your PyTorch installation:

```sh
pip install --upgrade torch --extra-index-url https://download.pytorch.org/whl/cu116
pip install git+https://github.com/ACEsuit/mace.git
```

# Models

- `ani500k_small` training data: https://www.nature.com/articles/sdata2017193
- `hydromace` https://github.com/RokasEl/hydromace
- `medium_spice` https://arxiv.org/abs/2312.15211
- `small_spice` https://arxiv.org/abs/2312.15211

## Example usages with ASE

```python
import mace_models
from ase.build import molecule

model = mace_models.load("medium_spice")

water = molecule("H2O")
water.calc = model.get_calculator(dtype="float64")

print(water.get_potential_energy())
>>> -14.159366
```

# References

Models are taken from https://github.com/ACEsuit/mace/blob/docs/docs/examples/ANI_trained_MACE.zip and from

```
@misc{kovacsMACEOFF23TransferableMachine2023,
  title = {MACE-OFF23: Transferable Machine Learning Force Fields for Organic Molecules},
  author = {Kov{\'a}cs, D{\'a}vid P{\'e}ter and Moore, J. Harry and Browning, Nicholas J. and Batatia, Ilyes and Horton, Joshua T. and Kapil, Venkat and Witt, William C. and Magd{\u a}u, Ioan-Bogdan and Cole, Daniel J. and Cs{\'a}nyi, G{\'a}bor},
  year = {2023},
  number = {arXiv:2312.15211},
}
```

MACE is described in
```
@misc{batatiaMACEHigherOrder2022,
  title = {{{MACE}}: {{Higher Order Equivariant Message Passing Neural Networks}} for {{Fast}} and {{Accurate Force Fields}}},
  shorttitle = {{{MACE}}},
  author = {Batatia, Ilyes and Kov{\'a}cs, D{\'a}vid P{\'e}ter and Simm, Gregor N. C. and Ortner, Christoph and Cs{\'a}nyi, G{\'a}bor},
  year = {2022},
  number = {arXiv:2206.07697},
  eprint = {2206.07697},
  primaryclass = {cond-mat, physics:physics, stat},
  publisher = {{arXiv}},
  urldate = {2022-06-19},
  archiveprefix = {arxiv},
  langid = {english}
}
```

