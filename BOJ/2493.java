import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.List;
import java.util.Stack;
import java.util.stream.Collectors;

public class Main {

	private static final StringBuilder sb = new StringBuilder();

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		List<Integer> tower = Arrays.stream(br.readLine().split(" "))
			.map(Integer::parseInt)
			.collect(Collectors.toList());
		Stack<List<Integer>> stack = new Stack<>();
		sb.append(0).append(" ");
		stack.push(Arrays.asList(tower.get(0), 1));
		for (int i = 1; i < N; i++) {
			if (stack.isEmpty()) {
				sb.append(0).append(" ");
			} else {
				if (stack.peek().get(0) >= tower.get(i)) {
					sb.append(stack.peek().get(1)).append(" ");
					stack.push(Arrays.asList(tower.get(i), i + 1));
				} else {
					while (!stack.isEmpty() && stack.peek().get(0) < tower.get(i)) {
						stack.pop();
					}
					if (!stack.isEmpty()) {
						sb.append(stack.peek().get(1)).append(" ");
						stack.push(Arrays.asList(tower.get(i), i + 1));
					}
					else{
						sb.append(0).append(" ");
						stack.push(Arrays.asList(tower.get(i), i + 1));
					}
				}
			}
		}
		System.out.println(sb);
	}

}