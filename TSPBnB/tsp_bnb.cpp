//Written by Andrew Davison for CSC 370: Design and Analysis of Algorithms
//Solves an instance of the Traveling Salesperson Problem by a Branch and Bound algorithm
//Reads input from city_distances.csv

#include <utility>
#include <sstream>
#include <string>
#include <fstream>
#include <iostream>
#include <stdio.h>
#include <vector>
#include <queue>
#include <numeric>
#include <algorithm>

//This is a function used to define a priority queue, so that those with a lower heuristic score are prioritized
// bool priority(node* left, node* right) {
//     return left->heuristic <= right->heuristic;
// };

std::pair<std::vector<std::string>, std::vector<std::vector<int>>> readFile(std::ifstream& tsp_input) {
    //Begin reading in data from the file
    //Holds temporary data for reading in from the file
    std::vector<std::string> city_names;
    std::vector<std::vector<int>> distances;
    std::string temp_data;
    std::string temp_line;
    bool in_data = false, is_first = true;
    int i = -1;

    //Look at each line
    while(std::getline(tsp_input, temp_line)) {
        std::stringstream line(temp_line);
        
        if (in_data) {
            distances.push_back({});
            i++;
        }

        //Process each line
        while(std::getline(line, temp_data, ',')) {
            if (is_first) {
                is_first = false;
            } else if (in_data) {
                distances[i].push_back(stoi(temp_data));
            } else {
                city_names.push_back(temp_data);
            }

        }

        is_first = true;
        in_data = true;  
    }

    return std::pair(city_names, distances);
}

//This is a node struct for generating the TSP tree
struct node {
    std::vector<int> path; 
    int path_cost;
    int lower_bound;

    friend bool operator< (node const& lhs, node const& rhs) {
        return lhs.lower_bound > rhs.lower_bound;
    }
};

int find_min_edge(std::vector<int> edges) {
    int min = INT_MAX;

    for (auto itr : edges) {
        if (itr != 0 && itr < min) {
            min = itr;
        }
    }

    return min;
}

int find_lower_bound(int current_length, std::vector<int> path, std::vector<std::vector<int>> distances) {
    int lower_bound = current_length;
    
    for (int i = 0; i < distances.size(); i++) {
        if (std::find(path.begin(), path.end(), i) == path.end()) {
            lower_bound += find_min_edge(distances[i]);
        }
    }

    return lower_bound;
}

std::pair<int, std::vector<int>> tsp_bnb(std::vector<std::vector<int>> distances) {
    //Make structure variables
    std::priority_queue<node> queue;
    int best_length = INT_MAX;
    std::vector<int> best_path;
    
    //Generate root of the tree
    auto root = node {{0}, 0, find_lower_bound(0, {}, distances)};
    queue.push(root);

    while (!queue.empty()) {
        node curr_node = queue.top();
        queue.pop();
        
        //Bound
        if (curr_node.lower_bound < best_length) {
            bool isLeaf = true;
            int j = curr_node.path.back();

            //Generate Children
            for (int i = 0; i < distances.size(); i++) {
                if (std::find(curr_node.path.begin(), curr_node.path.end(), i) == curr_node.path.end()) {
                    std::vector<int> new_path = curr_node.path;
                    
                    new_path.push_back(i);
                    int new_path_cost = curr_node.path_cost + distances[j][i];

                    queue.push(node{new_path, new_path_cost, find_lower_bound(new_path_cost, new_path, distances)});

                    isLeaf = false;
                }
            }

            //Check for best path if it is a leaf
            if (isLeaf) {
                curr_node.path_cost += distances[curr_node.path.back()][0];
                curr_node.path.push_back(0);

                if (curr_node.path_cost < best_length) {
                    best_length = curr_node.path_cost;
                    best_path = curr_node.path;
                }
            }
        }
    }

    return std::pair(best_length, best_path);
}

std::string print_path(std::vector<int> path, std::vector<std::string> city_names) {
    std::string city_path = "";

    for (auto itr : path) {
        city_path += city_names[itr] + " ";
    }

    return city_path;
}

int main() {
    //Read in TSP data
    std::ifstream tsp_input;
    tsp_input.open("city_distances.csv");

    //Read file
    auto tsp = readFile(tsp_input);
    tsp_input.close();

    auto city_names = tsp.first;
    auto distances = tsp.second;

    auto solution = tsp_bnb(distances);

    std::cout << "Kilometers traveled in optimal path: " << solution.first << "\n";
    std::cout << "Order of cities visited in optimal path: " << print_path(solution.second, city_names) << "\n";
}