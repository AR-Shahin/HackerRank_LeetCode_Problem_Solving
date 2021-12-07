#include <iostream>
using namespace std;

int main()
{
    int arr[] = {10, 10, 20, 20, 30, 30};
    int n = sizeof(arr) / sizeof(arr[0]);
    int k = 0;
    for (int i = 0; i < n; i++)
    {
        if (arr[i] != arr[i + 1])
        {
            arr[k] = arr[i];
            k++;
        }
    }

    for (int i = 0; i < k; i++)
    {
        cout << arr[i] << " ";
    }
}
