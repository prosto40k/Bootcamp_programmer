int n=5;
int [] array=new int[n];
for (int i = 0; i < n; i++)
{
    array[i]=Convert.ToInt32(Console.ReadLine());
}
System.Console.WriteLine("Вывели массив:"+"["+string.Join(" ",array)+"]"); 
//string.Join("разделитель",переменная)
System.Console.WriteLine($"Третий эдемент массива:{array[3]}");
//Сложность алгоритма(время работы) (аннотация) О(1)

// new int[n]{4,5,3,1,2}
//O(n)
// {1,2,3,4,5} = O(n*log(n))-быстрая сортировка
// ((5+1)/2)*5 = O(1)
// n<n*log(n)+1
int summ=0;
for (int i = 0; i < n-1; i++)
{
    summ+=array[i];
}
System.Console.WriteLine(summ);
//O(n)
// О-Большая аннотация