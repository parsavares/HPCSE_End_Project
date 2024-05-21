### HPCSE_End_Project Minimal Descriptions

#### salloc -p interactive --qos debug --time=2:00:00 -N 1 -n 1 -c 32
Allocates an interactive job with a high priority for 2 hours, using 1 node, 1 task, and 32 CPU cores.

#### eb --install-latest-eb-release
Installs the latest release of EasyBuild, a software build and installation framework.

#### module spider easybuild
Searches for available EasyBuild modules and their details.

#### module load tools/EasyBuild/4.9.1
Loads EasyBuild version 4.9.1 module, making its commands and environment available.

#### module use ~/.local/easyconfig/modules/all
Adds the local directory of EasyBuild module files to the module path.

#### module use /work/projects/mhpc-softenv/easybuild/aion-epyc-prod-2023a/modules/all/
Adds a project-specific directory of EasyBuild module files to the module path.

#### export EASYBUILD_JOB_BACKEND='Slurm'
Configures EasyBuild to use Slurm as the backend job scheduler for build jobs.

#### export EASYBUILD_PREFIX=$HOME/easybuild
Sets the base directory for EasyBuild installations and builds to the user's home directory.

#### export EASYBUILD_BUILDPATH=/dev/shm/$USER
Sets the build path for EasyBuild to the shared memory directory, which can improve build performance.

#### eb /home/users/pvares/.local/easybuild/software/EasyBuild/4.9.1/easybuild/easyconfigs/o/OpenFOAM/OpenFOAM-v2312-foss-2023a.eb --missing
Checks for and lists any missing dependencies required for building OpenFOAM.

#### eb /home/users/pvares/.local/easybuild/software/EasyBuild/4.9.1/easybuild/easyconfigs/o/OpenFOAM/OpenFOAM-v2312-foss-2023a.eb --job --job-cores 32 --job-max-walltime 11 --robot --trace
Submits the OpenFOAM build as a job with 32 cores, a maximum wall time of 11 hours, resolving dependencies automatically, and tracing the build process.

#### module use /home/users/pvares/easybuild/modules/all
Adds the user's EasyBuild module files directory to the module path.

#### module load cae/OpenFOAM/v2312-foss-2023a
Loads the OpenFOAM v2312 module built with the foss-2023a toolchain, making its commands and environment available.
