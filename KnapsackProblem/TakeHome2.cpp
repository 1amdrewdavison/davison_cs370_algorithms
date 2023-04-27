#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

int findLongestCommonSequence(std::string s1, std::string s2) {
	std::vector<std::vector<int>> seqArr = {{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {},{}, {}};
	
	for (int i = 0; i < s1.length(); i++) {
		for (int j = 0; j < s2.length(); j++) {
			if (s1.at(i) == s2.at(j)) {
				if (i == 0 || j == 0) {
                    seqArr[i].push_back(1);
				} else {
					seqArr[i].push_back(seqArr[i-1][j-1] + 1);
				}
			} else {
				if (i == 0 ) {
					if (j == 0) {
						seqArr[i].push_back(0);
					} else {
						seqArr[i].push_back(seqArr[i][j-1]);
					}
				} else {
					//Using addition as array concatenation
					if (j == 0) {
						seqArr[i].push_back(*std::max_element(seqArr[i-1].begin(), seqArr[i-1].begin()));
					} else {
						seqArr[i].push_back(std::max(seqArr[i-1][j], seqArr[i][j-1]));
					}
				}
			}
		}		
	}

	return seqArr[s1.length() - 1][s2.length() - 1];
}

int main() {
    auto max = findLongestCommonSequence("profile", "cloudpine");
    
    std::cout << max;
}