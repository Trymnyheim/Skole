# Oblig 2, IN2140

## How to read Master File Table

The function ``struct inode* load_inodes ( const char* master_file_table )``
reads all the elements in the master file table with the filename given by the
parameter `const char* master_file_table`, and then links all of them together
by storing pointers to all directories' child nodes in their entries field.

## Implementation requirements not met

All implementation requirements were met.

## Deviating implementations

No additional files were created, but three functions in `inode.c` were not in the
precode:

* `void free_entries( struct inode* node )`, frees all entries in a directory
    inode
* `void add_inode_to_parent( struct inode* parent, struct inode* child )` adds
    an inode `child` to the directory inode `parent`'s `entries` array.
* `void remove_inode_from_parent( struct inode* parent, struct inode* child )`
    does the opposite, removing the pointer to `child` from the `parent`'s
    `entries` array.

Additionally, a struct `Extent` was used: It came with the precode, but was not
mentioned in the instructions. It was used to store extents for all file inodes.
In order to make `debug_fs` work properly, `debug_fs_tree_walk` was modified to
use fields in the `Extent` struct.

## Failing tests

There are no failing tests.

