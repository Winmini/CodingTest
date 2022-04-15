
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

public class Main {

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int testCase = Integer.parseInt(br.readLine());
		for (int tc = 0; tc < testCase; tc++) {

			int n = Integer.parseInt(br.readLine());
			boolean[] visited = new boolean[n];

			String[] tmp = br.readLine().split(" ");
			int homeX = Integer.parseInt(tmp[0]);
			int homeY = Integer.parseInt(tmp[1]);

			List<int[]> stores = new ArrayList<>();
			for (int i = 0; i < n; i++) {
				tmp = br.readLine().split(" ");
				stores.add(new int[] {Integer.parseInt(tmp[0]), Integer.parseInt(tmp[1])});
			}
			tmp = br.readLine().split(" ");
			int destX = Integer.parseInt(tmp[0]);
			int destY = Integer.parseInt(tmp[1]);

			if (Math.abs(homeX - destX) + Math.abs(homeY - destY) <= 1000){
				System.out.println("happy");
				continue;
			}

			Stack<int[]> stack = new Stack<>();
			for (int i = 0; i < stores.size(); i++) {
				int dis = Math.abs(homeX - stores.get(i)[0]) + Math.abs(homeY - stores.get(i)[1]);
				if (dis <= 1000) {
					stack.add(stores.get(i));
					visited[i] = true;
				}
			}

			while (!stack.isEmpty()){
				int[] pos = stack.pop();

				for (int i = 0; i < stores.size(); i++) {
					if (visited[i])
						continue;
					int dis = Math.abs(pos[0] - stores.get(i)[0]) + Math.abs(pos[1] - stores.get(i)[1]);
					if (dis <= 1000) {
						stack.add(stores.get(i));
						visited[i] = true;
					}
				}
			}
			boolean possible = false;
			for (int i = 0; i < n; i++) {
				if (visited[i]){
					if (Math.abs(stores.get(i)[0] - destX) + Math.abs(stores.get(i)[1] - destY) <= 1000){
						possible = true;
						break;
					}
				}
			}
			if (possible)
				System.out.println("happy");
			else
				System.out.println("sad");

		}
	}

}

