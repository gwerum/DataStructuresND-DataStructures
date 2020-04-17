## find_files.py

### Code explanation

The goal of this exercise is to implement a method **find_files(suffix, path)**, which finds all files with a given file name *suffix* under a given *path*. The method returns a list of file paths for all files found.

It is not allowed to use **os.walk(path)**, therefore the **walk(path)** method has to be implemented. Starting with the parent directory "path" the parent directory and all its sub-directories have to be searched for existing files and sub-folders, which is best implemented in a recursive manner. To consider runtime efficiency for cases of deep & large folder structures, the walk method has been implemented as generator function. Additionally, exception handling has been implemented if the provided search path doesn't exist.

---

### Data structures

In this implementation a list for storing and returning the paths of all matching files is used. The **walk(path)** method uses a list respectively for returning subfolders and files found in each folder. Those lists will grow with the number of files F and sub-directories S found in a single folder, but not grow with the overall size of the directory tree under *path*, due to its use in a generator function.

---

### Runtime efficiency

**walk(path)**: As mentioned, the walk method is implemented recursively, therefore the time complexity increases linear with the number of recursions, which equal to the total number of directories D in the directory tree under *path*. Thus, time complexity is of order O(D). The space complexity depends on the space requirements of the generator function, whichs is dependend on the average number of files F and sub-directories S in each folder. 

**find_files(suffix, path)**: Finding all matching files requires walking all directories D under *path* and searching the files F stored in each directory. The space requirements equal the total number of matching files M.

|  | Time complexity | Space complexity |
| ------------------- | --------------- | ---------------- |
| *walk(path)* | O(D) | ~O(F+S) |
| *find_files(suffix, path)* | O(D x F) | O(M) |
| **Total** | **O(D x F + D) ~ O(D x F)** | **~O(F+S+M)** |

**D**: total number of (sub-)directories in directory tree under *path*
**S**: average number of sub-folders stored in each directoriy
**F**: average number of files stored in each directory
**M**: total number of matching files with suffix 

---

### Test Cases

The following five basic test cases for default and corner use cases have been created all using the test directory *testdir*:

1. Find all c-files 
2. Find non-existing cpp-files
3. Search non-existing folder *testdir2*
4. Find hidden files *.gitkeep*
5. Find all files for multiple suffixes ".c" and ".h"

The tests can be executed using the following command:

```
python -m unittest find_files.py
```