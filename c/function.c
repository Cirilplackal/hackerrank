/*Task

You have to write a function int max_of_four(int a, int b, int c, int d) which reads four arguments and returns the greatest of them.

+= : Add and assignment operator. It adds the right operand to the left operand and assigns the result to the left operand.

a += b is equivalent to a = a + b;

Input Format

Input will contain four integers -

, one in each line.

Output Format

Print the greatest of the four integers.
Note: I/O will be automatically handled.

Sample Input

3
4
6
5

Sample Output

6*/
int max_of_four(int a, int b, int c, int d) {
    int max1 = a > b ? a : b;
    int max2 = c > d ? c : d;
    return max1 > max2 ? max1 : max2;
}
