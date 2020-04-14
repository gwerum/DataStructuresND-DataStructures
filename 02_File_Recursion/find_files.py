import os
import unittest

import pdb

def walk(path):
  dir_path, dir_names, file_names = path, [], []
  # Get files and folder in dir_path
  for item in os.listdir(dir_path):
    item_path = os.path.join(dir_path, item)
    if os.path.isfile(item_path):
      file_names.append(item)
    elif os.path.isdir(item_path):
      dir_names.append(item)
  # Recurse on subfolders
  if dir_names:
    for dir_name in dir_names:
      yield from walk(os.path.join(dir_path, dir_name))

  yield dir_path, dir_names, file_names


def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    try:
      file_paths = []
      for dir_path, dir_names, file_names in walk(path):
        for file_name in [f for f in file_names if f.endswith(suffix)]:
          file_paths.append(os.path.join(dir_path, file_name))
      return file_paths
    except FileNotFoundError:
      print("Warning: folder '{}' not existing".format(path))
      return []


class TestFileFinder(unittest.TestCase):
  """docstring for TestFileFinder"""
  def test_find_c_files(self):
    expected_file_paths = ['./testdir/subdir1/a.c', './testdir/subdir3/subsubdir1/b.c', \
                          './testdir/subdir5/a.c', './testdir/t1.c']
    found_file_paths = find_files('.c', './testdir/')              
    self.assertEqual(sorted(expected_file_paths), sorted(found_file_paths))

  def test_find_non_existing_files(self):
    found_file_paths = find_files('.cpp', './testdir/')
    self.assertEqual(found_file_paths, [])

  def test_non_existing_folder(self):
    found_file_paths = find_files('.c', './testdir2/')
    self.assertEqual(found_file_paths, [])

  def test_find_hidden_files(self):
    expected_file_paths = ['./testdir/subdir2/.gitkeep', './testdir/subdir4/.gitkeep']
    found_file_paths = find_files('.gitkeep', './testdir/')              
    self.assertEqual(sorted(expected_file_paths), sorted(found_file_paths))

  def test_multiple_suffixes(self):
    expected_file_paths = ['./testdir/subdir1/a.c', './testdir/subdir3/subsubdir1/b.c', \
                          './testdir/subdir5/a.c', './testdir/t1.c', \
                          './testdir/subdir1/a.h', './testdir/subdir3/subsubdir1/b.h', \
                          './testdir/subdir5/a.h', './testdir/t1.h']
    found_file_paths = find_files(('.c', '.h'), './testdir/')              
    self.assertEqual(sorted(expected_file_paths), sorted(found_file_paths))




