import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.PriorityQueue;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int inputNumber = Integer.parseInt(br.readLine());
		PriorityQueue<Integer> cards = new PriorityQueue<>();
		for (int i = 0; i < inputNumber; i++) {
			cards.add(Integer.parseInt(br.readLine()));
		}
		int size = cards.size();
		int answer = 0;
		for (int i = 0; i < size - 1; i++) {
			int tmp1 = cards.poll();
			int tmp2 = cards.poll();
			cards.add(tmp1 + tmp2);
			answer += tmp1 + tmp2;
		}
		System.out.println(answer);
	}

}