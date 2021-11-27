import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		HashMap<String, Integer> numberOfNumber = new HashMap<String, Integer>();

		for (int i = 0; i < 10; i++) {
			numberOfNumber.put(Integer.toString(i), 0);
		}

		int multiplyInput = 1;
		for (int i = 0; i < 3; i++) {
			multiplyInput *= Integer.parseInt(br.readLine());
		}
		String answer = Integer.toString(multiplyInput);
		for (int i = 0; i < answer.length(); i++) {
			numberOfNumber.put(Character.toString(answer.charAt(i)),
				numberOfNumber.get(Character.toString(answer.charAt(i))) + 1);
		}

		for (int i = 0; i < 10; i++) {
			System.out.println(numberOfNumber.get(Integer.toString(i)));
		}
	}

}