import zntrack

from mace_models import LoadModel, XYZReader

project = zntrack.Project()

with project:
    LoadModel(
        model_path="data/ani500k_small_DFT.model",
        name="ani500k_small",
        info="""
        You're using the ani500k_small MACE model. The model is released under the MIT license.
        Note:
        If you are using this function, please cite the relevant paper associated with the MACE model, ANI dataset, and also the following:
        - "Evaluation of the MACE Force Field Architecture by Dávid Péter Kovács, Ilyes Batatia, Eszter Sára Arany, and Gábor Csányi, The Journal of Chemical Physics, 2023, URL: https://doi.org/10.1063/5.0155322
            """,
    )
    LoadModel(
        model_path="data/qm9_and_spice_hydrogenation.model",
        name="hydromace",
        info="""
        You're using the hydromace model. The model is released under the MIT license.
        """,
    )
    LoadModel(
        model_path="data/SPICE_sm_inv_neut_E0_swa.model",
        name="medium_spice",
        info="""
        You're using the medium_spice model. The model is released under the ASL license.
        Note:
        If you are using this function, please cite the relevant paper by Kovacs et.al., arXiv:2312.15211
              """,
    )
    LoadModel(
        model_path="data/SPICE_Mini_for_Gen_swa.model",
        name="small_spice",
        info="""
        You're using the small_spice model. The model is released under the ASL license.
        Note:
        If you are using this function, please cite the relevant paper by Kovacs et.al., arXiv:2312.15211
              """,
    )

    XYZReader(
        data_path="data/qm9_reference_data.xyz",
        name="simgen_reference_data_small",
        info="You're using QM9 data. Please cite the QM9 dataset paper. URL: https://doi.org/10.1038/sdata.2014.22",
    )
    XYZReader(
        data_path="data/qm9_reference_data_medium.xyz",
        name="simgen_reference_data_medium",
        info="You're using QM9 data. Please cite the QM9 dataset paper. URL: https://doi.org/10.1038/sdata.2014.22",
    )
    XYZReader(
        data_path="data/zinc_fragments_difflinker.xyz",
        name="linker_examples",
        info="You're using data from the DiffLinker paper. Please cite https://doi.org/10.48550/arXiv.2210.05274",
    )

project.run()
