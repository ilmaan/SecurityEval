import os
import pandas as pd
import re

# Define the base directories using raw strings to avoid escape sequence issues
base_dir_copilot = r'Testcases_Copilot'
base_dir_incoder = r'Testcases_Incoder'
base_dir_insecure = r'Testcases_Insecure_Code'

# Initialize a list to hold the dataset
data = []

# Function to read the content of the Python file
def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

# Function to extract and remove the prompt from the file content
def extract_and_remove_prompt(file_content):
    # Use regex to find the prompt between triple single quotes
    prompt_match = re.search(r"'''(.*?)'''", file_content, re.DOTALL)
    if prompt_match:
        prompt = prompt_match.group(1).strip()
        # Remove the prompt from the file content
        cleaned_content = re.sub(r"'''(.*?)'''", '', file_content, flags=re.DOTALL).strip()
        return prompt, cleaned_content
    return "", file_content.strip()

# Iterate over the subfolders in one of the base directories (assuming all have the same structure)
for subfolder in os.listdir(base_dir_copilot):
    # Check if the subfolder starts with 'CWE-'
    if subfolder.startswith('CWE-'):
        cwe_id = subfolder
        
        # Get paths to corresponding subfolders in other directories
        copilot_dir = os.path.join(base_dir_copilot, subfolder)
        incoder_dir = os.path.join(base_dir_incoder, subfolder)
        insecure_dir = os.path.join(base_dir_insecure, subfolder)

        # Get the list of Python files in the 'CWE' subfolder (assuming all folders have the same Python files)
        for file_name in os.listdir(copilot_dir):
            if file_name.endswith('.py'):
                # Construct the file paths
                copilot_file = os.path.join(copilot_dir, file_name)
                incoder_file = os.path.join(incoder_dir, file_name)
                insecure_file = os.path.join(insecure_dir, file_name)
                
                # Check if all files exist
                if os.path.exists(copilot_file) and os.path.exists(incoder_file) and os.path.exists(insecure_file):
                    # Read the content of the files
                    copilot_code = read_file(copilot_file)
                    incoder_code = read_file(incoder_file)
                    insecure_code = read_file(insecure_file)

                    # Extract the prompt from the insecure file (assuming the prompt is the same in all files)
                    prompt, insecure_code = extract_and_remove_prompt(insecure_code)
                    
                    # Remove the prompt from Incoder and Copilot code as well
                    _, incoder_code = extract_and_remove_prompt(incoder_code)
                    _, copilot_code = extract_and_remove_prompt(copilot_code)

                    # Append the data to the list
                    data.append([cwe_id, insecure_code, incoder_code, copilot_code, prompt])
                else:
                    print(f"File not found: {file_name}")

# Create a pandas DataFrame
df = pd.DataFrame(data, columns=['CWE_ID', 'Insecure_Code', 'Incoder_Code', 'Copilot_Code', 'Prompt'])

# Save the dataframe to a CSV file
df.to_csv('cwe1_python_dataset.csv', index=False)

print("CSV file 'cwe_python_dataset.csv' has been created successfully.")
