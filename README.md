# ComboListMakerFromDB
A python script that uses keywords to get specified combo's from a db combolist






This Python script allows users to search for specific keywords within a text file and extract lines containing those keywords, regardless of case (case-insensitive search). The main features of the script include:

File Selection:
The script uses a graphical file explorer (via Tkinter) to let the user select a text file for processing.

Keyword Search:
Users provide a list of keywords separated by commas. The script searches each line of the selected file and identifies lines containing any of the specified keywords, ignoring case differences.

Output to File:
Lines that match the keyword criteria are written to an output file named combo.txt in the same directory as the script.

Ease of Use:
The script automatically handles case-insensitive comparisons and ensures the output file is created only if there are matching lines.

This tool is useful for tasks that require filtering large text files based on multiple keywords.
