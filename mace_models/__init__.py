import zntrack
import torch 
import functools

class LoadModel(zntrack.Node):
    model_path: str = zntrack.dvc.deps()

    def run(self) -> None:
        pass
    
    @functools.lru_cache()
    def get_model(self, **kwargs) -> torch.nn.Module:
        with self.state.fs.open(self.model_path, 'rb') as f:
            return torch.load(f, **kwargs)
