# The-origin-of-a-late-type-galaxy.-Cosmological-simulations.
**Tools for analyzing cosmological simulations**

<a id="indice"></a>

- [About the project](#1)

- [How the code works](#2)

- [How to use the code](#3)

![T](/Gifs/CM_calculation.gif)
![T](/Gifs/temperatura.gif)

![T](/Gifs/Components.gif)


<a id="1"></a>
## [About the project](#indice)

The data of a AP3M-SPH cosmological simulation has been analyzed to find the origin of the components of a late-type galaxy using Python.

This is my Master's Thesis in Astrophysic for the Universidad Complutense de Madrid. 

In this project I have searched a possible relationship between the cosmic web and the components of a spiral galaxy, the spheroid formed by the halo and the bulge, and the disk formed by the thin and thick disk.

The result of this project implies that the orientation between the cosmic web and the components (of the galaxy) affect their evolution. It has been possible to characterize this evolution with the History of Stars Formation, the morphology, the magnitude of the angular momentum, the history of mass accreted... 

For all of this it has been necessary to create a code from scratch.

The Python project is divided in these tasks  : 

- Create a software to read and save the raw data given in Big Endian from the simulation, converting it into a simpler format. 

- Develop a code which can calculate and plot : 

  - Inertia Tensor and the Ellipsoid of Inertia. 
  - Angular Momentum.
  - Orientations between structures.
  - History of Stars Formation.
  - History of Mass Accreted.
  - Plot the structures in 3D with different information of interest.

- Create two robust algorithms to calculate a stable mass center for the cosmic web, the galaxy and its components from z=0 to  z= 10 (redshift). 

<a id="2"></a>
## [How the code works](#2)

The data is subject to IP laws and it cannot be uploaded, so I create a mock data to run the code. However, some functions of the program must be removed as there are some informations that cannot be recreated. 

The free trial can be found in the folder [Mock_trial_version](https://github.com/V-Nathir/The-origin-of-a-late-type-galaxy.-Cosmological-simulations./tree/main/Mock_Trial_Version).

The code is modular, which means that there is a main script that uses others with specific functions. The main script is named  CentralGalaxy.py or Mock_CentralGalaxy.py in the free trial version. The path tree of the script is: 

- CentralGalaxy.py uses : 
  - Def_CentralGalaxy: it contains the algorithm for the mass center calculation (when the name of a script is "def_name" this mean that "name"-scrip uses a lot this code.) 
  - InertiaTensor.py : performs the inertia tensor and the ellipsoid of intertia calculation. It also creates the Aitoff projection.
  - AngularMomentum.py : it performs the angular momentum calculation.
  - equations.py : equations needed to convert from simulation units to physics units. 
  - Packages.py : basic packages.
  - PostCM_V3.py : Algorithm to find the particle with major overdensity.
  - units.py : units. 
  - vector.py :it performs some plots. 
  
- ReadAndSave.py uses: 
  - Def_ReadAndSave.py : it selects and converts data from big endian to numpy arrays (the row data).
  - Packages.py 
 
There are also two peripheral scripts to check some operations: 

  - CheckOut.py
  - CheckEigenvector.py

The code needs three folders to run: 
  - /CentralGalaxy  : it contains three .dat with redshifts, identities and gas temperatures. Only one in the free trial. 
  - /CW : it contains the list of particles of the Cosmic Web. 
  - /Data : it contains the row data. 
 
However in the free trial version the /Data is not available so I provided the mock data in this folder:
 
 - /d5004 : it contains the processed data. This folder is created by ReadAndSave.py script and is divided in three sub-branches. 
    - /MRV : it contains the mass, position and velocity values.  (This is the only sub-branch in the free trial version.)
    - /HEADER : it contains the header information for each simulation snap.
    - /BAR : barionic information. 
    
<a id="3"></a>
## [How to use the code](#indice)

You need to clone the folder [Mock_trial_version](https://github.com/V-Nathir/The-origin-of-a-late-type-galaxy.-Cosmological-simulations./tree/main/Mock_Trial_Version)  and download the mock data https://drive.google.com/drive/folders/18cbDmcUqcDPyPLp7qfNrgPJ6FpN2Twf_?usp=sharing

All main folders must be in the same directory as the scripts. Example: CentralGalaxy.py reads ./CW or ./d5004_mock.

Then you can run the mock_CentralGalaxy.py or generate  new mock values with gen_mock.py. Please, use your terminal.

The script Mock_CentralGalaxy.py requires some inputs : 

- 1. If it is the first time that you run the code, enter 'yes'. This option selects the information of the particles for each structure. All the data of the particles is in /d5004_mock but without classifying  by its component. 
- 2. Then enter "yes" to generate the plots. 
- 3. The CM is already calculated because it requires some time, but you can enter "yes".
- 4. Enter 1,2,3 or 4
- 5. Enter 'no' ('yes' is not recommended while using the mock data) and then 'no' again (same reason)
- 6. Enter 1,2,3 or 4
- 7. Enter yes or no. 
