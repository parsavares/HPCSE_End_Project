# **HPCSE_Final_Project** 

# OpenFOAM-Documentation
 **Installation and Regression Testing of OpenFOAM** 

 OpenFOAM is a C++ toolbox for the development of customized numerical solvers, and pre-/post-processing utilities for the solution of continuum mechanics problems, most prominently including computational fluid dynamics (CFD). 
 
 **Scope** It is used in research organizations, academic institutes and across many types of industries, for example, automotive, manufacturing, process engineering and environmental engineering. 
 
**Purpose** The goals of this project are 
            1) To install recent versions of OpenFOAM on the Uni.lu HPC platform using EasyBuild.
            2) To set up a regression testing configuration for the installed OpenFOAM using ReFrame.

## **PART I. Installing latest release of EasyBuild & OpenFOAM** 

1. Allocating an interactive job with a high priority for 2 hours, using 1 node, 1 task, and 32 CPU cores.
 - **Command**: 
     ```bash
     salloc -p interactive --qos debug --time=2:00:00 -N 1 -n 1 -c 64
     ```
2. Installing the latest release of EasyBuild, a software build and installation framework.
- **Command**: 
     ```bash
     eb --install-latest-eb-release
     ```
3. Looking for available EasyBuild modules and their details.
- **Command**: 
     ```bash
     module spider easybuild
     ```
4. Now, by loading EasyBuild version 4.9.1 module, making its commands and environment available.
- **Command**: 
     ```bash
     module load tools/EasyBuild/4.9.1
     ```
5.The following command Adds the local directory of EasyBuild module files to the module path.
- **Command**: 
     ```bash
     module use ~/.local/easyconfig/modules/all
     ```
6. Running this command Adds a project-specific directory of EasyBuild module files to the module path.
- **Command**: 
     ```bash
     module use /work/projects/mhpc-softenv/easybuild/aion-epyc-prod-2023a/modules/all/
     ```
7. It Configures EasyBuild to use Slurm as the backend job scheduler for build jobs.
- **Command**: 
     ```bash
     export EASYBUILD_JOB_BACKEND='Slurm'
     ```
8. This command Sets the base directory for EasyBuild installations and builds to the user's home directory.
- **Command**: 
     ```bash
     export EASYBUILD_PREFIX=$HOME/easybuild
     ```
9. We Set the build path for EasyBuild to the shared memory directory, which can improve build performance.
- **Command**: 
     ```bash
     export EASYBUILD_BUILDPATH=/dev/shm/$USER
     ```
10. This command Checks for and lists any missing dependencies required for building OpenFOAM.
- **Command**: 
     ```bash
     eb /home/users/$USER/.local/easybuild/software/EasyBuild/4.9.1/easybuild/easyconfigs/o/OpenFOAM/OpenFOAM-v2312-foss-2023a.eb --missing
     ```
11. This command submits the OpenFOAM build as a job with 32 cores, a maximum wall time of 11 hours, resolving dependencies automatically, and tracing the build process.
    - by using `sq` you can see it running
    - after it finished OpenFOAM .out can be found at /home/users/$USER
    - the right output uploaded here you can check it. when you are opening the .out file, ath the end of it should have:
 - **Command**: 
     ```bash
     eb /home/users/$USER/.local/easybuild/software/EasyBuild/4.9.1/easybuild/easyconfigs/o/OpenFOAM/OpenFOAM-v2312-foss-2023a.eb --job --job-cores 32 --job-max-walltime 11 --robot --trace
     ```
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

12. It adds the user's EasyBuild module files directory to the module path.
- **Command**: 
    ```bash
    module use /home/users/$USER/easybuild/modules/all
    ```

13. loading OpenFOAM v2312 module built with the foss-2023a toolchain, making its commands and environment available.
- **Command**: 
    ```bash
    module load cae/OpenFOAM/v2312-foss-2023a
    ```

14. Now we repeat process again from the step 10th for installing OpenFOAM-11.
    - **Important**: don't forget to do: 1. `export EASYBUILD_JOB_BACKEND='Slurm'` 2. `export EASYBUILD_PREFIX=$HOME/easybuild` 3. `export EASYBUILD_BUILDPATH=/dev/shm/$USER` before doing this line.
 - **Command**: 
   ```bash
   eb /home/users/$USER/.local/easybuild/software/EasyBuild/4.9.1/easybuild/easyconfigs/o/OpenFOAM/OpenFOAM-11-foss-2023a.eb --job --job-cores 64 --job-max-walltime 3 --robot --trace
   ```

15.  Loading OpenFOAM 11 module built with the foss-2023a toolchain, making its commands and environment available.
- **Command**: 
     ```bash
    module load cae/OpenFOAM/11-foss-2023a
    ```
      

## **PART II. **

