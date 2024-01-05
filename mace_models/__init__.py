import functools

import ase.io as aio
import torch
import zntrack

try:
    from mace.calculators import MACECalculator
except ImportError:
    print(
        """
WARNING: MACE is not installed!

You need to install MACE to use this package.
You can install it via 'pip install git+https://github.com/ACEsuit/mace.git'
"""
    )


class LoadModel(zntrack.Node):
    model_path: str = zntrack.deps_path()
    info: str = zntrack.meta.Text(None)

    def _post_load_(self) -> None:
        if self.info is not None:
            print(self.info)

    def run(self) -> None:
        pass

    @functools.lru_cache()
    def get_model(self, **kwargs) -> torch.nn.Module:
        with self.state.fs.open(self.model_path, "rb") as f:
            if kwargs.get("device", None) is None:
                return torch.load(f)
            else:
                model = torch.load(f, map_location=kwargs["device"])
                model.to(kwargs["device"])
                return model

    def get_calculator(self, device=None, dtype="float32") -> MACECalculator:
        """Return the ASE calculator."""
        if device is None:
            device = "cuda" if torch.cuda.is_available() else "cpu"

        with self.state.use_tmp_path():
            return MACECalculator(
                model_paths=self.model_path,
                device=device,
                default_dtype=dtype,
            )

    def get_file(self, filename: str = "mace.model") -> None:
        """Download the model to a file."""
        self.state.fs.get_file(self.model_path, filename)


class XYZReader(zntrack.Node):
    data_path: str = zntrack.deps_path()
    info: str = zntrack.meta.Text(None)
    
    def _post_load_(self) -> None:
        if self.info is not None:
            print(self.info)

    def run(self) -> None:
        pass

    @functools.lru_cache()
    def get_atoms(self):
        with self.state.fs.open(self.data_path, "r") as f:
            return aio.read(f, format="extxyz", index=":")


@functools.wraps(LoadModel.from_rev)
def load(*args, **kwargs) -> LoadModel:
    if len(args) == 0 and "name" not in kwargs:
        kwargs["name"] = "medium_spice"

    if len(args) == 0 and "remote" not in kwargs:
        kwargs["remote"] = "https://github.com/RokasEl/MACE-Models"

    return LoadModel.from_rev(*args, **kwargs)
