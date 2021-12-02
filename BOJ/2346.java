import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.List;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int balloonSize = Integer.parseInt(br.readLine());
		List<String> balloon = new LinkedList<String>(Arrays.asList(br.readLine().split(" ")));
		List<Integer> balloonNumber = new LinkedList<>();
		for (int i = 0; i < balloonSize; i++) {
			balloonNumber.add(i + 1);
		}
		int location = 0;
		int currentSize = balloonSize;
		int[] answer = new int[balloonSize];
		int newLocation = 0;
		for (int i = 0; i < balloonSize; i++) {
			answer[i] = balloonNumber.get(location);
			if (Integer.parseInt(balloon.get(location)) > 0) {
				newLocation += Integer.parseInt(balloon.get(location)) - 1;
			} else {
				newLocation += Integer.parseInt(balloon.get(location));
			}
			balloon.remove(location);
			balloonNumber.remove(location);
			currentSize -= 1;
			if (newLocation < 0 && currentSize > 0) {
				newLocation = currentSize - ((-newLocation) % currentSize);
			}
			if (newLocation >= currentSize && currentSize > 0) {
				newLocation %= currentSize;
			}
			location = newLocation;
		}
		for (int ans : answer) {
			System.out.print(ans + " ");
		}
	}
}