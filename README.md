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
     salloc -p interactive --qos debug --time=2:00:00 -N 1 -n 1 -c 32
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
     srun -n 1 -c 32 ./Allrun
     ```

10. **Run the `Allrun` Script Directly (Optional)**
    - **Command**:
      ```bash
      ./Allrun
      ```

Similarly, we do verification and validation part to make sure of example results by comparing them with both v2312 and 11. 

# ** Running Test Examples for Post Processing Phase** 
  # **Verification and Validation Example with OpenFOAM v2312** 
   **Loading required modules** 
   ```bash
   module load tools/EasyBuild/4.9.1
   module use ~/.local/easyconfig/modules/all
   module use /work/projects/mhpc-softenv/easybuild/aion-epyc-prod-2023a/modules/all/
   export EASYBUILD_JOB_BACKEND='Slurm'
   export EASYBUILD_PREFIX=$HOME/easybuild
   export EASYBUILD_BUILDPATH=/dev/shm/$USER
  eb /home/users/$USER/.local/easybuild/software/EasyBuild/4.9.1/easybuild/easyconfigs/o/OpenFOAM/OpenFOAM-v2312-foss-2023a.eb --job --job-cores 32 --job-max-walltime 11 --robot --trace
   module use /home/users/$USER/easybuild/modules/all
   module load cae/OpenFOAM/v2312-foss-2023a
   ```
**Testing turbulenceModels from planeChannel**

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
srun -n 1 -c 32 ./Allrun
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
 
 we see that all of .png files are saved in plots directory. we can open and check .png files: 
 
![all_setups_yPlus_vs_epsilonPlus](https://github.com/parsavares/HPCSE_End_Project/assets/161458338/064d9284-f71d-455b-b29c-f323f2947c68)
![all_setups_yPlus_vs_kPlus0](https://github.com/parsavares/HPCSE_End_Project/assets/161458338/37eda302-3ceb-4735-ab38-9cd1fc25c468) 
![all_setups_yPlus_vs_kPlus1](https://github.com/parsavares/HPCSE_End_Project/assets/161458338/8fbd6300-2514-4cff-8e35-ab223ca3f637) 
![initial-iteration-residuals](https://github.com/parsavares/HPCSE_End_Project/assets/161458338/6c4c3a49-d873-4fc3-ac4d-a4cd5d374c96) 
![final-iteration-residuals](https://github.com/parsavares/HPCSE_End_Project/assets/161458338/06ecf7da-38a0-438c-8de3-b4c28ccf9c2f)
![yPlus_vs_uPlus](https://github.com/parsavares/HPCSE_End_Project/assets/161458338/41be7b13-201e-4643-8bd9-bb8cff815785)
![yPlus_vs_productionRatePlus](https://github.com/parsavares/HPCSE_End_Project/assets/161458338/5cc2b9e9-3792-4150-b492-a3404cafd01d)
![yPlus_vs_Rww](https://github.com/parsavares/HPCSE_End_Project/assets/161458338/91dbdbc1-2de7-4008-823b-fe64164999b8)
![yPlus_vs_Ruu](https://github.com/parsavares/HPCSE_End_Project/assets/161458338/b628af68-586f-43ec-98e6-3e5932c8d212)
![yPlus_vs_Rvv](https://github.com/parsavares/HPCSE_End_Project/assets/161458338/9022cda6-e3fe-46c5-94c3-2daacc87b831)







## **PART III. ** Reframe

