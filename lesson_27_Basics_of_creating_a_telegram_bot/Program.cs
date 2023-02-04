using System.Net.Http;


//JSON-служит для передачи данных между клиентом и сервером
// {
//     "ok":true,
//     "result":
//     {
//         "id":6142681683,
//         "is_bot":true,
//         "first_name":"\u041c\u043e\u0439 \u043f\u0435\u0440\u0432\u044b\u0439 \u0431\u043e\u0442",
//         "username":"FirstTest01_bot",
//         "can_join_groups":true,
//         "can_read_all_group_messages":false,
//         "supports_inline_queries":false
//     }
// }

// class GetMeModel
// {
//     bool ok;
//     ResultModel result;
// }

// class ResultModel
// {
//     long id;
//     bool is_bot;
//     string first_name;
//     string username;
// }

// Пишем парсер(нечто, Преобразующее(что то не понятное для нас) {JSON} во что то понятное нам) 
//для сложного объекта
// {
//     "наименование флага":значение флага,
// }

string token = File.ReadAllText("token.config");
HttpClient hc = new();
hc.BaseAddress = new Uri($"https://api.telegram.org/bot{token}/");

string contentObj = hc.GetStringAsync("getme").Result;
System.Console.WriteLine(contentObj);
31:38