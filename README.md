# Smart-Portable-Assistant

**Brief**
Smart-Portable-Assistant is an advanced assistant powered by Python packages and ML models, designed to provide next-gen support and assistance.

**Overview**
The ADA (Autonomous Digital Ally) project aims to create a reliable and companion-like assistant. It leverages cutting-edge technologies to deliver a seamless user experience.

## Commit Details (15:51 PM)

In this commit, several updates have been made to enhance the functionality of the assistant:

## Code Modification:
- The code has been refactored to include additional functionality for gathering system information.
- A new class called SystemInfoGatherer has been introduced to handle the logic for collecting system information.
- The class includes methods to gather details such as OS information, CPU stats, memory usage, disk information, drive count, PC location, internet connection status, and microphone availability.
- The collected information is stored in a dictionary named "system_info" and written to a JSON file called "system_info.json".
- The JSON file is saved in a specific directory based on the provided drive path.
- The class also incorporates methods to check internet connection status and microphone availability.

## Connection between Files:
- The code responsible for system information gathering has been moved to a separate file named "system_info_gatherer.py".
- The function "present_data()" in the original code has been modified to import the SystemInfoGatherer class from "system_info_gatherer.py".
- The "present_data()" function now invokes the "gather_system_info()" method of the SystemInfoGatherer class to collect system information and generate the "system_info.json" file.
- The remaining part of the code in "present_data()" is responsible for reading and presenting the data from the "system_info.json" file.

## Additional Features:
- The code has been enhanced to determine the type of device (PC, Laptop, or Unknown) using the "platform.machine()" method.
- The device type information is stored in the "device_info" dictionary along with the device category (PC, Laptop, or Unknown).
- The device information is added to the "system_info" dictionary and included in the generated "system_info.json" file.
- When presenting the data, the device type and category are displayed alongside other system information.

These updates improve the code's functionality by adopting a modular approach to gather system information, store it in a JSON file, and present it in a more organized manner. The addition of device type detection enhances understanding of the type of device on which the assistant is running.

*Update: Progress Report for Today - 15/06/2023*

Today's progress focused on significant modifications to the code to enhance system information gathering functionality. We introduced a new class, SystemInfoGatherer, to gather various system details, including OS, CPU, memory, disk, location, internet connection, and microphone availability. The gathered information is stored in the "system_info.json" file.

Furthermore, we added the ability to determine the device type (PC, Laptop, or Unknown) using the "platform.machine()" method. This information is included in the "system_info.json" file, and when presenting the data, the device type and category are displayed alongside other system information.

These changes improve the code's modularity, organization, and understanding of the system on which the assistant is running.

Next, we plan to further enhance the assistant's capabilities by integrating additional features and improving its interaction with users. Stay tuned for more updates!

## Maya Updates - Summary (24-06-2023)

Today, I made some updates to Maya, my personal project, to enhance its functionality and improve the user experience. Here's a brief overview of the key updates:

2. **System Information Enhancement:** The system information module has

 been enhanced to provide detailed information about the user's device. Maya can now retrieve and display information such as the operating system name, version, CPU details, memory usage, disk space, and more. Simply ask Maya for system information, and it will provide a comprehensive report.

Please note that Maya is currently not available for public testing. It's a personal project, and these updates are part of my ongoing development efforts.

I'll continue working on Maya to add more features and improvements. If you have any feedback or suggestions, feel free to share them with me.

Feel free to customize this markdown copy as per your needs.