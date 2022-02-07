
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class Solution {

	private static final StringBuilder sb = new StringBuilder();

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int testCase = 10;

		for (int tc = 1; tc <= testCase; tc++) {
			br.readLine();
			Stack<Character> stack = new Stack<>();
			int answer = 1;
			for (Character i : br.readLine().toCharArray()) {
				if (i == '(' || i == '[' || i == '{' || i == '<') {
					stack.add(i);
				}
				else{
					if (stack.isEmpty()){
						answer = 0;
						break;
					}
					else{
						if ((i == ')' && stack.peek() == '(') || (i == ']' && stack.peek() == '[')
							|| (i == '}' && stack.peek() == '{') || (i == '>' && stack.peek() == '<')){
							stack.pop();
						}
						else{
							answer = 0;
							break;
						}
					}
				}
			}
			sb.append("#").append(tc).append(" ").append(answer).append("\n");
		}

		System.out.print(sb);
	}

}