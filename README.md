[![ZnTrack](https://img.shields.io/badge/Powered%20by-ZnTrack-%23007CB0)](https://zntrack.readthedocs.io/en/latest/)
[![PyPI version](https://badge.fury.io/py/mace-models.svg)](https://badge.fury.io/py/mace-models)


# Pre-trained MACE models

Install the Model loader: `pip install mace-models` and load the models with:

```python
import mace_models

model = mace_models.load(
    rev="main"
)

model: "torch.nn.Module" = model.get_model()
calc: "mace.calculators.MACECalculator" = model.get_calculator()
```

Additionally a MACE installation is required:

```sh
pip install --upgrade torch --extra-index-url https://download.pytorch.org/whl/cu116
pip install git+https://github.com/ACEsuit/mace.git
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


