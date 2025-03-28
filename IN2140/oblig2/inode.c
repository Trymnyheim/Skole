#include "inode.h"
#include "block_allocation.h"

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define INT_DISK_SIZE 4
#define CHAR_DISK_SIZE 1
#define ENTRY_DISK_SIZE 8

#define INODE_ARRAY_SIZE 1024
#define BLOCK_SIZE 4096

#define EXIT {fs_shutdown(current_inode);return NULL;}

int next_id = 0; // The next ID to be assigned

void free_entries( struct inode* inode ) {
    // Frees all entries in the given inode
    if (!inode->is_directory) {
        for (int i = 0; i < inode->num_entries; i++) {
            free((struct Extent*) inode->entries[i]);
        }
    }
    if (inode->entries) free(inode->entries);
}

void add_inode_to_parent( struct inode* parent, struct inode* child ) {
    if (!parent) return;

    uintptr_t* old_entries = malloc(sizeof(uintptr_t) * parent->num_entries);
    for (int i = 0; i < parent->num_entries; i++) {
        old_entries[i] = parent->entries[i];
    }
    parent->num_entries++;
    free(parent->entries);
    parent->entries = malloc(sizeof(uintptr_t) * parent->num_entries);
    for (int i = 0; i < parent->num_entries-1; i++) {
        parent->entries[i] = old_entries[i];
    }
    parent->entries[parent->num_entries-1] = (uintptr_t) child;
    free(old_entries);
}

void remove_inode_from_parent(struct inode *parent, struct inode *child) {
  if (parent == NULL) {
    return;     // Child is root.
  }
  
  if (child == NULL || parent->num_entries == 0) {
      fprintf(stderr, "Error: Child not initialized or parent directory \"%s\" is empty\n", parent->name);
        return;
    }

    int index = -1;
    for (int i = 0; i < parent->num_entries; i++) {
      if (parent->entries[i] == (uintptr_t)child) {
          index = i;
            break;
        }
    }

    if (index == -1) {
      fprintf(stderr, "Error: \"%s\" not found in directory \"%s\"\n", child->name, parent->name);
      return;
    }
    
    // Fill gap:
    for (int i = index; i < parent->num_entries - 1; i++) {
      parent->entries[i] = parent->entries[i + 1];
    }
    // Reduce entry count
    parent->num_entries--;
}

struct inode* create_file( struct inode* parent, const char* name,
        char readonly, int size_in_bytes )
{
    if (find_inode_by_name(parent, name) != NULL) return NULL;
    struct inode *current_inode = calloc(1, sizeof(struct inode));
    current_inode->id = next_id++;
    current_inode->name = malloc(sizeof(char) * (strlen(name) + 1));
    strcpy(current_inode->name, name);
    current_inode->is_directory = 0;
    current_inode->is_readonly = readonly;
    current_inode->filesize = size_in_bytes;
    
    int necessary_blocks = current_inode->filesize / BLOCK_SIZE;
    if (current_inode->filesize % BLOCK_SIZE != 0) necessary_blocks++;
    
    struct Extent **extents = calloc(necessary_blocks + 1,
            sizeof(struct Extent));
    while (necessary_blocks > 0) {
        int blockno, extent = 0;
        if (extent > 4) extent = 4;
        else extent = necessary_blocks;

        while ((blockno = allocate_block(extent)) == -1 && extent > 0) {
            extent--;
        }
        if (extent == 0) {
            fs_shutdown(current_inode);
            return NULL;
        }
        struct Extent *current_extent = malloc(sizeof(struct Extent));
        current_extent->blockno = blockno;
        current_extent->extent = extent;
        extents[current_inode->num_entries] = current_extent;
        current_inode->num_entries++;

        necessary_blocks -= extent;
    }

    current_inode->entries = malloc(
            sizeof(struct Extent) * current_inode->num_entries
    );
    for (int i = 0; i < current_inode->num_entries; i++) {
        current_inode->entries[i] = (uintptr_t) extents[i];
    }

    free(extents);
    
    add_inode_to_parent(parent, current_inode);
    
    return current_inode;
}

struct inode* create_dir( struct inode* parent, const char* name )
{
    if (find_inode_by_name(parent, name) != NULL) return NULL;

    struct inode *current_inode = calloc(1, sizeof(struct inode));
    current_inode->id = next_id++;
    current_inode->name = malloc(sizeof(char) * (strlen(name) + 1));
    strcpy(current_inode->name, name);
    current_inode->is_directory = 1;
    current_inode->is_readonly = 0;
    current_inode->filesize = 0;
    current_inode->num_entries = 0;
    
    add_inode_to_parent(parent, current_inode);

    return current_inode;
}

