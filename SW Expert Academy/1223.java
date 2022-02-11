
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

public class Solution {

	private static final StringBuilder sb = new StringBuilder();

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int testCase = 10;

		for (int tc = 1; tc <= testCase; tc++) {
			sb.append("#").append(tc).append(" ");
			br.readLine();
			char[] input = br.readLine().toCharArray();
			List<Character> postfix = new ArrayList<>();
			Stack<Character> temp = new Stack<>();

			for (char i : input) {
				if (i != '+' && i != '*') {
					postfix.add(i);
				} else if (!temp.isEmpty() && i < temp.peek()) {
					temp.add(i);
				} else if (!temp.isEmpty() && i >= temp.peek()) {
					while (!temp.isEmpty() && i >= temp.peek()) {
						postfix.add(temp.pop());
					}
					temp.add(i);
				} else {
					temp.add(i);
				}
			}
			while (!temp.isEmpty()) {
				postfix.add(temp.pop());
			}

			Stack<Integer> arr = new Stack<>();

			for (char i : postfix) {
				if (i != '+' && i != '*') {
					arr.add(i - '0');
				} else if (i == '+') {
					arr.add(arr.pop() + arr.pop());
				} else {
					arr.add(arr.pop() * arr.pop());
				}
			}

			sb.append(arr.peek());
			sb.append("\n");
		}
		System.out.print(sb);
	}
}