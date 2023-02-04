from random import randint

'''
сделаем класс Chromosome, у которого будет три свойства :

rating - рейтинг хромосомы
size - размер хромосомы (ллинна массива генов)
genes - массив генов хромосомы (то, что раньше было самой хромосомой) 
'''
class Chromosome:
    def __init__(self, size, gene_pool):
        self.rating = 0
        self.size = size
        self.genes = bytearray(size)
        if gene_pool is not None:
            self.set_random_genes(gene_pool)
    '''
    Теперь напишем функцию для генерации соучайной хромосомы. Функция принимает два пар-ра:
    длина хромосомы, ко-ую надо получить, и набор генов, из ко-ых нужно сделать хр-му.
    '''
    def set_random_genes(self, gene_pool):
        gene_pool_range = len(gene_pool) - 1
        for i in range(self.size):
            rand_pos = randint(0, gene_pool_range)
            self.genes[i] = gene_pool[rand_pos]

def create_population(pop_size, chromo_size, genes):
    '''
    В функцию заполнения популяции мы так-же передаем размер популяции,
    размер хр-мы и генофонда, чтобы не зависеть от глобальных переменных.
    Подбор пар.
    '''
    population = [None] * pop_size
    for i in range(pop_size):
        population[i] = Chromosome(chromo_size, gene_pool)

    return population
'''
Фу-ия для выч-ия рейтинга - расстояние между двумя строками.
Напишем сразу для всей популяции, т.к других применений у нее нет:
Насколько вся популяция строк близка к целевой фразе
'''
def calc_rating(population, final_chromo):
    for chromo in population:
        chromo.rating = chromo.size
        for i in range(chromo.size):
            if chromo.genes[i] == final_chromo[i]:
                chromo.rating -= 1
'''
Сделаем сортировку хромосом по рейтингу. Это обычная сортировка пузырьком:
(По выживаемости)
'''
def sort_population(population):
    size = len(population)
    repeat = True
    while repeat:
        repeat = False
        for i in range(0, size - 1):
            bubble = population[i]
            if (bubble.rating > population[i + 1].rating):
                population[i] = population[i + 1]
                population[i + 1] = bubble
                repeat = True
    
def select(population, survivors):#Лучшие живите, худшие умрите
    # elitism selection
    size = len(survivors)
    for i in range(size):
        survivors[i] = population[i]

def repopulate(population, parents, children_count):
    '''
    Теперь, имея фу-ии для выбора родителей и для скрещивания, пишем фу-ию,
    ко-ая заполняет вторую половину популяции потомкам(родители сохраняются в первой половине)
    '''
    pop_size = len(population)
    while children_count < pop_size:
        p1_pos = get_parent_index(parents, None)
        p2_pos = get_parent_index(parents, p1_pos)
        p1 = parents[p1_pos]
        p2 = parents[p2_pos]
        population[children_count] = cross(p1, p2)
        population[children_count + 1] = cross(p2, p1)
        children_count += 2

def get_parent_index(parents, exclude_index):
    '''
   Среди выживших нужно отобрать пары родителей, для того чтобы получить
   от них потомков и востановить вторую половину популяции
    '''
    size = len(parents)
    while True:
        index = randint(0, size - 1)
        if exclude_index is None or exclude_index != index:
            return index

