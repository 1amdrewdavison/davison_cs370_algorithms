/* 
File written by Andrew Davison for CS370, Design and Analysis of Algorithms, with William Bailey in the spring of 2023 at Centre College.

This program uses a brute force method to analyse all possible solutions to the Knapsack Problem given a set of items.
It outputs each possible combination string, which denotes which items are taken through a list of 0s and 1s representing boolean values,
and then the total weight and value of each possible combination.

Additionally, the program takes in a positive integer from the user as a knapsack capacity. Using this, the program then
prints out in return the optimal solution to that version of the problem with the information above.

*/

#include <stdlib.h>
#include <iostream>
#include <stdio.h>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>

//Struct that holds all of the info on a given item
struct KnapsackItem {
    std::string item_name;
    int item_weight;
    int item_value;
};

std::vector<KnapsackItem> readFile(std::ifstream& knapsack_item_input) {
    //Begin reading in data from the file
    //Holds temporary data for reading in from the file
    std::vector<KnapsackItem> knapsack_items;
    std::string temp_name;
    std::string temp_weight;
    std::string temp_value;

    //Loop through the input file and put them into the vector of KnapsackItems
    while(knapsack_item_input.peek() != EOF) {
        std::getline(knapsack_item_input, temp_name);
        std::getline(knapsack_item_input, temp_weight);
        std::getline(knapsack_item_input, temp_value);
        knapsack_items.push_back({temp_name, atoi(temp_weight.c_str()), atoi(temp_value.c_str())});
    }

    return knapsack_items;
}

//Function for comparing knapsack items in order of value
//Passed into std::sort 
bool high_value_sort(const KnapsackItem& lhs, const KnapsackItem& rhs) {
    return lhs.item_value > rhs.item_value;
}

//Function for comparing knapsack items in order of value to weight ratio
//Passed into std::sort 
bool value_to_weight_sort(const KnapsackItem& lhs, const KnapsackItem& rhs) {
    return (lhs.item_value / lhs.item_weight) > (rhs.item_value / rhs.item_weight);
}

int main() {
    //Read in input file
    std::ifstream knapsack_item_input;
    knapsack_item_input.open("knapsack_input.txt");

    //Safety check
    if (!knapsack_item_input.is_open()) {
        perror("Failed to open the input file.");
        return EXIT_FAILURE;
    }

    //Create output file
    std::ofstream knapsack_combination_output;
    knapsack_combination_output.open("output.txt");

    //Safety check
    if (!knapsack_combination_output.is_open()) {
        perror("Failed to open the output file.");
        return EXIT_FAILURE;
    }

    //Read file
    auto knapsack_items = readFile(knapsack_item_input);

    knapsack_item_input.close();

    //Ask for knapsack capacity
    int knapsack_limit;

    std::cout << "Enter knapsack weight limit: ";
    std::cin >> knapsack_limit;

    //Keep track of best combination found by a value-based greedy approach
    int best_value_weight = 0;
    int best_value_value = 0;

    //Sort list according to value 
    std::sort(knapsack_items.begin(), knapsack_items.end(), &high_value_sort);

    //Iterate to find best combination according to a greedy solution
    for (auto item : knapsack_items) {
        if (best_value_weight + item.item_weight <= knapsack_limit) {
            best_value_value += item.item_value;
            best_value_weight += item.item_weight;
        }
    }

    //Keep track of best combination found by a value-based greedy approach
    int best_ratio_weight = 0;
    int best_ratio_value = 0;
    
    //Sort list according to ratio 
    std::sort(knapsack_items.begin(), knapsack_items.end(), &value_to_weight_sort);

    //Iterate to find best combination according to a greedy solution
    for (auto item : knapsack_items) {
        if (best_ratio_weight + item.item_weight <= knapsack_limit) {
            best_ratio_value += item.item_value;
            best_ratio_weight += item.item_weight;
        }
    }

    std::cout << "High value heuristic:\nw: " << best_value_weight << "\nv: " << best_value_value << "\n";
    std::cout << "Value to weight heuristic:\nw: " << best_ratio_weight << "\nv: " << best_ratio_value;

    knapsack_combination_output.close();
}