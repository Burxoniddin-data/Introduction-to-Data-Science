def typeBasedTransformer(**kwargs):
    transformed = {}
    for key in kwargs:
        value = kwargs[key]
        if isinstance(value, int) or isinstance(value, float):
            transformed[key] = value * value  
        elif isinstance(value, str):
            reversed = ""
            for char in value:
                reversed = char + reversed
            transformed[key] = reversed  
        elif isinstance(value, bool):
            if value is True:
                transformed[key] = False
            else:
                transformed[key] = True  
        elif isinstance(value, list):
            reversed_numbers = []
            for i in range(len(value) - 1, -1, -1):
                reversed_numbers.append(value[i])
            transformed[key] = reversed_numbers  
        elif isinstance(value, tuple):
            reversed_tuple_numbers = []
            for i in range(len(value) - 1, -1, -1):  
                reversed_tuple_numbers.append(value[i])
            transformed[key] = tuple(reversed_tuple_numbers)  
        elif isinstance(value, dict):
            unique_values = set()
            is_unique = True
            for v in value.values():
                if v in unique_values:
                    is_unique = False
                    break
                unique_values.add(v)
            if is_unique:
                swapped_dict = {}
                for k in value:
                    swapped_dict[value[k]] = k
                transformed[key] = swapped_dict
            else:
                transformed[key] = value  
        else:
            transformed[key] = value  
    return transformed

#you can enter numbers but you should change them manually from the function itself.
if __name__ == "__main__":
    print(typeBasedTransformer(num=69, text="Burxoniddin", flag=True, numbers_list=[5, 7, 19], my_tuple=(10, 34, 30), my_dict={"a": 1, "c": 6}, unknown_type={1, 2, 3}
    ))