struct inode* find_inode_by_name( struct inode* parent, const char* name )
{
    if (!parent || !parent->is_directory) return NULL;

    for (int i = 0; i < parent->num_entries; i++) {
        struct inode *current_inode = (struct inode*) parent->entries[i];
        if (strcmp(current_inode->name, name) == 0)
            return current_inode;
    }

    return NULL;
}

int delete_file( struct inode* parent, struct inode* node )
{
    if (node->is_directory || !parent->is_directory) {
        return -1;
    }
    char parent_contains_node = 0;
    for (int i = 0; i < parent->num_entries; i++) {
        if ((struct inode*) parent->entries[i] == node)
            parent_contains_node = 1;
    }
    if (!parent_contains_node) {
        return -1;
    }

    remove_inode_from_parent(parent, node);

    for (int entryno = 0; entryno < node->num_entries; entryno++) {
        struct Extent *current_extent = (struct Extent*) node->entries[entryno];
        for (int i = 0; i < current_extent->extent; i++) {
            free_block(current_extent->blockno + i);
        }
    }
    
    fs_shutdown(node);

    return 0;
}

int delete_dir( struct inode* parent, struct inode* node )
{
    if (!node->is_directory || !parent->is_directory
            || node->num_entries != 0) {
        return -1;
    }
    char parent_contains_node = 0;
    for (int i = 0; i < parent->num_entries; i++) {
        if ((struct inode*) parent->entries[i] == node)
            parent_contains_node = 1;
    }
    if (!parent_contains_node) {
        return -1;
    }
    
    remove_inode_from_parent(parent, node);
    fs_shutdown(node);

    return 0;
}

void save_inodes( const char* master_file_table, struct inode* root )
{
    FILE* f = fopen(master_file_table, "w");
    rec_save_inodes(f, root);
    fclose(f);
    return;
}

void rec_save_inodes(FILE* f, struct inode* node) {
    save_inode(f, node);
    if (!node->is_directory || node->num_entries == 0) {
        return;
    }
    // node is directory:
    struct inode* child;
    for (int i = 0; i < node->num_entries; i++) {
        child = (struct inode*)node->entries[i];
        rec_save_inodes(f, child);
    }
}

// Writes all data about inode to file:
void save_inode(FILE* f, struct inode* node) {
    fwrite(&node->id, sizeof(uint32_t), 1, f);
    uint32_t namelen = strlen(node->name) + 1;
    fwrite(&namelen, sizeof(uint32_t), 1, f);
    for (int i = 0; i < namelen; i++) {
        fwrite(&node->name[i], sizeof(char), 1, f);
    }
    fwrite(&node->is_directory, sizeof(char), 1, f);
    fwrite(&node->is_readonly, sizeof(char), 1, f);
    if (!node->is_directory) {
        fwrite(&node->filesize, sizeof(uint32_t), 1, f);
    }
    fwrite(&node->num_entries, sizeof(uint32_t), 1, f);

    for(int i = 0; i < node->num_entries; i++) {
        if (node->is_directory) {
            // Write id of children nodes:
            struct inode* child = (struct inode*)node->entries[i];
            fwrite(&child->id, sizeof(uintptr_t), 1, f);
        }
        else {
            // Write extents block_no and size:
            struct Extent* ext = (struct Extent*)node->entries[i];
            fwrite(&ext->blockno, sizeof(uint32_t), 1, f);
            fwrite(&ext->extent, sizeof(uint32_t), 1, f);
        }
    }
}

struct inode* load_inodes( const char* master_file_table )
{

    FILE *file = fopen(master_file_table, "rb"); // Mode: Read Binary
    
    // Contains all the inodes until all directories are correctly loaded
    struct inode **inodes = calloc(INODE_ARRAY_SIZE, sizeof(struct inode));

