#include <iostream>
#include <fstream>
#include <cstring>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <algorithm>

using namespace std;

struct trie_node {
    bool word;
    trie_node *children[26];
    int id;

    static int counter;

    // fill each trie node with zero
    trie_node() : word(false), id(counter) {
        memset(children, 0, sizeof(children));
        counter++;
    }
};

void insert_word(trie_node *root, const string &word);
bool remove_word(trie_node *root, const string &word);
void cleanup(trie_node *root);
string retrieve_word(const vector< pair<int, int> > &path);
bool is_valid(int x, int y);
void dfs(int x, int y, trie_node *root, trie_node *curr, set< pair<int, int> > *visited, vector< pair<int, int> > *curr_path, set<string> *result);

int trie_node::counter = 0;

// insert and store each letter in a word in a node
void insert_word(trie_node *root, const string &word) {
    if (word.length() == 0) {
        root->word = true;
        return;
    }
    int index = word[0] - 'A';
    if (!root->children[index])
        root->children[index] = new trie_node();
    insert_word(root->children[index], word.substr(1));
}

// remove word in trie tree
bool remove_word(trie_node *root, const string &word) {
    int nonempty = 0;
    for (int i = 0; i < 26; i++)
        if (root->children[i])
            nonempty++;
    if (word.length() == 0) {
        root->word = false;
        return nonempty = 0;
    }
    int index = word[0] - 'A';
    if (remove_word(root->children[index], word.substr(1))) {
        delete root->children[index];
        root->children[index] = NULL;
        return nonempty == 1;
    } else
        return false;
}

void cleanup(trie_node *root) {
    for (int i = 0; i < 26; i++)
        if (root->children[i])
            cleanup(root->children[i]);
    delete root;
}

// coordinate movement for 6 neighbors, in the order of up, up-right, bottom-right, bottom, bottom-left and up-left.
int dx[] = {0, 1, 1, 0, -1, -1}, dy[] = {1, 0, -1, -1, 0, 1};
vector< vector<char> > grid;
int num_layers;

string retrieve_word(const vector< pair<int, int> > &path) {
    string ans;
    for (int i = 0; i < (int) path.size(); i++)
        ans += grid[path[i].first][path[i].second];
    return ans;
}

// check whether it is a valid point on the grid
bool is_valid(int x, int y) {
    return x >= 0 && y >= 0 && x + y >= num_layers - 1 && y <= num_layers * 2 - 2
        && x <= num_layers * 2 - 2 && x + y <= num_layers * 3 - 3;
}

// depth first search
void dfs(int x, int y, trie_node *root, trie_node *curr, set< pair<int, int> > *visited, vector< pair<int, int> > *curr_path, set<string> *result) {
    if (visited->count(make_pair(x, y)) > 0)
        return;
    visited->insert(make_pair(x, y));
    curr_path->push_back(make_pair(x, y));
    if (curr->word) {
        string s = retrieve_word(*curr_path);
        result->insert(s);
        // remove repetitive words
        remove_word(root, s);
    }
    for (int r = 0; r < 6; ++r) {
        int nx = x + dx[r], ny = y + dy[r];
        if (!is_valid(nx, ny))
            continue;
        int index = grid[nx][ny] - 'A';
        if (!curr->children[index])
            continue;
        dfs(nx, ny, root, curr->children[index], visited, curr_path, result);
    }
    visited->erase(make_pair(x, y));
    curr_path->pop_back();
}

int main(int argc, char *argv[]) {
    // check whether command line has three arguments
    if (argc != 3) {
        cerr << "Usage: ./honeycomb.exe honeycomb.txt dictionary.txt" << endl;
        return 1;
    }
    ifstream fin_honeycomb(argv[1]), fin_dict(argv[2]);
    // read first line as number of layers
    fin_honeycomb >> num_layers;
    // initialize a two-dimensional vector
    grid = vector< vector<char> >(num_layers * 2 - 1, vector<char>(num_layers * 2 - 1));
    // store honeycomb.txt into two-dimensional vector of chars
    for (int i = 0; i < num_layers; i++) {
        string s;
        fin_honeycomb >> s;
        // center: (num_layers - 1, num_layers - 1)
        int x = num_layers - 1, y = num_layers - 1 + i;
        if (i == 0)
            grid[x][y] = s[0];
        else {
            int dir = 2, next = 0;
            for (int r = 0; r < 6; r++) {
                for (int j = 0; j < i; j++) {
                    grid[x][y] = s[next++];
                    x += dx[dir];
                    y += dy[dir];
                }
                // change direction of coordinate movement
                dir = (dir + 1) % 6;
            }
        }
    }
    fin_honeycomb.close();

    // store dictionary.txt into trie tree
    trie_node *root = new trie_node();
    string w;
    while (fin_dict >> w)
        insert_word(root, w);
    fin_dict.close();

    set< pair<int, int> > visited;
    vector< pair<int, int> > curr_path;
    set<string> ans;
    for (int x = 0; x < (int) grid.size(); x++)
        for (int y = 0; y < (int) grid[x].size(); y++)
            if (is_valid(x, y)) {
                int index = grid[x][y] - 'A';
                if (root->children[index])
                    dfs(x, y, root, root->children[index], &visited, &curr_path, &ans);
            }
    // print out words
    for (set<string>::iterator i = ans.begin(); i != ans.end(); i++)
        cout << *i << endl;

    cleanup(root);
    return 0;
}
