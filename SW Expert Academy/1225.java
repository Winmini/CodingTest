import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.stream.Collectors;

public class Solution {

	private static final StringBuilder sb = new StringBuilder();

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int testCase = 10;

		for (int tc = 1; tc <= testCase; tc++) {
			br.readLine();
			List<Integer> arr = Arrays.stream(br.readLine().split(" "))
				.map(Integer::parseInt)
				.collect(Collectors.toList());
			int minV = arr.stream().mapToInt(i -> i / 15).min().orElse(1) - 1;
			arr = arr.stream().map(i -> i - minV * 15).collect(Collectors.toList());
			int cnt = 1;
			while (arr.get(7) != 0) {
				arr.set(0, arr.get(0) - cnt);
				Collections.rotate(arr, -1);
				if (arr.get(7) < 0){
					arr.set(7, 0);
				}
				cnt %= 5;
				cnt += 1;
			}
			sb.append("#").append(tc).append(" ");
			arr.forEach(i -> sb.append(i).append(" "));
			sb.append("\n");
		}

		System.out.print(sb);
	}

}