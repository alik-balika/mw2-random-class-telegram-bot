from model.csv_parser import parse_file, create_generator

if __name__ == '__main__':
    weapons = parse_file("../assets/items.csv")
    slots = parse_file("../assets/slots.csv")

    generator = create_generator("../assets/modifications.csv", weapons, slots)

    generator.generate_random_class()
    print(generator.perks)
    print(generator.tactical)
    print(generator.lethal)
