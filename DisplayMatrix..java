import java.util.Arrays;
import java.util.Scanner;

public class DisplayMatrix {

  public static void main(String[] args) {
    
    // declare a 3x3 matrix
    int matrix[][] = null ;
    matrix = new int[3][3];
    
    // create Scanner class object to read input
    Scanner scan = new Scanner(System.in);
    
    // read matrix
    System.out.println("Enter 3x3 Matrix elements: ");
    for(int i=0; i<3; i++) {
      for(int j=0; j<3; j++) {
        matrix[i][j] = scan.nextInt();
      }
    }
    
    // display 2D array using for-each loop
    System.out.println("Entered Matrix: ");
    System.out.println(Arrays.deepToString(matrix)); 
    
    // close Scanner 
    scan.close();
  }

}