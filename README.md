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

> [!TIP]
> If you want to persist the models locally, use 
> ```sh
> git clone https://github.com/RokasEl/MACE-Models
> cd MACE-Models
> dvc pull
> ```
> and use `mace_models.load(remote="/path/to/MACE-Models")`


# Models

The following models are available under the MIT license:

- `ani500k_small` Model: https://doi.org/10.1063/5.0155322 Training data: https://www.nature.com/articles/sdata2017193
- `hydromace` https://github.com/RokasEl/hydromace
- `MACE-MP-0_large` https://arxiv.org/abs/2401.00096
- `MACE-MP-0` https://arxiv.org/abs/2401.00096
- `MACE-MP-0_small` https://arxiv.org/abs/2401.00096

## Example usage with ASE

```python
import mace_models
from ase.build import molecule

model = mace_models.load("MACE-MP-0_small")

water = molecule("H2O")
water.calc = model.get_calculator(dtype="float64")

print(water.get_potential_energy())
>>> -14.047933366728305
```

# References

```
@article{kovacsEvaluationMACEForce2023,
  title = {Evaluation of the {{MACE}} Force Field Architecture: {{From}} Medicinal Chemistry to Materials Science},
  shorttitle = {Evaluation of the {{MACE}} Force Field Architecture},
  author = {Kov{\'a}cs, D{\'a}vid P{\'e}ter and Batatia, Ilyes and Arany, Eszter S{\'a}ra and Cs{\'a}nyi, G{\'a}bor},
  year = {2023},
  journal = {The Journal of Chemical Physics},
  volume = {159},
  number = {4},
  pages = {044118},
  issn = {0021-9606},
  doi = {10.1063/5.0155322},
  urldate = {2024-01-17}
}
```

```
@misc{batatiaFoundationModelAtomistic2023,
  title = {A Foundation Model for Atomistic Materials Chemistry},
  author = {Batatia, Ilyes and Benner, Philipp and Chiang, Yuan and Elena, Alin M. and Kov{\'a}cs, D{\'a}vid P. and Riebesell, Janosh and Advincula, Xavier R. and Asta, Mark and Baldwin, William J. and Bernstein, Noam and Bhowmik, Arghya and Blau, Samuel M. and C{\u a}rare, Vlad and Darby, James P. and De, Sandip and Della Pia, Flaviano and Deringer, Volker L. and Elijo{\v s}ius, Rokas and {El-Machachi}, Zakariya and Fako, Edvin and Ferrari, Andrea C. and {Genreith-Schriever}, Annalena and George, Janine and Goodall, Rhys E. A. and Grey, Clare P. and Han, Shuang and Handley, Will and Heenen, Hendrik H. and Hermansson, Kersti and Holm, Christian and Jaafar, Jad and Hofmann, Stephan and Jakob, Konstantin S. and Jung, Hyunwook and Kapil, Venkat and Kaplan, Aaron D. and Karimitari, Nima and Kroupa, Namu and Kullgren, Jolla and Kuner, Matthew C. and Kuryla, Domantas and Liepuoniute, Guoda and Margraf, Johannes T. and Magd{\u a}u, Ioan-Bogdan and Michaelides, Angelos and Moore, J. Harry and Naik, Aakash A. and Niblett, Samuel P. and Norwood, Sam Walton and O'Neill, Niamh and Ortner, Christoph and Persson, Kristin A. and Reuter, Karsten and Rosen, Andrew S. and Schaaf, Lars L. and Schran, Christoph and Sivonxay, Eric and Stenczel, Tam{\'a}s K. and Svahn, Viktor and Sutton, Christopher and {van der Oord}, Cas and {Varga-Umbrich}, Eszter and Vegge, Tejs and Vondr{\'a}k, Martin and Wang, Yangshuai and Witt, William C. and Zills, Fabian and Cs{\'a}nyi, G{\'a}bor},
  year = {2023},
  number = {arXiv:2401.00096},
  eprint = {2401.00096},
  primaryclass = {cond-mat, physics:physics},
  publisher = {{arXiv}},
  doi = {10.48550/arXiv.2401.00096},
  urldate = {2024-01-17},
  archiveprefix = {arxiv}
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

