#include <bits/stdc++.h>
using namespace std;

int main()
{
	char a[25];
	cin >> a;
	int i = strlen(a);
	if(a[i-1] == 'r') printf("er\n");
	else printf("ist\n");
	return 0;
}