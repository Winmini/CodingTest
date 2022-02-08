
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.List;
import java.util.StringTokenizer;
import java.util.stream.Collectors;

public class Solution {

	private static final StringBuilder sb = new StringBuilder();

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		int testCase = 10;

		for (int tc = 1; tc <= testCase; tc++) {
				br.readLine();
			List<Integer> arr = Arrays.stream(br.readLine().split(" "))
				.parallel()
				.map(Integer::parseInt)
				.collect(Collectors.toCollection(LinkedList::new));
			int order = Integer.parseInt(br.readLine());
			st = new StringTokenizer(br.readLine());
			for (int i = 0; i < order; i++) {
				st.nextToken();
				int index = Integer.parseInt(st.nextToken());
				int n = Integer.parseInt(st.nextToken());
				List<Integer> tmpArr = new LinkedList<>();
				for (int j = 0; j < n; j++) {
					tmpArr.add(Integer.parseInt(st.nextToken()));
				}
				arr.addAll(index, tmpArr);
			}
			sb.append("#").append(tc).append(" ");
			arr.stream().limit(10).forEach(i -> sb.append(i).append(" "));
			sb.append("\n");
		}
		System.out.print(sb);
	}

}