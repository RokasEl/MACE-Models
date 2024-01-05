import zntrack

from mace_models import LoadModel, XYZReader

project = zntrack.Project()

with project:
    LoadModel(
        model_path="data/ani500k_small_DFT.model",
        name="ani500k_small",
        info="""
              The model is released under the MIT license.
    Note:
        If you are using this function, please cite the relevant paper associated with the MACE model, ANI dataset, and also the following:
        - "Evaluation of the MACE Force Field Architecture by Dávid Péter Kovács, Ilyes Batatia, Eszter Sára Arany, and Gábor Csányi, The Journal of Chemical Physics, 2023, URL: https://doi.org/10.1063/5.0155322
            """,
    )
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
    LoadModel(
        model_path="data/SPICE_Mini_for_Gen_swa.model",
        name="small_spice",
        info="""
The model is released under the ASL license.
              
    Note:
        If you are using this function, please cite the relevant paper by Kovacs et.al., arXiv:2312.15211
              """,
    )

    LoadModel(
        model_path="data/2023-10-29-mace-16M-pbenner-mptrj-no-conditional-loss.model",
        name="MACE-MP-0_large",
    )

    LoadModel(
        model_path="data/2023-12-03-mace-128-L1_epoch-199.model",
        name="MACE-MP-0",
    )

    LoadModel(
        model_path="data/2023-12-10-mace-128-L0_energy_epoch-249.model",
        name="MACE-MP-0_small",
    )

    XYZReader(
        data_path="data/qm9_reference_data.xyz",
        name="simgen_reference_data_small",
        info="Please cite the QM9 dataset paper. URL: https://doi.org/10.1038/sdata.2014.22",
    )
    XYZReader(
        data_path="data/qm9_reference_data_medium.xyz",
        name="simgen_reference_data_medium",
        info="Please cite the QM9 dataset paper. URL: https://doi.org/10.1038/sdata.2014.22",
    )
    XYZReader(
        data_path="data/zinc_fragments_difflinker.xyz",
        name="linker_examples",
        info="Please cite the DiffLinker paper. URL: https://doi.org/10.48550/arXiv.2210.05274",
    )

project.run()