def cross(chromo1, chromo2):
    '''
    РџРѕР»СѓС‡РёРІ РґРІСѓС… СЂРѕРґРёС‚РµР»РµР№, РјС‹ РјРѕР¶РµРј РїСЂРѕРІРµСЃС‚Рё СЃРєСЂРµС‰РёРІР°РЅРёРµ.
    Р•РіРѕ СЃСѓС‚СЊ РІ С‚РѕРј, С‡С‚РѕР±С‹ РєР°РєРёРј-С‚Рѕ РѕР±СЂР°Р·РѕРј РїРµСЂРµРјРµС€Р°С‚СЊ РіРµРЅС‹ РґРІСѓС… СЂРѕРґРёС‚РµР»РµР№ Рё РїРѕР»СѓС‡РёС‚СЊ РЅРѕРІСѓСЋ С…СЂРѕРјРѕСЃРѕРјСѓ-РїРѕС‚РѕРјРєР°.

    Р—РґРµСЃСЊ С‚Р°РєР¶Рµ РµСЃС‚СЊ РєСѓС‡Р° РјРµС‚РѕРґРѕРІ, Рё РјС‹ РѕРїСЏС‚СЊ РІРѕР·СЊРјС‘Рј С‡С‚Рѕ РїРѕРїСЂРѕС‰Рµ. РС‚Рѕ Р±СѓРґРµС‚ РѕРґРЅРѕС‚РѕС‡РµС‡РЅС‹Р№ РєСЂРѕСЃСЃРёРЅРіРѕРІРµСЂ.

    РњС‹ РІС‹Р±РёСЂР°РµРј СЃР»СѓС‡Р°Р№РЅСѓСЋ РїРѕР·РёС†РёСЋ РІРЅСѓС‚СЂРё С…СЂРѕРјРѕСЃРѕРјС‹, Рё РїРѕС‚РѕРјРѕРє РїРѕР»СѓС‡Р°РµС‚ РіРµРЅС‹ СЂРѕРґРёС‚РµР»СЏ в„–1 РѕС‚ РЅР°С‡Р°Р»Р° Рё РґРѕ СЌС‚РѕР№ РїРѕР·РёС†РёРё,
    Рё РіРµРЅС‹ СЂРѕРґРёС‚РµР»СЏ в„–2 РѕС‚ СЌС‚РѕР№ РїРѕР·РёС†РёРё Рё РґРѕ РєРѕРЅС†Р°.
    
    РљР°Р¶РґС‹Рµ РґРІР° СЂРѕРґРёС‚РµР»СЏ РїРѕСЂРѕР¶РґР°СЋС‚ РїР°СЂСѓ РїРѕС‚РѕРјРєРѕРІ. РўРѕ РµСЃС‚СЊ С„СѓРЅРєС†РёСЋ cross()
    РјС‹ РІС‹Р·С‹РІР°РµРј РґРІР°Р¶РґС‹: СЃРЅР°С‡Р°Р»Р° СЃ (СЂРѕРґРёС‚РµР»СЊ1, СЂРѕРґРёС‚РµР»СЊ2), Р·Р°С‚РµРј СЃ (СЂРѕРґРёС‚РµР»СЊ2, СЂРѕРґРёС‚РµР»СЊ1).
    '''
    size = chromo1.size
    point = randint(0, size - 1)
    child = Chromosome(size, None)
    for i in range(point):
        child.genes[i] = chromo1.genes[i]
    for i in range(point, size):
        child.genes[i] = chromo2.genes[i]

    return child

def mutate(population, chromo_count, gene_count, gene_pool):
    '''
    РјРѕР¶РЅРѕ РїРѕРґРІРµСЂРіР°С‚СЊ РјСѓС‚Р°С†РёРё С…РѕС‚СЊ 50% РїРѕРїСѓР»СЏС†РёРё,
    РЅРѕ РІРѕС‚ РєРѕР»РёС‡РµСЃС‚РІРѕ РіРµРЅРѕРІ Р»СѓС‡С€Рµ Р·Р°РґР°С‚СЊ 1.
    РС‚Рѕ Р·РЅР°С‡РёС‚, С‡С‚Рѕ Р·Р° 1 СЂР°Р· РјСѓС‚РёСЂСѓРµС‚ С‚РѕР»СЊРєРѕ РѕРґРёРЅ СЃРёРјРІРѕР» РІ СЃС‚СЂРѕРєРµ.
    Р‘С‹Р»Рё РЅРµСЂРµРґРєРё СЃР»СѓС‡Р°Рё, РєРѕРіРґР° СЃС‚СЂРѕРєР° Р±С‹Р»Р° СѓР¶Рµ РїРѕС‡С‚Рё РїСЂР°РІРёР»СЊРЅР°СЏ,
    С‚Рѕ РµСЃС‚СЊ РѕС‚Р»РёС‡Р°Р»Р°СЃСЊ РІСЃРµРіРѕ РѕРґРЅРёРј СЃРёРјРІРѕР»РѕРј, РЅРѕ РµСЃР»Рё РїРѕСЃР»Рµ РјСѓС‚Р°С†РёРё
    РІ РЅРµР№ РјРµРЅСЏРµС‚СЃСЏ Р±РѕР»СЊС€Рµ С‡РµРј РѕРґРёРЅ СЃРёРјРІРѕР», РјС‹ РЅР°РѕР±РѕСЂРѕС‚ СѓРґР°Р»СЏРµРјСЃСЏ РѕС‚ С†РµР»Рё.
    '''
    pop_size = len(population)
    gene_pool_size = len(gene_pool)
    for i in range(chromo_count):
        chromo_pos = randint(0, pop_size - 1)
        chromo = population[chromo_pos]
        for j in range(gene_count):
            gene_pos = randint(0, gene_pool_size - 1)
            gene = gene_pool[gene_pos]
            gene_pos = randint(0, chromo.size - 1)
            chromo.genes[gene_pos] = gene
