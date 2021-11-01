# EEE3097S
## Umutesa Munyurangabo & Batsile Molai
This is be our shared repository for our EEE3097S 2021 project.

This project is an extension of the buoy model design which will be installed on the pancake ice in the Southern Ocean in order to gather data on the ice for further research purposes. The aim is to design an ARM based IP to compress and encrypt data from an IMU sensor found in the SHARC Buoy.

Further information on the project is documented in our report found [here](https://github.com/BerthaMolai/EEE3097S/blob/main/Final%20Design%20Project%20Report.pdf).

The [compression](https://github.com/BerthaMolai/EEE3097S/tree/main/Compression_Algorithms) and [encryption](https://github.com/BerthaMolai/EEE3097S/tree/main/Encryptions%20Algorithms) subsystems were designed and tested separately, and these programs and tests can all be found in their respective folders.

When executed, the ICM20498.py program reads dta from the IMU and writes it to a file. The system.py program prompts the user to enter a file that needs to be compressed and encrypted, and upon processing the file: gives a key to further use when decrypting.
