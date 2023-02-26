#####################################################
# Python Basics (Data Structures, Func., Comprehensions)
#####################################################

# Task I:
x = 8
y = 3.2
z = 8j + 18
a = "Hello World"
b = True
c = 23 < 22
l = [1, 2, 3, 4]
d = {"Name": "Jake",
     "Age": 27,
     "Address": "Downtown"}
t = ("Machine Learning", "Data Science")
s = {"Python", "Machine Learning", "Data Science"}

print(type(x))
print(type(y))
print(type(z))
print(type(a))
print(type(b))
print(type(c))
print(type(l))
print(type(d))
print(type(t))
print(type(s))

# Task II:
text = "The goal is to turn data into information, and information into insight."

text = text.replace(",","")
text = text.replace(".","")

text = text.upper()
text = text.split()
print(text)

# Task III:
lst = ["D","A","T","A","S","C","I","E","N","C","E"]

# Adım 1: Verilen listenin eleman sayısına bakın.
len(lst)

# Adım 2: Sıfırıncı ve onuncu index'teki elemanları çağırın.
print(lst[0])
print(lst[10])

# Adım 3: Verilen liste üzerinden ["D","A","T","A"] listesi oluşturun.
n_list = lst[:4]

# Adım 4: Sekizinci index'teki elemanı silin.
lst.pop(8)
print(lst)

# Adım 5: Yeni bir eleman ekleyin.
lst.append("B")

# Adım 6: Sekizinci index'e  "N" elemanını tekrar ekleyin.
lst.insert(8, "N")
lst

# Task IV:
dict = {'Christian': ["America",18],
        'Daisy':["England",12],
        'Antonio':["Spain",22],
        'Dante':["Italy",25]}


# Adım 1: Key değerlerine erişiniz.
dict.keys()

# Adım 2: Value'lara erişiniz.
dict.values()

# Adım 3: Daisy key'ine ait 12 değerini 13 olarak güncelleyiniz.
dict["Daisy"] = ["England", 13]

# Adım 4: Key değeri Ahmet value değeri [Turkey,24] olan yeni bir değer ekleyiniz.
dict["Ahmet"] = ["Turkey", 24]

# Adım 5: Antonio'yu dictionary'den siliniz.
dict.pop("Antonio")


# Task V:
list_V = [2,13,18,93,22]

def seperator_even_odd(list_x):
    even_list = list()
    odd_list = list()
    for i in list_x:
        if i % 2 == 0:
            even_list.append(i)
        else:
            odd_list.append(i)

    print(even_list)
    print(odd_list)


seperator_even_odd(list_V)


# Task VI:
ogrenciler = ["Ali","Veli","Ayşe","Talat","Zeynep","Ece"]

for index, student in enumerate(ogrenciler):
    if index <= 2:
        print(f"Faculty of Engineering {index + 1}. student: {student}")
    else:
        print(f"Faculty of Medicine {index - 2}. student: {student}")


# Task VII:
ders_kodu = ["CMP1005","PSY1001","HUK1005","SEN2204"]
kredi = [3,4,2,4]
kontenjan = [30,75,150,25]

for index, i in enumerate(list(zip(ders_kodu, kredi, kontenjan))):
    print(f"Kredisi {i[1]} olan {i[0]} kodlu dersin kontenjanı {i[2]} kişidir.")


# Task VIII:

kume1 = set(["data", "python"])
kume2 = set(["data", "function", "qcut", "lambda", "python", "miuul"])


def subset_finder(cluster1, cluster2):
    if cluster1.issuperset(cluster2) == False:
        print(cluster2.difference(cluster1))
    else:
        print(cluster1.intersection(cluster2))


subset_finder(kume1, kume2)

# Comprehension Task I
# ListComprehension yapısı kullanarak "car_crashes" verisindeki numeric değişkenlerin isimlerini büyük harfe çeviriniz.
# Başına NUM ekleyiniz.
import seaborn as sns
df = sns.load_dataset("car_crashes")
df.columns

["NUM_" + col.upper() if df[col].dtype != "O" else col.upper() for col in df.columns]
df.dtypes

# Comprehension Task II
[col.upper() + "_FLAG" if "no" not in col else col.upper() for col in df.columns]
df.columns
df.dtypes

#
df_car = sns.load_dataset("car_crashes")

og_list = ["abbrev", "no_previous"]
b = list()

# Comprehension Task III
for col in df_car.columns:
    if col not in og_list:
        b.append(col)

print(b)

new_columns = [col for col in df_car.columns if col not in og_list]

new_df = df[new_columns]
new_df.head()


# Important Case:
def alternating(string):
    new_string = ""
    for string_index in range(len(string)):
        if string_index % 2 == 0:
            new_string += string[string_index].upper()
        else:
            new_string += string[string_index].lower()
    print(new_string)


# With Enumerate:
def alternating_with_enumerate(string):
    new_string = ""
    for i, letter in enumerate(string):
        if i % 2 == 0:
            new_string += letter.upper()
        else:
            new_string += letter.lower()

    print(new_string)
