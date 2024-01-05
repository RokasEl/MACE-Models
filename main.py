import zntrack

from mace_models import LoadModel, XYZReader

project = zntrack.Project()

with project:
    LoadModel(model_path="data/ani500k_small_DFT.model", name="ani500k_small")
    LoadModel(model_path="data/qm9_and_spice_hydrogenation.model", name="hydromace")
    LoadModel(
        model_path="data/SPICE_sm_inv_neut_E0_swa.model",
        name="medium_spice",
        info="""
The model is released under the ASL license.
              
    Note:
        If you are using this function, please cite the relevant paper by Kovacs et.al., arXiv:2312.15211
              """,
    )
    LoadModel(model_path="data/SPICE_Mini_for_Gen_swa.model", name="small_spice")

    XYZReader(data_path="data/qm9_reference_data.xyz", name="reference_data")
    XYZReader(
        data_path="data/qm9_reference_data_medium.xyz", name="qm9_medium_examples"
    )
    XYZReader(data_path="data/zinc_fragments_difflinker.xyz", name="linker_examples")

project.run()
