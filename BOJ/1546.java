import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int totalSubject = Integer.parseInt(br.readLine());
		StringTokenizer st = new StringTokenizer(br.readLine());
		int[] subjectScore = new int[totalSubject];
		double sum = 0.0;
		for (int i = 0; i < subjectScore.length; i++) {
			subjectScore[i] = Integer.parseInt(st.nextToken());
			sum += subjectScore[i];
		}
		Arrays.sort(subjectScore);
		double avg = sum / (double)subjectScore[totalSubject - 1];
		System.out.println(avg * 100 / totalSubject);
	}

}