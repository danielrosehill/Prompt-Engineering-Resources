import os

# Path to the folder containing Markdown files
folder_path = "/home/daniel/Git/prompt-eng-resources/techniques/llm-authored/pe-guides"

# Badge to add at the top of each file
badge = "![Written By GPT-4 Turbo](https://img.shields.io/badge/Written%20By-GPT--4%20Turbo-5A5A5A?style=for-the-badge&logo=openai&logoColor=white)\n\n"

# Iterate through all files in the folder
for filename in os.listdir(folder_path):
    # Construct full file path
    file_path = os.path.join(folder_path, filename)

    # Check if the file is a Markdown file
    if filename.endswith(".md") and os.path.isfile(file_path):
        # Read the content of the file
        with open(file_path, "r") as file:
            content = file.read()

        # Write the badge followed by the original content back to the file
        with open(file_path, "w") as file:
            file.write(badge + content)

print("Badge added to all Markdown files.")