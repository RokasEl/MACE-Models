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
        model_path="data/augmented_hydrogenation.model",
        name="hydromace",
        info="""
        You're using the hydromace model. The model is released under the MIT license.
        """,
    )
    LoadModel(
        model_path="data/qm9_only_hydrogenation.model",
        name="hydromace_qm9_only",
        info="""
        You're using the hydromace model. The model is released under the MIT license.
        """,
    )
    LoadModel(
        model_path="data/qm9_only_hydrogenation_high_noise.model",
        name="hydromace_qm9_only_high_noise",
        info="""
        You're using the hydromace model. The model is released under the MIT license.
        """,
    )
    LoadModel(
        model_path="data/spice_only_hydrogenation.model",
        name="hydromace_spice_only",
        info="""
        You're using the hydromace model. The model is released under the MIT license.
        """,
    )
    LoadModel(
        model_path="data/augmented_hydrogenation.model",
        name="augmented_hydromace",
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
        data_path="data/qm9_cleaned.xyz",
        name="qm9_all",
        info="You're using QM9 data. Please cite the QM9 dataset paper. URL: https://doi.org/10.1038/sdata.2014.22 \n These data correspond to using OpenBabel to generate SMILES from the QM9 dataset and removing fragmented or unsanitizable molecules.",
    )
    XYZReader(
        data_path="data/hydromace_training_data_augmented.xyz",
        name="hydromace_training",
        info="Training data for the hydromace model. Combination of cleaned QM9, subset of SPICE, and augmented with generated molecules.",
    )
    XYZReader(
        data_path="data/simgen_reference_data_nano.xyz",
        name="simgen_reference_data_nano",
        info="You're using QM9 data. Please cite the QM9 dataset paper. URL: https://doi.org/10.1038/sdata.2014.22",
    )
    XYZReader(
        data_path="data/simgen_reference_data_micro.xyz",
        name="simgen_reference_data_micro",
        info="You're using QM9 data. Please cite the QM9 dataset paper. URL: https://doi.org/10.1038/sdata.2014.22",
    )
    XYZReader(
        data_path="data/simgen_reference_data_tiny.xyz",
        name="simgen_reference_data_tiny",
        info="You're using QM9 data. Please cite the QM9 dataset paper. URL: https://doi.org/10.1038/sdata.2014.22",
    )
    XYZReader(
        data_path="data/simgen_reference_data_small.xyz",
        name="simgen_reference_data_small",
        info="You're using QM9 data. Please cite the QM9 dataset paper. URL: https://doi.org/10.1038/sdata.2014.22",
    )
    XYZReader(
        data_path="data/simgen_reference_data_medium.xyz",
        name="simgen_reference_data_medium",
        info="You're using QM9 data. Please cite the QM9 dataset paper. URL: https://doi.org/10.1038/sdata.2014.22",
    )
    XYZReader(
        data_path="data/simgen_reference_data_large.xyz",
        name="simgen_reference_data_large",
        info="You're using QM9 data. Please cite the QM9 dataset paper. URL: https://doi.org/10.1038/sdata.2014.22",
    )
    XYZReader(
        data_path="data/simgen_spice_reference_data_small.xyz",
        name="simgen_spice_reference_data_small",
        info="You're using SPICE data. Please cite the SPICE dataset paper. URL: https://doi.org/10.1038/s41597-022-01882-6",
    )
    XYZReader(
        data_path="data/simgen_spice_reference_data_medium.xyz",
        name="simgen_spice_reference_data_medium",
        info="You're using SPICE data. Please cite the SPICE dataset paper. URL: https://doi.org/10.1038/s41597-022-01882-6",
    )
    XYZReader(
        data_path="data/simgen_spice_reference_data_large.xyz",
        name="simgen_spice_reference_data_large",
        info="You're using SPICE data. Please cite the SPICE dataset paper. URL: https://doi.org/10.1038/s41597-022-01882-6",
    )
    XYZReader(
        data_path="data/zinc_fragments_difflinker.xyz",
        name="linker_examples",
        info="You're using data from the DiffLinker paper. Please cite https://doi.org/10.48550/arXiv.2210.05274",
    )
    XYZReader(
        data_path="data/dna_example_cut.xyz",
        name="DNA_example",
    )
    XYZReader(
        data_path="data/OA.xyz",
        name="OA_parent",
    )
    XYZReader(
        data_path="data/OA_ligands.xyz",
        name="OA_ligands",
    )
    XYZReader(
        data_path="data/OA_docked.xyz",
        name="OA_docked",
    )

project.repro()
