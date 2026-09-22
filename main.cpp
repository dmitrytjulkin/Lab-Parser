#include <stdio.h>

#include "tree.h"
#include ""

#define DEFAULT_INPUT_FILE "executable_file.txt"

int main (int argc, char* argv[])
{
    FILE* inp_ptr = {};

    if (argc == 1)
        inp_ptr = fopen ("executable_file.txt", "r");

    else
        inp_ptr = fopen (argv[1], "r");

    assert (inp_ptr);

    tree_t* parser = InitTree ();
    FromFileToTree (inp_ptr, parser);

    printf ("Through the code and directories, "
            "i alone am the programmer one");

    return 0;
}
