# Experiment 3

# Practice Source code management on GitHub. Experiment with the source code in experiment 1.

## Steps to Create a Repository on GitHub and Make a Git Commit

1. **Create a Repository on GitHub:**

   - Go to [GitHub](https://github.com) and log in to your account.
   - Click on the `+` icon in the top right corner and select `New repository`.
   - Enter a repository name (e.g., `Experiment1`), add a description (optional), and choose the visibility (public or private).
   - Click on `Create repository`.

2. **Initialize Git in the `Experiment1` Folder:**

   - Open a terminal and navigate to the `Experiment1` folder:
     ```sh
     cd /path/to/Experiment1
     ```
   - Initialize a new Git repository:
     ```sh
     git init
     ```

3. **Add Remote Repository:**

   - Add the GitHub repository as a remote:
     ```sh
     git remote add origin https://github.com/your-username/Experiment1.git
     ```
    **Note:** Replace `your-username` with your actual GitHub username.


4. **Add Files and Make a Commit:**

   - Add all files in the Experiment1 folder to the staging area:
     ```sh
     git add .
     ```
   - Commit the changes with a message:
     ```sh
     git commit -m "Initial commit for Experiment1"
     ```

5. **Push Changes to GitHub:**
   - Push the commit to the GitHub repository:
     ```sh
     git push -u origin master
     ```

You have now created a repository on GitHub and committed the files from the Experiment1 folder.
