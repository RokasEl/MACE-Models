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
            return torch.load(f, **kwargs)

class XYZReader(zntrack.Node):
    data_path: str = zntrack.dvc.deps()

    def run(self) -> None:
        pass

    def get_atoms(self):
        with self.state.fs.open(self.data_path) as f:
            return aio.read(f, format="extxyz", index=":")