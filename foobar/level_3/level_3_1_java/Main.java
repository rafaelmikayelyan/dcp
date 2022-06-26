// public class Solution {
public class Main {
    public static int solution(int[] l) {
        int triples = 0;
        int step = l.length;
        for (int i = 0; i < step - 2; i++) {
            for (int j = i + 1; j < step - 1; j++) {
                if (l[j] % l[i] == 0) {
                    for (int k = j + 1; k < step; k++) {
                        if (l[k] % l[j] == 0) {
                            triples += 1;
                        }
                    }
                }
            }
        }
        return triples;
    }
	public static void main(String[] args) {
		int[] myNumbers = {1, 2, 4};
		System.out.println(solution(myNumbers));
  }
}

// Somehow Java passed all 5 tests while Python did not... wtf... what am I missing?!
