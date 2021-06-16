# The-origin-of-a-late-type-galaxy.-Cosmological-simulations.
### Tools for analyzing cosmological simulations

## How to run the code

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

- Create an algorithm to calculate the mass center of the cosmic web, the galaxy and components from z=0 to  z= 10 (redshift). 

