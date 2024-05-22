# **HPCSE_Final_Project**
## **PART I. Installing latest release of EasyBuild & OpenFOAM**

1. **`salloc -p interactive --qos debug --time=2:00:00 -N 1 -n 1 -c 32`**
   - **Description**: Allocates an interactive job with a high priority for 2 hours, using 1 node, 1 task, and 32 CPU cores.

2. **`eb --install-latest-eb-release`**
   - **Description**: Installs the latest release of EasyBuild, a software build and installation framework.

3. **`module spider easybuild`**
   - **Description**: Searches for available EasyBuild modules and their details.

4. **`module load tools/EasyBuild/4.9.1`**
   - **Description**: Loads EasyBuild version 4.9.1 module, making its commands and environment available.

5. **`module use ~/.local/easyconfig/modules/all`**
   - **Description**: Adds the local directory of EasyBuild module files to the module path.

6. **`module use /work/projects/mhpc-softenv/easybuild/aion-epyc-prod-2023a/modules/all/`**
   - **Description**: Adds a project-specific directory of EasyBuild module files to the module path.

7. **`export EASYBUILD_JOB_BACKEND='Slurm'`**
   - **Description**: Configures EasyBuild to use Slurm as the backend job scheduler for build jobs.

8. **`export EASYBUILD_PREFIX=$HOME/easybuild`**
   - **Description**: Sets the base directory for EasyBuild installations and builds to the user's home directory.

9. **`export EASYBUILD_BUILDPATH=/dev/shm/$USER`**
   - **Description**: Sets the build path for EasyBuild to the shared memory directory, which can improve build performance.

10. **`eb /home/users/$USER/.local/easybuild/software/EasyBuild/4.9.1/easybuild/easyconfigs/o/OpenFOAM/OpenFOAM-v2312-foss-2023a.eb --missing`**
    - **Description**: Checks for and lists any missing dependencies required for building OpenFOAM.

11. **`eb /home/users/$USER/.local/easybuild/software/EasyBuild/4.9.1/easybuild/easyconfigs/o/OpenFOAM/OpenFOAM-v2312-foss-2023a.eb --job --job-cores 32 --job-max-walltime 11 --robot --trace`**
    - **Description**: Submits the OpenFOAM build as a job with 32 cores, a maximum wall time of 11 hours, resolving dependencies automatically, and tracing the build process.
    - by using `sq` you can see it running
    - after it finished OpenFOAM .out can be found at /home/users/$USER
    - the right output uploaded here you can check it. when you are opening the .out file, ath the end of it should have:
      
`
== COMPLETED: Installation ended successfully (took 1 hour 3 mins 41 secs)
`

`== Results of the build can be found in the log file(s) /home/users/$USER/easybuild/software/OpenFOAM/v2312-foss-2023a/eas$
`

`== Build succeeded for 1 out of 1
`

`== Temporary log file(s) /tmp/eb-j7o7pzoh/eb-txnweqte/easybuild-qnzsrnfi.log* have been removed.
`

`== Temporary directory /tmp/eb-j7o7pzoh/eb-txnweqte has been removed.
`

12. **`module use /home/users/$USER/easybuild/modules/all`**
    - **Description**: Adds the user's EasyBuild module files directory to the module path.

13. **`module load cae/OpenFOAM/v2312-foss-2023a`**
    - **Description**: Loads the OpenFOAM v2312 module built with the foss-2023a toolchain, making its commands and environment available.

13. **`eb /home/users/$USER/.local/easybuild/software/EasyBuild/4.9.1/easybuild/easyconfigs/o/OpenFOAM/OpenFOAM-11-foss-2023a.eb --job --job-cores 64 --job-max-walltime 3 --robot --trace`**
    - **Description**: now we repeat procees again from the 10th step for installing OpenFOAM-11.
    - **Important**: don't forget to do: 1. `export EASYBUILD_JOB_BACKEND='Slurm'` 2. `export EASYBUILD_PREFIX=$HOME/easybuild` 3. `export EASYBUILD_BUILDPATH=/dev/shm/$USER before doing this line`.

14. **`module load cae/OpenFOAM/11-foss-2023a`**
    - **Description**: Loads the OpenFOAM 11 module built with the foss-2023a toolchain, making its commands and environment available.
   
      
Parsa VARES

## **PART II. **

### Minimal Description for Running the OpenFOAM `motorBike` Tutorial on HPC

1. **Download the Tutorial Files**
   - **Command**: 
     ```bash
     wget https://develop.openfoam.com/Development/openfoam/-/archive/OpenFOAM-v2312/openfoam-OpenFOAM-v2312.zip?path=tutorials/incompressible/simpleFoam/motorBike -O openfoam-OpenFOAM-v2312-tutorials-incompressible-simpleFoam-motorBike.zip
     ```

2. **Create the Directory Structure**
   - **Command**:
     ```bash
     mkdir -p $HOME/OpenFOAM
     ```

3. **Upload the File to HPC**
   - **Description**: Use SCP or a similar tool to upload `openfoam-OpenFOAM-v2312-tutorials-incompressible-simpleFoam-motorBike.zip` to `$HOME/OpenFOAM` on the HPC.

4. **Unzip the Tutorial Files**
   - **Command**:
     ```bash
     unzip $HOME/OpenFOAM/openfoam-OpenFOAM-v2312-tutorials-incompressible-simpleFoam-motorBike.zip -d $HOME/OpenFOAM
     ```

5. **Navigate to the Tutorial Directory**
   - **Command**:
     ```bash
     cd $HOME/OpenFOAM/openfoam-OpenFOAM-v2312-tutorials-incompressible-simpleFoam-motorBike/tutorials/incompressible/simpleFoam/motorBike
     ```

6. **Source the OpenFOAM Environment Setup Script**
   - **Command**:
     ```bash
     source /home/users/pvares/easybuild/software/OpenFOAM/v2312-foss-2023a/OpenFOAM-v2312/etc/bashrc
     ```

7. **Verify the Environment Variable**
   - **Command**:
     ```bash
     echo $WM_PROJECT_DIR
     ```

8. **Make the `Allrun` Script Executable**
   - **Command**:
     ```bash
     chmod +x Allrun
     ```

9. **Run the `Allrun` Script Using `srun`**
   - **Command**:
     ```bash
     srun -n 1 -c 64 ./Allrun
     ```

10. **Run the `Allrun` Script Directly (Optional)**
    - **Command**:
      ```bash
      ./Allrun
      ```


## **PART II. **

