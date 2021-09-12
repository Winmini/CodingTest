// https://programmers.co.kr/learn/courses/30/lessons/72410

#include <iostream>
#include <string>
#include <vector>
#include <cctype>

using namespace std;

string solution(string new_id) {

	// 1단계
	int size = new_id.size();
	for (int i = 0; i < size; i++) {
		if (isalpha(new_id[i]) == 1024) {
			new_id[i] = tolower(new_id[i]);
		}
	}

	// 2단계
	vector<char> id;
	vector<char>::iterator iter;
	for (int i = 0; i < size; i++) {
		if ((isalpha(new_id[i]) == 1024) || (new_id[i] >= '0' && new_id[i] <= '9') || (new_id[i] == '-') || (new_id[i] == '_') || (new_id[i] == '.')) {
			id.push_back(new_id[i]);
		}
	}


	for (iter = id.begin(); iter != id.end();) {
		if (*iter == '.') {
			iter++;

			while (1) {
				if (iter == id.end()) break;
				if (*iter == '.') {
					iter = id.erase(iter);
				}
				else {
					break;
				}
			}
		}
		else iter++;
	}
	iter = id.begin();
	// 4단계
	if (!id.empty()) {
		if (id.front() == '.') id.erase(iter);
	}
	if (!id.empty()) {
		if (id.back() == '.') id.pop_back();
	}

	// 5단계
	if (!id.size()) id.push_back('a');

	// 6단계
	if (id.size() == 1) {
		id.push_back(id.front());
		id.push_back(id.front());
	}
	if (id.size() == 2) {
		id.push_back(id.back());
	}

	string answer;
	if (id.size() >= 15) {
		for (int i = 0; i < 15; i++) {
			if (i == 14) {
				if (id.front() == '.') break;
			}
			answer += id.front();
			id.erase(id.begin());
		}
	}
	else {
		size = id.size();
		for (int i = 0; i < size; i++) {
			answer += id.front();
			id.erase(id.begin());
		}
	}
	return answer;
}