#define ID_SIZE 1024
#define MAX_CHILD 1024

typedef struct Node
{
    int type;
    double value;
    char id[ID_SIZE];
    int child_num;
    struct Node child[MAX_CHILD];
};

Node *make_node(int type, double value, char *id);