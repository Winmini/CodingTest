import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Main {
	private static final StringBuilder sb = new StringBuilder();
	public static int[] parent;

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		// 0 zero 1 one 2 two 3 three 4 four 5 five 6 six 7 seven 8 eight 9 nine
		Map<String, String> stringMap = new HashMap<>();
		stringMap.put("0", "zero");
		stringMap.put("1", "one");
		stringMap.put("2", "two");
		stringMap.put("3", "three");
		stringMap.put("4", "four");
		stringMap.put("5", "five");
		stringMap.put("6", "six");
		stringMap.put("7", "seven");
		stringMap.put("8", "eight");
		stringMap.put("9", "nine");
		// 입력받은 숫자를 String으로 변환하는 맵

		List<Number> answer = new ArrayList<>();

		String[] input = br.readLine().split(" ");
		for (int i = Integer.parseInt(input[0]); i <= Integer.parseInt(input[1]); i++) {
			if (i < 10)
				answer.add(new Number(i, stringMap.get(String.valueOf(i))));
			// 10보다 작으면 숫자와 숫자에 맞는 string을 함께 list에 넣음
			else
				answer.add(new Number(i, stringMap.get(String.valueOf(i / 10)) + stringMap.get(String.valueOf(i % 10))));
			// 10보다 크면 숫자와, 숫자의 앞자리와 뒷자리를 분리해서 string으로 더한값을 넣음
		}
		answer.sort(Comparator.comparing(i -> i.priority));
		// string을 기준으로 정렬
		for (int i = 1; i <= answer.size(); i++) {
			sb.append(answer.get(i-1).num).append(" ");
			if (i % 10 == 0)
				sb.append("\n");
			// 10개 단위로 출력
		}
		System.out.println(sb);
	}

	static class Number {
		public int num;
		public String priority;

		public Number(int num, String priority) {
			this.num = num;
			this.priority = priority;
		}
	}
	// 숫자와 문자를 저장하는 클래스

}

