    public class PercolationStats {
    private int times, xindex, yindex;
    private double[] fraction;
 
    public PercolationStats(int N, int T) {    // perform T independent computational experiments on an N-by-N grid
        times = T;
        if (N <= 0 || T <= 0) {
            throw new IllegalArgumentException("input out of bounds");
        }
        fraction = new double[times];
        for (int i = 0; i < T; i++) {
            Percolation perc = new Percolation(N);
            int steps = 0;
            while (!perc.percolates()) {
                xindex = StdRandom.uniform(1, N + 1);
                yindex = StdRandom.uniform(1, N + 1);
                while (perc.isOpen(xindex, yindex)) {
                     xindex = StdRandom.uniform(1, N + 1);
                     yindex = StdRandom.uniform(1, N + 1);
                }
                perc.open(xindex, yindex);
                steps++;
            }   
            fraction[i] = (double) steps / (N * N);
        }
    }
       
    public double mean() {                    // sample mean of percolation threshold
        return StdStats.mean(fraction);
    }
    
    public double stddev() {                   // sample standard deviation of percolation threshold
        return StdStats.stddev(fraction);
    }
    
    public double confidenceLo() {            // returns lower bound of the 95% confidence interval
        return mean() - 1.96 * stddev() / Math.sqrt(times);
    }
    public double confidenceHi() {             // returns upper bound of the 95% confidence interval
        return mean() + 1.96 * stddev() / Math.sqrt(times);
    }
    public static void main(String[] args) {   // test client, described below
       PercolationStats test = new PercolationStats(Integer.parseInt(args[0]), Integer.parseInt(args[1]));
       StdOut.println("mean                    = " + test.mean());
       StdOut.println("stddev                  = " + test.stddev());
       StdOut.println("95% confidence interval = " + test.confidenceLo() + ", " + test.confidenceHi());
       return;
    }
}