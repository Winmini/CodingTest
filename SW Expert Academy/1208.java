
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Collections;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Solution {

	private static final StringBuilder sb = new StringBuilder();
	// private static final int[] dir_x = {0, 1, 0, -1};
	// private static final int[] dir_y = {1, 0, -1, 0};

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int testCase = 10;

		for (int tc = 1; tc <= testCase; tc++) {
			int num = Integer.parseInt(br.readLine());
			PriorityQueue<Integer> boxes = new PriorityQueue<>();
			PriorityQueue<Integer> rBoxes = new PriorityQueue<>(Collections.reverseOrder());
			StringTokenizer st = new StringTokenizer(br.readLine(), " ");
			while(st.hasMoreTokens()) {
				int tmp = Integer.parseInt(st.nextToken());
				boxes.add(tmp);
				rBoxes.add(tmp);
			}

			for (int i = 0; i < num; i++) {
				boxes.add(boxes.poll() + 1);
				rBoxes.add(rBoxes.poll() - 1);
			}

			sb.append("#").append(tc).append(" ").append(rBoxes.poll() - boxes.poll()).append("\n");
		}

		System.out.print(sb);
	}

}