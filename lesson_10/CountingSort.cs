int [] arr ={1,2,3,1,2,3,2,1,2,3,1,2,6,7,5,4,3,1,2}
int size=arr.Length;
int max=arr[0];
for (int i = 0; i < size; i++) 
{
    if (arr[i]>max) max=arr[i];
}
int[] counter=new int[max+1];
for (int i = 0; i < size; i++)
{
   counter[arr[i]]++;

}
int index=0;
for (int i = 0; i < max; i++)
{
    for (int j = 0; j < counter[i]; j++)
    {
        arr[index++]=i;
    }
}