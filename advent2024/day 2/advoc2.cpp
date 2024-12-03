#include <iostream>
#include <vector>
#include <fstream>
#include <string>
#include <sstream>
#include <cstdlib>  // For abs()

using namespace std;

// Function to check if levels are either strictly increasing or decreasing
bool isSorted(const vector<int>& levels) {
    bool increasing = true;
    bool decreasing = true;
    
    for (size_t i = 0; i < levels.size() - 1; i++) {
        if (levels[i] < levels[i + 1]) {
            decreasing = false;
        }
        if (levels[i] > levels[i + 1]) {
            increasing = false;
        }
    }

    return increasing || decreasing;
}

// Function to check if adjacent levels have valid differences
bool hasValidDifferences(const vector<int>& levels) {
    for (size_t i = 0; i < levels.size() - 1; i++) {
        int diff = abs(levels[i] - levels[i + 1]);
        if (diff < 1 || diff > 3) {
            return false;
        }
    }
    return true;
}

// Function to check if a report is safe
bool isSafeReport(const vector<int>& levels) {
    return isSorted(levels) && hasValidDifferences(levels);
}

// Function to check if removing one level from the report makes it safe
bool canBeSafeByRemovingOneLevel(const vector<int>& levels) {
    for (size_t i = 0; i < levels.size(); i++) {
        vector<int> modifiedLevels = levels;
        modifiedLevels.erase(modifiedLevels.begin() + i);
        if (isSafeReport(modifiedLevels)) {
            return true;
        }
    }
    return false;
}

int main() {
    vector<vector<int>> reports;
    ifstream f("text2.txt"); // Change the file name as needed

    if (!f.is_open()) {
        cout << "[*] File Not Found!" << endl;
        return 1; // Return early if the file is not found
    }

    string line;
    while (getline(f, line)) {
        istringstream lineStream(line);
        vector<int> levels;
        int level;
        while (lineStream >> level) {
            levels.push_back(level);
        }
        reports.push_back(levels);
    }
    f.close();

    int safeReportsCount = 0;

    // Part One: Count reports that are already safe
    for (const auto& report : reports) {
        if (isSafeReport(report)) {
            safeReportsCount++;
        }
    }

    // Part Two: Count reports that can be made safe by removing one level
    for (const auto& report : reports) {
        if (!isSafeReport(report) && canBeSafeByRemovingOneLevel(report)) {
            safeReportsCount++;
        }
    }

    cout << "Total number of safe reports: " << safeReportsCount << endl;

    return 0;
}
