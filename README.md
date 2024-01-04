[![ZnTrack](https://img.shields.io/badge/Powered%20by-ZnTrack-%23007CB0)](https://zntrack.readthedocs.io/en/latest/)

# Pre-trained MACE models

Models are taken from https://github.com/ACEsuit/mace/blob/docs/docs/examples/ANI_trained_MACE.zip

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
