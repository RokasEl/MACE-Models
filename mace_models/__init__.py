import zntrack
import torch 
import functools
import ase.io as aio

class LoadModel(zntrack.Node):
    model_path: str = zntrack.dvc.deps()

    def run(self) -> None:
        pass
    
    @functools.lru_cache()
    def get_model(self, **kwargs) -> torch.nn.Module:
        with self.state.fs.open(self.model_path, 'rb') as f:
            if kwargs.get("device", None) is None:
                return torch.load(f)
            else:
                model = torch.load(f, map_location=kwargs["device"])
                model.to(kwargs["device"])
                return model
class XYZReader(zntrack.Node):
    data_path: str = zntrack.dvc.deps()

    def run(self) -> None:
        pass

    @functools.lru_cache()
    def get_atoms(self):
        with self.state.fs.open(self.data_path, "r") as f:
            return aio.read(f, format="extxyz", index=":")