### Minimal Description for Running the OpenFOAM-v2312 `motorBike` Tutorial on HPC

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
    **Description**: Use SCP or a similar tool to upload `openfoam-OpenFOAM-v2312-tutorials-incompressible-simpleFoam-motorBike.zip` to `$HOME/OpenFOAM` on the HPC.
      - **Command**:
     ```bash
     scp openfoam-OpenFOAM-v2312-tutorials-incompressible-simpleFoam-motorBike.zip $HOME/OpenFOAM
     ```

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
     source /home/users/$USER/easybuild/software/OpenFOAM/v2312-foss-2023a/OpenFOAM-v2312/etc/bashrc
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
     srun -n 6 -c 10 ./Allrun
     ```

10. **Run the `Allrun` Script Directly (Optional)**
    - **Command**:
      ```bash
      ./Allrun
      ```
<!---
 ![image](https://github.com/parsavares/HPCSE_End_Project/assets/106035843/dcef86d4-9866-40f2-9f50-e8d797a0e7dd)
--> 
![9y8wrzf8](https://github.com/parsavares/HPCSE_End_Project/assets/161458338/2f8c9fa3-7d06-4c36-89cc-b3871ab37fb1)


# **Running Test Examples for Post Processing Phase** 
  # **Verification and Validation Example with OpenFOAM v2312** 
   **Loading required modules** 
   ```bash
   module load tools/EasyBuild/4.9.1
   module use ~/.local/easyconfig/modules/all
   module use /work/projects/mhpc-softenv/easybuild/aion-epyc-prod-2023a/modules/all/
   ```
   ```bash
   export EASYBUILD_JOB_BACKEND='Slurm'
   export EASYBUILD_PREFIX=$HOME/easybuild
   export EASYBUILD_BUILDPATH=/dev/shm/$USER
   ```
   **installing(optional if needed)** 
   ```bash

  eb /home/users/$USER/.local/easybuild/software/EasyBuild/4.9.1/easybuild/easyconfigs/o/OpenFOAM/OpenFOAM-v2312-foss-2023a.eb --job --job-cores 32 --job-max-walltime 11 --robot --trace
   ```

   ```bash
   module use /home/users/$USER/easybuild/modules/all
   module load cae/OpenFOAM/v2312-foss-2023a
   ```
**Testing 'turbulenceModels' from 'planeChannel'**

Now, we're gonna supposed to download tutorials of openfoam v2312, then upload them in openfoam directory that we have created for motorbike example: 
   ```bash
   wget https://develop.openfoam.com/Development/openfoam/-/archive/OpenFOAM-v2312/openfoam-OpenFOAM-v2312.zip?     path=tutorials/incompressible/simpleFoam -O openfoam-OpenFOAM-v2312-tutorials-incompressible-simpleFoam.zip
   mkdir -p $HOME/OpenFOAM
   scp openfoam-OpenFOAM-v2312-tutorials-incompressible-simpleFoam.zip $HOME/OpenFOAM
   unzip $HOME/OpenFOAM/openfoam-OpenFOAM-v2312-tutorials-incompressible-simpleFoam.zip -d $HOME/OpenFOAM
   cd $HOME/OpenFOAM/openfoam-OpenFOAM-v2312/tutorials/verificationAndValidation/turbulenceModels/planeChannel
  ```
Source the OpenFOAM Environment Setup

```bash
source /home/users/$USER/easybuild/software/OpenFOAM/v2312-foss-2023a/OpenFOAM-v2312/etc/bashrc
```
Verifying the Environment Variable 
```bash
echo $WM_PROJECT_DIR
```
![image](https://github.com/nahidjavadinara/OpenFOAM-Documentation/assets/161458338/2d7b007b-dffd-4fdb-8ea8-8b8da2a357e1) 

Execution and running 
```bash
chmod +x Allrun
srun -n 6 -c 10 ./Allrun
./Allrun
```
![image](https://github.com/nahidjavadinara/OpenFOAM-Documentation/assets/161458338/5e14d6a4-fe7b-487f-a990-3ef6ff926728)
![image](https://github.com/parsavares/HPCSE_End_Project/assets/161458338/ae69ec9b-9f15-4f05-85fa-3370f1e6cda1) 

Now, after running procedure it is possible to generate plots 
```bash
./plot
```
open the plots directory 
```bash
cd plots
```
![image](https://github.com/parsavares/HPCSE_End_Project/assets/161458338/477e3a8b-cdec-4ec4-9141-635f39056b13) 
 
 we see that all of .png files are saved in plots directory. (check ValidationVerfication folder for plots)


## **PART III. ** Reframe

# ReFrame Installation and Setup Guide

## Introduction
This section provides detail steps required for installing and setting up ReFrame on a system using EasyBuild and the Slurm job scheduler. The setup is intended for conducting HPC tests with specific emphasis on OpenFOAM applications.

### Step 1: Load EasyBuild Module
Load EasyBuild, a software build and installation framework.
```bash
module load tools/EasyBuild/4.9.1
```
### Step 2: Configure Module Paths 
```bash
module use ~/.local/easyconfig/modules/all
module use /work/projects/mhpc-softenv/easybuild/aion-epyc-prod-2023a/modules/all/
module use /home/users/$USER/easybuild/modules/all
```
### Step 3: Check ReFrame Version
Check if ReFrame 4.3.3 is available in the module list. 
```bash
module spider reframe
```
### Step 4: Environment Setup for Building ReFrame 
If ReFrame 4.3.3 is not found, setup environment variables and build it using EasyBuild. 
```bash
export EASYBUILD_JOB_BACKEND='Slurm'
export EASYBUILD_PREFIX=$HOME/easybuild
export EASYBUILD_BUILDPATH=/dev/shm/$USER
eb /home/users/pvares/.local/easybuild/software/EasyBuild/4.9.1/easybuild/easyconfigs/r/ReFrame/ReFrame-4.3.3.eb --job --job-cores 64 --job-max-walltime 3 --robot --trace
```
### Step 5: Load ReFrame 
```bash
module load devel/ReFrame/4.3.3
```
```bash
mkdir -p $HOME/ReFrame_test
cd $HOME/ReFrame_test
git clone https://github.com/reframe-hpc/hpc-tests.git
cd hpc-tests/apps/openfoam
```












