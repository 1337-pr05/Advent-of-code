#include <iostream>
#include <fstream>
#include <regex>
#include <string>
#include <algorithm>

using namespace std;

int extractAndCompute(const string& inputString) {
    regex pattern(R"(mul\((\d{1,3}),(\d{1,3})\))");
    smatch matches;
    string::const_iterator searchStart(inputString.cbegin());
    int total = 0;

    while (regex_search(searchStart, inputString.cend(), matches, pattern)) {
        int x = stoi(matches[1].str());
        int y = stoi(matches[2].str());
        total += x * y;
        searchStart = matches.suffix().first;
    }

    return total;
}

int main() {
    ifstream file("text.txt");
    if (!file) {
        cerr << "Error: Could not open the file!" << endl;
        return 1;
    }

    string inputString((istreambuf_iterator<char>(file)),
                            istreambuf_iterator<char>());
    file.close();

    // Start measuring time
    // auto start = chrono::high_resolution_clock::now();

    int result = extractAndCompute(inputString);
    cout << "Sum of all valid multiplications: " << result << endl;

    // Stop measuring time
    // auto end = chrono::high_resolution_clock::now();
    // chrono::duration<double> elapsed = end - start;

    // cout << "Execution time: " << elapsed.count() << " seconds" << endl;

    return 0;
}
