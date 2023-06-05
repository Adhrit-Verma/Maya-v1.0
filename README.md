# Smart-Portable-Assistant
 **Breif**
 It uses several python packages and ML models designed for next gen assisstance
 
 **Detail**
ADA: Autonomous Digital Ally
This full form suggests that the assistant is autonomous and can provide digital support and assistance, portraying a sense of reliability and companionship.

In this ***Commit*** at 15:51 PM changes made are :

**Code Modification:**

The code has been modified to include additional functionality for gathering system information.
A new class called SystemInfoGatherer has been created to encapsulate the logic for gathering system information.
The class has methods to gather information such as OS details, CPU information, memory information, disk information, drive count, PC location, internet connection status, and microphone availability.
The gathered information is stored in a dictionary called system_info which is then written to a JSON file named system_info.json.
The JSON file is saved in a specific directory based on the provided drive path.
The class also includes methods to check internet connection and microphone availability.

**Connection between Files:**

The code for gathering system information has been moved to a separate file named system_info_gatherer.py.
The present_data() function in the original code has been modified to import the SystemInfoGatherer class from the system_info_gatherer.py file.
The present_data() function now calls the gather_system_info() method of the SystemInfoGatherer class to gather system information and generate the system_info.json file.
The remaining part of the code in present_data() is responsible for reading and presenting the data from the system_info.json file.

**Additional Features:**

The code has been enhanced to determine the type of device it is (PC, Laptop, or Unknown) based on the machine type using the platform.machine() method.
The device type information is stored in the device_info dictionary along with the device category (PC, Laptop, or Unknown).
The device information is added to the system_info dictionary and included in the generated system_info.json file.
When presenting the data, the device type and category are displayed along with other system information.
These changes improve the functionality of the code by providing a modular approach to gather system information, storing it in a JSON file, and displaying it in a more organized manner. The addition of device type detection enhances the understanding of the type of device the system is running on.