import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Map;

public class Solution {

	static int[] parents;

	private static final StringBuilder sb = new StringBuilder();

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int testCase = Integer.parseInt(br.readLine());
		for (int tc = 1; tc <= testCase; tc++) {
			sb.append("#").append(tc).append(" ");
			String[] input = br.readLine().split(" ");
			parents = new int[Integer.parseInt(input[0]) + 1];
			Arrays.setAll(parents, i -> i);

			for (int i = 0; i < Integer.parseInt(input[1]); i++) {
				String[] order = br.readLine().split(" ");
				if(order[0].equals("0"))
					union(Integer.parseInt(order[1]), Integer.parseInt(order[2]));
				else if(find(Integer.parseInt(order[1])) ==  find(Integer.parseInt(order[2])))
					sb.append("1");
				else
					sb.append("0");

			}
			sb.append("\n");
		}
		System.out.println(sb);
	}

	public static int find(int x){
		if(x == parents[x])
			return x;
		return parents[x] = find(parents[x]);
	}

	public static boolean union(int a, int b){
		int x = find(a);
		int y = find(b);

		if (x == y)
			return false;
		if (x <= y)
			parents[y] = x;
		else
			parents[x] = y;
		return true;
	}
}