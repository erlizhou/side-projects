public class Percolation { 
    private static final int BLOCKED = 0;
    private static final int OPEN = 1;
    private int[][] grid;
    private int size;
    private WeightedQuickUnionUF weightedQuickUF;
   
    public Percolation(int N) {                // create N-by-N grid, with all sites blocked
        size = N;
        if (N <= 0) 
            throw new IllegalArgumentException("N must be a positive number");
        grid = new int[size + 2][size + 2];
        weightedQuickUF = new WeightedQuickUnionUF(size * size + 2);   
        for (int i = 1; i <= size; i++) {
            for (int j = 1; j <= size; j++) {
                grid[i][j] = BLOCKED;
            } 
        }
        if (N > 1) {
            for (int i = 1; i <= size; i++) {  // connect virtual top site to top row
                weightedQuickUF.union(0, i);
            }
            for (int i = size * (size - 1) + 1; i <= size * size; i++) {  // connect virtual bottom site to bottom row
                weightedQuickUF.union(i, size * size + 1);
            } 
        }
    }
    
    public void open(int i, int j) {           // open site (row i, column j) if it is not already
        if (checkValidity(i, j)) {
            markSiteOpen(i, j);
            linkSiteToNeighbors(i, j); 
        }
    }
    
    private boolean checkValidity(int i, int j) {
        if (i <= 0 || i > size) 
            throw new IndexOutOfBoundsException("row index i out of bounds");   
        if (j <= 0 || j > size) 
            throw new IndexOutOfBoundsException("column index j out of bounds"); 
        else 
            return true;
    }
    
    private void markSiteOpen(int i, int j) {
        grid[i][j] = OPEN;
    }
    
    private int xyTo1D(int i, int j) {  // map from a 2-dimensional pair to a 1-dimensional union find object index
        return (i - 1) * size + j;
    }
    
    private void linkSiteToNeighbors(int i, int j) { 
        if (isOpen(i + 1, j)) 
            weightedQuickUF.union(xyTo1D(i, j), xyTo1D(i + 1, j));
        if (isOpen(i, j + 1)) 
            weightedQuickUF.union(xyTo1D(i, j), xyTo1D(i, j + 1));
        if (isOpen(i - 1, j)) 
            weightedQuickUF.union(xyTo1D(i, j), xyTo1D(i - 1, j));
        if (isOpen(i, j - 1)) 
            weightedQuickUF.union(xyTo1D(i, j), xyTo1D(i, j - 1));    
    }
            
    public boolean isOpen(int i, int j) {     // is site (row i, column j) open?
            return grid[i][j] == OPEN;
    }
    
    public boolean isFull(int i, int j)  {    // is site (row i, column j) full? 
        if (size == 1)
            return isOpen(1, 1);
        else
            return weightedQuickUF.connected(0, xyTo1D(i, j)) && isOpen(i, j);
    }
    
    public boolean percolates() {             // does the system percolate?
        if (size == 1)
            return isOpen(1, 1);
        else
            return weightedQuickUF.connected(0, size * size + 1);
    }
    
    public static void main(String[] args) {   // test client, optional
        Percolation test = new Percolation(10);
        test.open(1, 1);
        System.out.println(test.isOpen(6, 0));
        System.out.println(test.isFull(6, 12));
        System.out.println(test.percolates());
    }
}   