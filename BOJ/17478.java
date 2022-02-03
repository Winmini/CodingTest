import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

	private static final StringBuilder sb = new StringBuilder();
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int k = Integer.parseInt(br.readLine());
		sb.append("어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.\n");
		solve(0, k);
		System.out.println(sb);
	}

	private static void solve(int n, int k) {
		if (n == k) {
			addUnderBar(n, "\"재귀함수가 뭔가요?\"\n");
			addUnderBar(n, "\"재귀함수는 자기 자신을 호출하는 함수라네\"\n");
			addUnderBar(n, "라고 답변하였지.\n");
			return;
		}
		addUnderBar(n, "\"재귀함수가 뭔가요?\"\n");
		addUnderBar(n, "\"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.\n");
		addUnderBar(n, "마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.\n");
		addUnderBar(n, "그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어.\"\n");
		solve(n + 1, k);
		addUnderBar(n, "라고 답변하였지.\n");
	}

	private static void addUnderBar(int n, String message) {
		for (int i = 0; i < n; i++)
			sb.append("____");
		sb.append(message);
	}
}