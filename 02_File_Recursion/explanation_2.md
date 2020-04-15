## find_files.py

### Code explanation

The goal of this exercise was to implement a method **find_files(suffix, path)**, which finds all files with a given file name *suffix* under a given *path*. The method returns a list of file paths for all files found.

Boundary condition was to not use **os.walk(path)**, therefore the **walk(path)** method had to be implemented by myself. Starting with the parent directory *path* the parent directory and all its sub-directories have to be searched for existing files and sub-folders. Since this is a repetitive task, which has to be performed for each (sub-)folder, this can be best implemented recursively. To consider runtime efficiency for cases of deep & large folder structures, the walk method has been implemented as generator function. Additionally, exception handling has been implemented if the provided search path doesn't exist.

### Data structures

In this implementation a list for storing and returning the file paths of the matching files is used. The `walk`methods uses a list respectively for returning subfolders and files found in each folder, which is of constant size due to the implementation of the function as a generator.

### Runtime efficiency

**walk(path)**: As mentioned, the walk method is implemented recursively, therefore the time complexity increases linear with the number of recursions, which equal the **total number of directories and sub-directories D** under the given path. Thus, the **time complexity is of order O(D)**. Since the walk method is implemented as generator function, the space complexity can be considered constant, equal to the size of the generator object in memory.

**find_files(suffix, path)**: Additionally to calling the generator object provided by the `walk()` and *walking* all the folders, the **find_files()** methods finds **all matching files N** of **all files M** in a given folder and stores them in a list. Finding all files is of **time complexity O(M)** and storing of **space complexity O(N)**. 

So, overall complexity can be approximated to the following (which could be further reduced if for example the total number of files M would be assumed to be way larger than the number of directories D):
```
Time complexity: O(D * M)
Space complexity: O(N)
```
**D**: total number of (sub-)directories
**M**: total number of files
**N**: total number of matching files

### Test Cases

Five basic test cases for default and corner use cases have been implemented in **class TestFileFinder()**, which can be executed using the following command:

```
python -m unittest find_files.py
```