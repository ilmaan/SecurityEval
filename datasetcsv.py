import os
import csv

# Define folder paths
testcases_insecure = 'C:\\Users\\Admin\\Documents\\MscCSULB\\SEM3\\CECS 697 Thesis\\RobotDataExtension\\SecurityEval\\Testcases_Insecure_Code'
testcases_incoder = 'C:\\Users\\Admin\\Documents\\MscCSULB\\SEM3\\CECS 697 Thesis\\RobotDataExtension\\SecurityEval\\Testcases_InCoder'
testcases_copilot = 'C:\\Users\\Admin\\Documents\\MscCSULB\\SEM3\\CECS 697 Thesis\\RobotDataExtension\\SecurityEval\\Testcases_Copilot'
testcases_prompt = 'C:\\Users\\Admin\\Documents\\MscCSULB\\SEM3\\CECS 697 Thesis\\RobotDataExtension\\SecurityEval\\Testcases_Prompt'

# Function to extract prompt (text between triple backticks ''' or comments)
def extract_prompt_from_file(file_content):
    prompt = ""
    inside_prompt = False
    lines = file_content.splitlines()
    for line in lines:
        if line.strip().startswith("'''") or line.strip().startswith('"""'):
            inside_prompt = not inside_prompt  # Toggle state between inside/outside prompt
        elif inside_prompt:
            prompt += line + '\n'
        
    return prompt.strip()

# Function to read code from a file
def read_code_from_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        return file.read()

# Create the CSV dataset
def create_csv_dataset():
    with open('vulnerability_dataset_extension2.csv', mode='w', newline='', encoding='utf-8') as csv_file:
        fieldnames = ['ID', 'Prompt', 'Insecure_Code', 'Incoder_Code', 'Copilot_Code']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()

        # Walk through CWE ID folders
        for cwe_folder in os.listdir(testcases_insecure):
            cwe_id = cwe_folder  # CWE ID

            insecure_cwe_path = os.path.join(testcases_insecure, cwe_folder)
            incoder_cwe_path = os.path.join(testcases_incoder, cwe_folder)
            copilot_cwe_path = os.path.join(testcases_copilot, cwe_folder)
            prompt_cwe_path = os.path.join(testcases_prompt, cwe_folder)

            if os.path.isdir(insecure_cwe_path):  # Ensure it's a folder
                for filename in os.listdir(insecure_cwe_path):
                    if filename.endswith('.py'):  # Check if it's a Python file
                        file_id = filename.replace('.py', '')  # File ID

                        # Read files from all 4 folders
                        insecure_file_path = os.path.join(insecure_cwe_path, filename)
                        incoder_file_path = os.path.join(incoder_cwe_path, filename)
                        copilot_file_path = os.path.join(copilot_cwe_path, filename)
                        prompt_file_path = os.path.join(prompt_cwe_path, filename)

                        # Read file contents
                        insecure_code = read_code_from_file(insecure_file_path)
                        incoder_code = read_code_from_file(incoder_file_path) if os.path.exists(incoder_file_path) else ''
                        copilot_code = read_code_from_file(copilot_file_path) if os.path.exists(copilot_file_path) else ''
                        prompt_content = read_code_from_file(prompt_file_path) if os.path.exists(prompt_file_path) else ''

                        # Extract prompt from the prompt folder file
                        prompt = extract_prompt_from_file(prompt_content)
                        if prompt == '' or prompt == None:
                            prompt =  prompt_content

                        # Write row to CSV
                        writer.writerow({
                            'ID': cwe_id,
                            'Prompt': prompt,
                            'Insecure_Code': insecure_code,
                            'Incoder_Code': incoder_code,
                            'Copilot_Code': copilot_code
                        })

if __name__ == "__main__":
    create_csv_dataset()
