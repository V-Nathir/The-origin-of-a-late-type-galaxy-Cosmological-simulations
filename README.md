# The-origin-of-a-late-type-galaxy.-Cosmological-simulations.
### Tools for analyzing cosmological simulations

## How works the code

A cause of the data is intellectual property and can not be upload I create a mock data to run the code but some functions of the program must be removed. There are some informations that can be recreate. 

The free trial can be found in the folder [Mock_trial_version](https://github.com/V-Nathir/The-origin-of-a-late-type-galaxy.-Cosmological-simulations./tree/main/Mock_Trial_Version).

The code is modular, it is mean that exists a main script that use others with specific functions. The main script is named as CentralGalaxy.py or Mock_CentralGalaxy.py in the free trial version. The tree-root of the scripst that uses is: 

- CentralGalaxy.py use : 
  - Def_CentralGalaxy: contains the algorithm for the mass center calculation (when the name of a scrip is "def_name" this mean that "name"-scrip uses a lot this code.) 
  - InertiaTensor.py : performs the inertia tensor and the ellipsoid of intertia calculation. Also creates the Aitoff projection.
  - AngularMomentum.py : performs the angular momentum calculation.
  - equations.py : equations needed to convert from simulation units to physics units. 
  - Packages.py : basic packages.
  - PostCM_V3.py : Algorithm to find the particle with major overdensity.
  - units.py : units. 
  - vector.py : performs some plots. 
  
- ReadAndSave.py use: 
  - Def_ReadAndSave.py : selects and converts data from big endian to numpy arrays.
  - Packages.py 
 
Also exist two peripheral scripts to check some operations: 

  - CheckOut.py
  - CheckEigenvector.py

The code needs three folders to run: 
  - /CentralGalaxy  : contains three .dat with redshifts, identities and gas temperatures. Only one in the free trial. 
  - /CW : contains the list of particles of the Cosmic Web. 
  - /Data : contains the row data. 
 
But in the free trial version the /Data is not available so I provided the mock data in this folder:
 
 - /d5004 : contains the processed data. This folder is created by ReadAndSave.py script and is divided in three sub-branches. 
    - /MRV : contains the mass, position and velocity values.  (This is the only sub-branche in the free trial version.)
    - /HEADER : contains the header information for each simulation snap.
    - /BAR : barionic information. 

## About the project

The data of a AP3M-SPH cosmological simulation has been analyzed to find the origin of the components of a late-type galaxy using Python.

This is my Master's Thesis in the Astrophysic field for the Universidad Complutense de Madrid. 

In this research I have researched a possible relationship between the cosmic web and the components of a spiral galaxy, the spheroide formed by the halo and the bulge, and, the disck formed by the thin and thick disk.

The result of this project implies that the orientation between the cosmic web and the components affects to their evolution. It has been possible characterize this evolution with the History of Stars Formation, the morphology, the magnitude of the angular momentum, the history of mass accreted... 

For all of thes it has been necessary to create a code from scratch.

The Python project is divided in these tasks  : 

- Create a software to read and save the raw data given in Big Endian from the simulation, converting it into a simpler format. 

- Develope a code that can calculate and plot : 

  - Inertia Tensor and the Ellipsoid of Inertia. 
  - Angular Momentum.
  - Orientations between structures.
  - History of Stars Formation.
  - History of Mass Accreted.
  - Plot the sctructures in 3D with different information of interes.

- Create two robust algorithm to calculate an stable mass center for the cosmic web, the galaxy and components from z=0 to  z= 10 (redshift). 

