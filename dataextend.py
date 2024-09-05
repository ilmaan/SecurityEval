import os
import csv


try:
    # Define the base directory for the dataset
    base_dir = "C:\\Users\\Admin\\Documents\\MscCSULB\\SEM3\\CECS 697 Thesis\\RobotDataExtension\\SecurityEval\\"  # Replace with your actual path

    # Define the folders
    folders = ["Testcases_Insecure_Code", "Testcases_InCoder", "Testcases_Copilot"]

    # Define the CWE-id for Improper Authentication
    cwe_id = "CWE-798"

    cwe_list = {
        # "CWE-120": "robotvul120.csv",
        "CWE-77": "robotvul77robot.csv",
        "CWE-190": "robotvul190.csv",
        "CWE-284": "robotvul284.csv",
        "CWE-287": "robotvul287.csv",
        "CWE-352": "robotvul352.csv",
        "CWE-798": "robotvul798.csv",
        "CWE-287": "robotvul287new.csv",
        "CWE-120": "robotvul120_robot.csv",
        "CWE-284": "robotvul284robot.csv",
        "CWE-285": "robotvul285robot.csv",
        "CWE-287": "robotvul287robot.csv",
        "CWE-352": "robotvul352.csv",
        "CWE-362": "robotvul362robot.csv",
        "CWE-400": "robotvul400robot.csv",
        "CWE-416": "robotvul416robot.csv",
        "CWE-506": "robotvul506robot.csv",
        "CWE-764": "robotvul764robot.csv",
        "CWE-798": "robotvul798robot.csv",
    }

    # Function to create directories if they don't exist
    def create_dir(path):
        if not os.path.exists(path):
            os.makedirs(path)

    # Function to write code to a file
    def write_to_file(path, content):
        with open(path, 'w') as file:
            file.write(content)


    for cwe_id in cwe_list:
        # Read the CSV file
        try:
            print("CWE",cwe_id,"IS",cwe_list[cwe_id])
            with open(cwe_list[cwe_id], 'r') as csvfile:
                reader = csv.DictReader(csvfile)
                
                for i, row in enumerate(reader, start=1):
                    # Create subdirectories for each folder
                    for folder in folders:
                        folder_path = os.path.join(base_dir, folder, cwe_id)
                        create_dir(folder_path)
                    
                    # Write insecure code
                    insecure_path = os.path.join(base_dir, "Testcases_Insecure_Code", cwe_id, f"example_{i}.py")
                    write_to_file(insecure_path, row['Testcases_Insecure_Code'])
                    
                    # Write InCoder secure code
                    incoder_path = os.path.join(base_dir, "Testcases_InCoder", cwe_id, f"example_{i}.py")
                    write_to_file(incoder_path, row['Testcases_InCoder'])
                    
                    # Write Copilot secure code
                    copilot_path = os.path.join(base_dir, "Testcases_Copilot", cwe_id, f"example_{i}.py")
                    write_to_file(copilot_path, row['Testcases_Copilot'])
                    
                    print(f"Created example_{i}.py in all three folders")
        except Exception as e:
            print(f"Error reading CSV file: {e}")

    print("Dataset extension complete!")
except Exception as e:
    print("ERROR HERE,,",e)