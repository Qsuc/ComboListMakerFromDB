import os
from tkinter import Tk, filedialog


def keyword_searcher(keywords):
    
    root = Tk()
    root.withdraw()  
    file_path = filedialog.askopenfilename(title="Select a file", filetypes=[("Text Files", "*.txt")])
    if not file_path:
        print("No file selected.")
        return
    
    output_lines = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            if any(keyword.lower() in line.lower() for keyword in keywords):
                output_lines.append(line)
    
    
    with open("combo.txt", 'w', encoding='utf-8') as output_file:
        output_file.writelines(output_lines)
    
    print(f"Lines containing keywords have been written to combo.txt")

if __name__ == "__main__":
    keywords = input("Enter keywords separated by commas: ").split(',')
    keywords = [kw.strip() for kw in keywords]
    keyword_searcher(keywords)
