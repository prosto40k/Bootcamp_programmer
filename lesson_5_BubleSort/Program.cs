/*
Cортировка пузырьком
Начальный массив: [3, 1, 5, 0, 7, 9, 8]
Сравнение двух элементов масива,когда совершаем перестановку
сравнение начинаем с начала
*/
Console.WriteLine("Введите кол-во элементов массива: ");
int n = Convert.ToInt32(Console.ReadLine());//Размер массива
int[] array = new int[n];//Создали массив
for (int i = 0; i < n; i++)//Заполняем массив
{
    Console.Write("Введите значения массива: ");
    array[i] = Convert.ToInt32(Console.ReadLine());
}
Console.WriteLine("Начальный массив: [" + string.Join(", ", array) + "]");
Console.WriteLine();               // " + строка.присоеденить("разделитель",переменная) )
for (int i = 0; i < n; i++)//i-кол-во проходов
{
    // if (array[i] > array[i + 1])
    //     {
    //         int temp = array[i];
    //         array[i] = array[i + 1];
    //         array[i + 1] = temp;
    //     }
    for (int j = 0; j < n - 1; j++)//j-проходимся по массиву,(int j = 1; j < n; j++) Почему размер-1?
    {
        if (array[j] > array[j + 1])//                        if (array[j-1] > array[j])
        {
            int temp = array[j];
            array[j] = array[j + 1];
            array[j + 1] = temp;
        }
    }
    Console.WriteLine(i + "[" + string.Join(", ", array) + "]");
}