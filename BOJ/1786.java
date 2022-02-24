import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Solution {

	static char[] pattern;
	static int[] lps;
	static StringBuilder sb = new StringBuilder();
	static int ans = 0;

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		char[] T = br.readLine().toCharArray();
		pattern = br.readLine().toCharArray();
		lps = new int[pattern.length];
		compute_lps();
		kmp_search(T);
		System.out.println(ans);
		System.out.println(sb);
	}

	public static void kmp_search(char[] txt) {
		int m = pattern.length;
		int n = txt.length;
		int i = 0;
		int j = 0;

		while (i < n) {
			if (pattern[j] == txt[i]) {
				i++;
				j++;
			} else if (pattern[j] != txt[i]) {
				if (j != 0)
					j = lps[j - 1];
				else
					i++;
			}
			if (j == m) {
				ans++;
				sb.append(i-j+1).append(" ");
				j = lps[j - 1];
			}
		}
	}

	public static void compute_lps() { // lps 배열 구하는 방법
		int len = 0;
		int i = 1;
		while (i < pattern.length) {
			if (pattern[len] == pattern[i]) {
				len++; //
				lps[i] = len;
				i++;
			} else {
				if (len != 0) {
					len = lps[len - 1];
				} else {
					lps[i] = 0;
					i++;
				}
			}
		}
	}
}