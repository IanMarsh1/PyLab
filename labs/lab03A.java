public class lab03A {
    public static long compute() {
        // Example task: Sum of numbers from 1 to 100 million
        long total = 0;
        for (int i = 1; i <= 100000000; i++) {
            total += i;
        }
        return total;
    }

    public static void main(String[] args) {
        long startTime = System.nanoTime();
        long result = compute();
        long endTime = System.nanoTime();

        System.out.println("Result: " + result);
        System.out.println("Time taken (seconds): " + (endTime - startTime) / 1e9);
    }
}
