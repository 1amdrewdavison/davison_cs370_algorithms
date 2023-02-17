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

//Function to turn the combination array into a string
std::string arrayToString(const std::vector<int> combination) {
    std::string str = "";
    for (auto digit : combination) {
        str += std::to_string(digit);
    }
    return str;
}

//Function that iterates the array from, left to right as if it was a binary number in reverse.
//If the starting digit is a zero, turn that into a one and the finish
//Otherwise, continue iterating until a zero is found and turn the ones into zeros along the way
//Returns true if successfully iterates, otherwise returns false to indicate that the combination array is finished
bool iterateArray(std::vector<int>& combination) {
    bool foundZero = false;
    
    for (int i = 0; i < combination.size(); i++) {
        auto digit = combination[i];

        if (digit == 0) {
            combination[i] = 1;
            foundZero = true;
            break;
        } else {
            combination[i] = 0;
        }
    }

    return foundZero;
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

    std::cout << "Enter knapsack weight limit: ";
    std::cin >> knapsack_limit;

    //Begin iterating through all possible combinations
    std::vector<int> item_selection_code(knapsack_items.size());
    std::fill_n(item_selection_code.begin(), knapsack_items.size(), 0);

    //Keep track of best combination
    std::vector<int> best_combination;
    int best_weight = knapsack_limit + 1;
    int best_value = -1;

    //This loop goes through each possible combination, totals its weight and value, prints it to output.txt, and saves the optimal solution
    //To change this such that it skips the first possible combination (no items), turn this into a while loop
    //I kept this first iteration in the case that the knapsack limit is 0, so that there is a solution
    do {
        int selection_weight = 0;
        int selection_value = 0;
        
        //Total up weight and value based on the decision tree of the combination array
        for (int i = 0; i < item_selection_code.size(); i++) {
            int digit = item_selection_code[i];
            
            if (digit == 1) {
                selection_weight += knapsack_items[i].item_weight;
                selection_value += knapsack_items[i].item_value;
            }    
        }
        
        //Output to file
        knapsack_combination_output << arrayToString(item_selection_code) << "\n" << selection_weight << "\n" << selection_value << "\n";

        //Update best solution if applicable
        if (selection_weight <= knapsack_limit && selection_value > best_value) {
            best_combination.assign(item_selection_code.begin(), item_selection_code.end());
            best_weight = selection_weight;
            best_value = selection_value;
        }
    } 
    while (iterateArray(item_selection_code));

    //Output optimal combination
    knapsack_combination_output << arrayToString(best_combination) << "\n" << best_weight << "\n" << best_value << "\n";

    knapsack_combination_output.close();
}