    while (1) {
        struct inode *current_inode;
        if ((current_inode = calloc(1, sizeof(struct inode))) <= 0)
            EXIT
        
        // All uses of fread check for error, in which case the entire function
        // returns NULL.
        // This one also checks that we haven't reached EOF, because that is
        // handled by breaking the loop (not returning NULL)
        
        // Reading ID
        if (fread(&current_inode->id, INT_DISK_SIZE, 1, file) <= 0 
                && !feof(file)) EXIT

        if (current_inode->id > next_id) next_id = current_inode->id + 1;

        // Because feof(file) only detects when we try accessing beyond the
        // file, not when we are at the end, this needs to be called after id is
        // attempted to be read.
        if (feof(file)) {
            fs_shutdown(current_inode);
            break;
        }
        
        // Reading name length
        uint32_t name_length;
        if (fread(&name_length, INT_DISK_SIZE, 1, file) <= 0) EXIT 
        // Mallocing space for the name and reading it
        if ((current_inode->name = malloc(sizeof(char) * name_length)) == 0)
            EXIT
        if (fread(current_inode->name, CHAR_DISK_SIZE, name_length, file) <= 0)
            EXIT
        // Reading the is_directory and is_readonly flags
        if (fread(&current_inode->is_directory, CHAR_DISK_SIZE, 1, file) <= 0)
            EXIT
        if (fread(&current_inode->is_readonly, CHAR_DISK_SIZE, 1, file) <= 0)
            EXIT
        // Reading filesize if we are working with a file
        if (!current_inode->is_directory) {
            if (fread(&current_inode->filesize, INT_DISK_SIZE, 1, file) <= 0)
                EXIT
        } else {
            current_inode->filesize = 0;
        }
        // Reading the number of entries
        if (fread(&current_inode->num_entries, INT_DISK_SIZE, 1, file) <= 0)
            EXIT
        // Reading entries
        if (!current_inode->is_directory) {
            // entries is an array of uintptr_t pointers to Extent-structs when
            // the inode is a file
            current_inode->entries = malloc(
                    sizeof(struct Extent) * current_inode->num_entries
            );
            for (int i = 0; i < current_inode->num_entries; i++) {
                current_inode->entries[i] = (uintptr_t) malloc(
                        sizeof(struct Extent)
                );
                // Reading blockno
                fread(
                        &(((struct Extent*)current_inode->entries[i])->blockno),
                        INT_DISK_SIZE, 1, file
                    );
                // Reading extent
                fread(
                        &(((struct Extent*)current_inode->entries[i])->extent),
                        INT_DISK_SIZE, 1, file
                     );
            }
        } else if (current_inode->num_entries != 0) {
            // If the inode is a directory and actually has any entries, the
            // entries array first contains the IDs of all the inodes it
            // contains. When all the inodes are read, the IDs will be replaced
            // by the actual pointer.
            if ((current_inode->entries = malloc(
                            sizeof(uintptr_t) * current_inode->num_entries
            )) == 0) EXIT 
            if (fread(current_inode->entries, 2*INT_DISK_SIZE, 
                        current_inode->num_entries, file) <= 0) EXIT 
        }

        inodes[current_inode->id] = current_inode;
    }
    
    // Updating directories' entries to contain the actual pointers instead of
    // just the IDs
    for (int i = 0; i < INODE_ARRAY_SIZE; i++) {
        if (inodes[i] == NULL) continue;
        if (!inodes[i]->is_directory) continue;
        for (int j = 0; j < inodes[i]->num_entries; j++) {
            inodes[i]->entries[j] = (uintptr_t) inodes[inodes[i]->entries[j]];
        }
    }

    fclose(file);
    struct inode *root = inodes[0];
    free(inodes);
    return root;

}

// Recursively shuts down the file system
void fs_shutdown( struct inode* inode )
{
    if (inode->name) free(inode->name);

    if (inode->is_directory && inode->num_entries > 0) {
        for (int i = 0; i < inode->num_entries; i++) {
            fs_shutdown((struct inode *) inode->entries[i]);
        }
    }
    free_entries(inode);
    free(inode);
}

/* This static variable is used to change the indentation while debug_fs
 * is walking through the tree of inodes and prints information.
 */
static int indent = 0;

static void debug_fs_print_table( const char* table );
static void debug_fs_tree_walk( struct inode* node, char* table );

void debug_fs( struct inode* node )
{
    char* table = calloc( NUM_BLOCKS, 1 );
    debug_fs_tree_walk( node, table );
    debug_fs_print_table( table );
    free( table );
}

static void debug_fs_tree_walk( struct inode* node, char* table )
{
    if( node == NULL ) return;
    for( int i=0; i<indent; i++ )
        printf("  ");
    if( node->is_directory )
    {
        printf("%s (id %d)\n", node->name, node->id );
        indent++;
        for( int i=0; i<node->num_entries; i++ )
        {
            struct inode* child = (struct inode*)node->entries[i];
            debug_fs_tree_walk( child, table );
        }
        indent--;
    }
    else
    {
        printf("%s (id %d size %d)\n", node->name, node->id, node->filesize );
        struct Extent** extents = (struct Extent**)node->entries;
        for (int i = 0; i < node->num_entries; i++) {
            for (int j = 0; j < extents[i]->extent; j++) {
                table[extents[i]->blockno + j] = 1;
            }
        }
    }
}

static void debug_fs_print_table( const char* table )
{
    printf("Blocks recorded in master file table:");
    for( int i=0; i<NUM_BLOCKS; i++ )
    {
        if( i % 20 == 0 ) printf("\n%03d: ", i);
        printf("%d", table[i] );
    }
    printf("\n\n");
}

