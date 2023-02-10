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

struct KnapsackItem {
    std::string item_name;
    int item_weight;
    int item_value;
};

std::string arrayToString(std::vector<int> combination) {
    std::string str = "";
    for (auto digit : combination) {
        str += std::to_string(digit);
    }
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

    knapsack_item_input.close();

    //Ask for knapsack capacity
    int knapsack_limit;

    std::cout << "Enter knapsack weight limit:";
    std::cin >> knapsack_limit;

    //Begin iterating through all possible combinations
    std::vector<int> item_selection_code(knapsack_items.size());
    std::fill_n(item_selection_code, knapsack_items.size(), 0);

    //Keep track of best combination
    std::vector<int> item_selection_code(knapsack_items.size());
    int best_weight = knapsack_limit + 1;
    int best_value = -1;

    for (int i = 0; i < knapsack_items.size(); i++) {
        int selection_weight = 0;
        int selection_value = 0;
        
        for (int j : item_selection_code) {
            if (j = 1) {
                selection_weight += knapsack_items[j].item_weight;
                selection_value += knapsack_items[j].item_value;
            }    
        }

        knapsack_combination_output << arrayToString(item_selection_code) << "\n" << selection_weight << "\n" << selection_value << "\n";
    }

    knapsack_combination_output.close();
}