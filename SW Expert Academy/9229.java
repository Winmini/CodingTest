
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

public class Solution {

	private static final StringBuilder sb = new StringBuilder();

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int testCase = Integer.parseInt(br.readLine());

		for (int tc = 1; tc <= testCase; tc++) {
			int answer = -1;
			String[] input = br.readLine().split(" ");
			int N = Integer.parseInt(input[0]);
			int M = Integer.parseInt(input[1]);

			List<Integer> arr = Arrays.stream(br.readLine().split(" "))
				.parallel()
				.map(Integer::parseInt)
				.filter(i -> i < M)
				.sorted()
				.collect(Collectors.toList());

			if (arr.size() >= 2) {
				int start = 0;
				int end = arr.size() - 1;
				while (start != end) {
					if (arr.get(start) + arr.get(end) <= M) {
						answer = Math.max(answer, arr.get(start) + arr.get(end));
						start += 1;
					} else {
						end -= 1;
					}
				}
			}
			sb.append("#").append(tc).append(" ").append(answer).append("\n");
		}
		System.out.print(sb);
	}

}