import csv
import os

from model.generator import RandomClassGenerator


def parse_file(file_name):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, file_name)

    with open(file_path) as csv_file:
        return _read_file(csv_file)


def _read_file(csv_file):
    csv_reader = csv.reader(csv_file, delimiter=',')
    _skip_header_row(csv_reader)
    return _create_id_to_item_map(csv_reader)


def _skip_header_row(csv_reader):
    next(csv_reader, None)


def _create_id_to_item_map(csv_reader):
    id_to_weapon = {}
    for row in csv_reader:
        weapon_id = row[0]
        weapon_name = row[1]
        id_to_weapon[weapon_id] = weapon_name
    return id_to_weapon


def create_generator(file_name, weapons, slots):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, file_name)

    with open(file_path) as csv_file:
        return _read_modifications_file(csv_file, weapons, slots)


def _read_modifications_file(csv_file, weapons, slots):
    csv_reader = csv.reader(csv_file, delimiter=',')
    _skip_header_row(csv_reader)
    return _create_generator(csv_reader, weapons, slots)


def _create_generator(csv_reader, weapons, slots):
    generator = RandomClassGenerator()
    _add_weapons_with_no_attachments(generator)
    for row in csv_reader:
        _parse_fields_from_csv_and_generate_weapon(generator, row, slots, weapons)
    return generator


def _add_weapons_with_no_attachments(generator):
    melee_and_launchers = {'RPG-7', 'Strela-P', 'Riot Shield', 'Dual Kodachis', 'PILA', 'Combat Knife', 'JOKR'}
    for weapon in melee_and_launchers:
        generator.add_weapon(weapon)


def _parse_fields_from_csv_and_generate_weapon(generator, row, slots, weapons):
    weapon = weapons[row[1]]
    attachment = row[2]
    slot = slots[row[3]]
    _add_attachment_to_weapon(generator, weapon, attachment, slot)


def _add_attachment_to_weapon(generator, weapon_name, attachment, slot):
    generator.add_weapon(weapon_name)
    weapon = generator.get_weapon(weapon_name)
    weapon.add_attachment_to_slot(attachment, slot)