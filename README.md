# map_deformation_measurements
Example images in the map_images folder, raw data in the data folder, python script which plots the data

#script.py

Script takes .csv file(s) with distances measured on the built map under "-m" argument; single file with ground
truth measurements under "-g" argument.

measurement .csv structure:

ticks | 1-2 | 1-3 | ...
-------|---- | ----|--------
map no1 | 10.2 |15.8 | ...
map no2 | 10.4 |15.1 | ...
. | 10.1 |15.6 | ...
. | 10.8 |15.7 | ...
. | 10.0 |15.8 | ...


Graph shows mean values of the each distance of each file. For each mean value "1-alpha" range is drawn and it 
is the range outside of which error will appear with "alpha" probability.


An example of calling python script:

python script.py -m data/FER_gmapping.csv data/FER_gmapping_wpm.csv data/FER_cartographer.csv -g data/FER_ground_truth.csv


Script is used for SLAM algorithms evaluation in the conference paper https://link.springer.com/chapter/10.1007/978-3-319-70833-1_2.
