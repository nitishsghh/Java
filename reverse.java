// Java Reverse Program
// Diagonal elements of matrix
import java.io.*;

class java
{
static int N = 4;

// Function to swap
// diagonals elements
static void reverseDiagonal(int array[][])
{
	int i = 0, j = N;
	int temp = 0;
	while (i < j)
	{

		// For reversing elements of major diagonal.
	
		temp = array[i][i];
		array[i][i] = array[j - 1][j - 1];
		array[j - 1][j - 1] = temp;

		// For reversing elements of minor diagonal.

		temp = array[i][j - 1];
		array[i][j - 1] = array[j - 1][i];
		array[j - 1][i] = temp;

		i++;
		j--;
	}

	// Print matrix after reversals.

		for (i = 0; i < N; ++i)
	{
		for (j = 0; j < N; ++j)
			System.out.print(array[i][j] + " ");
			System.out.println();
	}
}

// other used in matrix
public static void main (String[] args)
{
	int matrix[][] = {{1, 2, 3, 4},
					{5, 6, 7, 8},
					{9, 10, 11, 12},
					{13, 14, 15, 16}};
	reverseDiagonal(matrix);
}
}