'''
РґР»СЏ СЃРѕР±СЃС‚РІРµРЅРЅРѕРіРѕ СѓРґРѕР±СЃС‚РІР° СЃРґРµР»Р°РµРј Р±РѕР»РµРµ Р°РєРєСѓСЂР°С‚РЅС‹Р№ РІС‹РІРѕРґ РїРѕРїСѓР»СЏС†РёРё РЅР° РїРµС‡Р°С‚СЊ СЃ РїРѕСЂСЏРґРєРѕРІС‹Рј РЅРѕРјРµСЂРѕРј Рё СЂРµР№С‚РёРЅРіРѕРј:
'''
def print_population(population):
    i = 0
    for chromo in population:
        i += 1
        print(str(i) + '. ' + str(chromo.rating) + ': ' + chromo.genes.decode())
'''
  Генофонд - это строка-справочник, ко-ая содержит все возможные гены. Его и финальную строку
  (будем теперь говорить по научному: хромосому) мы закодируем в байтовые массивы.
'''
gene_pool = bytearray(b'abcdefghijklmnopqrstuvwxyz ') #если хотите по русски ставите сюда весь русский алфовит

final_chromo = bytearray(b'i love geekbrains') #целевая фраза

chromo_size = len(final_chromo)
population_size = 20
'''
В нашем случае мы для селекции возьмем метод элит. У нас будет элита в виде лучшей половины популяции,
ко-ая будет переходить в новую популяцию и порождать потомков, чтобы заполнить вторую половину новой популяции

Список хромосом уже отсортирован по рейтингу и поэтому задача селекции решена(берем топ 10), го
ради будущей реализации других методов нам надо сделать формальный отбор. То есть - поместим нах избранников
в список "выживших".

Заведем для выживших список фиксированной длины заранее и будем им пользоваться все время:
'''
survivors = [None] * (population_size // 2)

population = create_population(population_size, chromo_size, gene_pool)

iteration_count = 0

while True:  
    iteration_count += 1  #СЃС‡РµС‚С‡РёРє РїРѕРєРѕР»РµРЅРёСЏ
    calc_rating(population, final_chromo) #СЂР°СЃС‡РµС‚ СЂРµР№С‚РёРЅРіР° РїРѕРїСѓР»СЏС†РёРё
    sort_population(population) #СЃРѕСЂС‚РёСЂРѕРІРєР° РїРѕРїСѓР»СЏС†РёРё, РІ РЅР°С‡Р°Р»Рµ - СЌР»РёС‚Р°
    print('*** ' + str(iteration_count) + ' ***')
    print_population(population) #РїРµС‡Р°С‚Р°РµРј РїРѕРїСѓР»СЏС†РёСЋ
    if population[0].rating == 0:   
        '''
        РџСЂРё РґРѕСЃС‚РёР¶РµРЅРёРё С†РµР»РµРІРѕР№ СЃС‚СЂРѕРєРё Сѓ РїРµСЂРІРѕР№ С…СЂРѕРјРѕСЃРѕРјС‹ РІ СЃРїРёСЃРєРµ Р±СѓРґРµС‚ СЂРµР№С‚РёРЅРі 0.
        РћР±РЅР°СЂСѓР¶РёРІ С‚Р°РєРѕРµ СѓСЃР»РѕРІРёРµ, РјС‹ РїСЂРµРєСЂР°С‰Р°РµРј С†РёРєР», С‚Р°Рє РєР°Рє С†РµР»СЊ РґРѕСЃС‚РёРіРЅСѓС‚Р°.
        РњС‹ С‚Р°РєР¶Рµ РїРµС‡Р°С‚Р°РµРј С‚РµРєСѓС‰СѓСЋ РїРѕРїСѓР»СЏС†РёСЋ РЅР° РєР°Р¶РґРѕРј С€Р°РіРµ С†РёРєР»Р°:
        '''
        break
    if iteration_count==20:break
    select(population, survivors)   #РѕС‚Р±РѕСЂ СЌР»РёС‚С‹ - СЂРѕРґРёС‚РµР»РµР№ РІ РїРµСЂРІСѓСЋ С‡Р°СЃС‚СЊ
    repopulate(population, survivors, population_size // 2)   #РІС‚РѕСЂСѓСЋ С‡Р°СЃС‚СЊ РїРѕРїСѓР»СЏС†РёРё Р·Р°РїРѕР»СЏРЅРµРј РґРµС‚СЊРјРё
    mutate(population, 10, 1, gene_pool) #РІС‹РїРѕР»РЅСЏРµРј РјСѓС‚Р°С†РёСЋ РїРѕ 1 РіРµРЅСѓ

#43:51 Lesson 16