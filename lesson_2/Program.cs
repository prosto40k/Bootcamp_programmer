// Найти максимальну сумму m чисел массива

int[] RandomIntArray(int size=10,int min=0,int max=5)
{
    
    int[] a=new int[size];
    Random random=new Random();
    for(int i=0;i<size;i++)
    a[i]=random.Next(min,max);
    return a;
}

// int SumM(int[] a,int m) //цикл в цикле -  
//                         //сложность=сложность^2
// {
//     int max=0;
//     for (int i = 0; i < a.Length-m; i++)
//     {
//         int t=0;
//         for (int j = i; j < i+m; j++)
//         {
//             t +=a[j];
//         }
//         if (t>max) max=t;
//     }
//     return max;
// }

int SumM1(int[] a,int m) //цикл за циклом - 
{                        //сложность=сложность+сложность
    int i = 0;
    int max=0;
    for (int j = 0; j < m;j++) max +=a[j];//пробегаем по m элементов  
    int t=max;                            //масивва и находим сумму 
    
    // Но зачем первый цикл?Без ничго ничего не работает...
    
    for (i = 1; i < a.Length - m; i++)//(a.Length - m) - не нужно  
    {                                 //доходить до коца массива
        t= t-a[i-1] + a[i+(m-1)];     //т.к с позиции (a.Length - m-1)
        if(t>max)max=t;               //сумму m элементвов не подсчитать
    }
    return max;
}

void Print(int[] a)
{
    for(int i=0;i<a.Length;i++)
        System.Console.Write($"{a[i],2}");
}

int[] m=RandomIntArray();
Print(m);
System.Console.WriteLine();
System.Console.WriteLine(SumM1(m,3));
//Теория базовых алгаритмов
//Изучение алгаритмов
//Что такое оперативная память,стэк,куча в стэке)

