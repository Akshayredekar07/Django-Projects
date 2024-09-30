# import os  

# # Define the range for creating files  
# start = 5  
# end = 20  

# # Create Markdown files  
# for i in range(start, end + 1):  
#     filename = f"Django{i:02}.md"  # Format number with leading zero  
#     with open(filename, 'w') as f:  
#         f.write(f"")  
    
#     print(f"Created file: {filename}")

import os  

# Define the folder name  
folder_name = 'ABC'  

# Create the folder if it doesn't exist  
if not os.path.exists(folder_name):  
    os.makedirs(folder_name)  
    print(f"Created directory: {folder_name}")  

# Define the range for creating files  
start = 5  
end = 20  

# Create empty Markdown files in the ABC folder  
for i in range(start, end + 1):  
    filename = f"Django{i:02}.md"  # Format number with leading zero  
    filepath = os.path.join(folder_name, filename)  # Create full path  
    with open(filepath, 'w') as f:  
        # No content written inside the file  
        pass  
    
    print(f"Created file: {filepath}")