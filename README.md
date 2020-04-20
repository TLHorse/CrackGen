![CrackGen Icon](https://raw.githubusercontent.com/TLHorse/CrackGen/master/img/CrackGenIcon.png)
# CrackGen
A macOS CrackMe generator.

| Name | Desription |
| :-: | :-: |
| App name | CrackGen |
| Latest version | v1.0.0 |
| Platform | `macOS` |
| Programming | `Python` |
| Language | Chinese |
| GUI framework | `PySimpleGUI` |
| CM format | Unix executable |
| CM type | TUI Program |

# Screenshots

![Main Window](https://github.com/TLHorse/CrackGen/raw/master/img/Main%20Window.png)
![Generate Succeed](https://raw.githubusercontent.com/TLHorse/CrackGen/master/img/Generate%20Succeed.jpg)
![Generated CM](https://raw.githubusercontent.com/TLHorse/CrackGen/master/img/Generated%20CM.jpg)

# Usage

1. First, slide the slider on the home page to set the number of times the CM uses the algorithm.
2. Fill in the `CrackMe name` field to name your CM.
3. Select the **root directory** of the `CrackMe template dependency` project.
4. Select an export directory, such as `/Users/xxx/Downloads'.
5. Click on Generate, then wait for a moment and you will be prompted for a success or error (if you produce an error, please report your error to me).
6. If the target directory has a file with the same name, a message to overwrite or cancel will be displayed.
7. If it is successful, you will be instructed to open the folder where the CM is located.

# Q&A
- What is CrackMe?

  They are all little programs that are open for others to try cracking, the person making CrackMe may be a programmer who wants to test his or her software protection skills, or a cracker who wants to challenge the cracking prowess of other crackers, or someone who is learning to crack and making up little programs for him or herself to crack. KeygenMe is asking someone else to make its keygen (serial number generator), ReverseMe is asking someone else to reverse its algorithm, and UnpackMe is asking someone else to successfully unpack it.

- How does this software work?

  **A look at how it works first will help to operate the software later.**
  1. The software will first display the main window for the user to enter information.
  2. Generate a random sequence of algorithms through the "number of operations" field in the input information.
  3. The algorithm sequence is stitched together to generate the `Swift` code file.
  4. The program will embed the `Swift` code file into an existing `Xcode` project (this project file is provided by me) in a project directory, determined by the "CM template dependencies" field set by the user in the main window.
  5. Once the `Xcode` project for the CrackMe is ready, CrackGen will automatically execute the `xcodebuild` command in the project directory to compile the CrackMe.
  6. Use `Python` to change the name of the program files (executables) generated in the compilation directory to a user-set name.
  7. Move the final CrackMe to the target folder, then delete the compile folder.
