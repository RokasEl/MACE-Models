import zntrack

from mace_models import LoadModel, XYZReader

project = zntrack.Project()

with project:
    LoadModel(model_path="data/ani500k_small_DFT.model", name="ani500k_small")
    LoadModel(model_path="data/qm9_and_spice_hydrogenation.model", name="hydromace")
    
    XYZReader(data_path="data/qm9_reference_data.xyz", name="reference_data")
    XYZReader(data_path="data/zinc_fragments_difflinker.xyz", name="linker_examples")

project.run()
