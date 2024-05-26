import reframe as rfm
import reframe.utility.sanity as sn

@rfm.simple_test
class ChemFoamH2Test(rfm.RunOnlyRegressionTest):
    descr = 'Run chemFoam h2 tutorial with OpenFOAM'
    valid_systems = ['*']
    valid_prog_environs = ['*']
    sourcesdir = '$HOME/OpenFOAM/openfoam-OpenFOAM-v2312-tutorials-combustion-chemFoam-h2/tutorials/combustion/chemFoam/h2'
    
    executable = './Allrun'
    
    # Time limit for the test
    time_limit = '2h'

    # Define the pre- and post-run commands
    pre_run = [
        'module use ~/.local/easyconfig/modules/all',
        'module use /work/projects/mhpc-softenv/easybuild/aion-epyc-prod-2023a/modules/all/',
        'module use /home/users/$USER/easybuild/modules/all',
        'module load tools/EasyBuild/4.9.1',
        'module load cae/OpenFOAM/v2312-foss-2023a',
        'source /home/users/$USER/easybuild/software/OpenFOAM/v2312-foss-2023a/OpenFOAM-v2312/etc/bashrc',
        'chmod +x Allrun'
    ]

    # Sanity patterns to verify the simulation ran correctly
    sanity_patterns = sn.assert_found(r'End', sn.stdout)

    # Number of tasks and CPUs
    num_tasks = 6
    num_cpus_per_task = 6

    # Performance patterns (optional, add if you want to check performance)
    # perf_patterns = {
    #     'time': sn.extractsingle(r'ExecutionTime = (\S+) s', sn.stdout, 1, float)
    # }

    # Reference values for performance check (optional)
    # reference = {
    #     '*': {
    #         'time': (300, None, 0.1, 's'),
    #     }
    # }
