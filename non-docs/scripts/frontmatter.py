import os

# Define the folder path
folder_path = "/home/daniel/Git/prompt-eng-resources/techniques/llm-authored/pe-guides"

# Function to convert filename to title format
def filename_to_title(filename):
    # Remove the .md extension and replace hyphens with spaces
    base_name = os.path.splitext(filename)[0]
    # Capitalize each word
    title = " ".join(word.capitalize() for word in base_name.split("-"))
    return title

# Iterate through all Markdown files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith(".md"):
        file_path = os.path.join(folder_path, filename)
        
        # Generate the title from the filename
        title = filename_to_title(filename)
        
        # Read the current content of the file
        with open(file_path, "r") as file:
            content = file.read()
        
        # Create YAML frontmatter
        yaml_frontmatter = f"---\ntitle: \"{title}\"\n---\n\n"
        
        # Check if YAML frontmatter already exists (to avoid duplicates)
        if not content.startswith("---"):
            # Prepend YAML frontmatter to the content
            updated_content = yaml_frontmatter + content
            
            # Write back to the file
            with open(file_path, "w") as file:
                file.write(updated_content)

print("YAML frontmatter added to all Markdown files.")