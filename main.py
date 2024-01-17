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
        model_path="data/2023-10-29-mace-16M-pbenner-mptrj-no-conditional-loss.model",
        name="MACE-MP-0_large",
        info="""
        You're using the MACE-MP-0_large model. The model is released under the MIT license.
        Note:
        If you are using this model, please cite the relevant paper for the Materials Project,
        any paper associated with the MACE model, and also the following:
        - MACE-Universal by Yuan Chiang, 2023, Hugging Face, Revision e5ebd9b,
            DOI: 10.57967/hf/1202, URL: https://huggingface.co/cyrusyc/mace-universal
        - Matbench Discovery by Janosh Riebesell, Rhys EA Goodall, Philipp Benner, Yuan Chiang,
            Alpha A Lee, Anubhav Jain, Kristin A Persson, 2023, arXiv:2308.14920
        - https://arxiv.org/abs/2401.00096
           """,
    )

    LoadModel(
        model_path="data/2023-12-03-mace-128-L1_epoch-199.model",
        name="MACE-MP-0",
        info="""
        You're using the MACE-MP-0 model. The model is released under the MIT license.
        Note:
        If you are using this model, please cite the relevant paper for the Materials Project,
        any paper associated with the MACE model, and also the following:
        - MACE-Universal by Yuan Chiang, 2023, Hugging Face, Revision e5ebd9b,
            DOI: 10.57967/hf/1202, URL: https://huggingface.co/cyrusyc/mace-universal
        - Matbench Discovery by Janosh Riebesell, Rhys EA Goodall, Philipp Benner, Yuan Chiang,
            Alpha A Lee, Anubhav Jain, Kristin A Persson, 2023, arXiv:2308.14920
        - https://arxiv.org/abs/2401.00096
           """,
    )

    LoadModel(
        model_path="data/2023-12-10-mace-128-L0_energy_epoch-249.model",
        name="MACE-MP-0_small",
        info="""
        You're using the MACE-MP-0_small model. The model is released under the MIT license.
        Note:
        If you are using this model, please cite the relevant paper for the Materials Project,
        any paper associated with the MACE model, and also the following:
        - MACE-Universal by Yuan Chiang, 2023, Hugging Face, Revision e5ebd9b,
            DOI: 10.57967/hf/1202, URL: https://huggingface.co/cyrusyc/mace-universal
        - Matbench Discovery by Janosh Riebesell, Rhys EA Goodall, Philipp Benner, Yuan Chiang,
            Alpha A Lee, Anubhav Jain, Kristin A Persson, 2023, arXiv:2308.14920
        - https://arxiv.org/abs/2401.00096
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
