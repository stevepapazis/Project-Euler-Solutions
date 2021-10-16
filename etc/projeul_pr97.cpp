//Large non-Mersenne prime

/*The first known prime found to exceed one million digits was discovered in 1999, and is a 
Mersenne prime of the form 2**6972593-1; it contains exactly 2,098,960 digits. Subsequently 
other Mersenne primes, of the form 2**p-1, have been found which contain more digits.

However, in 2004 there was found a massive non-Mersenne prime which contains 2,357,207 digits:
28433*2**7830457+1.

Find the last ten digits of this prime number.*/

#include <iostream>
#include <cstdlib>
using namespace std;

main()
{
	float matrix[10]={2};
	int j,i(1);
	
	for(i;i<7830457;i++)
	{
		for(j=0;j<=9;j++)
		{
			matrix[j] *= 2;
			if (matrix[j] > 9)
			{
				if (j != 9) matrix[j+1] += .5; 
				matrix[j] = int(matrix[j])%10;
			}
		}
	}
	for(j=0;j<=9;j++) matrix[j] *= 28433;
	for(j=0;j<9;j++)
	{	matrix[j+1] += matrix[j]/10;
		matrix[j] = int(matrix[j])%10; }
	matrix[9] = int(matrix[9])%10;
	matrix[0]++;
	cout<<"Solution: ";
	for(j=0;j<=9;j++) cout<<matrix[9-j];
	
	cout<<endl;
	system("pause");
	return -1;
}
