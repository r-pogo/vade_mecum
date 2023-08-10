# *args **kwargs

* --> asterisk is unpacking operator
```python
pizzas = ["Margherita", "Salame", "Quattro stagioni"]
print(pizzas)
['Margherita', 'Salame', 'Quattro stagioni'] # one list object

print(*pizzas)
Margherita Salame Quattro stagioni # prints each actual name
```
```python
def make_pizza(*toppings): # naming convention would be *args
    print(toppings)

make_pizza('pepperoni')
make_pizza('pieczarki', 'rucola', 'salame piccante')

('pepperoni',)
('pieczarki', 'rucola', 'salame piccante') # tu tworzy krotke i umieszcza otrzymane wartosci
```

!UWAGA! Python najpierw dopasowuje argumenty pozycyjne oraz argumenty w postaci słow kluczowych  
, a dopiero pózniej zbiera pozostałe argumenty dla ostatniego parametru.

```python
def make_pizza(size, *toppings):
    print(f"Cooking pizza {size}, with:")
    for topping in toppings:
        print(f"- {topping}")
    
make_pizza("large", 'prosciutto')
make_pizza("medium", 'gorgonzola', 'acciughe', 'rucola')

Cooking pizza large, with:
- prosciutto
Cooking pizza medium, with:
- gorgonzola
- acciughe
- rucola
    
```

**kwargs ---> umożliwia akceptowanie dowolną liczbę par klucz-wartość, tworzy pust  
słownik w który umieszcza otrzymane pary klucz-wartość

```python
def make_pizza(size, *toppings, **details): # naming convention would be **kwargs
    print(f"Cooking pizza {size}, with:")
    for topping in toppings:
        print(f"- {topping}")
    print("\n Details of order:")
    for key, item in details.items():
        print(f"- {key}: {item}")
    
make_pizza("large", 'prosciutto', delivery=True)

Cooking pizza large, with:
- prosciutto
 Details of order:
- delivery: TrueCooking pizza large, with:
- prosciutto
{'delivery': True}
```