def kwargsAcceptFun(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

#you can give your own answers or you can just write them directly from the fuction itself if you dont want to type it
if __name__ == '__main__':
    name = input("Enter your favourite car: ")
    company = input("Produced by: ")
    country = input("Where it is produced: ")
    kwargsAcceptFun(car_name = name, company_name = company, country_name = country)
